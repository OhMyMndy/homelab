# RepositoryRuleDetailed

A repository rule with ruleset details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**ruleset_source_type** | **str** | The type of source for the ruleset that includes this rule. | [optional] 
**ruleset_source** | **str** | The name of the source of the ruleset that includes this rule. | [optional] 
**ruleset_id** | **int** | The ID of the ruleset that includes this rule. | [optional] 
**parameters** | [**RepositoryRuleCodeScanningParameters**](RepositoryRuleCodeScanningParameters.md) |  | [optional] 

## Example

```python
from github_openapi.models.repository_rule_detailed import RepositoryRuleDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleDetailed from a JSON string
repository_rule_detailed_instance = RepositoryRuleDetailed.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleDetailed.to_json())

# convert the object into a dict
repository_rule_detailed_dict = repository_rule_detailed_instance.to_dict()
# create an instance of RepositoryRuleDetailed from a dict
repository_rule_detailed_from_dict = RepositoryRuleDetailed.from_dict(repository_rule_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


