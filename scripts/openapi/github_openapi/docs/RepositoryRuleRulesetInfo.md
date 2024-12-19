# RepositoryRuleRulesetInfo

User-defined metadata to store domain-specific information limited to 8 keys with scalar values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ruleset_source_type** | **str** | The type of source for the ruleset that includes this rule. | [optional] 
**ruleset_source** | **str** | The name of the source of the ruleset that includes this rule. | [optional] 
**ruleset_id** | **int** | The ID of the ruleset that includes this rule. | [optional] 

## Example

```python
from github_openapi.models.repository_rule_ruleset_info import RepositoryRuleRulesetInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleRulesetInfo from a JSON string
repository_rule_ruleset_info_instance = RepositoryRuleRulesetInfo.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleRulesetInfo.to_json())

# convert the object into a dict
repository_rule_ruleset_info_dict = repository_rule_ruleset_info_instance.to_dict()
# create an instance of RepositoryRuleRulesetInfo from a dict
repository_rule_ruleset_info_from_dict = RepositoryRuleRulesetInfo.from_dict(repository_rule_ruleset_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


