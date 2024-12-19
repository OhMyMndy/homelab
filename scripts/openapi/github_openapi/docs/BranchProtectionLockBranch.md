# BranchProtectionLockBranch

Whether to set the branch as read-only. If this is true, users will not be able to push to the branch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] [default to False]

## Example

```python
from github_openapi.models.branch_protection_lock_branch import BranchProtectionLockBranch

# TODO update the JSON string below
json = "{}"
# create an instance of BranchProtectionLockBranch from a JSON string
branch_protection_lock_branch_instance = BranchProtectionLockBranch.from_json(json)
# print the JSON string representation of the object
print(BranchProtectionLockBranch.to_json())

# convert the object into a dict
branch_protection_lock_branch_dict = branch_protection_lock_branch_instance.to_dict()
# create an instance of BranchProtectionLockBranch from a dict
branch_protection_lock_branch_from_dict = BranchProtectionLockBranch.from_dict(branch_protection_lock_branch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


