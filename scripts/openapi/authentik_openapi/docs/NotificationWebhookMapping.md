# NotificationWebhookMapping

NotificationWebhookMapping Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**name** | **str** |  | 
**expression** | **str** |  | 

## Example

```python
from authentik_openapi.models.notification_webhook_mapping import NotificationWebhookMapping

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationWebhookMapping from a JSON string
notification_webhook_mapping_instance = NotificationWebhookMapping.from_json(json)
# print the JSON string representation of the object
print(NotificationWebhookMapping.to_json())

# convert the object into a dict
notification_webhook_mapping_dict = notification_webhook_mapping_instance.to_dict()
# create an instance of NotificationWebhookMapping from a dict
notification_webhook_mapping_from_dict = NotificationWebhookMapping.from_dict(notification_webhook_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


