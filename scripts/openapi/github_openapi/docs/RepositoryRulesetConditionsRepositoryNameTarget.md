# RepositoryRulesetConditionsRepositoryNameTarget

Parameters for a repository name condition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_name** | [**RepositoryRulesetConditionsRepositoryNameTargetRepositoryName**](RepositoryRulesetConditionsRepositoryNameTargetRepositoryName.md) |  | 

## Example

```python
from github_openapi.models.repository_ruleset_conditions_repository_name_target import RepositoryRulesetConditionsRepositoryNameTarget

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRulesetConditionsRepositoryNameTarget from a JSON string
repository_ruleset_conditions_repository_name_target_instance = RepositoryRulesetConditionsRepositoryNameTarget.from_json(json)
# print the JSON string representation of the object
print(RepositoryRulesetConditionsRepositoryNameTarget.to_json())

# convert the object into a dict
repository_ruleset_conditions_repository_name_target_dict = repository_ruleset_conditions_repository_name_target_instance.to_dict()
# create an instance of RepositoryRulesetConditionsRepositoryNameTarget from a dict
repository_ruleset_conditions_repository_name_target_from_dict = RepositoryRulesetConditionsRepositoryNameTarget.from_dict(repository_ruleset_conditions_repository_name_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


