# WebhookLabelDeleted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**label** | [**WebhooksLabel**](WebhooksLabel.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_label_deleted import WebhookLabelDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookLabelDeleted from a JSON string
webhook_label_deleted_instance = WebhookLabelDeleted.from_json(json)
# print the JSON string representation of the object
print(WebhookLabelDeleted.to_json())

# convert the object into a dict
webhook_label_deleted_dict = webhook_label_deleted_instance.to_dict()
# create an instance of WebhookLabelDeleted from a dict
webhook_label_deleted_from_dict = WebhookLabelDeleted.from_dict(webhook_label_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


