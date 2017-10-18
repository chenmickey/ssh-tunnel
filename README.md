# ssh-tunnel

## How to deploy?
### 内网客户机器配置以及使用
+ 配置客户机器
```bash
remoteIp=
bridgePort=10000
remoteUser=root
sudo yum install autossh openssh-server -y
sudo ssh-copy-id -p 22 ${remoteUser}@${remoteIp} 
```
+ 在客户机器和vps机器之间建立隧道
```bash
autossh -M 7777 -NR ${bridgePort}:localhost:22 ${remoteUser}@${vpsIp} -p22
autossh -M 7777 -NR 10000:localhost:22 dysec@47.92.160.84 -p22
```

### vps机器配置以及使用
+ vps ssh配置
```bash
vim /etc/ssh/sshd_config
GatewayPorts yes
sudo systemctl restart sshd
```

+ 检查客户机器是否建立隧道成功
```bash
echo "查看10000端口是否有程序在监听"
netstat -antp
echo "如果存在程序监听10000端口，说明客户机和vps之间隧道建立成功，继续下一步"
```

+ 在vps上穿越到客户机
```bash
ssh -p 10000 root@localhost
```


## How to install?
+ 如何下载
+ 如何安装