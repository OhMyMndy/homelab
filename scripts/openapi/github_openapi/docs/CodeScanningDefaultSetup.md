# CodeScanningDefaultSetup

Configuration for code scanning default setup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | Code scanning default setup has been configured or not. | [optional] 
**languages** | **List[str]** | Languages to be analyzed. | [optional] 
**query_suite** | **str** | CodeQL query suite to be used. | [optional] 
**updated_at** | **datetime** | Timestamp of latest configuration update. | [optional] 
**schedule** | **str** | The frequency of the periodic analysis. | [optional] 

## Example

```python
from github_openapi.models.code_scanning_default_setup import CodeScanningDefaultSetup

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScanningDefaultSetup from a JSON string
code_scanning_default_setup_instance = CodeScanningDefaultSetup.from_json(json)
# print the JSON string representation of the object
print(CodeScanningDefaultSetup.to_json())

# convert the object into a dict
code_scanning_default_setup_dict = code_scanning_default_setup_instance.to_dict()
# create an instance of CodeScanningDefaultSetup from a dict
code_scanning_default_setup_from_dict = CodeScanningDefaultSetup.from_dict(code_scanning_default_setup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


