# WebhookCustomPropertyUpdated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**definition** | [**CustomProperty**](CustomProperty.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_custom_property_updated import WebhookCustomPropertyUpdated

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCustomPropertyUpdated from a JSON string
webhook_custom_property_updated_instance = WebhookCustomPropertyUpdated.from_json(json)
# print the JSON string representation of the object
print(WebhookCustomPropertyUpdated.to_json())

# convert the object into a dict
webhook_custom_property_updated_dict = webhook_custom_property_updated_instance.to_dict()
# create an instance of WebhookCustomPropertyUpdated from a dict
webhook_custom_property_updated_from_dict = WebhookCustomPropertyUpdated.from_dict(webhook_custom_property_updated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


