# ActionsCacheList

Repository actions caches

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | Total number of caches | 
**actions_caches** | [**List[ActionsCacheListActionsCachesInner]**](ActionsCacheListActionsCachesInner.md) | Array of caches | 

## Example

```python
from github_openapi.models.actions_cache_list import ActionsCacheList

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsCacheList from a JSON string
actions_cache_list_instance = ActionsCacheList.from_json(json)
# print the JSON string representation of the object
print(ActionsCacheList.to_json())

# convert the object into a dict
actions_cache_list_dict = actions_cache_list_instance.to_dict()
# create an instance of ActionsCacheList from a dict
actions_cache_list_from_dict = ActionsCacheList.from_dict(actions_cache_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


