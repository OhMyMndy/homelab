# SecretScanningPushProtectionBypass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | [**SecretScanningPushProtectionBypassReason**](SecretScanningPushProtectionBypassReason.md) |  | [optional] 
**expire_at** | **datetime** | The time that the bypass will expire in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
**token_type** | **str** | The token type this bypass is for. | [optional] 

## Example

```python
from github_openapi.models.secret_scanning_push_protection_bypass import SecretScanningPushProtectionBypass

# TODO update the JSON string below
json = "{}"
# create an instance of SecretScanningPushProtectionBypass from a JSON string
secret_scanning_push_protection_bypass_instance = SecretScanningPushProtectionBypass.from_json(json)
# print the JSON string representation of the object
print(SecretScanningPushProtectionBypass.to_json())

# convert the object into a dict
secret_scanning_push_protection_bypass_dict = secret_scanning_push_protection_bypass_instance.to_dict()
# create an instance of SecretScanningPushProtectionBypass from a dict
secret_scanning_push_protection_bypass_from_dict = SecretScanningPushProtectionBypass.from_dict(secret_scanning_push_protection_bypass_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


