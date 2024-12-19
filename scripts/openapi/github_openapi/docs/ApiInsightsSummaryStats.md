# ApiInsightsSummaryStats

API Insights usage summary stats for an organization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_request_count** | **int** | The total number of requests within the queried time period | [optional] 
**rate_limited_request_count** | **int** | The total number of requests that were rate limited within the queried time period | [optional] 

## Example

```python
from github_openapi.models.api_insights_summary_stats import ApiInsightsSummaryStats

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInsightsSummaryStats from a JSON string
api_insights_summary_stats_instance = ApiInsightsSummaryStats.from_json(json)
# print the JSON string representation of the object
print(ApiInsightsSummaryStats.to_json())

# convert the object into a dict
api_insights_summary_stats_dict = api_insights_summary_stats_instance.to_dict()
# create an instance of ApiInsightsSummaryStats from a dict
api_insights_summary_stats_from_dict = ApiInsightsSummaryStats.from_dict(api_insights_summary_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


