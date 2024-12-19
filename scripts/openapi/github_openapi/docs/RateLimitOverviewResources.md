# RateLimitOverviewResources


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**core** | [**RateLimit**](RateLimit.md) |  | 
**graphql** | [**RateLimit**](RateLimit.md) |  | [optional] 
**search** | [**RateLimit**](RateLimit.md) |  | 
**code_search** | [**RateLimit**](RateLimit.md) |  | [optional] 
**source_import** | [**RateLimit**](RateLimit.md) |  | [optional] 
**integration_manifest** | [**RateLimit**](RateLimit.md) |  | [optional] 
**code_scanning_upload** | [**RateLimit**](RateLimit.md) |  | [optional] 
**actions_runner_registration** | [**RateLimit**](RateLimit.md) |  | [optional] 
**scim** | [**RateLimit**](RateLimit.md) |  | [optional] 
**dependency_snapshots** | [**RateLimit**](RateLimit.md) |  | [optional] 
**code_scanning_autofix** | [**RateLimit**](RateLimit.md) |  | [optional] 

## Example

```python
from github_openapi.models.rate_limit_overview_resources import RateLimitOverviewResources

# TODO update the JSON string below
json = "{}"
# create an instance of RateLimitOverviewResources from a JSON string
rate_limit_overview_resources_instance = RateLimitOverviewResources.from_json(json)
# print the JSON string representation of the object
print(RateLimitOverviewResources.to_json())

# convert the object into a dict
rate_limit_overview_resources_dict = rate_limit_overview_resources_instance.to_dict()
# create an instance of RateLimitOverviewResources from a dict
rate_limit_overview_resources_from_dict = RateLimitOverviewResources.from_dict(rate_limit_overview_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


