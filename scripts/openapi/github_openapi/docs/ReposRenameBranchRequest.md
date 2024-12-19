# ReposRenameBranchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_name** | **str** | The new name of the branch. | 

## Example

```python
from github_openapi.models.repos_rename_branch_request import ReposRenameBranchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposRenameBranchRequest from a JSON string
repos_rename_branch_request_instance = ReposRenameBranchRequest.from_json(json)
# print the JSON string representation of the object
print(ReposRenameBranchRequest.to_json())

# convert the object into a dict
repos_rename_branch_request_dict = repos_rename_branch_request_instance.to_dict()
# create an instance of ReposRenameBranchRequest from a dict
repos_rename_branch_request_from_dict = ReposRenameBranchRequest.from_dict(repos_rename_branch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


