# WebhooksIssueComment

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
**performed_via_github_app** | [**Integration**](Integration.md) |  | 
**reactions** | [**Reactions**](Reactions.md) |  | 
**updated_at** | **datetime** |  | 
**url** | **str** | URL for the issue comment | 
**user** | [**User3**](User3.md) |  | 

## Example

```python
from github_openapi.models.webhooks_issue_comment import WebhooksIssueComment

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksIssueComment from a JSON string
webhooks_issue_comment_instance = WebhooksIssueComment.from_json(json)
# print the JSON string representation of the object
print(WebhooksIssueComment.to_json())

# convert the object into a dict
webhooks_issue_comment_dict = webhooks_issue_comment_instance.to_dict()
# create an instance of WebhooksIssueComment from a dict
webhooks_issue_comment_from_dict = WebhooksIssueComment.from_dict(webhooks_issue_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


