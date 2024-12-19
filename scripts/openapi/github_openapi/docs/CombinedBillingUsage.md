# CombinedBillingUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days_left_in_billing_cycle** | **int** | Numbers of days left in billing cycle. | 
**estimated_paid_storage_for_month** | **int** | Estimated storage space (GB) used in billing cycle. | 
**estimated_storage_for_month** | **int** | Estimated sum of free and paid storage space (GB) used in billing cycle. | 

## Example

```python
from github_openapi.models.combined_billing_usage import CombinedBillingUsage

# TODO update the JSON string below
json = "{}"
# create an instance of CombinedBillingUsage from a JSON string
combined_billing_usage_instance = CombinedBillingUsage.from_json(json)
# print the JSON string representation of the object
print(CombinedBillingUsage.to_json())

# convert the object into a dict
combined_billing_usage_dict = combined_billing_usage_instance.to_dict()
# create an instance of CombinedBillingUsage from a dict
combined_billing_usage_from_dict = CombinedBillingUsage.from_dict(combined_billing_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


