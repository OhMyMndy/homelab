# BranchRestrictionPolicy

Branch Restriction Policy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**users_url** | **str** |  | 
**teams_url** | **str** |  | 
**apps_url** | **str** |  | 
**users** | [**List[BranchRestrictionPolicyUsersInner]**](BranchRestrictionPolicyUsersInner.md) |  | 
**teams** | [**List[BranchRestrictionPolicyTeamsInner]**](BranchRestrictionPolicyTeamsInner.md) |  | 
**apps** | [**List[BranchRestrictionPolicyAppsInner]**](BranchRestrictionPolicyAppsInner.md) |  | 

## Example

```python
from github_openapi.models.branch_restriction_policy import BranchRestrictionPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of BranchRestrictionPolicy from a JSON string
branch_restriction_policy_instance = BranchRestrictionPolicy.from_json(json)
# print the JSON string representation of the object
print(BranchRestrictionPolicy.to_json())

# convert the object into a dict
branch_restriction_policy_dict = branch_restriction_policy_instance.to_dict()
# create an instance of BranchRestrictionPolicy from a dict
branch_restriction_policy_from_dict = BranchRestrictionPolicy.from_dict(branch_restriction_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


