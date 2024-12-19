# RepositoryRuleDetailedOneOf9


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**ruleset_source_type** | **str** | The type of source for the ruleset that includes this rule. | [optional] 
**ruleset_source** | **str** | The name of the source of the ruleset that includes this rule. | [optional] 
**ruleset_id** | **int** | The ID of the ruleset that includes this rule. | [optional] 

## Example

```python
from github_openapi.models.repository_rule_detailed_one_of9 import RepositoryRuleDetailedOneOf9

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleDetailedOneOf9 from a JSON string
repository_rule_detailed_one_of9_instance = RepositoryRuleDetailedOneOf9.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleDetailedOneOf9.to_json())

# convert the object into a dict
repository_rule_detailed_one_of9_dict = repository_rule_detailed_one_of9_instance.to_dict()
# create an instance of RepositoryRuleDetailedOneOf9 from a dict
repository_rule_detailed_one_of9_from_dict = RepositoryRuleDetailedOneOf9.from_dict(repository_rule_detailed_one_of9_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


