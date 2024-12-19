# PatchedNotificationRequest

Notification Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**EventRequest**](EventRequest.md) |  | [optional] 
**seen** | **bool** |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_notification_request import PatchedNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedNotificationRequest from a JSON string
patched_notification_request_instance = PatchedNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedNotificationRequest.to_json())

# convert the object into a dict
patched_notification_request_dict = patched_notification_request_instance.to_dict()
# create an instance of PatchedNotificationRequest from a dict
patched_notification_request_from_dict = PatchedNotificationRequest.from_dict(patched_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


