# CodespaceGitStatus

Details about the codespace's git repository.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ahead** | **int** | The number of commits the local repository is ahead of the remote. | [optional] 
**behind** | **int** | The number of commits the local repository is behind the remote. | [optional] 
**has_unpushed_changes** | **bool** | Whether the local repository has unpushed changes. | [optional] 
**has_uncommitted_changes** | **bool** | Whether the local repository has uncommitted changes. | [optional] 
**ref** | **str** | The current branch (or SHA if in detached HEAD state) of the local repository. | [optional] 

## Example

```python
from github_openapi.models.codespace_git_status import CodespaceGitStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CodespaceGitStatus from a JSON string
codespace_git_status_instance = CodespaceGitStatus.from_json(json)
# print the JSON string representation of the object
print(CodespaceGitStatus.to_json())

# convert the object into a dict
codespace_git_status_dict = codespace_git_status_instance.to_dict()
# create an instance of CodespaceGitStatus from a dict
codespace_git_status_from_dict = CodespaceGitStatus.from_dict(codespace_git_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


