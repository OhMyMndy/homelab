# WebhookSecretScanningAlertCreated


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
from github_openapi.models.webhook_secret_scanning_alert_created import WebhookSecretScanningAlertCreated

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSecretScanningAlertCreated from a JSON string
webhook_secret_scanning_alert_created_instance = WebhookSecretScanningAlertCreated.from_json(json)
# print the JSON string representation of the object
print(WebhookSecretScanningAlertCreated.to_json())

# convert the object into a dict
webhook_secret_scanning_alert_created_dict = webhook_secret_scanning_alert_created_instance.to_dict()
# create an instance of WebhookSecretScanningAlertCreated from a dict
webhook_secret_scanning_alert_created_from_dict = WebhookSecretScanningAlertCreated.from_dict(webhook_secret_scanning_alert_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


