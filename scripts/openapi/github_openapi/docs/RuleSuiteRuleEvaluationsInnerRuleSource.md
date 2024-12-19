# RuleSuiteRuleEvaluationsInnerRuleSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of rule source. | [optional] 
**id** | **int** | The ID of the rule source. | [optional] 
**name** | **str** | The name of the rule source. | [optional] 

## Example

```python
from github_openapi.models.rule_suite_rule_evaluations_inner_rule_source import RuleSuiteRuleEvaluationsInnerRuleSource

# TODO update the JSON string below
json = "{}"
# create an instance of RuleSuiteRuleEvaluationsInnerRuleSource from a JSON string
rule_suite_rule_evaluations_inner_rule_source_instance = RuleSuiteRuleEvaluationsInnerRuleSource.from_json(json)
# print the JSON string representation of the object
print(RuleSuiteRuleEvaluationsInnerRuleSource.to_json())

# convert the object into a dict
rule_suite_rule_evaluations_inner_rule_source_dict = rule_suite_rule_evaluations_inner_rule_source_instance.to_dict()
# create an instance of RuleSuiteRuleEvaluationsInnerRuleSource from a dict
rule_suite_rule_evaluations_inner_rule_source_from_dict = RuleSuiteRuleEvaluationsInnerRuleSource.from_dict(rule_suite_rule_evaluations_inner_rule_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


