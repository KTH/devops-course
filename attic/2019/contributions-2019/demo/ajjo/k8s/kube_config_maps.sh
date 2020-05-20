# Create a ConfigMap, example-vault-agent-config
kubectl create configmap example-vault-agent-config --from-file=./configs-k8s/

# View the created ConfigMap
kubectl get configmap example-vault-agent-config -o yaml
