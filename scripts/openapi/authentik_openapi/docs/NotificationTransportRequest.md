# NotificationTransportRequest

NotificationTransport Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**mode** | [**NotificationTransportModeEnum**](NotificationTransportModeEnum.md) |  | [optional] 
**webhook_url** | **str** |  | [optional] 
**webhook_mapping** | **str** |  | [optional] 
**send_once** | **bool** | Only send notification once, for example when sending a webhook into a chat channel. | [optional] 

## Example

```python
from authentik_openapi.models.notification_transport_request import NotificationTransportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationTransportRequest from a JSON string
notification_transport_request_instance = NotificationTransportRequest.from_json(json)
# print the JSON string representation of the object
print(NotificationTransportRequest.to_json())

# convert the object into a dict
notification_transport_request_dict = notification_transport_request_instance.to_dict()
# create an instance of NotificationTransportRequest from a dict
notification_transport_request_from_dict = NotificationTransportRequest.from_dict(notification_transport_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


