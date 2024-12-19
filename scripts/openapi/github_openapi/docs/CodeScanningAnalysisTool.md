# CodeScanningAnalysisTool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the tool used to generate the code scanning analysis. | [optional] 
**version** | **str** | The version of the tool used to generate the code scanning analysis. | [optional] 
**guid** | **str** | The GUID of the tool used to generate the code scanning analysis, if provided in the uploaded SARIF data. | [optional] 

## Example

```python
from github_openapi.models.code_scanning_analysis_tool import CodeScanningAnalysisTool

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScanningAnalysisTool from a JSON string
code_scanning_analysis_tool_instance = CodeScanningAnalysisTool.from_json(json)
# print the JSON string representation of the object
print(CodeScanningAnalysisTool.to_json())

# convert the object into a dict
code_scanning_analysis_tool_dict = code_scanning_analysis_tool_instance.to_dict()
# create an instance of CodeScanningAnalysisTool from a dict
code_scanning_analysis_tool_from_dict = CodeScanningAnalysisTool.from_dict(code_scanning_analysis_tool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


