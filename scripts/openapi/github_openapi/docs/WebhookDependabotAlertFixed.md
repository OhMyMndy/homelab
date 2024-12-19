# WebhookDependabotAlertFixed


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
from github_openapi.models.webhook_dependabot_alert_fixed import WebhookDependabotAlertFixed

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDependabotAlertFixed from a JSON string
webhook_dependabot_alert_fixed_instance = WebhookDependabotAlertFixed.from_json(json)
# print the JSON string representation of the object
print(WebhookDependabotAlertFixed.to_json())

# convert the object into a dict
webhook_dependabot_alert_fixed_dict = webhook_dependabot_alert_fixed_instance.to_dict()
# create an instance of WebhookDependabotAlertFixed from a dict
webhook_dependabot_alert_fixed_from_dict = WebhookDependabotAlertFixed.from_dict(webhook_dependabot_alert_fixed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


