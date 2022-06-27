# Output of `kubectl get pods,svc`

mac@macs-MacBook-Pro labs % kubectl get pods,svc
NAME                                   READY   STATUS    RESTARTS   AGE
pod/python-app-node-864958b595-wbplt   1/1     Running   0          10m

NAME                      TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
service/kubernetes        ClusterIP      10.96.0.1       <none>        443/TCP        34m
service/python-app-node   LoadBalancer   10.102.72.120   <pending>     80:32131/TCP   10m


![output](../images/kubectl_get_pods_svc.png)

# Using yml files

- Ouput of `kubectl get pods, svc`: 

mac@macs-MacBook-Pro labs % kubectl get pods,svc
NAME                                        READY   STATUS    RESTARTS   AGE
pod/python-app-deployment-c6cf58f46-9xjn5   1/1     Running   0          11m
pod/python-app-deployment-c6cf58f46-mkndh   1/1     Running   0          11m
pod/python-app-deployment-c6cf58f46-x6j4b   1/1     Running   0          11m

NAME                            TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
service/kubernetes              ClusterIP      10.96.0.1        <none>        443/TCP        71m
service/my-service              NodePort       10.103.209.168   <none>        80:31019/TCP   11m
service/python-app-deployment   LoadBalancer   10.109.44.162    <pending>     80:32141/TCP   67m
mac@macs-MacBook-Pro labs % 

![kubectl get pods svc](../images/yml_get_pods_svc.png)


