# Shadowsocks 
*配置文件中竟然不能带注释, 只能单独起一个md文件了.*

官方关于docker镜像的文档可见[Shadowsocks-libev Docker Image](https://github.com/shadowsocks/shadowsocks-libev/tree/master/docker/alpine)

## 配置文件示例解释
```json
{
    // server’s hostname or IP
    "server":"0.0.0.0",
    // server’s port number
    // 官方的 Dockerfile 中User是`nobody`, 所以端口 >= 1025
    "server_port": 80,
    // 
    "password":"gfw, fuck you",

    // encrypt_method
    "method":"chacha20",

    // the socket timeout in seconds. The default value is 60
    "timeout":300,

    // Enable TCP_NODELAY.
    "no_delay": true,
    
    // Enable TCP fast open.
    // Only available with Linux kernel > 3.7.0
    "fast_open":true,

    //Enable port reuse.
    // Only available with Linux kernel > 3.9.0.
    "reuse_port": true
    
    // Resovle hostname to IPv6 address first
    // "ipv6_first": true,
    
    // Enable SIP003 plugin. (Experimental)
    // "plugin": "obfs-server",
    // Set SIP003 plugin options. (Experimental)
    // "plugin_opts": "obfs=http",
    
    // Setup name servers for internal DNS resolver (libc-ares). 
    // The default server is fetched from /etc/resolv.conf.
    // "nameserver": "8.8.8.8",
    
    // tcp_and_udp | udp_only | tcp_only(default)
    // "mode": "tcp_only"

    // Run as a specific user.
    // "user": "nobody"

    // Enable ACL (Access Control List) and specify config file.
    // "acl": "/path/to/acl"
}
```
## 便捷工具
* 生成密码: [Duckduckgo Password](https://duckduckgo.com/?q=password+12&t=ffsb&ia=answer)
