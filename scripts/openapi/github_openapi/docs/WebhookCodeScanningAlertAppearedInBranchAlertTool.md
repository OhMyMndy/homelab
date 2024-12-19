# WebhookCodeScanningAlertAppearedInBranchAlertTool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the tool used to generate the code scanning analysis alert. | 
**version** | **str** | The version of the tool used to detect the alert. | 

## Example

```python
from github_openapi.models.webhook_code_scanning_alert_appeared_in_branch_alert_tool import WebhookCodeScanningAlertAppearedInBranchAlertTool

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCodeScanningAlertAppearedInBranchAlertTool from a JSON string
webhook_code_scanning_alert_appeared_in_branch_alert_tool_instance = WebhookCodeScanningAlertAppearedInBranchAlertTool.from_json(json)
# print the JSON string representation of the object
print(WebhookCodeScanningAlertAppearedInBranchAlertTool.to_json())

# convert the object into a dict
webhook_code_scanning_alert_appeared_in_branch_alert_tool_dict = webhook_code_scanning_alert_appeared_in_branch_alert_tool_instance.to_dict()
# create an instance of WebhookCodeScanningAlertAppearedInBranchAlertTool from a dict
webhook_code_scanning_alert_appeared_in_branch_alert_tool_from_dict = WebhookCodeScanningAlertAppearedInBranchAlertTool.from_dict(webhook_code_scanning_alert_appeared_in_branch_alert_tool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

