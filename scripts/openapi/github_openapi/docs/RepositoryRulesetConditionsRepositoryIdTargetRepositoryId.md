# RepositoryRulesetConditionsRepositoryIdTargetRepositoryId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_ids** | **List[int]** | The repository IDs that the ruleset applies to. One of these IDs must match for the condition to pass. | [optional] 

## Example

```python
from github_openapi.models.repository_ruleset_conditions_repository_id_target_repository_id import RepositoryRulesetConditionsRepositoryIdTargetRepositoryId

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRulesetConditionsRepositoryIdTargetRepositoryId from a JSON string
repository_ruleset_conditions_repository_id_target_repository_id_instance = RepositoryRulesetConditionsRepositoryIdTargetRepositoryId.from_json(json)
# print the JSON string representation of the object
print(RepositoryRulesetConditionsRepositoryIdTargetRepositoryId.to_json())

# convert the object into a dict
repository_ruleset_conditions_repository_id_target_repository_id_dict = repository_ruleset_conditions_repository_id_target_repository_id_instance.to_dict()
# create an instance of RepositoryRulesetConditionsRepositoryIdTargetRepositoryId from a dict
repository_ruleset_conditions_repository_id_target_repository_id_from_dict = RepositoryRulesetConditionsRepositoryIdTargetRepositoryId.from_dict(repository_ruleset_conditions_repository_id_target_repository_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


