# GitRef

Git references within a repository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | **str** |  | 
**node_id** | **str** |  | 
**url** | **str** |  | 
**object** | [**GitRefObject**](GitRefObject.md) |  | 

## Example

```python
from github_openapi.models.git_ref import GitRef

# TODO update the JSON string below
json = "{}"
# create an instance of GitRef from a JSON string
git_ref_instance = GitRef.from_json(json)
# print the JSON string representation of the object
print(GitRef.to_json())

# convert the object into a dict
git_ref_dict = git_ref_instance.to_dict()
# create an instance of GitRef from a dict
git_ref_from_dict = GitRef.from_dict(git_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


