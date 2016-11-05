#!/usr/bin/env bash

# TODO: Figure out of `EXPOSE 80` is necessary in Dockerfile

arg="$1"

export DOCKER_BUILD_VERSION="v3"
export PROJECT_ID="cltk-api-148615"
export ACCOUNT="kyle@kyle-p-johnson.com"
export REGION="us-central1"
export ZONE="us-central1-a"
export APP_NAME="cltk_api_v2"
export CLUSTER_NAME="cltk-api-v2-c0"
export MACHINE_TYPE="f1-micro"
export NUM_NODES="3"
export MIN_NODES="3"
export MAX_NODES="5"
export SERVICE_NAME="cltk-api-d0"


if [ $arg = "build" ]; then
    echo "Building and running Docker ..."
    docker stop $(docker ps -a -q)
    docker rm $(docker ps -a -q)
    docker build -t gcr.io/$PROJECT_ID/$APP_NAME:$DOCKER_BUILD_VERSION .
    docker run -p 80:80 --name $APP_NAME gcr.io/$PROJECT_ID/$APP_NAME:$DOCKER_BUILD_VERSION
fi


if [ $arg = "deploy" ]; then
    echo "Pushing to Google Cloud Platform ..."

    echo "Setting up user defaults ..."
    gcloud config set account $ACCOUNT
    gcloud config set compute/zone $ZONE
    gcloud config set project $PROJECT_ID

    echo "Pushing Docker app to GCP ..."
    gcloud docker -- push gcr.io/$PROJECT_ID/$APP_NAME:$DOCKER_BUILD_VERSION
    echo ""

    echo "Creating cluster on GCP ..."
    gcloud container clusters create $CLUSTER_NAME --zone $ZONE --machine-type $MACHINE_TYPE \
      --num-nodes $NUM_NODES --enable-autoscaling --min-nodes=$MIN_NODES --max-nodes=$MAX_NODES
    echo ""

    echo 'Deploying cluster (as a "pod") ...'
    # Must get credentials for cluster first, before interacting with it
    gcloud container clusters get-credentials $CLUSTER_NAME
    kubectl run $SERVICE_NAME --image=gcr.io/$PROJECT_ID/$APP_NAME:$DOCKER_BUILD_VERSION --port=80
    echo ""

    echo 'Exposing pod IP to the Internet (as a "service") ...'
    kubectl expose deployment $SERVICE_NAME --type="LoadBalancer"
    # This prints the external IP, will take a minute:
    echo "Waiting 60 secs for external IP to become available ..."
    echo 'If no "EXTERNAL-IP" available, run "kubectl get services $DEPLOYMENT_NAME" (getting $DEPLOYMENT_NAME from this Bash file).'
    wait 60
    kubectl get services $SERVICE_NAME
    # TODO: get just external IP and curl it with: `kubectl describe services $DEPLOYMENT_NAME | grep "LoadBalancer Ingress"`
fi

#TODO: Figure out whether "service" and "deployment" need different names
if [ $arg = "destroy" ]; then
    kubectl delete services $SERVICE_NAME
    kubectl delete deployment $SERVICE_NAME
    gcloud container clusters delete $CLUSTER_NAME
fi