# WebhookCodeScanningAlertAppearedInBranchAlertRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A short description of the rule used to detect the alert. | 
**id** | **str** | A unique identifier for the rule used to detect the alert. | 
**severity** | **str** | The severity of the alert. | 

## Example

```python
from github_openapi.models.webhook_code_scanning_alert_appeared_in_branch_alert_rule import WebhookCodeScanningAlertAppearedInBranchAlertRule

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCodeScanningAlertAppearedInBranchAlertRule from a JSON string
webhook_code_scanning_alert_appeared_in_branch_alert_rule_instance = WebhookCodeScanningAlertAppearedInBranchAlertRule.from_json(json)
# print the JSON string representation of the object
print(WebhookCodeScanningAlertAppearedInBranchAlertRule.to_json())

# convert the object into a dict
webhook_code_scanning_alert_appeared_in_branch_alert_rule_dict = webhook_code_scanning_alert_appeared_in_branch_alert_rule_instance.to_dict()
# create an instance of WebhookCodeScanningAlertAppearedInBranchAlertRule from a dict
webhook_code_scanning_alert_appeared_in_branch_alert_rule_from_dict = WebhookCodeScanningAlertAppearedInBranchAlertRule.from_dict(webhook_code_scanning_alert_appeared_in_branch_alert_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


