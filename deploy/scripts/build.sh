#!/usr/bin/env bash
# author : owen-carter

remoteIp=
remotePort=22
remoteUser=
rsaPath=~/.ssh/id_rsa.pub

bridgePort=10037

sudo yum install autossh openssh-server -y
sudo pip install supervisor

if [ -e "${rsaPath}" ];
then
    echo "id_rsa.pub is already exist!"
else
    echo "id_rsa.pub is not exist!"
    ssh-keygen -t rsa
fi

sudo ssh-copy-id -p 22 -i ${rsaPath} ${remoteUser}@${remoteIp}

echo "Start to write the autossh.service"
sudo cat >> /etc/supervisor/config.d/autossh.ini <<EOF
[program:autossh]
command=/usr/bin/autossh -M 7777 -NR ${bridgePort}:localhost:22 ${remoteUser}@${remoteIp} -p22
directory=~
numprocs=1
process_name=%(program_name)s
priority=999
umask=022
startsecs=60
startretries=3
exitcodes=0,2
autorestart=true
stopsignal=INT

autostart=false
autorestart=true
stopasgroup=true
killasgroup=true

stdout_logfile=/var/log/supervisor/autossh.log
stdout_logfile_maxbytes=1MB
stdout_logfile_backups=10
stdout_capture_maxbytes=1MB
stderr_logfile=/var/log/supervisor/autossh.log
stderr_logfile_maxbytes=1MB
stderr_logfile_backups=10
stderr_capture_maxbytes=1MB
EOF

supervisorctl update
supervisorctl reload
supervisorctl start autossh
