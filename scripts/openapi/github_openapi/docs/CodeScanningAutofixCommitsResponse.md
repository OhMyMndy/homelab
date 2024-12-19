# CodeScanningAutofixCommitsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_ref** | **str** | The Git reference of target branch for the commit. For more information, see \&quot;[Git References](https://git-scm.com/book/en/v2/Git-Internals-Git-References)\&quot; in the Git documentation. | [optional] 
**sha** | **str** | SHA of commit with autofix. | [optional] 

## Example

```python
from github_openapi.models.code_scanning_autofix_commits_response import CodeScanningAutofixCommitsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScanningAutofixCommitsResponse from a JSON string
code_scanning_autofix_commits_response_instance = CodeScanningAutofixCommitsResponse.from_json(json)
# print the JSON string representation of the object
print(CodeScanningAutofixCommitsResponse.to_json())

# convert the object into a dict
code_scanning_autofix_commits_response_dict = code_scanning_autofix_commits_response_instance.to_dict()
# create an instance of CodeScanningAutofixCommitsResponse from a dict
code_scanning_autofix_commits_response_from_dict = CodeScanningAutofixCommitsResponse.from_dict(code_scanning_autofix_commits_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


