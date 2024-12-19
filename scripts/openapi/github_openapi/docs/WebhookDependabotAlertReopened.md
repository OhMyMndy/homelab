# WebhookDependabotAlertReopened


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
from github_openapi.models.webhook_dependabot_alert_reopened import WebhookDependabotAlertReopened

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDependabotAlertReopened from a JSON string
webhook_dependabot_alert_reopened_instance = WebhookDependabotAlertReopened.from_json(json)
# print the JSON string representation of the object
print(WebhookDependabotAlertReopened.to_json())

# convert the object into a dict
webhook_dependabot_alert_reopened_dict = webhook_dependabot_alert_reopened_instance.to_dict()
# create an instance of WebhookDependabotAlertReopened from a dict
webhook_dependabot_alert_reopened_from_dict = WebhookDependabotAlertReopened.from_dict(webhook_dependabot_alert_reopened_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


