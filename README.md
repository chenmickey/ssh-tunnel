# ssh-tunnel
### Ssh反向穿透

### 内网客户机器配置以及使用
+ 配置客户机器
```bash
remoteIp=47.92.160.84
bridgePort=10000
remoteUser=dysec

sudo yum install autossh openssh-server -y

sudo ssh-copy-id -p 22 ${remoteUser}@${remoteIp} <<EOF
yr83jdie.cn89
EOF
```
+ 在客户机器和vps机器之间建立隧道
```bash
autossh -M 7777 -NR 10000:localhost:22 dysec@47.92.160.84 -p22
echo "autossh -M ${监听端口} -NR ${桥接端口}:localhost:22 ${vps用户名称}@${vpsIp} -p22"
```

### vps机器配置以及使用
+ vps ssh配置
```bash
vim /etc/ssh/sshd_config
GatewayPorts yes
sudo systemctl restart sshd
```
+ 登录vps（10000端口,密码：yr83jdie.cn89）
```bash
ssh dysec@47.92.160.84 # 
echo "查看10000端口是否有程序在监听"
netstat -antp
echo "如果存在程序监听10000端口，说明客户机和vps之间隧道建立成功，继续下一步"
```
+ 在vps上穿越到客户机
```bash
ssh -p 10000 root@localhost
echo "登录成功既可以获得客户机器shell"
```


```bash
ssh -p 10204 root@localhost
```


echo "dac.2017" | sudo supervisorctl start autossh
