# ReposCreateRepoRulesetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the ruleset. | 
**target** | **str** | The target of the ruleset | [optional] [default to 'branch']
**enforcement** | [**RepositoryRuleEnforcement**](RepositoryRuleEnforcement.md) |  | 
**bypass_actors** | [**List[RepositoryRulesetBypassActor]**](RepositoryRulesetBypassActor.md) | The actors that can bypass the rules in this ruleset | [optional] 
**conditions** | [**RepositoryRulesetConditions**](RepositoryRulesetConditions.md) |  | [optional] 
**rules** | [**List[RepositoryRule]**](RepositoryRule.md) | An array of rules within the ruleset. | [optional] 

## Example

```python
from github_openapi.models.repos_create_repo_ruleset_request import ReposCreateRepoRulesetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposCreateRepoRulesetRequest from a JSON string
repos_create_repo_ruleset_request_instance = ReposCreateRepoRulesetRequest.from_json(json)
# print the JSON string representation of the object
print(ReposCreateRepoRulesetRequest.to_json())

# convert the object into a dict
repos_create_repo_ruleset_request_dict = repos_create_repo_ruleset_request_instance.to_dict()
# create an instance of ReposCreateRepoRulesetRequest from a dict
repos_create_repo_ruleset_request_from_dict = ReposCreateRepoRulesetRequest.from_dict(repos_create_repo_ruleset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


