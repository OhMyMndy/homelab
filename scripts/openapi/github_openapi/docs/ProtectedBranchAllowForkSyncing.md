# ProtectedBranchAllowForkSyncing

Whether users can pull changes from upstream when the branch is locked. Set to `true` to allow fork syncing. Set to `false` to prevent fork syncing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] [default to False]

## Example

```python
from github_openapi.models.protected_branch_allow_fork_syncing import ProtectedBranchAllowForkSyncing

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectedBranchAllowForkSyncing from a JSON string
protected_branch_allow_fork_syncing_instance = ProtectedBranchAllowForkSyncing.from_json(json)
# print the JSON string representation of the object
print(ProtectedBranchAllowForkSyncing.to_json())

# convert the object into a dict
protected_branch_allow_fork_syncing_dict = protected_branch_allow_fork_syncing_instance.to_dict()
# create an instance of ProtectedBranchAllowForkSyncing from a dict
protected_branch_allow_fork_syncing_from_dict = ProtectedBranchAllowForkSyncing.from_dict(protected_branch_allow_fork_syncing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


