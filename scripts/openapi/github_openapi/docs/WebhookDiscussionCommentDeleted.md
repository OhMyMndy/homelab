# WebhookDiscussionCommentDeleted


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
from github_openapi.models.webhook_discussion_comment_deleted import WebhookDiscussionCommentDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDiscussionCommentDeleted from a JSON string
webhook_discussion_comment_deleted_instance = WebhookDiscussionCommentDeleted.from_json(json)
# print the JSON string representation of the object
print(WebhookDiscussionCommentDeleted.to_json())

# convert the object into a dict
webhook_discussion_comment_deleted_dict = webhook_discussion_comment_deleted_instance.to_dict()
# create an instance of WebhookDiscussionCommentDeleted from a dict
webhook_discussion_comment_deleted_from_dict = WebhookDiscussionCommentDeleted.from_dict(webhook_discussion_comment_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


