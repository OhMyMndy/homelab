# ActionsCacheListActionsCachesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**ref** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**last_accessed_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**size_in_bytes** | **int** |  | [optional] 

## Example

```python
from github_openapi.models.actions_cache_list_actions_caches_inner import ActionsCacheListActionsCachesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsCacheListActionsCachesInner from a JSON string
actions_cache_list_actions_caches_inner_instance = ActionsCacheListActionsCachesInner.from_json(json)
# print the JSON string representation of the object
print(ActionsCacheListActionsCachesInner.to_json())

# convert the object into a dict
actions_cache_list_actions_caches_inner_dict = actions_cache_list_actions_caches_inner_instance.to_dict()
# create an instance of ActionsCacheListActionsCachesInner from a dict
actions_cache_list_actions_caches_inner_from_dict = ActionsCacheListActionsCachesInner.from_dict(actions_cache_list_actions_caches_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


