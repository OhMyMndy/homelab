# BranchRestrictionPolicyAppsInnerOwner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**node_id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**repos_url** | **str** |  | [optional] 
**events_url** | **str** |  | [optional] 
**hooks_url** | **str** |  | [optional] 
**issues_url** | **str** |  | [optional] 
**members_url** | **str** |  | [optional] 
**public_members_url** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**gravatar_id** | **str** |  | [optional] 
**html_url** | **str** |  | [optional] 
**followers_url** | **str** |  | [optional] 
**following_url** | **str** |  | [optional] 
**gists_url** | **str** |  | [optional] 
**starred_url** | **str** |  | [optional] 
**subscriptions_url** | **str** |  | [optional] 
**organizations_url** | **str** |  | [optional] 
**received_events_url** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**site_admin** | **bool** |  | [optional] 
**user_view_type** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.branch_restriction_policy_apps_inner_owner import BranchRestrictionPolicyAppsInnerOwner

# TODO update the JSON string below
json = "{}"
# create an instance of BranchRestrictionPolicyAppsInnerOwner from a JSON string
branch_restriction_policy_apps_inner_owner_instance = BranchRestrictionPolicyAppsInnerOwner.from_json(json)
# print the JSON string representation of the object
print(BranchRestrictionPolicyAppsInnerOwner.to_json())

# convert the object into a dict
branch_restriction_policy_apps_inner_owner_dict = branch_restriction_policy_apps_inner_owner_instance.to_dict()
# create an instance of BranchRestrictionPolicyAppsInnerOwner from a dict
branch_restriction_policy_apps_inner_owner_from_dict = BranchRestrictionPolicyAppsInnerOwner.from_dict(branch_restriction_policy_apps_inner_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


