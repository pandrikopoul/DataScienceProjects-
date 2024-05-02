# Cloud Computing Assignment 2023
## Group 12

### Add secret to k8s
```bash
kubectl create secret generic auth --from-file=<path to auth folder>
```

### Make rest-api accessible from Browser
docker run --rm -d --name nginx-proxy -p 80:80 --network minikube nginx:alpine /bin/sh -c 'echo "server {
    listen       80;
    server_name  34.249.240.171;
    location / {
        proxy_pass http://192.168.49.2:30674;
    }
}" > /etc/nginx/conf.d/my_rest_api.conf && nginx -g "daemon off;"'

