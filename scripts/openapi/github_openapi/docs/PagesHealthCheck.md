# PagesHealthCheck

Pages Health Check Status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | [**PagesHealthCheckDomain**](PagesHealthCheckDomain.md) |  | [optional] 
**alt_domain** | [**PagesHealthCheckAltDomain**](PagesHealthCheckAltDomain.md) |  | [optional] 

## Example

```python
from github_openapi.models.pages_health_check import PagesHealthCheck

# TODO update the JSON string below
json = "{}"
# create an instance of PagesHealthCheck from a JSON string
pages_health_check_instance = PagesHealthCheck.from_json(json)
# print the JSON string representation of the object
print(PagesHealthCheck.to_json())

# convert the object into a dict
pages_health_check_dict = pages_health_check_instance.to_dict()
# create an instance of PagesHealthCheck from a dict
pages_health_check_from_dict = PagesHealthCheck.from_dict(pages_health_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


