#!/bin/bash

# Pull latest image from ECR
echo "Pulling latest Docker image..."
docker pull $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$IMAGE_REPO_NAME:latest

# Run the container
echo "Starting musician-app container..."
docker run -d \
  --name musician-app \
  --restart unless-stopped \
  -p 5000:5000 \
  $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$IMAGE_REPO_NAME:latest

echo "Container started successfully!"
docker ps | grep musician-app
