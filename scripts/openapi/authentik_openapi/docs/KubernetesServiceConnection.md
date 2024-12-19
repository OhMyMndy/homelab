# KubernetesServiceConnection

KubernetesServiceConnection Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**name** | **str** |  | 
**local** | **bool** | If enabled, use the local connection. Required Docker socket/Kubernetes Integration | [optional] 
**component** | **str** |  | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**kubeconfig** | **object** | Paste your kubeconfig here. authentik will automatically use the currently selected context. | [optional] 
**verify_ssl** | **bool** | Verify SSL Certificates of the Kubernetes API endpoint | [optional] 

## Example

```python
from authentik_openapi.models.kubernetes_service_connection import KubernetesServiceConnection

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesServiceConnection from a JSON string
kubernetes_service_connection_instance = KubernetesServiceConnection.from_json(json)
# print the JSON string representation of the object
print(KubernetesServiceConnection.to_json())

# convert the object into a dict
kubernetes_service_connection_dict = kubernetes_service_connection_instance.to_dict()
# create an instance of KubernetesServiceConnection from a dict
kubernetes_service_connection_from_dict = KubernetesServiceConnection.from_dict(kubernetes_service_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


