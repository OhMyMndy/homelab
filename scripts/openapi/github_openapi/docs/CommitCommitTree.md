# CommitCommitTree


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sha** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.commit_commit_tree import CommitCommitTree

# TODO update the JSON string below
json = "{}"
# create an instance of CommitCommitTree from a JSON string
commit_commit_tree_instance = CommitCommitTree.from_json(json)
# print the JSON string representation of the object
print(CommitCommitTree.to_json())

# convert the object into a dict
commit_commit_tree_dict = commit_commit_tree_instance.to_dict()
# create an instance of CommitCommitTree from a dict
commit_commit_tree_from_dict = CommitCommitTree.from_dict(commit_commit_tree_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


