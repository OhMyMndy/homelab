# RateLimitOverview

Rate Limit Overview

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | [**RateLimitOverviewResources**](RateLimitOverviewResources.md) |  | 
**rate** | [**RateLimit**](RateLimit.md) |  | 

## Example

```python
from github_openapi.models.rate_limit_overview import RateLimitOverview

# TODO update the JSON string below
json = "{}"
# create an instance of RateLimitOverview from a JSON string
rate_limit_overview_instance = RateLimitOverview.from_json(json)
# print the JSON string representation of the object
print(RateLimitOverview.to_json())

# convert the object into a dict
rate_limit_overview_dict = rate_limit_overview_instance.to_dict()
# create an instance of RateLimitOverview from a dict
rate_limit_overview_from_dict = RateLimitOverview.from_dict(rate_limit_overview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


