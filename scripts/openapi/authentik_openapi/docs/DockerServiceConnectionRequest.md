# DockerServiceConnectionRequest

DockerServiceConnection Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**local** | **bool** | If enabled, use the local connection. Required Docker socket/Kubernetes Integration | [optional] 
**url** | **str** | Can be in the format of &#39;unix://&lt;path&gt;&#39; when connecting to a local docker daemon, or &#39;https://&lt;hostname&gt;:2376&#39; when connecting to a remote system. | 
**tls_verification** | **str** | CA which the endpoint&#39;s Certificate is verified against. Can be left empty for no validation. | [optional] 
**tls_authentication** | **str** | Certificate/Key used for authentication. Can be left empty for no authentication. | [optional] 

## Example

```python
from authentik_openapi.models.docker_service_connection_request import DockerServiceConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DockerServiceConnectionRequest from a JSON string
docker_service_connection_request_instance = DockerServiceConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(DockerServiceConnectionRequest.to_json())

# convert the object into a dict
docker_service_connection_request_dict = docker_service_connection_request_instance.to_dict()
# create an instance of DockerServiceConnectionRequest from a dict
docker_service_connection_request_from_dict = DockerServiceConnectionRequest.from_dict(docker_service_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


