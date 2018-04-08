# 万恶的centos

1. docker-runc丢失问题
https://www.centos.org/forums/viewtopic.php?t=61747
自己建link, 指向```/usr/libexec/docker/docker-runc-current```
参考
```ln -s /usr/libexec/docker/docker-runc-current  /usr/bin/docker-runc```
同理还有```docker-proxy```, 一样的套路.