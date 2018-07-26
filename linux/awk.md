#AWK与sed

找出所有不是```172.16.154.27:5000```仓储的镜像, 然后打上仓储tag
```bash
docker images | grep -v 172.16.154.27:5000 | awk 'NR>=2 {print $1x":"$2}' | awk -F "/" '{printf "%s ",$0; print "172.16.154.27:5000/"$NF;}'| xargs -L 1 docker tag
```
找出所有```172.16.154.27:5000```仓储的镜像, 然后推到远端
```bash
docker images | grep 172.16.154.27:5000 | awk '{print $1x":"$2}' | xargs -L 1 docker push
docker images | grep 172.16.154.27:5000 | awk '{print $1x":"$2}' | xargs -L 1 docker rmi
```
文本去重
```sh
awk '!seen[$0]++' filename
```
