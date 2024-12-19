# ProtectedBranchLockBranch

Whether to set the branch as read-only. If this is true, users will not be able to push to the branch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] [default to False]

## Example

```python
from github_openapi.models.protected_branch_lock_branch import ProtectedBranchLockBranch

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectedBranchLockBranch from a JSON string
protected_branch_lock_branch_instance = ProtectedBranchLockBranch.from_json(json)
# print the JSON string representation of the object
print(ProtectedBranchLockBranch.to_json())

# convert the object into a dict
protected_branch_lock_branch_dict = protected_branch_lock_branch_instance.to_dict()
# create an instance of ProtectedBranchLockBranch from a dict
protected_branch_lock_branch_from_dict = ProtectedBranchLockBranch.from_dict(protected_branch_lock_branch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


