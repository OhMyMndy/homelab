# ApiInsightsTimeStatsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** |  | [optional] 
**total_request_count** | **int** |  | [optional] 
**rate_limited_request_count** | **int** |  | [optional] 

## Example

```python
from github_openapi.models.api_insights_time_stats_inner import ApiInsightsTimeStatsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInsightsTimeStatsInner from a JSON string
api_insights_time_stats_inner_instance = ApiInsightsTimeStatsInner.from_json(json)
# print the JSON string representation of the object
print(ApiInsightsTimeStatsInner.to_json())

# convert the object into a dict
api_insights_time_stats_inner_dict = api_insights_time_stats_inner_instance.to_dict()
# create an instance of ApiInsightsTimeStatsInner from a dict
api_insights_time_stats_inner_from_dict = ApiInsightsTimeStatsInner.from_dict(api_insights_time_stats_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


