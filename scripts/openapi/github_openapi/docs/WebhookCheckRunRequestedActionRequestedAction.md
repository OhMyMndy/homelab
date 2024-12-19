# WebhookCheckRunRequestedActionRequestedAction

The action requested by the user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | The integrator reference of the action requested by the user. | [optional] 

## Example

```python
from github_openapi.models.webhook_check_run_requested_action_requested_action import WebhookCheckRunRequestedActionRequestedAction

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCheckRunRequestedActionRequestedAction from a JSON string
webhook_check_run_requested_action_requested_action_instance = WebhookCheckRunRequestedActionRequestedAction.from_json(json)
# print the JSON string representation of the object
print(WebhookCheckRunRequestedActionRequestedAction.to_json())

# convert the object into a dict
webhook_check_run_requested_action_requested_action_dict = webhook_check_run_requested_action_requested_action_instance.to_dict()
# create an instance of WebhookCheckRunRequestedActionRequestedAction from a dict
webhook_check_run_requested_action_requested_action_from_dict = WebhookCheckRunRequestedActionRequestedAction.from_dict(webhook_check_run_requested_action_requested_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


