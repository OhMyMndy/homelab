# WebhookCodeScanningAlertClosedByUserAlertRule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A short description of the rule used to detect the alert. | 
**full_description** | **str** |  | [optional] 
**help** | **str** |  | [optional] 
**help_uri** | **str** | A link to the documentation for the rule used to detect the alert. | [optional] 
**id** | **str** | A unique identifier for the rule used to detect the alert. | 
**name** | **str** |  | [optional] 
**severity** | **str** | The severity of the alert. | 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from github_openapi.models.webhook_code_scanning_alert_closed_by_user_alert_rule import WebhookCodeScanningAlertClosedByUserAlertRule

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCodeScanningAlertClosedByUserAlertRule from a JSON string
webhook_code_scanning_alert_closed_by_user_alert_rule_instance = WebhookCodeScanningAlertClosedByUserAlertRule.from_json(json)
# print the JSON string representation of the object
print(WebhookCodeScanningAlertClosedByUserAlertRule.to_json())

# convert the object into a dict
webhook_code_scanning_alert_closed_by_user_alert_rule_dict = webhook_code_scanning_alert_closed_by_user_alert_rule_instance.to_dict()
# create an instance of WebhookCodeScanningAlertClosedByUserAlertRule from a dict
webhook_code_scanning_alert_closed_by_user_alert_rule_from_dict = WebhookCodeScanningAlertClosedByUserAlertRule.from_dict(webhook_code_scanning_alert_closed_by_user_alert_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


