# WebhookProjectCardConverted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**changes** | [**WebhookProjectCardConvertedChanges**](WebhookProjectCardConvertedChanges.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**project_card** | [**WebhooksProjectCard**](WebhooksProjectCard.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_project_card_converted import WebhookProjectCardConverted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectCardConverted from a JSON string
webhook_project_card_converted_instance = WebhookProjectCardConverted.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectCardConverted.to_json())

# convert the object into a dict
webhook_project_card_converted_dict = webhook_project_card_converted_instance.to_dict()
# create an instance of WebhookProjectCardConverted from a dict
webhook_project_card_converted_from_dict = WebhookProjectCardConverted.from_dict(webhook_project_card_converted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


