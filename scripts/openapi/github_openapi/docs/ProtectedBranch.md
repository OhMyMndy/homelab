# ProtectedBranch

Branch protections protect branches

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**required_status_checks** | [**StatusCheckPolicy**](StatusCheckPolicy.md) |  | [optional] 
**required_pull_request_reviews** | [**ProtectedBranchRequiredPullRequestReviews**](ProtectedBranchRequiredPullRequestReviews.md) |  | [optional] 
**required_signatures** | [**BranchProtectionRequiredSignatures**](BranchProtectionRequiredSignatures.md) |  | [optional] 
**enforce_admins** | [**ProtectedBranchEnforceAdmins**](ProtectedBranchEnforceAdmins.md) |  | [optional] 
**required_linear_history** | [**ProtectedBranchRequiredLinearHistory**](ProtectedBranchRequiredLinearHistory.md) |  | [optional] 
**allow_force_pushes** | [**ProtectedBranchRequiredLinearHistory**](ProtectedBranchRequiredLinearHistory.md) |  | [optional] 
**allow_deletions** | [**ProtectedBranchRequiredLinearHistory**](ProtectedBranchRequiredLinearHistory.md) |  | [optional] 
**restrictions** | [**BranchRestrictionPolicy**](BranchRestrictionPolicy.md) |  | [optional] 
**required_conversation_resolution** | [**ProtectedBranchRequiredConversationResolution**](ProtectedBranchRequiredConversationResolution.md) |  | [optional] 
**block_creations** | [**ProtectedBranchRequiredLinearHistory**](ProtectedBranchRequiredLinearHistory.md) |  | [optional] 
**lock_branch** | [**ProtectedBranchLockBranch**](ProtectedBranchLockBranch.md) |  | [optional] 
**allow_fork_syncing** | [**ProtectedBranchAllowForkSyncing**](ProtectedBranchAllowForkSyncing.md) |  | [optional] 

## Example

```python
from github_openapi.models.protected_branch import ProtectedBranch

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectedBranch from a JSON string
protected_branch_instance = ProtectedBranch.from_json(json)
# print the JSON string representation of the object
print(ProtectedBranch.to_json())

# convert the object into a dict
protected_branch_dict = protected_branch_instance.to_dict()
# create an instance of ProtectedBranch from a dict
protected_branch_from_dict = ProtectedBranch.from_dict(protected_branch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


