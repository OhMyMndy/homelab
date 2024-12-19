# ActionsBillingUsageMinutesUsedBreakdown


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ubuntu** | **int** | Total minutes used on Ubuntu runner machines. | [optional] 
**macos** | **int** | Total minutes used on macOS runner machines. | [optional] 
**windows** | **int** | Total minutes used on Windows runner machines. | [optional] 
**ubuntu_4_core** | **int** | Total minutes used on Ubuntu 4 core runner machines. | [optional] 
**ubuntu_8_core** | **int** | Total minutes used on Ubuntu 8 core runner machines. | [optional] 
**ubuntu_16_core** | **int** | Total minutes used on Ubuntu 16 core runner machines. | [optional] 
**ubuntu_32_core** | **int** | Total minutes used on Ubuntu 32 core runner machines. | [optional] 
**ubuntu_64_core** | **int** | Total minutes used on Ubuntu 64 core runner machines. | [optional] 
**windows_4_core** | **int** | Total minutes used on Windows 4 core runner machines. | [optional] 
**windows_8_core** | **int** | Total minutes used on Windows 8 core runner machines. | [optional] 
**windows_16_core** | **int** | Total minutes used on Windows 16 core runner machines. | [optional] 
**windows_32_core** | **int** | Total minutes used on Windows 32 core runner machines. | [optional] 
**windows_64_core** | **int** | Total minutes used on Windows 64 core runner machines. | [optional] 
**macos_12_core** | **int** | Total minutes used on macOS 12 core runner machines. | [optional] 
**total** | **int** | Total minutes used on all runner machines. | [optional] 

## Example

```python
from github_openapi.models.actions_billing_usage_minutes_used_breakdown import ActionsBillingUsageMinutesUsedBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsBillingUsageMinutesUsedBreakdown from a JSON string
actions_billing_usage_minutes_used_breakdown_instance = ActionsBillingUsageMinutesUsedBreakdown.from_json(json)
# print the JSON string representation of the object
print(ActionsBillingUsageMinutesUsedBreakdown.to_json())

# convert the object into a dict
actions_billing_usage_minutes_used_breakdown_dict = actions_billing_usage_minutes_used_breakdown_instance.to_dict()
# create an instance of ActionsBillingUsageMinutesUsedBreakdown from a dict
actions_billing_usage_minutes_used_breakdown_from_dict = ActionsBillingUsageMinutesUsedBreakdown.from_dict(actions_billing_usage_minutes_used_breakdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


