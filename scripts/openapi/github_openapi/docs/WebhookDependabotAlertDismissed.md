# WebhookDependabotAlertDismissed


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
from github_openapi.models.webhook_dependabot_alert_dismissed import WebhookDependabotAlertDismissed

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDependabotAlertDismissed from a JSON string
webhook_dependabot_alert_dismissed_instance = WebhookDependabotAlertDismissed.from_json(json)
# print the JSON string representation of the object
print(WebhookDependabotAlertDismissed.to_json())

# convert the object into a dict
webhook_dependabot_alert_dismissed_dict = webhook_dependabot_alert_dismissed_instance.to_dict()
# create an instance of WebhookDependabotAlertDismissed from a dict
webhook_dependabot_alert_dismissed_from_dict = WebhookDependabotAlertDismissed.from_dict(webhook_dependabot_alert_dismissed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


