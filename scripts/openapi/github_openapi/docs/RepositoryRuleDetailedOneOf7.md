# RepositoryRuleDetailedOneOf7


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**parameters** | [**RepositoryRulePullRequestParameters**](RepositoryRulePullRequestParameters.md) |  | [optional] 
**ruleset_source_type** | **str** | The type of source for the ruleset that includes this rule. | [optional] 
**ruleset_source** | **str** | The name of the source of the ruleset that includes this rule. | [optional] 
**ruleset_id** | **int** | The ID of the ruleset that includes this rule. | [optional] 

## Example

```python
from github_openapi.models.repository_rule_detailed_one_of7 import RepositoryRuleDetailedOneOf7

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleDetailedOneOf7 from a JSON string
repository_rule_detailed_one_of7_instance = RepositoryRuleDetailedOneOf7.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleDetailedOneOf7.to_json())

# convert the object into a dict
repository_rule_detailed_one_of7_dict = repository_rule_detailed_one_of7_instance.to_dict()
# create an instance of RepositoryRuleDetailedOneOf7 from a dict
repository_rule_detailed_one_of7_from_dict = RepositoryRuleDetailedOneOf7.from_dict(repository_rule_detailed_one_of7_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


