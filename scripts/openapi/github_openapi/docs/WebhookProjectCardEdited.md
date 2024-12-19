# WebhookProjectCardEdited


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**changes** | [**WebhookProjectCardEditedChanges**](WebhookProjectCardEditedChanges.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**project_card** | [**WebhooksProjectCard**](WebhooksProjectCard.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_project_card_edited import WebhookProjectCardEdited

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectCardEdited from a JSON string
webhook_project_card_edited_instance = WebhookProjectCardEdited.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectCardEdited.to_json())

# convert the object into a dict
webhook_project_card_edited_dict = webhook_project_card_edited_instance.to_dict()
# create an instance of WebhookProjectCardEdited from a dict
webhook_project_card_edited_from_dict = WebhookProjectCardEdited.from_dict(webhook_project_card_edited_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


