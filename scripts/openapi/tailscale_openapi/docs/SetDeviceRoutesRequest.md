# SetDeviceRoutesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**routes** | **List[str]** | The new list of enabled subnet routes.  | [optional] 

## Example

```python
from tailscale_openapi.models.set_device_routes_request import SetDeviceRoutesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetDeviceRoutesRequest from a JSON string
set_device_routes_request_instance = SetDeviceRoutesRequest.from_json(json)
# print the JSON string representation of the object
print(SetDeviceRoutesRequest.to_json())

# convert the object into a dict
set_device_routes_request_dict = set_device_routes_request_instance.to_dict()
# create an instance of SetDeviceRoutesRequest from a dict
set_device_routes_request_from_dict = SetDeviceRoutesRequest.from_dict(set_device_routes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


