# WebhookIssueCommentCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**comment** | [**IssueComment**](IssueComment.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**issue** | [**WebhookIssueCommentCreatedIssue**](WebhookIssueCommentCreatedIssue.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_issue_comment_created import WebhookIssueCommentCreated

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookIssueCommentCreated from a JSON string
webhook_issue_comment_created_instance = WebhookIssueCommentCreated.from_json(json)
# print the JSON string representation of the object
print(WebhookIssueCommentCreated.to_json())

# convert the object into a dict
webhook_issue_comment_created_dict = webhook_issue_comment_created_instance.to_dict()
# create an instance of WebhookIssueCommentCreated from a dict
webhook_issue_comment_created_from_dict = WebhookIssueCommentCreated.from_dict(webhook_issue_comment_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


