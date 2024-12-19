# CommitSearchResultItemCommit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**CommitSearchResultItemCommitAuthor**](CommitSearchResultItemCommitAuthor.md) |  | 
**committer** | [**NullableGitUser**](NullableGitUser.md) |  | 
**comment_count** | **int** |  | 
**message** | **str** |  | 
**tree** | [**ShortBranchCommit**](ShortBranchCommit.md) |  | 
**url** | **str** |  | 
**verification** | [**Verification**](Verification.md) |  | [optional] 

## Example

```python
from github_openapi.models.commit_search_result_item_commit import CommitSearchResultItemCommit

# TODO update the JSON string below
json = "{}"
# create an instance of CommitSearchResultItemCommit from a JSON string
commit_search_result_item_commit_instance = CommitSearchResultItemCommit.from_json(json)
# print the JSON string representation of the object
print(CommitSearchResultItemCommit.to_json())

# convert the object into a dict
commit_search_result_item_commit_dict = commit_search_result_item_commit_instance.to_dict()
# create an instance of CommitSearchResultItemCommit from a dict
commit_search_result_item_commit_from_dict = CommitSearchResultItemCommit.from_dict(commit_search_result_item_commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


