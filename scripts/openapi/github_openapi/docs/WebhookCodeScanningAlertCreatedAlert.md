# WebhookCodeScanningAlertCreatedAlert

The code scanning alert involved in the event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The time that the alert was created in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ.&#x60; | 
**dismissed_at** | **object** | The time that the alert was dismissed in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | 
**dismissed_by** | **object** |  | 
**dismissed_comment** | **str** | The dismissal comment associated with the dismissal of the alert. | [optional] 
**dismissed_reason** | **object** | The reason for dismissing or closing the alert. Can be one of: &#x60;false positive&#x60;, &#x60;won&#39;t fix&#x60;, and &#x60;used in tests&#x60;. | 
**fixed_at** | **object** |  | [optional] 
**html_url** | **str** | The GitHub URL of the alert resource. | 
**instances_url** | **str** |  | [optional] 
**most_recent_instance** | [**AlertInstance**](AlertInstance.md) |  | [optional] 
**number** | **int** | The code scanning alert number. | 
**rule** | [**WebhookCodeScanningAlertClosedByUserAlertRule**](WebhookCodeScanningAlertClosedByUserAlertRule.md) |  | 
**state** | **str** | State of a code scanning alert. | 
**tool** | [**WebhookCodeScanningAlertCreatedAlertTool**](WebhookCodeScanningAlertCreatedAlertTool.md) |  | 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_code_scanning_alert_created_alert import WebhookCodeScanningAlertCreatedAlert

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCodeScanningAlertCreatedAlert from a JSON string
webhook_code_scanning_alert_created_alert_instance = WebhookCodeScanningAlertCreatedAlert.from_json(json)
# print the JSON string representation of the object
print(WebhookCodeScanningAlertCreatedAlert.to_json())

# convert the object into a dict
webhook_code_scanning_alert_created_alert_dict = webhook_code_scanning_alert_created_alert_instance.to_dict()
# create an instance of WebhookCodeScanningAlertCreatedAlert from a dict
webhook_code_scanning_alert_created_alert_from_dict = WebhookCodeScanningAlertCreatedAlert.from_dict(webhook_code_scanning_alert_created_alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


