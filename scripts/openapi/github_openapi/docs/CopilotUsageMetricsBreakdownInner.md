# CopilotUsageMetricsBreakdownInner

Breakdown of Copilot usage by editor for this language

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | The language in which Copilot suggestions were shown to users in the specified editor. | [optional] 
**editor** | **str** | The editor in which Copilot suggestions were shown to users for the specified language. | [optional] 
**suggestions_count** | **int** | The number of Copilot suggestions shown to users in the editor specified during the day specified. | [optional] 
**acceptances_count** | **int** | The number of Copilot suggestions accepted by users in the editor specified during the day specified. | [optional] 
**lines_suggested** | **int** | The number of lines of code suggested by Copilot in the editor specified during the day specified. | [optional] 
**lines_accepted** | **int** | The number of lines of code accepted by users in the editor specified during the day specified. | [optional] 
**active_users** | **int** | The number of users who were shown Copilot completion suggestions in the editor specified during the day specified. | [optional] 

## Example

```python
from github_openapi.models.copilot_usage_metrics_breakdown_inner import CopilotUsageMetricsBreakdownInner

# TODO update the JSON string below
json = "{}"
# create an instance of CopilotUsageMetricsBreakdownInner from a JSON string
copilot_usage_metrics_breakdown_inner_instance = CopilotUsageMetricsBreakdownInner.from_json(json)
# print the JSON string representation of the object
print(CopilotUsageMetricsBreakdownInner.to_json())

# convert the object into a dict
copilot_usage_metrics_breakdown_inner_dict = copilot_usage_metrics_breakdown_inner_instance.to_dict()
# create an instance of CopilotUsageMetricsBreakdownInner from a dict
copilot_usage_metrics_breakdown_inner_from_dict = CopilotUsageMetricsBreakdownInner.from_dict(copilot_usage_metrics_breakdown_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


