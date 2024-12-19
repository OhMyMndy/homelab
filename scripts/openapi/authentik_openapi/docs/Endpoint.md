# Endpoint

Endpoint Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**name** | **str** |  | 
**provider** | **int** |  | 
**provider_obj** | [**RACProvider**](RACProvider.md) |  | [readonly] 
**protocol** | [**ProtocolEnum**](ProtocolEnum.md) |  | 
**host** | **str** |  | 
**settings** | **object** |  | [optional] 
**property_mappings** | **List[str]** |  | [optional] 
**auth_mode** | [**AuthModeEnum**](AuthModeEnum.md) |  | 
**launch_url** | **str** | Build actual launch URL (the provider itself does not have one, just individual endpoints) | [readonly] 
**maximum_connections** | **int** |  | [optional] 

## Example

```python
from authentik_openapi.models.endpoint import Endpoint

# TODO update the JSON string below
json = "{}"
# create an instance of Endpoint from a JSON string
endpoint_instance = Endpoint.from_json(json)
# print the JSON string representation of the object
print(Endpoint.to_json())

# convert the object into a dict
endpoint_dict = endpoint_instance.to_dict()
# create an instance of Endpoint from a dict
endpoint_from_dict = Endpoint.from_dict(endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


