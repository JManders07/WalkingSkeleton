# WalkingSkeleton

## First you have to build the images for the consumer and producer
docker build -t consumer-image -f Dockerfile .
docker build -t producer-image -f Dockerfile .

## To start consumer docker container:
docker run --rm --name consumer --network="host" consumer-image

## To start producer docker container:
docker fun --rm --name producer --network="host" producer-image