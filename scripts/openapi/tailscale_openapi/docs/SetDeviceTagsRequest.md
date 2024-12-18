# SetDeviceTagsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **List[str]** | The new list of tags for the device.  | [optional] 

## Example

```python
from tailscale_openapi.models.set_device_tags_request import SetDeviceTagsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetDeviceTagsRequest from a JSON string
set_device_tags_request_instance = SetDeviceTagsRequest.from_json(json)
# print the JSON string representation of the object
print(SetDeviceTagsRequest.to_json())

# convert the object into a dict
set_device_tags_request_dict = set_device_tags_request_instance.to_dict()
# create an instance of SetDeviceTagsRequest from a dict
set_device_tags_request_from_dict = SetDeviceTagsRequest.from_dict(set_device_tags_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


