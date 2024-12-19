# CodeScanningAutofixCommits

Commit an autofix for a code scanning alert

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_ref** | **str** | The Git reference of target branch for the commit. Branch needs to already exist.  For more information, see \&quot;[Git References](https://git-scm.com/book/en/v2/Git-Internals-Git-References)\&quot; in the Git documentation. | [optional] 
**message** | **str** | Commit message to be used. | [optional] 

## Example

```python
from github_openapi.models.code_scanning_autofix_commits import CodeScanningAutofixCommits

# TODO update the JSON string below
json = "{}"
# create an instance of CodeScanningAutofixCommits from a JSON string
code_scanning_autofix_commits_instance = CodeScanningAutofixCommits.from_json(json)
# print the JSON string representation of the object
print(CodeScanningAutofixCommits.to_json())

# convert the object into a dict
code_scanning_autofix_commits_dict = code_scanning_autofix_commits_instance.to_dict()
# create an instance of CodeScanningAutofixCommits from a dict
code_scanning_autofix_commits_from_dict = CodeScanningAutofixCommits.from_dict(code_scanning_autofix_commits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


