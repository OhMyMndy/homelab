# WebhookCustomPropertyDeletedDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_name** | **str** | The name of the property that was deleted. | 

## Example

```python
from github_openapi.models.webhook_custom_property_deleted_definition import WebhookCustomPropertyDeletedDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCustomPropertyDeletedDefinition from a JSON string
webhook_custom_property_deleted_definition_instance = WebhookCustomPropertyDeletedDefinition.from_json(json)
# print the JSON string representation of the object
print(WebhookCustomPropertyDeletedDefinition.to_json())

# convert the object into a dict
webhook_custom_property_deleted_definition_dict = webhook_custom_property_deleted_definition_instance.to_dict()
# create an instance of WebhookCustomPropertyDeletedDefinition from a dict
webhook_custom_property_deleted_definition_from_dict = WebhookCustomPropertyDeletedDefinition.from_dict(webhook_custom_property_deleted_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


