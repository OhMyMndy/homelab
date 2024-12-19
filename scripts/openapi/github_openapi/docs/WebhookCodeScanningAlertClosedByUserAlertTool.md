# WebhookCodeScanningAlertClosedByUserAlertTool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** |  | [optional] 
**name** | **str** | The name of the tool used to generate the code scanning analysis alert. | 
**version** | **str** | The version of the tool used to detect the alert. | 

## Example

```python
from github_openapi.models.webhook_code_scanning_alert_closed_by_user_alert_tool import WebhookCodeScanningAlertClosedByUserAlertTool

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCodeScanningAlertClosedByUserAlertTool from a JSON string
webhook_code_scanning_alert_closed_by_user_alert_tool_instance = WebhookCodeScanningAlertClosedByUserAlertTool.from_json(json)
# print the JSON string representation of the object
print(WebhookCodeScanningAlertClosedByUserAlertTool.to_json())

# convert the object into a dict
webhook_code_scanning_alert_closed_by_user_alert_tool_dict = webhook_code_scanning_alert_closed_by_user_alert_tool_instance.to_dict()
# create an instance of WebhookCodeScanningAlertClosedByUserAlertTool from a dict
webhook_code_scanning_alert_closed_by_user_alert_tool_from_dict = WebhookCodeScanningAlertClosedByUserAlertTool.from_dict(webhook_code_scanning_alert_closed_by_user_alert_tool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


