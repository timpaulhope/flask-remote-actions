#!/bin/bash
# This pulls the latest Home Assistant image and recreates the container 
echo "Stopping Home Assistant"
sudo docker-compose -f /path/to/docker/homeassistant/docker-compose.yml stop
echo "Pulling latest image"
sudo docker-compose -f /path/to/docker/homeassistant/docker-compose.yml pull
echo "Recreating Home Assistant"
sudo docker-compose -f /path/to/docker/homeassistant/docker-compose.yml up -d
echo "Home Assistant Updated"
