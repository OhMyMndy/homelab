# CodeScanningAutofix


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**CodeScanningAutofixStatus**](CodeScanningAutofixStatus.md) |  | 
**description** | **str** | The description of an autofix. | 
**started_at** | **datetime** | The start time of an autofix in ISO 8601 format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [readonly] 

## Example

```python
from github_openapi.models.code_scanning_autofix import CodeScanningAutofix

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScanningAutofix from a JSON string
code_scanning_autofix_instance = CodeScanningAutofix.from_json(json)
# print the JSON string representation of the object
print(CodeScanningAutofix.to_json())

# convert the object into a dict
code_scanning_autofix_dict = code_scanning_autofix_instance.to_dict()
# create an instance of CodeScanningAutofix from a dict
code_scanning_autofix_from_dict = CodeScanningAutofix.from_dict(code_scanning_autofix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


