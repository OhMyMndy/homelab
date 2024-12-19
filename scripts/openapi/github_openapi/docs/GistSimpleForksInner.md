# GistSimpleForksInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**user** | [**PublicUser**](PublicUser.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from github_openapi.models.gist_simple_forks_inner import GistSimpleForksInner

# TODO update the JSON string below
json = "{}"
# create an instance of GistSimpleForksInner from a JSON string
gist_simple_forks_inner_instance = GistSimpleForksInner.from_json(json)
# print the JSON string representation of the object
print(GistSimpleForksInner.to_json())

# convert the object into a dict
gist_simple_forks_inner_dict = gist_simple_forks_inner_instance.to_dict()
# create an instance of GistSimpleForksInner from a dict
gist_simple_forks_inner_from_dict = GistSimpleForksInner.from_dict(gist_simple_forks_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


