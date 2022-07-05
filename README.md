Once microservice setup need to create images:
docker build --tag "tagname" . #. means here
docker image tag "tagname" "yourdockerrepo:tagname"

Push image to repo
docker push "yourdockerrepo":tagnam
