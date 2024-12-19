# ServiceConnection

ServiceConnection Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**name** | **str** |  | 
**local** | **bool** | If enabled, use the local connection. Required Docker socket/Kubernetes Integration | [optional] 
**component** | **str** | Return component used to edit this object | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 

## Example

```python
from authentik_openapi.models.service_connection import ServiceConnection

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceConnection from a JSON string
service_connection_instance = ServiceConnection.from_json(json)
# print the JSON string representation of the object
print(ServiceConnection.to_json())

# convert the object into a dict
service_connection_dict = service_connection_instance.to_dict()
# create an instance of ServiceConnection from a dict
service_connection_from_dict = ServiceConnection.from_dict(service_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


