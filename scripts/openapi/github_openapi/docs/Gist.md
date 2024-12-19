# Gist

Gist

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
**files** | [**Dict[str, GistFilesValue]**](GistFilesValue.md) |  | 
**public** | **bool** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**description** | **str** |  | 
**comments** | **int** |  | 
**user** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**comments_url** | **str** |  | 
**owner** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | [optional] 
**truncated** | **bool** |  | [optional] 
**forks** | **List[object]** |  | [optional] 
**history** | **List[object]** |  | [optional] 

## Example

```python
from github_openapi.models.gist import Gist

# TODO update the JSON string below
json = "{}"
# create an instance of Gist from a JSON string
gist_instance = Gist.from_json(json)
# print the JSON string representation of the object
print(Gist.to_json())

# convert the object into a dict
gist_dict = gist_instance.to_dict()
# create an instance of Gist from a dict
gist_from_dict = Gist.from_dict(gist_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


