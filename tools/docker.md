# Docker

```zsh
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
docker rmi -f $(docker images)

docker ps --format '{{.Names}}'
docker logs -f cli
docker logs dev-peer0.org2.example.com-mycc-1.0
```
