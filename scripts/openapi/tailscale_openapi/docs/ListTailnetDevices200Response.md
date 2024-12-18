# ListTailnetDevices200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | [**List[Device]**](Device.md) |  | [optional] 

## Example

```python
from tailscale_openapi.models.list_tailnet_devices200_response import ListTailnetDevices200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListTailnetDevices200Response from a JSON string
list_tailnet_devices200_response_instance = ListTailnetDevices200Response.from_json(json)
# print the JSON string representation of the object
print(ListTailnetDevices200Response.to_json())

# convert the object into a dict
list_tailnet_devices200_response_dict = list_tailnet_devices200_response_instance.to_dict()
# create an instance of ListTailnetDevices200Response from a dict
list_tailnet_devices200_response_from_dict = ListTailnetDevices200Response.from_dict(list_tailnet_devices200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


