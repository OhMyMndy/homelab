# ReposUpdateOrgRulesetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the ruleset. | [optional] 
**target** | **str** | The target of the ruleset | [optional] 
**enforcement** | [**RepositoryRuleEnforcement**](RepositoryRuleEnforcement.md) |  | [optional] 
**bypass_actors** | [**List[RepositoryRulesetBypassActor]**](RepositoryRulesetBypassActor.md) | The actors that can bypass the rules in this ruleset | [optional] 
**conditions** | [**OrgRulesetConditions**](OrgRulesetConditions.md) |  | [optional] 
**rules** | [**List[RepositoryRule]**](RepositoryRule.md) | An array of rules within the ruleset. | [optional] 

## Example

```python
from github_openapi.models.repos_update_org_ruleset_request import ReposUpdateOrgRulesetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposUpdateOrgRulesetRequest from a JSON string
repos_update_org_ruleset_request_instance = ReposUpdateOrgRulesetRequest.from_json(json)
# print the JSON string representation of the object
print(ReposUpdateOrgRulesetRequest.to_json())

# convert the object into a dict
repos_update_org_ruleset_request_dict = repos_update_org_ruleset_request_instance.to_dict()
# create an instance of ReposUpdateOrgRulesetRequest from a dict
repos_update_org_ruleset_request_from_dict = ReposUpdateOrgRulesetRequest.from_dict(repos_update_org_ruleset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


