cp docker_vue/Dockerfile .

IMAGE_NAME="vue"
IMAGE_TAG="latest"

docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .


rm Dockerfile
