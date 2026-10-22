# Exercise 1: Hello Pod

## Objective
Deploy an NGINX pod in Kubernetes and access the application.

## Environment
- Kubernetes playground: Killercoda
- Container image: nginx
- Pod name: hello-k8s
- Service type: NodePort

## Steps performed

### 1. Create the pod
`kubectl run hello-k8s --image=nginx --port=80`

### 2. Verify the pod
`kubectl get pods`

The pod reached `Running` status with `1/1` containers ready.

### 3. Expose the pod
`kubectl expose pod hello-k8s --type=NodePort --port=80`

### 4. Verify the service
`kubectl get services`

The service was created successfully with type `NodePort`.

### 5. Verify NGINX
`kubectl port-forward service/hello-k8s 8080:80`

`curl http://127.0.0.1:8080`

The curl request returned the default NGINX welcome HTML.

## Screenshots
- `screenshots/01-pod-running.png`
- `screenshots/02-service-created.png`
- `screenshots/03-nginx-verified.png`

## Result
Successfully created an NGINX pod, exposed it through a NodePort service, and verified the application response.
