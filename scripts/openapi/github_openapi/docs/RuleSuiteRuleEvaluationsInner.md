# RuleSuiteRuleEvaluationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_source** | [**RuleSuiteRuleEvaluationsInnerRuleSource**](RuleSuiteRuleEvaluationsInnerRuleSource.md) |  | [optional] 
**enforcement** | **str** | The enforcement level of this rule source. | [optional] 
**result** | **str** | The result of the evaluation of the individual rule. | [optional] 
**rule_type** | **str** | The type of rule. | [optional] 
**details** | **str** | The detailed failure message for the rule. Null if the rule passed. | [optional] 

## Example

```python
from github_openapi.models.rule_suite_rule_evaluations_inner import RuleSuiteRuleEvaluationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RuleSuiteRuleEvaluationsInner from a JSON string
rule_suite_rule_evaluations_inner_instance = RuleSuiteRuleEvaluationsInner.from_json(json)
# print the JSON string representation of the object
print(RuleSuiteRuleEvaluationsInner.to_json())

# convert the object into a dict
rule_suite_rule_evaluations_inner_dict = rule_suite_rule_evaluations_inner_instance.to_dict()
# create an instance of RuleSuiteRuleEvaluationsInner from a dict
rule_suite_rule_evaluations_inner_from_dict = RuleSuiteRuleEvaluationsInner.from_dict(rule_suite_rule_evaluations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


