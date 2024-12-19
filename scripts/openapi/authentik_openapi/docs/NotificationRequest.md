# NotificationRequest

Notification Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**EventRequest**](EventRequest.md) |  | [optional] 
**seen** | **bool** |  | [optional] 

## Example

```python
from authentik_openapi.models.notification_request import NotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationRequest from a JSON string
notification_request_instance = NotificationRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationRequest.to_json())

# convert the object into a dict
notification_request_dict = notification_request_instance.to_dict()
# create an instance of NotificationRequest from a dict
notification_request_from_dict = NotificationRequest.from_dict(notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


