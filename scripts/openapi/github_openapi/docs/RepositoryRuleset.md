# RepositoryRuleset

A set of rules to apply when specified conditions are met.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the ruleset | 
**name** | **str** | The name of the ruleset | 
**target** | **str** | The target of the ruleset | [optional] 
**source_type** | **str** | The type of the source of the ruleset | [optional] 
**source** | **str** | The name of the source | 
**enforcement** | [**RepositoryRuleEnforcement**](RepositoryRuleEnforcement.md) |  | 
**bypass_actors** | [**List[RepositoryRulesetBypassActor]**](RepositoryRulesetBypassActor.md) | The actors that can bypass the rules in this ruleset | [optional] 
**current_user_can_bypass** | **str** | The bypass type of the user making the API request for this ruleset. This field is only returned when querying the repository-level endpoint. | [optional] 
**node_id** | **str** |  | [optional] 
**links** | [**RepositoryRulesetLinks**](RepositoryRulesetLinks.md) |  | [optional] 
**conditions** | [**RepositoryRulesetConditions**](RepositoryRulesetConditions.md) |  | [optional] 
**rules** | [**List[RepositoryRule]**](RepositoryRule.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from github_openapi.models.repository_ruleset import RepositoryRuleset

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleset from a JSON string
repository_ruleset_instance = RepositoryRuleset.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleset.to_json())

# convert the object into a dict
repository_ruleset_dict = repository_ruleset_instance.to_dict()
# create an instance of RepositoryRuleset from a dict
repository_ruleset_from_dict = RepositoryRuleset.from_dict(repository_ruleset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


