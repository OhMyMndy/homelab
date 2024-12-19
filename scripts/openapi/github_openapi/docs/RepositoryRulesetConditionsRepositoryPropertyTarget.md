# RepositoryRulesetConditionsRepositoryPropertyTarget

Parameters for a repository property condition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_property** | [**RepositoryRulesetConditionsRepositoryPropertyTargetRepositoryProperty**](RepositoryRulesetConditionsRepositoryPropertyTargetRepositoryProperty.md) |  | 

## Example

```python
from github_openapi.models.repository_ruleset_conditions_repository_property_target import RepositoryRulesetConditionsRepositoryPropertyTarget

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRulesetConditionsRepositoryPropertyTarget from a JSON string
repository_ruleset_conditions_repository_property_target_instance = RepositoryRulesetConditionsRepositoryPropertyTarget.from_json(json)
# print the JSON string representation of the object
print(RepositoryRulesetConditionsRepositoryPropertyTarget.to_json())

# convert the object into a dict
repository_ruleset_conditions_repository_property_target_dict = repository_ruleset_conditions_repository_property_target_instance.to_dict()
# create an instance of RepositoryRulesetConditionsRepositoryPropertyTarget from a dict
repository_ruleset_conditions_repository_property_target_from_dict = RepositoryRulesetConditionsRepositoryPropertyTarget.from_dict(repository_ruleset_conditions_repository_property_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


