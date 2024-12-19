# CommitSearchResultItem

Commit Search Result Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**sha** | **str** |  | 
**html_url** | **str** |  | 
**comments_url** | **str** |  | 
**commit** | [**CommitSearchResultItemCommit**](CommitSearchResultItemCommit.md) |  | 
**author** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**committer** | [**NullableGitUser**](NullableGitUser.md) |  | 
**parents** | [**List[FileCommitCommitParentsInner]**](FileCommitCommitParentsInner.md) |  | 
**repository** | [**MinimalRepository**](MinimalRepository.md) |  | 
**score** | **float** |  | 
**node_id** | **str** |  | 
**text_matches** | [**List[SearchResultTextMatchesInner]**](SearchResultTextMatchesInner.md) |  | [optional] 

## Example

```python
from github_openapi.models.commit_search_result_item import CommitSearchResultItem

# TODO update the JSON string below
json = "{}"
# create an instance of CommitSearchResultItem from a JSON string
commit_search_result_item_instance = CommitSearchResultItem.from_json(json)
# print the JSON string representation of the object
print(CommitSearchResultItem.to_json())

# convert the object into a dict
commit_search_result_item_dict = commit_search_result_item_instance.to_dict()
# create an instance of CommitSearchResultItem from a dict
commit_search_result_item_from_dict = CommitSearchResultItem.from_dict(commit_search_result_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


