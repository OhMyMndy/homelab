# CodeownersErrorsErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line** | **int** | The line number where this errors occurs. | 
**column** | **int** | The column number where this errors occurs. | 
**source** | **str** | The contents of the line where the error occurs. | [optional] 
**kind** | **str** | The type of error. | 
**suggestion** | **str** | Suggested action to fix the error. This will usually be &#x60;null&#x60;, but is provided for some common errors. | [optional] 
**message** | **str** | A human-readable description of the error, combining information from multiple fields, laid out for display in a monospaced typeface (for example, a command-line setting). | 
**path** | **str** | The path of the file where the error occured. | 

## Example

```python
from github_openapi.models.codeowners_errors_errors_inner import CodeownersErrorsErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CodeownersErrorsErrorsInner from a JSON string
codeowners_errors_errors_inner_instance = CodeownersErrorsErrorsInner.from_json(json)
# print the JSON string representation of the object
print(CodeownersErrorsErrorsInner.to_json())

# convert the object into a dict
codeowners_errors_errors_inner_dict = codeowners_errors_errors_inner_instance.to_dict()
# create an instance of CodeownersErrorsErrorsInner from a dict
codeowners_errors_errors_inner_from_dict = CodeownersErrorsErrorsInner.from_dict(codeowners_errors_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


