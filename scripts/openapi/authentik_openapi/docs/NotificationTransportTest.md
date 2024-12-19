# NotificationTransportTest

Notification test serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | **List[str]** |  | 

## Example

```python
from authentik_openapi.models.notification_transport_test import NotificationTransportTest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationTransportTest from a JSON string
notification_transport_test_instance = NotificationTransportTest.from_json(json)
# print the JSON string representation of the object
print(NotificationTransportTest.to_json())

# convert the object into a dict
notification_transport_test_dict = notification_transport_test_instance.to_dict()
# create an instance of NotificationTransportTest from a dict
notification_transport_test_from_dict = NotificationTransportTest.from_dict(notification_transport_test_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


