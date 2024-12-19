# PatchedNotificationRuleRequest

NotificationRule Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**transports** | **List[str]** | Select which transports should be used to notify the user. If none are selected, the notification will only be shown in the authentik UI. | [optional] 
**severity** | [**SeverityEnum**](SeverityEnum.md) | Controls which severity level the created notifications will have. | [optional] 
**group** | **str** | Define which group of users this notification should be sent and shown to. If left empty, Notification won&#39;t ben sent. | [optional] 

## Example

```python
from authentik_openapi.models.patched_notification_rule_request import PatchedNotificationRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedNotificationRuleRequest from a JSON string
patched_notification_rule_request_instance = PatchedNotificationRuleRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedNotificationRuleRequest.to_json())

# convert the object into a dict
patched_notification_rule_request_dict = patched_notification_rule_request_instance.to_dict()
# create an instance of PatchedNotificationRuleRequest from a dict
patched_notification_rule_request_from_dict = PatchedNotificationRuleRequest.from_dict(patched_notification_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


