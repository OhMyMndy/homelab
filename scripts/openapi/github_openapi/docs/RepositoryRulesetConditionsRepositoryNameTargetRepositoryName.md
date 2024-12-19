# RepositoryRulesetConditionsRepositoryNameTargetRepositoryName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** | Array of repository names or patterns to include. One of these patterns must match for the condition to pass. Also accepts &#x60;~ALL&#x60; to include all repositories. | [optional] 
**exclude** | **List[str]** | Array of repository names or patterns to exclude. The condition will not pass if any of these patterns match. | [optional] 
**protected** | **bool** | Whether renaming of target repositories is prevented. | [optional] 

## Example

```python
from github_openapi.models.repository_ruleset_conditions_repository_name_target_repository_name import RepositoryRulesetConditionsRepositoryNameTargetRepositoryName

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRulesetConditionsRepositoryNameTargetRepositoryName from a JSON string
repository_ruleset_conditions_repository_name_target_repository_name_instance = RepositoryRulesetConditionsRepositoryNameTargetRepositoryName.from_json(json)
# print the JSON string representation of the object
print(RepositoryRulesetConditionsRepositoryNameTargetRepositoryName.to_json())

# convert the object into a dict
repository_ruleset_conditions_repository_name_target_repository_name_dict = repository_ruleset_conditions_repository_name_target_repository_name_instance.to_dict()
# create an instance of RepositoryRulesetConditionsRepositoryNameTargetRepositoryName from a dict
repository_ruleset_conditions_repository_name_target_repository_name_from_dict = RepositoryRulesetConditionsRepositoryNameTargetRepositoryName.from_dict(repository_ruleset_conditions_repository_name_target_repository_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


