# WebhookDiscussionCommentCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**comment** | [**WebhooksComment**](WebhooksComment.md) |  | 
**discussion** | [**Discussion**](Discussion.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_discussion_comment_created import WebhookDiscussionCommentCreated

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDiscussionCommentCreated from a JSON string
webhook_discussion_comment_created_instance = WebhookDiscussionCommentCreated.from_json(json)
# print the JSON string representation of the object
print(WebhookDiscussionCommentCreated.to_json())

# convert the object into a dict
webhook_discussion_comment_created_dict = webhook_discussion_comment_created_instance.to_dict()
# create an instance of WebhookDiscussionCommentCreated from a dict
webhook_discussion_comment_created_from_dict = WebhookDiscussionCommentCreated.from_dict(webhook_discussion_comment_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


