# ServiceConnectionRequest

ServiceConnection Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**local** | **bool** | If enabled, use the local connection. Required Docker socket/Kubernetes Integration | [optional] 

## Example

```python
from authentik_openapi.models.service_connection_request import ServiceConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceConnectionRequest from a JSON string
service_connection_request_instance = ServiceConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(ServiceConnectionRequest.to_json())

# convert the object into a dict
service_connection_request_dict = service_connection_request_instance.to_dict()
# create an instance of ServiceConnectionRequest from a dict
service_connection_request_from_dict = ServiceConnectionRequest.from_dict(service_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


