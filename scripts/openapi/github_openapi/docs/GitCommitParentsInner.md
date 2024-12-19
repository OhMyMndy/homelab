# GitCommitParentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sha** | **str** | SHA for the commit | 
**url** | **str** |  | 
**html_url** | **str** |  | 

## Example

```python
from github_openapi.models.git_commit_parents_inner import GitCommitParentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GitCommitParentsInner from a JSON string
git_commit_parents_inner_instance = GitCommitParentsInner.from_json(json)
# print the JSON string representation of the object
print(GitCommitParentsInner.to_json())

# convert the object into a dict
git_commit_parents_inner_dict = git_commit_parents_inner_instance.to_dict()
# create an instance of GitCommitParentsInner from a dict
git_commit_parents_inner_from_dict = GitCommitParentsInner.from_dict(git_commit_parents_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


