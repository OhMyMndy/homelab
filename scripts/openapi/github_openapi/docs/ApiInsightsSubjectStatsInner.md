# ApiInsightsSubjectStatsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject_type** | **str** |  | [optional] 
**subject_name** | **str** |  | [optional] 
**subject_id** | **int** |  | [optional] 
**total_request_count** | **int** |  | [optional] 
**rate_limited_request_count** | **int** |  | [optional] 
**last_rate_limited_timestamp** | **str** |  | [optional] 
**last_request_timestamp** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.api_insights_subject_stats_inner import ApiInsightsSubjectStatsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInsightsSubjectStatsInner from a JSON string
api_insights_subject_stats_inner_instance = ApiInsightsSubjectStatsInner.from_json(json)
# print the JSON string representation of the object
print(ApiInsightsSubjectStatsInner.to_json())

# convert the object into a dict
api_insights_subject_stats_inner_dict = api_insights_subject_stats_inner_instance.to_dict()
# create an instance of ApiInsightsSubjectStatsInner from a dict
api_insights_subject_stats_inner_from_dict = ApiInsightsSubjectStatsInner.from_dict(api_insights_subject_stats_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


