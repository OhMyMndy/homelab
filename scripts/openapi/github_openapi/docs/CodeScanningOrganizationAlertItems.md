# CodeScanningOrganizationAlertItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** | The security alert number. | [readonly] 
**created_at** | **datetime** | The time that the alert was created in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [readonly] 
**updated_at** | **datetime** | The time that the alert was last updated in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] [readonly] 
**url** | **str** | The REST API URL of the alert resource. | [readonly] 
**html_url** | **str** | The GitHub URL of the alert resource. | [readonly] 
**instances_url** | **str** | The REST API URL for fetching the list of instances for an alert. | [readonly] 
**state** | [**CodeScanningAlertState**](CodeScanningAlertState.md) |  | 
**fixed_at** | **datetime** | The time that the alert was no longer detected and was considered fixed in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] [readonly] 
**dismissed_by** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**dismissed_at** | **datetime** | The time that the alert was dismissed in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [readonly] 
**dismissed_reason** | [**CodeScanningAlertDismissedReason**](CodeScanningAlertDismissedReason.md) |  | 
**dismissed_comment** | **str** | The dismissal comment associated with the dismissal of the alert. | [optional] 
**rule** | [**CodeScanningAlertRuleSummary**](CodeScanningAlertRuleSummary.md) |  | 
**tool** | [**CodeScanningAnalysisTool**](CodeScanningAnalysisTool.md) |  | 
**most_recent_instance** | [**CodeScanningAlertInstance**](CodeScanningAlertInstance.md) |  | 
**repository** | [**SimpleRepository**](SimpleRepository.md) |  | 

## Example

```python
from github_openapi.models.code_scanning_organization_alert_items import CodeScanningOrganizationAlertItems

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScanningOrganizationAlertItems from a JSON string
code_scanning_organization_alert_items_instance = CodeScanningOrganizationAlertItems.from_json(json)
# print the JSON string representation of the object
print(CodeScanningOrganizationAlertItems.to_json())

# convert the object into a dict
code_scanning_organization_alert_items_dict = code_scanning_organization_alert_items_instance.to_dict()
# create an instance of CodeScanningOrganizationAlertItems from a dict
code_scanning_organization_alert_items_from_dict = CodeScanningOrganizationAlertItems.from_dict(code_scanning_organization_alert_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


