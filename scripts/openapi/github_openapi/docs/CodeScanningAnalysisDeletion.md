# CodeScanningAnalysisDeletion

Successful deletion of a code scanning analysis

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_analysis_url** | **str** | Next deletable analysis in chain, without last analysis deletion confirmation | [readonly] 
**confirm_delete_url** | **str** | Next deletable analysis in chain, with last analysis deletion confirmation | [readonly] 

## Example

```python
from github_openapi.models.code_scanning_analysis_deletion import CodeScanningAnalysisDeletion

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScanningAnalysisDeletion from a JSON string
code_scanning_analysis_deletion_instance = CodeScanningAnalysisDeletion.from_json(json)
# print the JSON string representation of the object
print(CodeScanningAnalysisDeletion.to_json())

# convert the object into a dict
code_scanning_analysis_deletion_dict = code_scanning_analysis_deletion_instance.to_dict()
# create an instance of CodeScanningAnalysisDeletion from a dict
code_scanning_analysis_deletion_from_dict = CodeScanningAnalysisDeletion.from_dict(code_scanning_analysis_deletion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


