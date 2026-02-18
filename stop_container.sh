#!/bin/bash

# Stop and remove existing container if running
if [ "$(docker ps -q -f name=musician-app)" ]; then
  echo "Stopping running musician-app container..."
  docker stop musician-app
  docker rm musician-app
  echo "Container stopped and removed."
else
  echo "No running musician-app container found. Skipping."
fi

# Remove old images to free up space (keep last 2)
echo "Cleaning up old Docker images..."
docker image prune -f
