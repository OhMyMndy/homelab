# CodeownersErrors

A list of errors found in a repo's CODEOWNERS file

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[CodeownersErrorsErrorsInner]**](CodeownersErrorsErrorsInner.md) |  | 

## Example

```python
from github_openapi.models.codeowners_errors import CodeownersErrors

# TODO update the JSON string below
json = "{}"
# create an instance of CodeownersErrors from a JSON string
codeowners_errors_instance = CodeownersErrors.from_json(json)
# print the JSON string representation of the object
print(CodeownersErrors.to_json())

# convert the object into a dict
codeowners_errors_dict = codeowners_errors_instance.to_dict()
# create an instance of CodeownersErrors from a dict
codeowners_errors_from_dict = CodeownersErrors.from_dict(codeowners_errors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


