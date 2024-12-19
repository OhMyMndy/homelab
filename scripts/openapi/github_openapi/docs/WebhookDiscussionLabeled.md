# WebhookDiscussionLabeled


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**discussion** | [**Discussion**](Discussion.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**label** | [**WebhooksLabel**](WebhooksLabel.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_discussion_labeled import WebhookDiscussionLabeled

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDiscussionLabeled from a JSON string
webhook_discussion_labeled_instance = WebhookDiscussionLabeled.from_json(json)
# print the JSON string representation of the object
print(WebhookDiscussionLabeled.to_json())

# convert the object into a dict
webhook_discussion_labeled_dict = webhook_discussion_labeled_instance.to_dict()
# create an instance of WebhookDiscussionLabeled from a dict
webhook_discussion_labeled_from_dict = WebhookDiscussionLabeled.from_dict(webhook_discussion_labeled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


