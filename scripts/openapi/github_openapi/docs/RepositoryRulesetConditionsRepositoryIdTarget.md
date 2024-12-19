# RepositoryRulesetConditionsRepositoryIdTarget

Parameters for a repository ID condition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_id** | [**RepositoryRulesetConditionsRepositoryIdTargetRepositoryId**](RepositoryRulesetConditionsRepositoryIdTargetRepositoryId.md) |  | 

## Example

```python
from github_openapi.models.repository_ruleset_conditions_repository_id_target import RepositoryRulesetConditionsRepositoryIdTarget

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRulesetConditionsRepositoryIdTarget from a JSON string
repository_ruleset_conditions_repository_id_target_instance = RepositoryRulesetConditionsRepositoryIdTarget.from_json(json)
# print the JSON string representation of the object
print(RepositoryRulesetConditionsRepositoryIdTarget.to_json())

# convert the object into a dict
repository_ruleset_conditions_repository_id_target_dict = repository_ruleset_conditions_repository_id_target_instance.to_dict()
# create an instance of RepositoryRulesetConditionsRepositoryIdTarget from a dict
repository_ruleset_conditions_repository_id_target_from_dict = RepositoryRulesetConditionsRepositoryIdTarget.from_dict(repository_ruleset_conditions_repository_id_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


