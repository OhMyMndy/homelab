# ProtectedBranchEnforceAdmins


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**enabled** | **bool** |  | 

## Example

```python
from github_openapi.models.protected_branch_enforce_admins import ProtectedBranchEnforceAdmins

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectedBranchEnforceAdmins from a JSON string
protected_branch_enforce_admins_instance = ProtectedBranchEnforceAdmins.from_json(json)
# print the JSON string representation of the object
print(ProtectedBranchEnforceAdmins.to_json())

# convert the object into a dict
protected_branch_enforce_admins_dict = protected_branch_enforce_admins_instance.to_dict()
# create an instance of ProtectedBranchEnforceAdmins from a dict
protected_branch_enforce_admins_from_dict = ProtectedBranchEnforceAdmins.from_dict(protected_branch_enforce_admins_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


