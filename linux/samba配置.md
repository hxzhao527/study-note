Samba服务 linux提供文件共享服务，windows可访问

# 安装
只列 ubuntu 的
> sudo apt-get install samba

配置文件在 
> /etc/samba/smb.conf

# 配置
配置文件分为几个模块，和 ini 文件类似
* [global]
* [homes]
* [printers]
* [自定义小节]

对应全局设置，用户登录后的家目录，打印机共享，自定义

配置前将原配置文件备份：
sudo cp /etc/samba/smb.conf /etc/samba/smb.conf.backup

# global 部分

workgroup = WORKGROUP
说明：指明共享所在的工作组，可以是NT域名、工作组名

server string = samba server on ubuntu
说明：客户端看到的服务器的描述信息

netbios name = ubuntu_smb
说明：设置Samba Server的NetBIOS名称。如果不填，则默认会使用该服务器的DNS名称的第一部分。netbios name和workgroup名字不要设置成一样了

interfaces = 127.0.0.0/8 eth0
说明：设置Samba Server监听哪些网卡，可以写网卡名，也可以写该网卡的IP地址

hosts allow = 192.168.1. 192.168.163. 192.168.153.
说明：表示允许连接到Samba Server的客户端，多个参数以空格隔开。可以用一个IP表示，也可以用一个网段表示。我这里只允许3个网段里的所有客户端访问samba server。

security = user
说明：设置用户访问Samba Server的验证方式，一共有四种验证方式。 
1. share：用户访问Samba Server不需要提供用户名和口令, 安全性能较低。 
2. user：Samba Server共享目录只能被授权的用户访问,由Samba Server负责检查账号和密码的正确性。账号和密码要在本Samba Server中建立。 
3. server：依靠其他Windows NT/2000或Samba Server来验证用户的账号和密码,是一种代理验证。此种安全模式下,系统管理员可以把所有的Windows用户和口令集中到一个NT系统上,使用Windows NT进行Samba认证, 远程服务器可以自动认证全部用户和口令,如果认证失败,Samba将使用用户级安全模式作为替代的方式。 
4. domain：域安全级别,使用主域控制器(PDC)来完成认证。

username map = /etc/samba/smbusers
说明：用来定义用户名映射，比如可以将root换成administrator、admin等。要事先在smbusers文件中定义好。比如：root = administrator admin，这样就可以用administrator或admin这两个用户来代替root登陆Samba Server，以保护Linux的系统账号root。后面会介绍这个文件。

encrypt passwords = true
说明：是否将认证密码加密。因为现在windows操作系统都是使用加密密码，所以一般要开启此项。

passdb backend = smbpasswd
说明：passdb backend密码验证后端。目前支持的有三种：smbpasswd、tdbsam和ldapsam。其中smbpasswd方式是使用smb自己的工具smbpasswd来给系统用户（真实用户或者虚拟用户）设置一个Samba密码，客户端就用这个密码来访问Samba的资源。smbpasswd文件默认在/etc/samba目录下，不过有时候要手工建立该文件。

smb passwd file =/etc/samba/smbpasswd
说明：用来定义samba用户的密码文件。smbpasswd文件如果默认不存在，要手工新建。后面有介绍这个文件。

log file = /var/log/samba/log.%m
说明：设定 samba server 日志文件的储存位置和文件名(%m代表客户端主机名)。

max open files = 1000
说明：同一客户最多能打开的文件数目

socket options = TCP_NODELAY
说明：用来设置服务器和客户端之间会话的Socket选项，可以优化传输速度。

# 自定义部分

comment = code
说明：comment是对该共享的描述，可以是任意字符串。

path = /home/songyd/code
说明：path用来指定共享目录的路径。

writable = yes
说明：writable用来指定该共享路径是否可写。这里我们允许写入，以满足文件双向共享。

browseable = yes
说明：browseable用来指定该共享是否可以浏览。

available = yes
说明：available用来指定该共享资源是否可用。

# smbusers 文件
该文件格式如下：
系统用户名 = 映射的虚拟账号1，映射的虚拟账号2，...

例如：
`songyd = admin`

songyd用户是samba用户，也是一个Linux系统的账号，为了不让samba用户知道存在songyd这个系统账号，可用这个文件实现songyd账号到虚拟账号admin的一个映射。只需告诉使用者用admin账号登陆即可，这样就保护了songyd这个账号。当然此时用songyd账号登陆samba也是可以的。

# 注意
有时发现smbpasswd命令即使执行没有错误，但/etc/samba/smbpasswd中却没有添加任何内容。这是由于smb.conf的passdb backend参数配置不正确，此参数必须设置为smbpasswd，这时smbpasswd -a songyd才会在/etc/samba/smbpasswd文件中添加记录。
