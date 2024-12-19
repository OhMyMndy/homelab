# ChecksCreateSuiteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**head_sha** | **str** | The sha of the head commit. | 

## Example

```python
from github_openapi.models.checks_create_suite_request import ChecksCreateSuiteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChecksCreateSuiteRequest from a JSON string
checks_create_suite_request_instance = ChecksCreateSuiteRequest.from_json(json)
# print the JSON string representation of the object
print(ChecksCreateSuiteRequest.to_json())

# convert the object into a dict
checks_create_suite_request_dict = checks_create_suite_request_instance.to_dict()
# create an instance of ChecksCreateSuiteRequest from a dict
checks_create_suite_request_from_dict = ChecksCreateSuiteRequest.from_dict(checks_create_suite_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


