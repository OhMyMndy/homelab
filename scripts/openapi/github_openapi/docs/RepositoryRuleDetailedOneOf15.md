# RepositoryRuleDetailedOneOf15


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**parameters** | [**RepositoryRuleWorkflowsParameters**](RepositoryRuleWorkflowsParameters.md) |  | [optional] 
**ruleset_source_type** | **str** | The type of source for the ruleset that includes this rule. | [optional] 
**ruleset_source** | **str** | The name of the source of the ruleset that includes this rule. | [optional] 
**ruleset_id** | **int** | The ID of the ruleset that includes this rule. | [optional] 

## Example

```python
from github_openapi.models.repository_rule_detailed_one_of15 import RepositoryRuleDetailedOneOf15

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleDetailedOneOf15 from a JSON string
repository_rule_detailed_one_of15_instance = RepositoryRuleDetailedOneOf15.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleDetailedOneOf15.to_json())

# convert the object into a dict
repository_rule_detailed_one_of15_dict = repository_rule_detailed_one_of15_instance.to_dict()
# create an instance of RepositoryRuleDetailedOneOf15 from a dict
repository_rule_detailed_one_of15_from_dict = RepositoryRuleDetailedOneOf15.from_dict(repository_rule_detailed_one_of15_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


