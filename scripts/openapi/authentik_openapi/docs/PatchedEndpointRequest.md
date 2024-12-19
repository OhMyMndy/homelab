# PatchedEndpointRequest

Endpoint Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**provider** | **int** |  | [optional] 
**protocol** | [**ProtocolEnum**](ProtocolEnum.md) |  | [optional] 
**host** | **str** |  | [optional] 
**settings** | **object** |  | [optional] 
**property_mappings** | **List[str]** |  | [optional] 
**auth_mode** | [**AuthModeEnum**](AuthModeEnum.md) |  | [optional] 
**maximum_connections** | **int** |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_endpoint_request import PatchedEndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedEndpointRequest from a JSON string
patched_endpoint_request_instance = PatchedEndpointRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedEndpointRequest.to_json())

# convert the object into a dict
patched_endpoint_request_dict = patched_endpoint_request_instance.to_dict()
# create an instance of PatchedEndpointRequest from a dict
patched_endpoint_request_from_dict = PatchedEndpointRequest.from_dict(patched_endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


