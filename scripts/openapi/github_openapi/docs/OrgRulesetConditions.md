# OrgRulesetConditions

Conditions for an organization ruleset. The branch and tag rulesets conditions object should contain both `repository_name` and `ref_name` properties, or both `repository_id` and `ref_name` properties, or both `repository_property` and `ref_name` properties. The push rulesets conditions object does not require the `ref_name` property. For repository policy rulesets, the conditions object should only contain the `repository_name`, the `repository_id`, or the `repository_property`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref_name** | [**RepositoryRulesetConditionsRefName**](RepositoryRulesetConditionsRefName.md) |  | [optional] 
**repository_name** | [**RepositoryRulesetConditionsRepositoryNameTargetRepositoryName**](RepositoryRulesetConditionsRepositoryNameTargetRepositoryName.md) |  | 
**repository_id** | [**RepositoryRulesetConditionsRepositoryIdTargetRepositoryId**](RepositoryRulesetConditionsRepositoryIdTargetRepositoryId.md) |  | 
**repository_property** | [**RepositoryRulesetConditionsRepositoryPropertyTargetRepositoryProperty**](RepositoryRulesetConditionsRepositoryPropertyTargetRepositoryProperty.md) |  | 

## Example

```python
from github_openapi.models.org_ruleset_conditions import OrgRulesetConditions

# TODO update the JSON string below
json = "{}"
# create an instance of OrgRulesetConditions from a JSON string
org_ruleset_conditions_instance = OrgRulesetConditions.from_json(json)
# print the JSON string representation of the object
print(OrgRulesetConditions.to_json())

# convert the object into a dict
org_ruleset_conditions_dict = org_ruleset_conditions_instance.to_dict()
# create an instance of OrgRulesetConditions from a dict
org_ruleset_conditions_from_dict = OrgRulesetConditions.from_dict(org_ruleset_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


