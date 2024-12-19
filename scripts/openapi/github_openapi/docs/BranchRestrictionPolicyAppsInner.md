# BranchRestrictionPolicyAppsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**slug** | **str** |  | [optional] 
**node_id** | **str** |  | [optional] 
**owner** | [**BranchRestrictionPolicyAppsInnerOwner**](BranchRestrictionPolicyAppsInnerOwner.md) |  | [optional] 
**name** | **str** |  | [optional] 
**client_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**external_url** | **str** |  | [optional] 
**html_url** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**permissions** | [**BranchRestrictionPolicyAppsInnerPermissions**](BranchRestrictionPolicyAppsInnerPermissions.md) |  | [optional] 
**events** | **List[str]** |  | [optional] 

## Example

```python
from github_openapi.models.branch_restriction_policy_apps_inner import BranchRestrictionPolicyAppsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BranchRestrictionPolicyAppsInner from a JSON string
branch_restriction_policy_apps_inner_instance = BranchRestrictionPolicyAppsInner.from_json(json)
# print the JSON string representation of the object
print(BranchRestrictionPolicyAppsInner.to_json())

# convert the object into a dict
branch_restriction_policy_apps_inner_dict = branch_restriction_policy_apps_inner_instance.to_dict()
# create an instance of BranchRestrictionPolicyAppsInner from a dict
branch_restriction_policy_apps_inner_from_dict = BranchRestrictionPolicyAppsInner.from_dict(branch_restriction_policy_apps_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


