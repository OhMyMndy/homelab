# SecretScanningCreatePushProtectionBypassRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | [**SecretScanningPushProtectionBypassReason**](SecretScanningPushProtectionBypassReason.md) |  | 
**placeholder_id** | **str** | The ID of the push protection bypass placeholder. This value is returned on any push protected routes. | 

## Example

```python
from github_openapi.models.secret_scanning_create_push_protection_bypass_request import SecretScanningCreatePushProtectionBypassRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SecretScanningCreatePushProtectionBypassRequest from a JSON string
secret_scanning_create_push_protection_bypass_request_instance = SecretScanningCreatePushProtectionBypassRequest.from_json(json)
# print the JSON string representation of the object
print(SecretScanningCreatePushProtectionBypassRequest.to_json())

# convert the object into a dict
secret_scanning_create_push_protection_bypass_request_dict = secret_scanning_create_push_protection_bypass_request_instance.to_dict()
# create an instance of SecretScanningCreatePushProtectionBypassRequest from a dict
secret_scanning_create_push_protection_bypass_request_from_dict = SecretScanningCreatePushProtectionBypassRequest.from_dict(secret_scanning_create_push_protection_bypass_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


