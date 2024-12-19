# RuleSuitesInner


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
**evaluation_result** | **str** | The result of the rule evaluations for rules with the &#x60;active&#x60; and &#x60;evaluate&#x60; enforcement statuses, demonstrating whether rules would pass or fail if all rules in the rule suite were &#x60;active&#x60;. | [optional] 

## Example

```python
from github_openapi.models.rule_suites_inner import RuleSuitesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RuleSuitesInner from a JSON string
rule_suites_inner_instance = RuleSuitesInner.from_json(json)
# print the JSON string representation of the object
print(RuleSuitesInner.to_json())

# convert the object into a dict
rule_suites_inner_dict = rule_suites_inner_instance.to_dict()
# create an instance of RuleSuitesInner from a dict
rule_suites_inner_from_dict = RuleSuitesInner.from_dict(rule_suites_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


