# Record

* ### Set  pacman source
  
  ```shell
  pacman-mirror -i -c China -m rank
  pacman -Syy 
  ```

* ### switch kernel
  
  ```
  Menu -> Settings -> Manjaro Settings Manager -> Kernel
  
  Install the kernel you prefer and uninstall others.
  ```

* ### install docky
  
  ```shell
  pacman -S plank
  ```
  
  * *after installed, there is a line mid the screen*
    
    `Menu -> Settings -> Windows Controller Adjust -> Mixer -> toggle off the 'dock shadow'`
  
  * *config docky*
    
    `plank --preferences` to config theme

* ### install font
  
  ```shell
  pacman -S wqy-bitmapfont wqy-microhei wqy-zenhei
  ```

* ### respair after `nvidia` failed
  
  1. if screen blank, `Alt + F4` will close `lightDM` . Through tty to reboot;
  
  2. use `usb-live` mount the root part,
  
  3. `chroot` to uninstall `nvidia`

* ### ss-server docker-compose.yml
  
  ```yaml
  version: "3.3"
  services: 
    shadowsocks:
      image: shadowsocks/shadowsocks-libev
      ports: 
        - target: 8080
          published: 6527
      restart: always
      volumes:
        - "${PWD}/shadowsocks.json:/etc/shadowsocks.json"
      command: ["ss-server", "-c", "/etc/shadowsocks.json","-vv"]
  ```

* ### ss-local systemd
  
  ```shell
  pacman -S shadowsocks-libev
  cp shadowsock.json /etc/shadowsocks/${servername}.json
  systemctl enable shadowsocks-libev@${servername}
  ```

* ### privoxy
  1. install: `pacman -S privoxy`
  2. config `/etc/privoxy/config`
      ```
      listen-address 192.168.1.1:8118 # income
      forward-socks5 / localhost:9050 . # forward to sock5
      ```
  3. enable service
  
