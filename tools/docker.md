# Docker

```zsh
docker container ls

docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
docker rmi -f $(docker images)

docker stop e123
docker start e123
docker restart e123

docker ps --format '{{.Names}}'
docker logs -f cli
docker logs dev-peer0.org2.example.com-mycc-1.0
```
