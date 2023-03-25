#!/bin/bash

######################################
## Shell Script to Build Docker Image
######################################

# Build for ARM64 
docker build --platform=linux/arm64 --pull --rm -f "Dockerfile" -t plex-mqtt-connector:latest-arm64 "."

# Build for AMD64
docker build --platform=linux/amd64 --pull --rm -f "Dockerfile" -t plex-mqtt-connector:latest-amd64 "."

# Tag and push ARM64
docker tag plex-mqtt-connector:latest-arm64 pyronox/plex-mqtt-connector:latest-arm64
docker push pyronox/plex-mqtt-connector:latest-arm64

# Tag and push ARM64
docker tag plex-mqtt-connector:latest-amd64 pyronox/plex-mqtt-connector:latest-amd64
docker push pyronox/plex-mqtt-connector:latest-amd64
