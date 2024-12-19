# FileCommitCommitTree


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**sha** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.file_commit_commit_tree import FileCommitCommitTree

# TODO update the JSON string below
json = "{}"
# create an instance of FileCommitCommitTree from a JSON string
file_commit_commit_tree_instance = FileCommitCommitTree.from_json(json)
# print the JSON string representation of the object
print(FileCommitCommitTree.to_json())

# convert the object into a dict
file_commit_commit_tree_dict = file_commit_commit_tree_instance.to_dict()
# create an instance of FileCommitCommitTree from a dict
file_commit_commit_tree_from_dict = FileCommitCommitTree.from_dict(file_commit_commit_tree_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


