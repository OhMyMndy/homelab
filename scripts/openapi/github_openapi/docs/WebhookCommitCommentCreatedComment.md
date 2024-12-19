# WebhookCommitCommentCreatedComment

The [commit comment](${externalDocsUpapp/api/description/components/schemas/webhooks/issue-comment-created.yamlrl}/rest/commits/comments#get-a-commit-comment) resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author_association** | **str** | How the author is associated with the repository. | 
**body** | **str** | The text of the comment. | 
**commit_id** | **str** | The SHA of the commit to which the comment applies. | 
**created_at** | **str** |  | 
**html_url** | **str** |  | 
**id** | **int** | The ID of the commit comment. | 
**line** | **int** | The line of the blob to which the comment applies. The last line of the range for a multi-line comment | 
**node_id** | **str** | The node ID of the commit comment. | 
**path** | **str** | The relative path of the file to which the comment applies. | 
**position** | **int** | The line index in the diff to which the comment applies. | 
**reactions** | [**Reactions**](Reactions.md) |  | [optional] 
**updated_at** | **str** |  | 
**url** | **str** |  | 
**user** | [**User1**](User1.md) |  | 

## Example

```python
from github_openapi.models.webhook_commit_comment_created_comment import WebhookCommitCommentCreatedComment

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCommitCommentCreatedComment from a JSON string
webhook_commit_comment_created_comment_instance = WebhookCommitCommentCreatedComment.from_json(json)
# print the JSON string representation of the object
print(WebhookCommitCommentCreatedComment.to_json())

# convert the object into a dict
webhook_commit_comment_created_comment_dict = webhook_commit_comment_created_comment_instance.to_dict()
# create an instance of WebhookCommitCommentCreatedComment from a dict
webhook_commit_comment_created_comment_from_dict = WebhookCommitCommentCreatedComment.from_dict(webhook_commit_comment_created_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


