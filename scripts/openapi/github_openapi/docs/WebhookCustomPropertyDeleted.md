# WebhookCustomPropertyDeleted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**definition** | [**WebhookCustomPropertyDeletedDefinition**](WebhookCustomPropertyDeletedDefinition.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_custom_property_deleted import WebhookCustomPropertyDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCustomPropertyDeleted from a JSON string
webhook_custom_property_deleted_instance = WebhookCustomPropertyDeleted.from_json(json)
# print the JSON string representation of the object
print(WebhookCustomPropertyDeleted.to_json())

# convert the object into a dict
webhook_custom_property_deleted_dict = webhook_custom_property_deleted_instance.to_dict()
# create an instance of WebhookCustomPropertyDeleted from a dict
webhook_custom_property_deleted_from_dict = WebhookCustomPropertyDeleted.from_dict(webhook_custom_property_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


