# CodeScanningDefaultSetupOptions

Feature options for code scanning default setup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**runner_type** | **str** | Whether to use labeled runners or standard GitHub runners. | [optional] 
**runner_label** | **str** | The label of the runner to use for code scanning default setup when runner_type is &#39;labeled&#39;. | [optional] 

## Example

```python
from github_openapi.models.code_scanning_default_setup_options import CodeScanningDefaultSetupOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScanningDefaultSetupOptions from a JSON string
code_scanning_default_setup_options_instance = CodeScanningDefaultSetupOptions.from_json(json)
# print the JSON string representation of the object
print(CodeScanningDefaultSetupOptions.to_json())

# convert the object into a dict
code_scanning_default_setup_options_dict = code_scanning_default_setup_options_instance.to_dict()
# create an instance of CodeScanningDefaultSetupOptions from a dict
code_scanning_default_setup_options_from_dict = CodeScanningDefaultSetupOptions.from_dict(code_scanning_default_setup_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


