# WebhookDependabotAlertCreated


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
from github_openapi.models.webhook_dependabot_alert_created import WebhookDependabotAlertCreated

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDependabotAlertCreated from a JSON string
webhook_dependabot_alert_created_instance = WebhookDependabotAlertCreated.from_json(json)
# print the JSON string representation of the object
print(WebhookDependabotAlertCreated.to_json())

# convert the object into a dict
webhook_dependabot_alert_created_dict = webhook_dependabot_alert_created_instance.to_dict()
# create an instance of WebhookDependabotAlertCreated from a dict
webhook_dependabot_alert_created_from_dict = WebhookDependabotAlertCreated.from_dict(webhook_dependabot_alert_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


