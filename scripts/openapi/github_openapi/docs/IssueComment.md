# IssueComment

The [comment](https://docs.github.com/rest/issues/comments#get-an-issue-comment) itself.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_association** | **str** | How the author is associated with the repository. | 
**body** | **str** | Contents of the issue comment | 
**created_at** | **datetime** |  | 
**html_url** | **str** |  | 
**id** | **int** | Unique identifier of the issue comment | 
**issue_url** | **str** |  | 
**node_id** | **str** |  | 
**performed_via_github_app** | [**NullableIntegration**](NullableIntegration.md) |  | 
**reactions** | [**Reactions**](Reactions.md) |  | 
**updated_at** | **datetime** |  | 
**url** | **str** | URL for the issue comment | 
**user** | [**User1**](User1.md) |  | 

## Example

```python
from github_openapi.models.issue_comment import IssueComment

# TODO update the JSON string below
json = "{}"
# create an instance of IssueComment from a JSON string
issue_comment_instance = IssueComment.from_json(json)
# print the JSON string representation of the object
print(IssueComment.to_json())

# convert the object into a dict
issue_comment_dict = issue_comment_instance.to_dict()
# create an instance of IssueComment from a dict
issue_comment_from_dict = IssueComment.from_dict(issue_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


