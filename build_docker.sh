#!/usr/bin/env bash

export PROJECT_ID="cltk-api-148615"
export VERSION="v1"

docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker build -t gcr.io/$PROJECT_ID/hello-node-nginx:$VERSION .
docker run -p 80:80 --name hello_tutorial_nginx gcr.io/$PROJECT_ID/hello-node-nginx:$VERSION
