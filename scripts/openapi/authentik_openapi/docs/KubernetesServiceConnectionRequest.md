# KubernetesServiceConnectionRequest

KubernetesServiceConnection Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**local** | **bool** | If enabled, use the local connection. Required Docker socket/Kubernetes Integration | [optional] 
**kubeconfig** | **object** | Paste your kubeconfig here. authentik will automatically use the currently selected context. | [optional] 
**verify_ssl** | **bool** | Verify SSL Certificates of the Kubernetes API endpoint | [optional] 

## Example

```python
from authentik_openapi.models.kubernetes_service_connection_request import KubernetesServiceConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesServiceConnectionRequest from a JSON string
kubernetes_service_connection_request_instance = KubernetesServiceConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(KubernetesServiceConnectionRequest.to_json())

# convert the object into a dict
kubernetes_service_connection_request_dict = kubernetes_service_connection_request_instance.to_dict()
# create an instance of KubernetesServiceConnectionRequest from a dict
kubernetes_service_connection_request_from_dict = KubernetesServiceConnectionRequest.from_dict(kubernetes_service_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


