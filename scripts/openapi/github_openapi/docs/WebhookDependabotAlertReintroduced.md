# WebhookDependabotAlertReintroduced


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
from github_openapi.models.webhook_dependabot_alert_reintroduced import WebhookDependabotAlertReintroduced

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDependabotAlertReintroduced from a JSON string
webhook_dependabot_alert_reintroduced_instance = WebhookDependabotAlertReintroduced.from_json(json)
# print the JSON string representation of the object
print(WebhookDependabotAlertReintroduced.to_json())

# convert the object into a dict
webhook_dependabot_alert_reintroduced_dict = webhook_dependabot_alert_reintroduced_instance.to_dict()
# create an instance of WebhookDependabotAlertReintroduced from a dict
webhook_dependabot_alert_reintroduced_from_dict = WebhookDependabotAlertReintroduced.from_dict(webhook_dependabot_alert_reintroduced_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


