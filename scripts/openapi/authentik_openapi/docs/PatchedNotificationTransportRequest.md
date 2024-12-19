# PatchedNotificationTransportRequest

NotificationTransport Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**mode** | [**NotificationTransportModeEnum**](NotificationTransportModeEnum.md) |  | [optional] 
**webhook_url** | **str** |  | [optional] 
**webhook_mapping** | **str** |  | [optional] 
**send_once** | **bool** | Only send notification once, for example when sending a webhook into a chat channel. | [optional] 

## Example

```python
from authentik_openapi.models.patched_notification_transport_request import PatchedNotificationTransportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedNotificationTransportRequest from a JSON string
patched_notification_transport_request_instance = PatchedNotificationTransportRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedNotificationTransportRequest.to_json())

# convert the object into a dict
patched_notification_transport_request_dict = patched_notification_transport_request_instance.to_dict()
# create an instance of PatchedNotificationTransportRequest from a dict
patched_notification_transport_request_from_dict = PatchedNotificationTransportRequest.from_dict(patched_notification_transport_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


