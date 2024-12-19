# WebhookCustomPropertyValuesUpdated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | [optional] 
**new_property_values** | [**List[CustomPropertyValue]**](CustomPropertyValue.md) | The new custom property values for the repository. | 
**old_property_values** | [**List[CustomPropertyValue]**](CustomPropertyValue.md) | The old custom property values for the repository. | 

## Example

```python
from github_openapi.models.webhook_custom_property_values_updated import WebhookCustomPropertyValuesUpdated

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCustomPropertyValuesUpdated from a JSON string
webhook_custom_property_values_updated_instance = WebhookCustomPropertyValuesUpdated.from_json(json)
# print the JSON string representation of the object
print(WebhookCustomPropertyValuesUpdated.to_json())

# convert the object into a dict
webhook_custom_property_values_updated_dict = webhook_custom_property_values_updated_instance.to_dict()
# create an instance of WebhookCustomPropertyValuesUpdated from a dict
webhook_custom_property_values_updated_from_dict = WebhookCustomPropertyValuesUpdated.from_dict(webhook_custom_property_values_updated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


