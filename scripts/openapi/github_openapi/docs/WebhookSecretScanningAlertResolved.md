# WebhookSecretScanningAlertResolved


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**alert** | [**SecretScanningAlertWebhook**](SecretScanningAlertWebhook.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_secret_scanning_alert_resolved import WebhookSecretScanningAlertResolved

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSecretScanningAlertResolved from a JSON string
webhook_secret_scanning_alert_resolved_instance = WebhookSecretScanningAlertResolved.from_json(json)
# print the JSON string representation of the object
print(WebhookSecretScanningAlertResolved.to_json())

# convert the object into a dict
webhook_secret_scanning_alert_resolved_dict = webhook_secret_scanning_alert_resolved_instance.to_dict()
# create an instance of WebhookSecretScanningAlertResolved from a dict
webhook_secret_scanning_alert_resolved_from_dict = WebhookSecretScanningAlertResolved.from_dict(webhook_secret_scanning_alert_resolved_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


