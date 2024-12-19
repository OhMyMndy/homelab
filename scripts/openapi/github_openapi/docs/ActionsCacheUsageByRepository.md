# ActionsCacheUsageByRepository

GitHub Actions Cache Usage by repository.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_name** | **str** | The repository owner and name for the cache usage being shown. | 
**active_caches_size_in_bytes** | **int** | The sum of the size in bytes of all the active cache items in the repository. | 
**active_caches_count** | **int** | The number of active caches in the repository. | 

## Example

```python
from github_openapi.models.actions_cache_usage_by_repository import ActionsCacheUsageByRepository

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsCacheUsageByRepository from a JSON string
actions_cache_usage_by_repository_instance = ActionsCacheUsageByRepository.from_json(json)
# print the JSON string representation of the object
print(ActionsCacheUsageByRepository.to_json())

# convert the object into a dict
actions_cache_usage_by_repository_dict = actions_cache_usage_by_repository_instance.to_dict()
# create an instance of ActionsCacheUsageByRepository from a dict
actions_cache_usage_by_repository_from_dict = ActionsCacheUsageByRepository.from_dict(actions_cache_usage_by_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


