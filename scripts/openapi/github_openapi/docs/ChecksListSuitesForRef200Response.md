# ChecksListSuitesForRef200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**check_suites** | [**List[CheckSuite]**](CheckSuite.md) |  | 

## Example

```python
from github_openapi.models.checks_list_suites_for_ref200_response import ChecksListSuitesForRef200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ChecksListSuitesForRef200Response from a JSON string
checks_list_suites_for_ref200_response_instance = ChecksListSuitesForRef200Response.from_json(json)
# print the JSON string representation of the object
print(ChecksListSuitesForRef200Response.to_json())

# convert the object into a dict
checks_list_suites_for_ref200_response_dict = checks_list_suites_for_ref200_response_instance.to_dict()
# create an instance of ChecksListSuitesForRef200Response from a dict
checks_list_suites_for_ref200_response_from_dict = ChecksListSuitesForRef200Response.from_dict(checks_list_suites_for_ref200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


