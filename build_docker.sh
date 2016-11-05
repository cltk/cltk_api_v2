#!/usr/bin/env bash

arg="$1"

export DOCKER_BUILD_VERSION="v2"
export PROJECT_ID="cltk-api-148615"
export ACCOUNT="kyle@kyle-p-johnson.com"
export REGION="us-central1-a"
export APP_NAME="cltk_api_v2"
export CLUSTER_NAME="cltk-api-v2-c1"
export MACHINE_TYPE="f1-micro"
export NUM_NODES="3"
export MIN_NODES="3"
export MAX_NODES="5"


if [ $arg = "build" ]; then
    echo "Building and running Docker"
    docker stop $(docker ps -a -q)
    docker rm $(docker ps -a -q)
    docker build -t gcr.io/$PROJECT_ID/$APP_NAME:$DOCKER_BUILD_VERSION .
    docker run -p 80:80 --name $APP_NAME gcr.io/$PROJECT_ID/$APP_NAME:$DOCKER_BUILD_VERSION
fi


if [ $arg = "deploy" ]; then
    echo "Pushing to Google Cloud Platform"

    gcloud config set account $ACCOUNT
    # prob can be rm'd for --zone
    gcloud config set compute/zone $REGION
    gcloud config set project $PROJECT_ID

    gcloud docker -- push gcr.io/$PROJECT_ID/$APP_NAME:$DOCKER_BUILD_VERSION
    gcloud container clusters create $CLUSTER_NAME --zone $REGION --machine-type $MACHINE_TYPE \
      --num-nodes $NUM_NODES --enable-autoscaling --min-nodes=$MIN_NODES --max-nodes=$MAX_NODES

#    gcloud container clusters get-credentials $NAME
#    kubectl run $NAME --image=gcr.io/$PROJECT_ID/$NAME:$VERSION --port=80
#    kubectl get deployments
#    kubectl get pods
fi
