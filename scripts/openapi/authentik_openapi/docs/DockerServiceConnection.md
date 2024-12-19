# DockerServiceConnection

DockerServiceConnection Serializer

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
**url** | **str** | Can be in the format of &#39;unix://&lt;path&gt;&#39; when connecting to a local docker daemon, or &#39;https://&lt;hostname&gt;:2376&#39; when connecting to a remote system. | 
**tls_verification** | **str** | CA which the endpoint&#39;s Certificate is verified against. Can be left empty for no validation. | [optional] 
**tls_authentication** | **str** | Certificate/Key used for authentication. Can be left empty for no authentication. | [optional] 

## Example

```python
from authentik_openapi.models.docker_service_connection import DockerServiceConnection

# TODO update the JSON string below
json = "{}"
# create an instance of DockerServiceConnection from a JSON string
docker_service_connection_instance = DockerServiceConnection.from_json(json)
# print the JSON string representation of the object
print(DockerServiceConnection.to_json())

# convert the object into a dict
docker_service_connection_dict = docker_service_connection_instance.to_dict()
# create an instance of DockerServiceConnection from a dict
docker_service_connection_from_dict = DockerServiceConnection.from_dict(docker_service_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


