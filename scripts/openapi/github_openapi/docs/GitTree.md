# GitTree

The hierarchy between files in a Git repository.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sha** | **str** |  | 
**url** | **str** |  | 
**truncated** | **bool** |  | 
**tree** | [**List[GitTreeTreeInner]**](GitTreeTreeInner.md) | Objects specifying a tree structure | 

## Example

```python
from github_openapi.models.git_tree import GitTree

# TODO update the JSON string below
json = "{}"
# create an instance of GitTree from a JSON string
git_tree_instance = GitTree.from_json(json)
# print the JSON string representation of the object
print(GitTree.to_json())

# convert the object into a dict
git_tree_dict = git_tree_instance.to_dict()
# create an instance of GitTree from a dict
git_tree_from_dict = GitTree.from_dict(git_tree_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


