# CommitCommit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**author** | [**NullableGitUser**](NullableGitUser.md) |  | 
**committer** | [**NullableGitUser**](NullableGitUser.md) |  | 
**message** | **str** |  | 
**comment_count** | **int** |  | 
**tree** | [**CommitCommitTree**](CommitCommitTree.md) |  | 
**verification** | [**Verification**](Verification.md) |  | [optional] 

## Example

```python
from github_openapi.models.commit_commit import CommitCommit

# TODO update the JSON string below
json = "{}"
# create an instance of CommitCommit from a JSON string
commit_commit_instance = CommitCommit.from_json(json)
# print the JSON string representation of the object
print(CommitCommit.to_json())

# convert the object into a dict
commit_commit_dict = commit_commit_instance.to_dict()
# create an instance of CommitCommit from a dict
commit_commit_from_dict = CommitCommit.from_dict(commit_commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


