# CodeScanningDefaultSetupUpdate

Configuration for code scanning default setup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The desired state of code scanning default setup. | [optional] 
**runner_type** | **str** | Runner type to be used. | [optional] 
**runner_label** | **str** | Runner label to be used if the runner type is labeled. | [optional] 
**query_suite** | **str** | CodeQL query suite to be used. | [optional] 
**languages** | **List[str]** | CodeQL languages to be analyzed. | [optional] 

## Example

```python
from github_openapi.models.code_scanning_default_setup_update import CodeScanningDefaultSetupUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScanningDefaultSetupUpdate from a JSON string
code_scanning_default_setup_update_instance = CodeScanningDefaultSetupUpdate.from_json(json)
# print the JSON string representation of the object
print(CodeScanningDefaultSetupUpdate.to_json())

# convert the object into a dict
code_scanning_default_setup_update_dict = code_scanning_default_setup_update_instance.to_dict()
# create an instance of CodeScanningDefaultSetupUpdate from a dict
code_scanning_default_setup_update_from_dict = CodeScanningDefaultSetupUpdate.from_dict(code_scanning_default_setup_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


