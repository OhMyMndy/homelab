# WebhookDependabotAlertAutoReopened


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**alert** | [**DependabotAlert**](DependabotAlert.md) |  | 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_dependabot_alert_auto_reopened import WebhookDependabotAlertAutoReopened

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDependabotAlertAutoReopened from a JSON string
webhook_dependabot_alert_auto_reopened_instance = WebhookDependabotAlertAutoReopened.from_json(json)
# print the JSON string representation of the object
print(WebhookDependabotAlertAutoReopened.to_json())

# convert the object into a dict
webhook_dependabot_alert_auto_reopened_dict = webhook_dependabot_alert_auto_reopened_instance.to_dict()
# create an instance of WebhookDependabotAlertAutoReopened from a dict
webhook_dependabot_alert_auto_reopened_from_dict = WebhookDependabotAlertAutoReopened.from_dict(webhook_dependabot_alert_auto_reopened_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


