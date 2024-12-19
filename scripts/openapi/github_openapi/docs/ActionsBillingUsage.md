# ActionsBillingUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_minutes_used** | **int** | The sum of the free and paid GitHub Actions minutes used. | 
**total_paid_minutes_used** | **int** | The total paid GitHub Actions minutes used. | 
**included_minutes** | **int** | The amount of free GitHub Actions minutes available. | 
**minutes_used_breakdown** | [**ActionsBillingUsageMinutesUsedBreakdown**](ActionsBillingUsageMinutesUsedBreakdown.md) |  | 

## Example

```python
from github_openapi.models.actions_billing_usage import ActionsBillingUsage

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsBillingUsage from a JSON string
actions_billing_usage_instance = ActionsBillingUsage.from_json(json)
# print the JSON string representation of the object
print(ActionsBillingUsage.to_json())

# convert the object into a dict
actions_billing_usage_dict = actions_billing_usage_instance.to_dict()
# create an instance of ActionsBillingUsage from a dict
actions_billing_usage_from_dict = ActionsBillingUsage.from_dict(actions_billing_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


