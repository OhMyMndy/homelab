# ProtectedBranchAdminEnforced

Protected Branch Admin Enforced

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**enabled** | **bool** |  | 

## Example

```python
from github_openapi.models.protected_branch_admin_enforced import ProtectedBranchAdminEnforced

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectedBranchAdminEnforced from a JSON string
protected_branch_admin_enforced_instance = ProtectedBranchAdminEnforced.from_json(json)
# print the JSON string representation of the object
print(ProtectedBranchAdminEnforced.to_json())

# convert the object into a dict
protected_branch_admin_enforced_dict = protected_branch_admin_enforced_instance.to_dict()
# create an instance of ProtectedBranchAdminEnforced from a dict
protected_branch_admin_enforced_from_dict = ProtectedBranchAdminEnforced.from_dict(protected_branch_admin_enforced_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


