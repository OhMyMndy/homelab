# BranchRestrictionPolicyTeamsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**node_id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**html_url** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**privacy** | **str** |  | [optional] 
**notification_setting** | **str** |  | [optional] 
**permission** | **str** |  | [optional] 
**members_url** | **str** |  | [optional] 
**repositories_url** | **str** |  | [optional] 
**parent** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.branch_restriction_policy_teams_inner import BranchRestrictionPolicyTeamsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BranchRestrictionPolicyTeamsInner from a JSON string
branch_restriction_policy_teams_inner_instance = BranchRestrictionPolicyTeamsInner.from_json(json)
# print the JSON string representation of the object
print(BranchRestrictionPolicyTeamsInner.to_json())

# convert the object into a dict
branch_restriction_policy_teams_inner_dict = branch_restriction_policy_teams_inner_instance.to_dict()
# create an instance of BranchRestrictionPolicyTeamsInner from a dict
branch_restriction_policy_teams_inner_from_dict = BranchRestrictionPolicyTeamsInner.from_dict(branch_restriction_policy_teams_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


