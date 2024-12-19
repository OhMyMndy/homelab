# CodeScanningDefaultSetupUpdateResponse

You can use `run_url` to track the status of the run. This includes a property status and conclusion. You should not rely on this always being an actions workflow run object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_id** | **int** | ID of the corresponding run. | [optional] 
**run_url** | **str** | URL of the corresponding run. | [optional] 

## Example

```python
from github_openapi.models.code_scanning_default_setup_update_response import CodeScanningDefaultSetupUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScanningDefaultSetupUpdateResponse from a JSON string
code_scanning_default_setup_update_response_instance = CodeScanningDefaultSetupUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(CodeScanningDefaultSetupUpdateResponse.to_json())

# convert the object into a dict
code_scanning_default_setup_update_response_dict = code_scanning_default_setup_update_response_instance.to_dict()
# create an instance of CodeScanningDefaultSetupUpdateResponse from a dict
code_scanning_default_setup_update_response_from_dict = CodeScanningDefaultSetupUpdateResponse.from_dict(code_scanning_default_setup_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


