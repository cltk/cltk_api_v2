# About

This is the CLTK's API, including the code, Dockerfile, and deployment script for Google Cloud Platform.

To develop and run this app and run on GCP:

1. Install Docker on your local machine
1. Run `gcp_build_deploy.sh build` to test that everything works fine. `curl localhost` will give you `The CLTK API`. 
1. Install the [GCP commandline tools](https://cloud.google.com/sdk/docs/#install_the_latest_cloud_tools_version_cloudsdk_current_version).
1. Initialize gcloud settings with `gcloud init`
1. Edit the variables at the top of `gcp_build_deploy.sh` if you need.
1. Run `gcp_build_deploy.sh deploy`. This will take about 5 minutes and at the end you'll be given an external IP to go to. This should also give `The CLTK API`.
1. To completely teardown your remote deployment, run `gcp_build_deploy.sh destroy`.
