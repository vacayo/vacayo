#!/usr/bin/env bash
#-- Usage  --#
# $ ./ops.sh ENV ACTION [PROJECT] [--OPTIONS]


#-- Arguments  --#
if [ "$#" -eq 0 ]; then
  echo "Command is missing arguments"
  echo "USAGE ./ops.sh ENV ACTION [PROJECT] [--OPTIONS]"
  exit 1
fi

if [ -z ${CHICORY_HOME} ]; then
  echo "Please set your CHICORY_HOME environment variable first!"
  echo "This should point to the directory that houses all of your Chicory projects on your local machine."
  exit 1
fi

# extract required arguments into variables
ZONE=us-east1-b
CLUSTER=kubernetes
ENV=${1}
GCLOUD_PROJECT="vacayo-${ENV}"
ACTION=${2:-help}
PROJECT=${3}
PROJECT_DIR=$(pwd)
NUM=1
KEY=""

if [ -n "${PROJECT}" ]; then
  PROJECT_DIR="${CHICORY_HOME}/${PROJECT}"
fi

APP=$(basename `cd ${PROJECT_DIR} && git rev-parse --show-toplevel`) &> /dev/null
VERSION=$(cd ${PROJECT_DIR} && git branch | grep '*' | sed 's/* //')-$(date +%Y-%m-%d-%H-%M) &> /dev/null
YAML="${PROJECT_DIR}/deployment/${ENV}.yml" &> /dev/null


# extract options and their arguments into variables.
TEMP=`getopt -o v:y:n:k: --long version:yaml:num:key: -n 'ops.sh' -- "$@"`
if [ $? != 0 ] ; then echo "Terminating..." >&2 ; exit 1 ; fi
eval set -- "${TEMP}"
while true ; do
  case "$1" in
    -v|--version)
        VERSION=${2} ; shift 2 ;;
    -y|--yaml)
        YAML=${2} ; shift 2 ;;
    -n|--num)
        NUM=${2} ; shift 2 ;;
    -k|--key)
        KEY=${2} ; shift 2 ;;
    --) shift ; break ;;
    *) echo "Internal error!" ; exit 1 ;;
  esac
done

#-- Functions  --#

init () {
  # Configure the gcloud environment
  gcloud config set project ${GCLOUD_PROJECT}
  gcloud config set compute/zone ${ZONE}
  gcloud container clusters get-credentials ${CLUSTER} &> /dev/null
  if [ $? -eq 0 ]; then
    echo "Updated cluster endpoint and auth data for ${ZONE}/${GCLOUD_PROJECT}/${CLUSTER}"
  else
    echo "Cluster ${ZONE}/${GCLOUD_PROJECT}/${CLUSTER} does not exist!"
    read -p "Do you want to create it (y/n)? " answer
    case ${answer:0:1} in
      Y|y )  create_cluster;;
      * ) exit;;
    esac
  fi
}

create_cluster () {
  # Create a Kubernetes cluster on Google Container Enginer (GCE)
  echo "Creating Kubernetes cluster ${ZONE}/${GCLOUD_PROJECT}/${CLUSTER}"
  gcloud container clusters create ${CLUSTER} --num-nodes 1 --machine-type g1-small
}

build_image () {
  gcloud docker -- images | grep gcr.io/${GCLOUD_PROJECT}/${APP} | grep ${VERSION}
  if [ $? -eq 0 ]; then
    echo "Docker image gcr.io/${GCLOUD_PROJECT}/${APP}:${VERSION} already exists on GCR"
  else
    # Build Docker Images on Google Container Repository (GCR)
    echo "Building new Docker image gcr.io/${GCLOUD_PROJECT}/${APP}:${VERSION} on GCR"
    docker build --force-rm=true -t gcr.io/${GCLOUD_PROJECT}/${APP}:${VERSION} ${PROJECT_DIR}
    gcloud docker -- push gcr.io/${GCLOUD_PROJECT}/${APP}:${VERSION}

    docker tag gcr.io/${GCLOUD_PROJECT}/${APP}:${VERSION} gcr.io/${GCLOUD_PROJECT}/${APP}:latest
    gcloud docker -- push gcr.io/${GCLOUD_PROJECT}/${APP}:latest
  fi

}

deploy () {
  # Check if Deployment exists
  kubectl get deployment ${APP} &> /dev/null
  if [ $? -eq 0 ]; then
    upgrade_deployment
  else
    create_deployment
  fi
}

create_deployment() {
  # Create the Deployment and expose the Service
  if [ -z "${YAML}" ]; then
    echo "Creating default Deployment ${ZONE}/${GCLOUD_PROJECT}/${CLUSTER}/${APP}"
    kubectl run ${APP} --image=gcr.io/${GCLOUD_PROJECT}/${APP}:${VERSION} --port=80 --image-pull-policy=Always
  else
    echo "Creating YAML Deployment ${ZONE}/${GCLOUD_PROJECT}/${CLUSTER}/${APP} from ${YAML}"
    cat ${YAML} | sed -e "s/DEPLOY_TRIGGER/${VERSION}/g" | kubectl create -f -
  fi

  echo "Creating Load Balancer service ${ZONE}/${GCLOUD_PROJECT}/${CLUSTER}/${APP}"
  kubectl expose deployment ${APP} --target-port=80 --type="NodePort" &> /dev/null
}

upgrade_deployment() {
  # Upgrade the image version of the Deployment
  echo "Upgrading deployment ${ZONE}/${GCLOUD_PROJECT}/${CLUSTER}/${APP} to version latest:${VERSION}"
  cat ${YAML} | sed -e "s/DEPLOY_TRIGGER/${VERSION}/g" | kubectl apply -f -
}

scale_deployment() {
  # Scale the replicas of the Deployment
  echo "Scaling deployment ${ZONE}/${GCLOUD_PROJECT}/${CLUSTER}/${APP} to ${NUM} replicas"
  kubectl scale deployment ${APP} --replicas=${NUM}
}

cloudsql() {
  docker pull gcr.io/cloudsql-docker/gce-proxy:1.09
  docker ps -a -q --filter ancestor=gcr.io/cloudsql-docker/gce-proxy:1.09 --format="{{.ID}}" | xargs docker stop | xargs docker rm
  docker run -d -v /cloudsql:/cloudsql -v ${KEY}:/config -p 127.0.0.1:6543:6543 gcr.io/cloudsql-docker/gce-proxy:1.09 /cloud_sql_proxy -instances=${GCLOUD_PROJECT}:us-east1:${APP}=tcp:0.0.0.0:6543 -credential_file=/config
}

console() {
  open http://localhost:8001/ui
  kubectl proxy
}

ssh() {
  CONTAINER_ID=$(kubectl get pods | grep ${PROJECT} | grep Running | awk '{print $1}' | head -1)
  kubectl exec -it ${CONTAINER_ID} bash
}

pool() {
    gcloud container node-pools create n1-standard-2 \
        --cluster kubernetes \
        --machine-type n1-standard-2 \
        --image-type COS \
        --disk-size 100 \
        --num-nodes 2 \
        --scopes compute-rw,storage-rw,sql-admin
}
main () {
#  set -o errexit

  # Initialize the environment
  init

  # Process ACTION
  if [ ${ACTION} == 'deploy' ]; then
    build_image
    deploy
  elif [ ${ACTION} == 'build' ]; then
    build_image
  elif [ ${ACTION} == 'scale' ]; then
    scale_deployment
  elif [ ${ACTION} == 'console' ]; then
    console
  elif [ ${ACTION} == 'cloudsql' ]; then
    cloudsql
  elif [ ${ACTION} == 'ssh' ]; then
    ssh
  elif [ ${ACTION} == 'help' ]; then
    :
  else
    echo "Invalid argument ACTION=${ACTION}"
    exit 1
  fi

  set +o errexit
}
main
