# ApiInsightsUserStatsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor_type** | **str** |  | [optional] 
**actor_name** | **str** |  | [optional] 
**actor_id** | **int** |  | [optional] 
**integration_id** | **int** |  | [optional] 
**oauth_application_id** | **int** |  | [optional] 
**total_request_count** | **int** |  | [optional] 
**rate_limited_request_count** | **int** |  | [optional] 
**last_rate_limited_timestamp** | **str** |  | [optional] 
**last_request_timestamp** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.api_insights_user_stats_inner import ApiInsightsUserStatsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInsightsUserStatsInner from a JSON string
api_insights_user_stats_inner_instance = ApiInsightsUserStatsInner.from_json(json)
# print the JSON string representation of the object
print(ApiInsightsUserStatsInner.to_json())

# convert the object into a dict
api_insights_user_stats_inner_dict = api_insights_user_stats_inner_instance.to_dict()
# create an instance of ApiInsightsUserStatsInner from a dict
api_insights_user_stats_inner_from_dict = ApiInsightsUserStatsInner.from_dict(api_insights_user_stats_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


