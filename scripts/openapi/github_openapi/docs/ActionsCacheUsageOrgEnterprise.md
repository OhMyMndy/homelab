# ActionsCacheUsageOrgEnterprise


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_active_caches_count** | **int** | The count of active caches across all repositories of an enterprise or an organization. | 
**total_active_caches_size_in_bytes** | **int** | The total size in bytes of all active cache items across all repositories of an enterprise or an organization. | 

## Example

```python
from github_openapi.models.actions_cache_usage_org_enterprise import ActionsCacheUsageOrgEnterprise

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsCacheUsageOrgEnterprise from a JSON string
actions_cache_usage_org_enterprise_instance = ActionsCacheUsageOrgEnterprise.from_json(json)
# print the JSON string representation of the object
print(ActionsCacheUsageOrgEnterprise.to_json())

# convert the object into a dict
actions_cache_usage_org_enterprise_dict = actions_cache_usage_org_enterprise_instance.to_dict()
# create an instance of ActionsCacheUsageOrgEnterprise from a dict
actions_cache_usage_org_enterprise_from_dict = ActionsCacheUsageOrgEnterprise.from_dict(actions_cache_usage_org_enterprise_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


