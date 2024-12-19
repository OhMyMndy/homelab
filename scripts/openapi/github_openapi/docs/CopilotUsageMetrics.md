# CopilotUsageMetrics

Summary of Copilot usage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **date** | The date for which the usage metrics are reported, in &#x60;YYYY-MM-DD&#x60; format. | 
**total_suggestions_count** | **int** | The total number of Copilot code completion suggestions shown to users. | [optional] 
**total_acceptances_count** | **int** | The total number of Copilot code completion suggestions accepted by users. | [optional] 
**total_lines_suggested** | **int** | The total number of lines of code completions suggested by Copilot. | [optional] 
**total_lines_accepted** | **int** | The total number of lines of code completions accepted by users. | [optional] 
**total_active_users** | **int** | The total number of users who were shown Copilot code completion suggestions during the day specified. | [optional] 
**total_chat_acceptances** | **int** | The total instances of users who accepted code suggested by Copilot Chat in the IDE (panel and inline). | [optional] 
**total_chat_turns** | **int** | The total number of chat turns (prompt and response pairs) sent between users and Copilot Chat in the IDE. | [optional] 
**total_active_chat_users** | **int** | The total number of users who interacted with Copilot Chat in the IDE during the day specified. | [optional] 
**breakdown** | [**List[CopilotUsageMetricsBreakdownInner]**](CopilotUsageMetricsBreakdownInner.md) | Breakdown of Copilot code completions usage by language and editor | 

## Example

```python
from github_openapi.models.copilot_usage_metrics import CopilotUsageMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of CopilotUsageMetrics from a JSON string
copilot_usage_metrics_instance = CopilotUsageMetrics.from_json(json)
# print the JSON string representation of the object
print(CopilotUsageMetrics.to_json())

# convert the object into a dict
copilot_usage_metrics_dict = copilot_usage_metrics_instance.to_dict()
# create an instance of CopilotUsageMetrics from a dict
copilot_usage_metrics_from_dict = CopilotUsageMetrics.from_dict(copilot_usage_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


