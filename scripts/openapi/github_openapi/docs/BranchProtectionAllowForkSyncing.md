# BranchProtectionAllowForkSyncing

Whether users can pull changes from upstream when the branch is locked. Set to `true` to allow fork syncing. Set to `false` to prevent fork syncing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] [default to False]

## Example

```python
from github_openapi.models.branch_protection_allow_fork_syncing import BranchProtectionAllowForkSyncing

# TODO update the JSON string below
json = "{}"
# create an instance of BranchProtectionAllowForkSyncing from a JSON string
branch_protection_allow_fork_syncing_instance = BranchProtectionAllowForkSyncing.from_json(json)
# print the JSON string representation of the object
print(BranchProtectionAllowForkSyncing.to_json())

# convert the object into a dict
branch_protection_allow_fork_syncing_dict = branch_protection_allow_fork_syncing_instance.to_dict()
# create an instance of BranchProtectionAllowForkSyncing from a dict
branch_protection_allow_fork_syncing_from_dict = BranchProtectionAllowForkSyncing.from_dict(branch_protection_allow_fork_syncing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


