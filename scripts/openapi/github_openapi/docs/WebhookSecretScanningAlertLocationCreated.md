# WebhookSecretScanningAlertLocationCreated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**alert** | [**SecretScanningAlertWebhook**](SecretScanningAlertWebhook.md) |  | 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**location** | [**SecretScanningLocation**](SecretScanningLocation.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_secret_scanning_alert_location_created import WebhookSecretScanningAlertLocationCreated

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSecretScanningAlertLocationCreated from a JSON string
webhook_secret_scanning_alert_location_created_instance = WebhookSecretScanningAlertLocationCreated.from_json(json)
# print the JSON string representation of the object
print(WebhookSecretScanningAlertLocationCreated.to_json())

# convert the object into a dict
webhook_secret_scanning_alert_location_created_dict = webhook_secret_scanning_alert_location_created_instance.to_dict()
# create an instance of WebhookSecretScanningAlertLocationCreated from a dict
webhook_secret_scanning_alert_location_created_from_dict = WebhookSecretScanningAlertLocationCreated.from_dict(webhook_secret_scanning_alert_location_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


