# PatchedDockerServiceConnectionRequest

DockerServiceConnection Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**local** | **bool** | If enabled, use the local connection. Required Docker socket/Kubernetes Integration | [optional] 
**url** | **str** | Can be in the format of &#39;unix://&lt;path&gt;&#39; when connecting to a local docker daemon, or &#39;https://&lt;hostname&gt;:2376&#39; when connecting to a remote system. | [optional] 
**tls_verification** | **str** | CA which the endpoint&#39;s Certificate is verified against. Can be left empty for no validation. | [optional] 
**tls_authentication** | **str** | Certificate/Key used for authentication. Can be left empty for no authentication. | [optional] 

## Example

```python
from authentik_openapi.models.patched_docker_service_connection_request import PatchedDockerServiceConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedDockerServiceConnectionRequest from a JSON string
patched_docker_service_connection_request_instance = PatchedDockerServiceConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedDockerServiceConnectionRequest.to_json())

# convert the object into a dict
patched_docker_service_connection_request_dict = patched_docker_service_connection_request_instance.to_dict()
# create an instance of PatchedDockerServiceConnectionRequest from a dict
patched_docker_service_connection_request_from_dict = PatchedDockerServiceConnectionRequest.from_dict(patched_docker_service_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


