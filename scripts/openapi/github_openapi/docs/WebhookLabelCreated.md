# WebhookLabelCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**label** | [**WebhooksLabel**](WebhooksLabel.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_label_created import WebhookLabelCreated

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookLabelCreated from a JSON string
webhook_label_created_instance = WebhookLabelCreated.from_json(json)
# print the JSON string representation of the object
print(WebhookLabelCreated.to_json())

# convert the object into a dict
webhook_label_created_dict = webhook_label_created_instance.to_dict()
# create an instance of WebhookLabelCreated from a dict
webhook_label_created_from_dict = WebhookLabelCreated.from_dict(webhook_label_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


