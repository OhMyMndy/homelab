# WebhookProjectCardMoved


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**changes** | [**WebhookProjectCardMovedChanges**](WebhookProjectCardMovedChanges.md) |  | [optional] 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**project_card** | [**WebhookProjectCardMovedProjectCard**](WebhookProjectCardMovedProjectCard.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_project_card_moved import WebhookProjectCardMoved

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectCardMoved from a JSON string
webhook_project_card_moved_instance = WebhookProjectCardMoved.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectCardMoved.to_json())

# convert the object into a dict
webhook_project_card_moved_dict = webhook_project_card_moved_instance.to_dict()
# create an instance of WebhookProjectCardMoved from a dict
webhook_project_card_moved_from_dict = WebhookProjectCardMoved.from_dict(webhook_project_card_moved_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


