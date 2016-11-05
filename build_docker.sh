#!/usr/bin/env bash

export PROJECT_ID="cltk-api-148615"
export VERSION="v2"

docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker build -t gcr.io/$PROJECT_ID/cltk_api_v2:$VERSION .
docker run -p 80:80 --name cltk_api_v2 gcr.io/$PROJECT_ID/cltk_api_v2:$VERSION
