# RuleSuite

Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the rule insight. | [optional] 
**actor_id** | **int** | The number that identifies the user. | [optional] 
**actor_name** | **str** | The handle for the GitHub user account. | [optional] 
**before_sha** | **str** | The first commit sha before the push evaluation. | [optional] 
**after_sha** | **str** | The last commit sha in the push evaluation. | [optional] 
**ref** | **str** | The ref name that the evaluation ran on. | [optional] 
**repository_id** | **int** | The ID of the repository associated with the rule evaluation. | [optional] 
**repository_name** | **str** | The name of the repository without the &#x60;.git&#x60; extension. | [optional] 
**pushed_at** | **datetime** |  | [optional] 
**result** | **str** | The result of the rule evaluations for rules with the &#x60;active&#x60; enforcement status. | [optional] 
**evaluation_result** | **str** | The result of the rule evaluations for rules with the &#x60;active&#x60; and &#x60;evaluate&#x60; enforcement statuses, demonstrating whether rules would pass or fail if all rules in the rule suite were &#x60;active&#x60;. Null if no rules with &#x60;evaluate&#x60; enforcement status were run. | [optional] 
**rule_evaluations** | [**List[RuleSuiteRuleEvaluationsInner]**](RuleSuiteRuleEvaluationsInner.md) | Details on the evaluated rules. | [optional] 

## Example

```python
from github_openapi.models.rule_suite import RuleSuite

# TODO update the JSON string below
json = "{}"
# create an instance of RuleSuite from a JSON string
rule_suite_instance = RuleSuite.from_json(json)
# print the JSON string representation of the object
print(RuleSuite.to_json())

# convert the object into a dict
rule_suite_dict = rule_suite_instance.to_dict()
# create an instance of RuleSuite from a dict
rule_suite_from_dict = RuleSuite.from_dict(rule_suite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


