# Building Docker Images
Once microservice setup need to create images: <br>
docker build --tag "tagname" . #. means here <br>
docker build -t cbadebeysja/flask-service-getto:python-docker-be2-amd64 --build-arg ARCH=amd64/ . <br>
docker image tag "tagname" "yourdockerrepo:tagname" <br>

Push image to repo: <br>
docker push "yourdockerrepo":tagnam <br>

# Managing service/deployments
kubectl get deployments <br>
kubectl get svc <br>
kubectl get pods <br>
kubectl describe pods <br>
kubectl describe svc "name of service"
kubectl logs "name of pod" ["name of container"] <br>
