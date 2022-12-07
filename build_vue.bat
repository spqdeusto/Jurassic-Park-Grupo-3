@echo off

COPY  "docker_vue\Dockerfile" "."
SET IMAGE_NAME=vue
SET IMAGE_TAG=latest
docker "build" "-t" "%IMAGE_NAME%:%IMAGE_TAG%" "."
DEL  "Dockerfile"
