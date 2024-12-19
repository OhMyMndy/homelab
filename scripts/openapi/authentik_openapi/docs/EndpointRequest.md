# EndpointRequest

Endpoint Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**provider** | **int** |  | 
**protocol** | [**ProtocolEnum**](ProtocolEnum.md) |  | 
**host** | **str** |  | 
**settings** | **object** |  | [optional] 
**property_mappings** | **List[str]** |  | [optional] 
**auth_mode** | [**AuthModeEnum**](AuthModeEnum.md) |  | 
**maximum_connections** | **int** |  | [optional] 

## Example

```python
from authentik_openapi.models.endpoint_request import EndpointRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointRequest from a JSON string
endpoint_request_instance = EndpointRequest.from_json(json)
# print the JSON string representation of the object
print(EndpointRequest.to_json())

# convert the object into a dict
endpoint_request_dict = endpoint_request_instance.to_dict()
# create an instance of EndpointRequest from a dict
endpoint_request_from_dict = EndpointRequest.from_dict(endpoint_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


