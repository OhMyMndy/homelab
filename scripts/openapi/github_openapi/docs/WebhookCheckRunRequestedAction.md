# WebhookCheckRunRequestedAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**check_run** | [**CheckRunWithSimpleCheckSuite**](CheckRunWithSimpleCheckSuite.md) |  | 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**requested_action** | [**WebhookCheckRunRequestedActionRequestedAction**](WebhookCheckRunRequestedActionRequestedAction.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_check_run_requested_action import WebhookCheckRunRequestedAction

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCheckRunRequestedAction from a JSON string
webhook_check_run_requested_action_instance = WebhookCheckRunRequestedAction.from_json(json)
# print the JSON string representation of the object
print(WebhookCheckRunRequestedAction.to_json())

# convert the object into a dict
webhook_check_run_requested_action_dict = webhook_check_run_requested_action_instance.to_dict()
# create an instance of WebhookCheckRunRequestedAction from a dict
webhook_check_run_requested_action_from_dict = WebhookCheckRunRequestedAction.from_dict(webhook_check_run_requested_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


