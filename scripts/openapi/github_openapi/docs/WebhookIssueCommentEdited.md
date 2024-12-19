# WebhookIssueCommentEdited


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**changes** | [**WebhooksChanges**](WebhooksChanges.md) |  | 
**comment** | [**WebhooksIssueComment**](WebhooksIssueComment.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**issue** | [**WebhookIssueCommentEditedIssue**](WebhookIssueCommentEditedIssue.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_issue_comment_edited import WebhookIssueCommentEdited

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookIssueCommentEdited from a JSON string
webhook_issue_comment_edited_instance = WebhookIssueCommentEdited.from_json(json)
# print the JSON string representation of the object
print(WebhookIssueCommentEdited.to_json())

# convert the object into a dict
webhook_issue_comment_edited_dict = webhook_issue_comment_edited_instance.to_dict()
# create an instance of WebhookIssueCommentEdited from a dict
webhook_issue_comment_edited_from_dict = WebhookIssueCommentEdited.from_dict(webhook_issue_comment_edited_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


