# WebhookCodeScanningAlertReopenedAlert

The code scanning alert involved in the event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The time that the alert was created in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ.&#x60; | 
**dismissed_at** | **str** | The time that the alert was dismissed in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | 
**dismissed_by** | **object** |  | 
**dismissed_reason** | **str** | The reason for dismissing or closing the alert. Can be one of: &#x60;false positive&#x60;, &#x60;won&#39;t fix&#x60;, and &#x60;used in tests&#x60;. | 
**html_url** | **str** | The GitHub URL of the alert resource. | 
**most_recent_instance** | [**AlertInstance**](AlertInstance.md) |  | [optional] 
**number** | **int** | The code scanning alert number. | 
**rule** | [**WebhookCodeScanningAlertClosedByUserAlertRule**](WebhookCodeScanningAlertClosedByUserAlertRule.md) |  | 
**state** | **str** | State of a code scanning alert. | 
**tool** | [**WebhookCodeScanningAlertClosedByUserAlertTool**](WebhookCodeScanningAlertClosedByUserAlertTool.md) |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_code_scanning_alert_reopened_alert import WebhookCodeScanningAlertReopenedAlert

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCodeScanningAlertReopenedAlert from a JSON string
webhook_code_scanning_alert_reopened_alert_instance = WebhookCodeScanningAlertReopenedAlert.from_json(json)
# print the JSON string representation of the object
print(WebhookCodeScanningAlertReopenedAlert.to_json())

# convert the object into a dict
webhook_code_scanning_alert_reopened_alert_dict = webhook_code_scanning_alert_reopened_alert_instance.to_dict()
# create an instance of WebhookCodeScanningAlertReopenedAlert from a dict
webhook_code_scanning_alert_reopened_alert_from_dict = WebhookCodeScanningAlertReopenedAlert.from_dict(webhook_code_scanning_alert_reopened_alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


