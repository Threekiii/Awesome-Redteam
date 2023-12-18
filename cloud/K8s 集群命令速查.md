# K8s 集群命令速查

## Kubernetes 简介

Kubernetes 是当今最流行的容器编排工具之一，为企业应用部署和管理提供了高效、稳定的解决方案。

Kubernetes 容器集是一个或多个 Linux® 容器的集合，也是 Kubernetes 应用的最小单位。任何一个的容器集可以由多个紧密耦合的容器组成（高级用例），也可以由单个容器组成（更常见的用例）。

Pod 是Kubernetes 中可部署的最小、最基本对象。 一个Pod 代表集群中正在运行的单个进程实例。 Pod 包含一个或多个容器，例如Docker 容器。 当Pod 运行多个容器时，这些容器将作为一个实体进行管理并共用Pod 的资源。

参考链接：

- https://mp.weixin.qq.com/s/gupDTwhJ-krCJmUzDq6p9Q 【K8s安全】集群信息收集一篇通

## 方法和技巧

收集Kubernetes集群信息的方法和技巧：

1. 收集物理资源信息：通过使用工具（如Prometheus）来监控节点、CPU、内存等物理资源的利用率，以及检查硬件故障。 
2. 收集日志信息：通过使用工具（如ELK Stack或Fluentd）来聚合、搜索和分析各个组件的日志，快速识别和解决问题。 
3. 收集网络信息：使用工具（如Weave Scope或Cilium）来监视容器之间的网络通信，并检查网络连接和流量是否正常。 
4. 收集安全信息：使用工具（如Kube-Bench）来检测Kubernetes集群是否符合最佳实践和安全标准，并发现潜在的安全漏洞和风险。 
5. 收集运行时信息：使用工具（如Datadog或Sysdig）来监控Kubernetes集群中的容器应用程序运行状态，以便实时发现和修复问题。

## 外部信息收集

### 集群信息

```
kubectl cluster-info
```

### 集群列表

```
kubectl config get-clusters
```

### 用户列表

```
kubectl config get-contexts
```

### 环境变量

```
env
```

```
env | grep KUBE
```

### 配置信息

```
# /home/r00t/.kube/config 是 env | grep KUBE的输出结果
cat /home/r00t/.kube/config
```

### 节点信息

```
# 节点列表
kubectl get nodes
```

```
# node1地址
ping node1 -c 1
```

```
# node2地址
ping node2 -c 1
```

### 资源列表

```
kubectl get all
```

### 命名空间

```
kubectl get namespaces
```

### Pod 信息

```
# 获取Pod
kubectl get pod
```

```
# Pod详细信息
kubectl describe pod <PodName>
```

```
# yaml格式显示Pod的详细信息
kubectl get pod <pod-name> -o yaml
```

```
# 获取所有pod信息
kubectl get pods --all-namespaces -o wide
```

### 服务信息

```
kubectl get service
```

```
kubectl describe service <ServiceName>
```

### Deployment 信息

```
# deployment基础信息
kubectl get deployment
```

```
# deployment详细信息
kubectl describe deployment <deploymentName>
```

### 日志信息

```
# 系统日志
cat /var/log/messages
```

```
# 组件日志
journalctl -u kube-apiserver
journalctl -u kube-scheduler
journalctl -u kubelet |tail
```

```
# 容器日志
docker logs <容器ID>
```

### SSH 私钥

```
ls -al ~/
ls -al ~/.ssh
cat ~/.ssh/id_rsa
```

### 历史命令

```
# 检索敏感历史连接记录以及连接账户密码信息
cat ~/.bash_history
```

### 面板相关

```
# 查看面板pod和service状态
kubectl get pods,svc -n kubernetes-dashboard -o wide
```

```
# 查看serviceaccount和secrets
kubectl get sa,secrets -n kubernetes-dashboard
```

```
# 查看token
kubectl describe secrets kubernetes-dashboard-token-8kxnh -n kubernetes-dashboard
```

```
# 查看token
kubectl describe secret admin-myuser-token-jcj9d -n kubernetes-dashboard
```

## 内部信息

### 环境信息

```
env
```

```
env | grep KUBERNETES
```

### 容器检测

```
ls -al
```

### 内核版本

```
# 需要下载kubectl到pod中，再执行以下命令来获取node节点的内核版本信息
kubectl get nodes -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.nodeInfo.kernelVersion}{"\n"}{end}'
```

### Token

K8s 集群创建的 Pod 中容器内部默认携带 K8s Service Account 认证凭据`/run/secrets/kubernetes.io/serviceaccount/token`，利用该凭据可以认证 K8s API-Server 服务器并访问高权限接口，如果执行成功意味着该账号拥有高权限，可以直接利用 Service Account 管理 K8s 集群。

```
cat /var/run/secrets/kuberenetes.io/serviceaccount/token
```

### Secret

K8s Secrets 用于存储敏感数据，从 Secrets 中获取的 AK 及通信凭证可用户后续渗透中从外部或云产品 API 窃取信息。

```
#命令格式
./cdk run k8s-secret-dump (auto|<service-account-token-path>)
    
#使用实例
./cdk run k8s-secret-dump auto
```

### 安全策略

对于已经获取了 kubeconfig 或 sa 账号权限，进而想要创建特殊配置的容器，但是受到了 K8s Pod Security Policies 的限制时可以使用这个 Exploit 获取 Pod Security Policies 的规则信息。

```
#命令格式
./cdk run k8s-psp-dump (auto|<service-account-token-path>

#使用实例
./cdk run k8s-psp-dump auto
2021/03/24 22:15:58 getting K8s api-server API addr.
  Find K8s api-server in ENV: https://ip:8443
2021/03/24 22:15:58 trying to dump K8s Pod Security Policies with local service-account: token
2021/03/24 22:15:58 requesting  /apis/policy/v1beta1/podsecuritypolicies
2021/03/24 22:15:58 dump Pod Security Policies success, saved in:  k8s_pod_security_policies.json
2021/03/24 22:15:58 requesting  /api/v1/namespaces/default/pods
2021/03/24 22:15:58 K8S Pod Security Policies rule list:
2021/03/24 22:15:58 rule { securityContext.hostPID: true } is not allowed.
2021/03/24 22:15:58 rule { securityContext.hostIPC: true } is not allowed.
2021/03/24 22:15:58 rule { volumes[0].hostPath.pathPrefix: \"/proc\" } is not allowed.
2021/03/24 22:15:58 rule { volumes[1].hostPath.pathPrefix: \"/dev\" } is not allowed.
2021/03/24 22:15:58 rule { volumes[2].hostPath.pathPrefix: \"/sys\" } is not allowed.
2021/03/24 22:15:58 rule { volumes[3].hostPath.pathPrefix: \"/\" } is not allowed.
2021/03/24 22:15:58 rule { containers[0].securityContext.capabilities.add: \"SYS_ADMIN\" } is not allowed.
2021/03/24 22:15:58 rule { containers[0].securityContext.capabilities.add: \"SYS_PTRACE\" } is not allowed.
```

### 内部网络

- Flannel默认使用 10.244.0.0/16 网络
- Calico默认使用192.168.0.0/16 网络