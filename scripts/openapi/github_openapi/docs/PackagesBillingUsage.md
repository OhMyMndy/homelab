# PackagesBillingUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_gigabytes_bandwidth_used** | **int** | Sum of the free and paid storage space (GB) for GitHuub Packages. | 
**total_paid_gigabytes_bandwidth_used** | **int** | Total paid storage space (GB) for GitHuub Packages. | 
**included_gigabytes_bandwidth** | **int** | Free storage space (GB) for GitHub Packages. | 

## Example

```python
from github_openapi.models.packages_billing_usage import PackagesBillingUsage

# TODO update the JSON string below
json = "{}"
# create an instance of PackagesBillingUsage from a JSON string
packages_billing_usage_instance = PackagesBillingUsage.from_json(json)
# print the JSON string representation of the object
print(PackagesBillingUsage.to_json())

# convert the object into a dict
packages_billing_usage_dict = packages_billing_usage_instance.to_dict()
# create an instance of PackagesBillingUsage from a dict
packages_billing_usage_from_dict = PackagesBillingUsage.from_dict(packages_billing_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


