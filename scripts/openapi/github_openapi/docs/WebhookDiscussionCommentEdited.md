# WebhookDiscussionCommentEdited


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**changes** | [**WebhookDiscussionCommentEditedChanges**](WebhookDiscussionCommentEditedChanges.md) |  | 
**comment** | [**WebhooksComment**](WebhooksComment.md) |  | 
**discussion** | [**Discussion**](Discussion.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_discussion_comment_edited import WebhookDiscussionCommentEdited

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDiscussionCommentEdited from a JSON string
webhook_discussion_comment_edited_instance = WebhookDiscussionCommentEdited.from_json(json)
# print the JSON string representation of the object
print(WebhookDiscussionCommentEdited.to_json())

# convert the object into a dict
webhook_discussion_comment_edited_dict = webhook_discussion_comment_edited_instance.to_dict()
# create an instance of WebhookDiscussionCommentEdited from a dict
webhook_discussion_comment_edited_from_dict = WebhookDiscussionCommentEdited.from_dict(webhook_discussion_comment_edited_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


