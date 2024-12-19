# RepositoryRulesetConditionsRepositoryPropertyTargetRepositoryProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | [**List[RepositoryRulesetConditionsRepositoryPropertySpec]**](RepositoryRulesetConditionsRepositoryPropertySpec.md) | The repository properties and values to include. All of these properties must match for the condition to pass. | [optional] 
**exclude** | [**List[RepositoryRulesetConditionsRepositoryPropertySpec]**](RepositoryRulesetConditionsRepositoryPropertySpec.md) | The repository properties and values to exclude. The condition will not pass if any of these properties match. | [optional] 

## Example

```python
from github_openapi.models.repository_ruleset_conditions_repository_property_target_repository_property import RepositoryRulesetConditionsRepositoryPropertyTargetRepositoryProperty

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRulesetConditionsRepositoryPropertyTargetRepositoryProperty from a JSON string
repository_ruleset_conditions_repository_property_target_repository_property_instance = RepositoryRulesetConditionsRepositoryPropertyTargetRepositoryProperty.from_json(json)
# print the JSON string representation of the object
print(RepositoryRulesetConditionsRepositoryPropertyTargetRepositoryProperty.to_json())

# convert the object into a dict
repository_ruleset_conditions_repository_property_target_repository_property_dict = repository_ruleset_conditions_repository_property_target_repository_property_instance.to_dict()
# create an instance of RepositoryRulesetConditionsRepositoryPropertyTargetRepositoryProperty from a dict
repository_ruleset_conditions_repository_property_target_repository_property_from_dict = RepositoryRulesetConditionsRepositoryPropertyTargetRepositoryProperty.from_dict(repository_ruleset_conditions_repository_property_target_repository_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


