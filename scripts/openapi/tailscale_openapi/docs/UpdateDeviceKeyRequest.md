# UpdateDeviceKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_expiry_disabled** | **bool** | - If &#x60;true&#x60;, disable the device&#39;s key expiry. The original key expiry time is still maintained. Upon re-enabling, the key will expire at that original time. - If &#x60;false&#x60;, enable the device&#39;s key expiry. Sets the key to expire at the original expiry time prior to disabling. The key may already have expired. In that case, the device must be re-authenticated.  | 

## Example

```python
from tailscale_openapi.models.update_device_key_request import UpdateDeviceKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDeviceKeyRequest from a JSON string
update_device_key_request_instance = UpdateDeviceKeyRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDeviceKeyRequest.to_json())

# convert the object into a dict
update_device_key_request_dict = update_device_key_request_instance.to_dict()
# create an instance of UpdateDeviceKeyRequest from a dict
update_device_key_request_from_dict = UpdateDeviceKeyRequest.from_dict(update_device_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


