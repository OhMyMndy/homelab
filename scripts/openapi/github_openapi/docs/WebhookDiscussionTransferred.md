# WebhookDiscussionTransferred


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**changes** | [**WebhookDiscussionTransferredChanges**](WebhookDiscussionTransferredChanges.md) |  | 
**discussion** | [**Discussion**](Discussion.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_discussion_transferred import WebhookDiscussionTransferred

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDiscussionTransferred from a JSON string
webhook_discussion_transferred_instance = WebhookDiscussionTransferred.from_json(json)
# print the JSON string representation of the object
print(WebhookDiscussionTransferred.to_json())

# convert the object into a dict
webhook_discussion_transferred_dict = webhook_discussion_transferred_instance.to_dict()
# create an instance of WebhookDiscussionTransferred from a dict
webhook_discussion_transferred_from_dict = WebhookDiscussionTransferred.from_dict(webhook_discussion_transferred_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


