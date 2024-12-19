# BaseGist

Base Gist

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**forks_url** | **str** |  | 
**commits_url** | **str** |  | 
**id** | **str** |  | 
**node_id** | **str** |  | 
**git_pull_url** | **str** |  | 
**git_push_url** | **str** |  | 
**html_url** | **str** |  | 
**files** | [**Dict[str, BaseGistFilesValue]**](BaseGistFilesValue.md) |  | 
**public** | **bool** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**description** | **str** |  | 
**comments** | **int** |  | 
**user** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**comments_url** | **str** |  | 
**owner** | [**SimpleUser**](SimpleUser.md) |  | [optional] 
**truncated** | **bool** |  | [optional] 
**forks** | **List[object]** |  | [optional] 
**history** | **List[object]** |  | [optional] 

## Example

```python
from github_openapi.models.base_gist import BaseGist

# TODO update the JSON string below
json = "{}"
# create an instance of BaseGist from a JSON string
base_gist_instance = BaseGist.from_json(json)
# print the JSON string representation of the object
print(BaseGist.to_json())

# convert the object into a dict
base_gist_dict = base_gist_instance.to_dict()
# create an instance of BaseGist from a dict
base_gist_from_dict = BaseGist.from_dict(base_gist_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


