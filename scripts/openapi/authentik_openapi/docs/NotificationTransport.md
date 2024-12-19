# NotificationTransport

NotificationTransport Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**name** | **str** |  | 
**mode** | [**NotificationTransportModeEnum**](NotificationTransportModeEnum.md) |  | [optional] 
**mode_verbose** | **str** | Return selected mode with a UI Label | [readonly] 
**webhook_url** | **str** |  | [optional] 
**webhook_mapping** | **str** |  | [optional] 
**send_once** | **bool** | Only send notification once, for example when sending a webhook into a chat channel. | [optional] 

## Example

```python
from authentik_openapi.models.notification_transport import NotificationTransport

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationTransport from a JSON string
notification_transport_instance = NotificationTransport.from_json(json)
# print the JSON string representation of the object
print(NotificationTransport.to_json())

# convert the object into a dict
notification_transport_dict = notification_transport_instance.to_dict()
# create an instance of NotificationTransport from a dict
notification_transport_from_dict = NotificationTransport.from_dict(notification_transport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


