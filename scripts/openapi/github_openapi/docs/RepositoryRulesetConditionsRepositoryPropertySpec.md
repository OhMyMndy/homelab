# RepositoryRulesetConditionsRepositoryPropertySpec

Parameters for a targeting a repository property

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the repository property to target | 
**property_values** | **List[str]** | The values to match for the repository property | 
**source** | **str** | The source of the repository property. Defaults to &#39;custom&#39; if not specified. | [optional] 

## Example

```python
from github_openapi.models.repository_ruleset_conditions_repository_property_spec import RepositoryRulesetConditionsRepositoryPropertySpec

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRulesetConditionsRepositoryPropertySpec from a JSON string
repository_ruleset_conditions_repository_property_spec_instance = RepositoryRulesetConditionsRepositoryPropertySpec.from_json(json)
# print the JSON string representation of the object
print(RepositoryRulesetConditionsRepositoryPropertySpec.to_json())

# convert the object into a dict
repository_ruleset_conditions_repository_property_spec_dict = repository_ruleset_conditions_repository_property_spec_instance.to_dict()
# create an instance of RepositoryRulesetConditionsRepositoryPropertySpec from a dict
repository_ruleset_conditions_repository_property_spec_from_dict = RepositoryRulesetConditionsRepositoryPropertySpec.from_dict(repository_ruleset_conditions_repository_property_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


