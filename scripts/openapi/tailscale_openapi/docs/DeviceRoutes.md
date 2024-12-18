# DeviceRoutes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertised_routes** | **List[str]** | The subnets this device requests to expose.  | [optional] 
**enabled_routes** | **List[str]** | The subnet routes for this device that have been approved by a tailnet admin.  | [optional] 

## Example

```python
from tailscale_openapi.models.device_routes import DeviceRoutes

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceRoutes from a JSON string
device_routes_instance = DeviceRoutes.from_json(json)
# print the JSON string representation of the object
print(DeviceRoutes.to_json())

# convert the object into a dict
device_routes_dict = device_routes_instance.to_dict()
# create an instance of DeviceRoutes from a dict
device_routes_from_dict = DeviceRoutes.from_dict(device_routes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


