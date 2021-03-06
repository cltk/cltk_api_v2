# About

This is the CLTK's API, including the code, Dockerfile, and deployment script for Google Cloud Platform.

To develop and run this app and run on GCP:

1. If you're only testing the Flask app, just serve with `python app/app.py`. Check with `curl 0.0.0.0:5000`.
1. [Install Docker](https://www.docker.com/) on your local machine.
1. Run `gcp.sh build` to test that everything works fine. `curl localhost` will give you a 200 response. 
1. Install the [GCP commandline tools](https://cloud.google.com/sdk/docs/#install_the_latest_cloud_tools_version_cloudsdk_current_version).
1. Initialize gcloud settings with `gcloud init`.
1. Edit the variables at the top of `gcp.sh` if you need.
1. Run `gcp.sh deploy`. This will take about 5 minutes (including time both to push files to the server, and for Google to launch and assign an external IP) and at the end you'll be given an external IP to go to. This should also give a 200 response.
1. To update an already-deployed service, increment `DOCKER_BUILD_VERSION` and run `./gcp.sh build` and then `./gcp.sh update`.
1. To completely teardown your remote deployment, run `gcp.sh destroy`.
