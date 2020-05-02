### Simply flask application deployed using nginx (reverse proxy) and containerized using dockerfile and deployed to kubernetes using minikube

Steps:

1. Prerequisites::
- Ubuntu Host System
- Minikube (latest)
- Virtualbox
- Helm
- Dockerhub account
- Github account

2. Setup::
- Install minikube and enable the following addons:
   - helm-tiller
   - ingress-dns
- Install stable/jenkins (official jenkins chart) using helm install command.
- Install Kubernetes, Docker jenkins plugins form within jenkins dashboard.
- Check that you can connect to kubernetes from jenkins system settings section.
- generate an access token in dockerhub and add it as a jenkins security credential.
- use the fabric8-rbac.yaml to create a cluster role and bind the default user to that role, adjust to meet your permission targets.
- run ```minikube tunnel``` to allow the created service to get an extenal ip address when created.

3. Deploy and test::
- use the Jenkinsfile to test your setup and adjust the code to align with your aim.
- the following files should also be adjusted to your workflow:
  - deployment.yaml, service.yaml and used to create a deployment and a service to expose that deployment.

4. In dashboard check for the allocated external ip for the created service and click to see your app