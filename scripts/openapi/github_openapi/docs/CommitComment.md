# CommitComment

Commit Comment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**html_url** | **str** |  | 
**url** | **str** |  | 
**id** | **int** |  | 
**node_id** | **str** |  | 
**body** | **str** |  | 
**path** | **str** |  | 
**position** | **int** |  | 
**line** | **int** |  | 
**commit_id** | **str** |  | 
**user** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**author_association** | [**AuthorAssociation**](AuthorAssociation.md) |  | 
**reactions** | [**ReactionRollup**](ReactionRollup.md) |  | [optional] 

## Example

```python
from github_openapi.models.commit_comment import CommitComment

# TODO update the JSON string below
json = "{}"
# create an instance of CommitComment from a JSON string
commit_comment_instance = CommitComment.from_json(json)
# print the JSON string representation of the object
print(CommitComment.to_json())

# convert the object into a dict
commit_comment_dict = commit_comment_instance.to_dict()
# create an instance of CommitComment from a dict
commit_comment_from_dict = CommitComment.from_dict(commit_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


