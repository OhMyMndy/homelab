# ReposUpdateRepoRulesetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the ruleset. | [optional] 
**target** | **str** | The target of the ruleset | [optional] 
**enforcement** | [**RepositoryRuleEnforcement**](RepositoryRuleEnforcement.md) |  | [optional] 
**bypass_actors** | [**List[RepositoryRulesetBypassActor]**](RepositoryRulesetBypassActor.md) | The actors that can bypass the rules in this ruleset | [optional] 
**conditions** | [**RepositoryRulesetConditions**](RepositoryRulesetConditions.md) |  | [optional] 
**rules** | [**List[RepositoryRule]**](RepositoryRule.md) | An array of rules within the ruleset. | [optional] 

## Example

```python
from github_openapi.models.repos_update_repo_ruleset_request import ReposUpdateRepoRulesetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposUpdateRepoRulesetRequest from a JSON string
repos_update_repo_ruleset_request_instance = ReposUpdateRepoRulesetRequest.from_json(json)
# print the JSON string representation of the object
print(ReposUpdateRepoRulesetRequest.to_json())

# convert the object into a dict
repos_update_repo_ruleset_request_dict = repos_update_repo_ruleset_request_instance.to_dict()
# create an instance of ReposUpdateRepoRulesetRequest from a dict
repos_update_repo_ruleset_request_from_dict = ReposUpdateRepoRulesetRequest.from_dict(repos_update_repo_ruleset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


