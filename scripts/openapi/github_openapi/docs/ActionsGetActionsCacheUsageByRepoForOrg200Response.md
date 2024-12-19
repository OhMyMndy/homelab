# ActionsGetActionsCacheUsageByRepoForOrg200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**repository_cache_usages** | [**List[ActionsCacheUsageByRepository]**](ActionsCacheUsageByRepository.md) |  | 

## Example

```python
from github_openapi.models.actions_get_actions_cache_usage_by_repo_for_org200_response import ActionsGetActionsCacheUsageByRepoForOrg200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsGetActionsCacheUsageByRepoForOrg200Response from a JSON string
actions_get_actions_cache_usage_by_repo_for_org200_response_instance = ActionsGetActionsCacheUsageByRepoForOrg200Response.from_json(json)
# print the JSON string representation of the object
print(ActionsGetActionsCacheUsageByRepoForOrg200Response.to_json())

# convert the object into a dict
actions_get_actions_cache_usage_by_repo_for_org200_response_dict = actions_get_actions_cache_usage_by_repo_for_org200_response_instance.to_dict()
# create an instance of ActionsGetActionsCacheUsageByRepoForOrg200Response from a dict
actions_get_actions_cache_usage_by_repo_for_org200_response_from_dict = ActionsGetActionsCacheUsageByRepoForOrg200Response.from_dict(actions_get_actions_cache_usage_by_repo_for_org200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


