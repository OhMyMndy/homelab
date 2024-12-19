# CopilotUsageMetricsDay

Copilot usage metrics for a given day.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | The date for which the usage metrics are aggregated, in &#x60;YYYY-MM-DD&#x60; format. | 
**total_active_users** | **int** | The total number of Copilot users with activity belonging to any Copilot feature, globally, for the given day. Includes passive activity such as receiving a code suggestion, as well as engagement activity such as accepting a code suggestion or prompting chat. Does not include authentication events. Is not limited to the individual features detailed on the endpoint. | [optional] 
**total_engaged_users** | **int** | The total number of Copilot users who engaged with any Copilot feature, for the given day. Examples include but are not limited to accepting a code suggestion, prompting Copilot chat, or triggering a PR Summary. Does not include authentication events. Is not limited to the individual features detailed on the endpoint. | [optional] 
**copilot_ide_code_completions** | [**CopilotIdeCodeCompletions**](CopilotIdeCodeCompletions.md) |  | [optional] 
**copilot_ide_chat** | [**CopilotIdeChat**](CopilotIdeChat.md) |  | [optional] 
**copilot_dotcom_chat** | [**CopilotDotcomChat**](CopilotDotcomChat.md) |  | [optional] 
**copilot_dotcom_pull_requests** | [**CopilotDotcomPullRequests**](CopilotDotcomPullRequests.md) |  | [optional] 

## Example

```python
from github_openapi.models.copilot_usage_metrics_day import CopilotUsageMetricsDay

# TODO update the JSON string below
json = "{}"
# create an instance of CopilotUsageMetricsDay from a JSON string
copilot_usage_metrics_day_instance = CopilotUsageMetricsDay.from_json(json)
# print the JSON string representation of the object
print(CopilotUsageMetricsDay.to_json())

# convert the object into a dict
copilot_usage_metrics_day_dict = copilot_usage_metrics_day_instance.to_dict()
# create an instance of CopilotUsageMetricsDay from a dict
copilot_usage_metrics_day_from_dict = CopilotUsageMetricsDay.from_dict(copilot_usage_metrics_day_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


