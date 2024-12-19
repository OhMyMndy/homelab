# BranchRestrictionPolicyAppsInnerPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **str** |  | [optional] 
**contents** | **str** |  | [optional] 
**issues** | **str** |  | [optional] 
**single_file** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.branch_restriction_policy_apps_inner_permissions import BranchRestrictionPolicyAppsInnerPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of BranchRestrictionPolicyAppsInnerPermissions from a JSON string
branch_restriction_policy_apps_inner_permissions_instance = BranchRestrictionPolicyAppsInnerPermissions.from_json(json)
# print the JSON string representation of the object
print(BranchRestrictionPolicyAppsInnerPermissions.to_json())

# convert the object into a dict
branch_restriction_policy_apps_inner_permissions_dict = branch_restriction_policy_apps_inner_permissions_instance.to_dict()
# create an instance of BranchRestrictionPolicyAppsInnerPermissions from a dict
branch_restriction_policy_apps_inner_permissions_from_dict = BranchRestrictionPolicyAppsInnerPermissions.from_dict(branch_restriction_policy_apps_inner_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


