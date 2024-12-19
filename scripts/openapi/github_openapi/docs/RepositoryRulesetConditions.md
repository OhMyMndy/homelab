# RepositoryRulesetConditions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref_name** | [**RepositoryRulesetConditionsRefName**](RepositoryRulesetConditionsRefName.md) |  | [optional] 
**repository_name** | [**RepositoryRulesetConditionsRepositoryNameTargetRepositoryName**](RepositoryRulesetConditionsRepositoryNameTargetRepositoryName.md) |  | 
**repository_id** | [**RepositoryRulesetConditionsRepositoryIdTargetRepositoryId**](RepositoryRulesetConditionsRepositoryIdTargetRepositoryId.md) |  | 
**repository_property** | [**RepositoryRulesetConditionsRepositoryPropertyTargetRepositoryProperty**](RepositoryRulesetConditionsRepositoryPropertyTargetRepositoryProperty.md) |  | 

## Example

```python
from github_openapi.models.repository_ruleset_conditions import RepositoryRulesetConditions

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRulesetConditions from a JSON string
repository_ruleset_conditions_instance = RepositoryRulesetConditions.from_json(json)
# print the JSON string representation of the object
print(RepositoryRulesetConditions.to_json())

# convert the object into a dict
repository_ruleset_conditions_dict = repository_ruleset_conditions_instance.to_dict()
# create an instance of RepositoryRulesetConditions from a dict
repository_ruleset_conditions_from_dict = RepositoryRulesetConditions.from_dict(repository_ruleset_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


