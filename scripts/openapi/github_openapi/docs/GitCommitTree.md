# GitCommitTree


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sha** | **str** | SHA for the commit | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.git_commit_tree import GitCommitTree

# TODO update the JSON string below
json = "{}"
# create an instance of GitCommitTree from a JSON string
git_commit_tree_instance = GitCommitTree.from_json(json)
# print the JSON string representation of the object
print(GitCommitTree.to_json())

# convert the object into a dict
git_commit_tree_dict = git_commit_tree_instance.to_dict()
# create an instance of GitCommitTree from a dict
git_commit_tree_from_dict = GitCommitTree.from_dict(git_commit_tree_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


