# WebhookLabelEdited


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**changes** | [**WebhookLabelEditedChanges**](WebhookLabelEditedChanges.md) |  | [optional] 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**label** | [**WebhooksLabel**](WebhooksLabel.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_label_edited import WebhookLabelEdited

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookLabelEdited from a JSON string
webhook_label_edited_instance = WebhookLabelEdited.from_json(json)
# print the JSON string representation of the object
print(WebhookLabelEdited.to_json())

# convert the object into a dict
webhook_label_edited_dict = webhook_label_edited_instance.to_dict()
# create an instance of WebhookLabelEdited from a dict
webhook_label_edited_from_dict = WebhookLabelEdited.from_dict(webhook_label_edited_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


