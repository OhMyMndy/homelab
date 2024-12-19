# PatchedNotificationWebhookMappingRequest

NotificationWebhookMapping Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**expression** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_notification_webhook_mapping_request import PatchedNotificationWebhookMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedNotificationWebhookMappingRequest from a JSON string
patched_notification_webhook_mapping_request_instance = PatchedNotificationWebhookMappingRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedNotificationWebhookMappingRequest.to_json())

# convert the object into a dict
patched_notification_webhook_mapping_request_dict = patched_notification_webhook_mapping_request_instance.to_dict()
# create an instance of PatchedNotificationWebhookMappingRequest from a dict
patched_notification_webhook_mapping_request_from_dict = PatchedNotificationWebhookMappingRequest.from_dict(patched_notification_webhook_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


