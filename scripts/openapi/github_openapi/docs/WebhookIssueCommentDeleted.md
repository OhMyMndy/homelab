# WebhookIssueCommentDeleted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**comment** | [**WebhooksIssueComment**](WebhooksIssueComment.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**issue** | [**WebhookIssueCommentDeletedIssue**](WebhookIssueCommentDeletedIssue.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_issue_comment_deleted import WebhookIssueCommentDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookIssueCommentDeleted from a JSON string
webhook_issue_comment_deleted_instance = WebhookIssueCommentDeleted.from_json(json)
# print the JSON string representation of the object
print(WebhookIssueCommentDeleted.to_json())

# convert the object into a dict
webhook_issue_comment_deleted_dict = webhook_issue_comment_deleted_instance.to_dict()
# create an instance of WebhookIssueCommentDeleted from a dict
webhook_issue_comment_deleted_from_dict = WebhookIssueCommentDeleted.from_dict(webhook_issue_comment_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


