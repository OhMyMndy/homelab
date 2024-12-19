# WebhookCommitCommentCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action performed. Can be &#x60;created&#x60;. | 
**comment** | [**WebhookCommitCommentCreatedComment**](WebhookCommitCommentCreatedComment.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_commit_comment_created import WebhookCommitCommentCreated

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCommitCommentCreated from a JSON string
webhook_commit_comment_created_instance = WebhookCommitCommentCreated.from_json(json)
# print the JSON string representation of the object
print(WebhookCommitCommentCreated.to_json())

# convert the object into a dict
webhook_commit_comment_created_dict = webhook_commit_comment_created_instance.to_dict()
# create an instance of WebhookCommitCommentCreated from a dict
webhook_commit_comment_created_from_dict = WebhookCommitCommentCreated.from_dict(webhook_commit_comment_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


