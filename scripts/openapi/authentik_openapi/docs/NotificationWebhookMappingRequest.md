# NotificationWebhookMappingRequest

NotificationWebhookMapping Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**expression** | **str** |  | 

## Example

```python
from authentik_openapi.models.notification_webhook_mapping_request import NotificationWebhookMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationWebhookMappingRequest from a JSON string
notification_webhook_mapping_request_instance = NotificationWebhookMappingRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationWebhookMappingRequest.to_json())

# convert the object into a dict
notification_webhook_mapping_request_dict = notification_webhook_mapping_request_instance.to_dict()
# create an instance of NotificationWebhookMappingRequest from a dict
notification_webhook_mapping_request_from_dict = NotificationWebhookMappingRequest.from_dict(notification_webhook_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


