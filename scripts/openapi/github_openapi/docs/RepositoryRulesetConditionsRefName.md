# RepositoryRulesetConditionsRefName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** | Array of ref names or patterns to include. One of these patterns must match for the condition to pass. Also accepts &#x60;~DEFAULT_BRANCH&#x60; to include the default branch or &#x60;~ALL&#x60; to include all branches. | [optional] 
**exclude** | **List[str]** | Array of ref names or patterns to exclude. The condition will not pass if any of these patterns match. | [optional] 

## Example

```python
from github_openapi.models.repository_ruleset_conditions_ref_name import RepositoryRulesetConditionsRefName

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRulesetConditionsRefName from a JSON string
repository_ruleset_conditions_ref_name_instance = RepositoryRulesetConditionsRefName.from_json(json)
# print the JSON string representation of the object
print(RepositoryRulesetConditionsRefName.to_json())

# convert the object into a dict
repository_ruleset_conditions_ref_name_dict = repository_ruleset_conditions_ref_name_instance.to_dict()
# create an instance of RepositoryRulesetConditionsRefName from a dict
repository_ruleset_conditions_ref_name_from_dict = RepositoryRulesetConditionsRefName.from_dict(repository_ruleset_conditions_ref_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


