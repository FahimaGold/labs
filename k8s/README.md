# Output of `kubectl get pods,svc`

mac@macs-MacBook-Pro labs % kubectl get pods,svc
NAME                                   READY   STATUS    RESTARTS   AGE
pod/python-app-node-864958b595-wbplt   1/1     Running   0          10m

NAME                      TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)        AGE
service/kubernetes        ClusterIP      10.96.0.1       <none>        443/TCP        34m
service/python-app-node   LoadBalancer   10.102.72.120   <pending>     80:32131/TCP   10m


![output](../images/kubectl_get_pods_svc.png)
