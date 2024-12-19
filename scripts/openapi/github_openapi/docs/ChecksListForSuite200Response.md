# ChecksListForSuite200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | 
**check_runs** | [**List[CheckRun]**](CheckRun.md) |  | 

## Example

```python
from github_openapi.models.checks_list_for_suite200_response import ChecksListForSuite200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ChecksListForSuite200Response from a JSON string
checks_list_for_suite200_response_instance = ChecksListForSuite200Response.from_json(json)
# print the JSON string representation of the object
print(ChecksListForSuite200Response.to_json())

# convert the object into a dict
checks_list_for_suite200_response_dict = checks_list_for_suite200_response_instance.to_dict()
# create an instance of ChecksListForSuite200Response from a dict
checks_list_for_suite200_response_from_dict = ChecksListForSuite200Response.from_dict(checks_list_for_suite200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


