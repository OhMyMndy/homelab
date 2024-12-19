# SecretScanningAlertWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** | The security alert number. | [optional] [readonly] 
**created_at** | **datetime** | The time that the alert was created in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] [readonly] 
**updated_at** | **datetime** | The time that the alert was last updated in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] [readonly] 
**url** | **str** | The REST API URL of the alert resource. | [optional] [readonly] 
**html_url** | **str** | The GitHub URL of the alert resource. | [optional] [readonly] 
**locations_url** | **str** | The REST API URL of the code locations for this alert. | [optional] 
**resolution** | [**SecretScanningAlertResolutionWebhook**](SecretScanningAlertResolutionWebhook.md) |  | [optional] 
**resolved_at** | **datetime** | The time that the alert was resolved in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
**resolved_by** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | [optional] 
**resolution_comment** | **str** | An optional comment to resolve an alert. | [optional] 
**secret_type** | **str** | The type of secret that secret scanning detected. | [optional] 
**secret_type_display_name** | **str** | User-friendly name for the detected secret, matching the &#x60;secret_type&#x60;. For a list of built-in patterns, see \&quot;[Supported secret scanning patterns](https://docs.github.com/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#supported-secrets).\&quot; | [optional] 
**validity** | **str** | The token status as of the latest validity check. | [optional] 
**push_protection_bypassed** | **bool** | Whether push protection was bypassed for the detected secret. | [optional] 
**push_protection_bypassed_by** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | [optional] 
**push_protection_bypassed_at** | **datetime** | The time that push protection was bypassed in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
**push_protection_bypass_request_reviewer** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | [optional] 
**push_protection_bypass_request_reviewer_comment** | **str** | An optional comment when reviewing a push protection bypass. | [optional] 
**push_protection_bypass_request_comment** | **str** | An optional comment when requesting a push protection bypass. | [optional] 
**push_protection_bypass_request_html_url** | **str** | The URL to a push protection bypass request. | [optional] 
**publicly_leaked** | **bool** | Whether the detected secret was publicly leaked. | [optional] 
**multi_repo** | **bool** | Whether the detected secret was found in multiple repositories in the same organization or business. | [optional] 

## Example

```python
from github_openapi.models.secret_scanning_alert_webhook import SecretScanningAlertWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of SecretScanningAlertWebhook from a JSON string
secret_scanning_alert_webhook_instance = SecretScanningAlertWebhook.from_json(json)
# print the JSON string representation of the object
print(SecretScanningAlertWebhook.to_json())

# convert the object into a dict
secret_scanning_alert_webhook_dict = secret_scanning_alert_webhook_instance.to_dict()
# create an instance of SecretScanningAlertWebhook from a dict
secret_scanning_alert_webhook_from_dict = SecretScanningAlertWebhook.from_dict(secret_scanning_alert_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


