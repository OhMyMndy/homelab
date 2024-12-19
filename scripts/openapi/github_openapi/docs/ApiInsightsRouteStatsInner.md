# ApiInsightsRouteStatsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_method** | **str** | The HTTP method | [optional] 
**api_route** | **str** | The API path&#39;s route template | [optional] 
**total_request_count** | **int** | The total number of requests within the queried time period | [optional] 
**rate_limited_request_count** | **int** | The total number of requests that were rate limited within the queried time period | [optional] 
**last_rate_limited_timestamp** | **str** |  | [optional] 
**last_request_timestamp** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.api_insights_route_stats_inner import ApiInsightsRouteStatsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInsightsRouteStatsInner from a JSON string
api_insights_route_stats_inner_instance = ApiInsightsRouteStatsInner.from_json(json)
# print the JSON string representation of the object
print(ApiInsightsRouteStatsInner.to_json())

# convert the object into a dict
api_insights_route_stats_inner_dict = api_insights_route_stats_inner_instance.to_dict()
# create an instance of ApiInsightsRouteStatsInner from a dict
api_insights_route_stats_inner_from_dict = ApiInsightsRouteStatsInner.from_dict(api_insights_route_stats_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


