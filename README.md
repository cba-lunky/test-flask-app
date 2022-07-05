Once microservice setup need to create images:
docker build --tag "tagname" . #. means here
docker build -t cbadebeysja/flask-service-getto:python-docker-be2-amd64 --build-arg ARCH=amd64/ .
docker image tag "tagname" "yourdockerrepo:tagname"

Push image to repo
docker push "yourdockerrepo":tagnam
