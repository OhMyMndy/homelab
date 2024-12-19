# RepositoryRuleUpdateParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**update_allows_fetch_and_merge** | **bool** | Branch can pull changes from its upstream repository | 

## Example

```python
from github_openapi.models.repository_rule_update_parameters import RepositoryRuleUpdateParameters

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleUpdateParameters from a JSON string
repository_rule_update_parameters_instance = RepositoryRuleUpdateParameters.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleUpdateParameters.to_json())

# convert the object into a dict
repository_rule_update_parameters_dict = repository_rule_update_parameters_instance.to_dict()
# create an instance of RepositoryRuleUpdateParameters from a dict
repository_rule_update_parameters_from_dict = RepositoryRuleUpdateParameters.from_dict(repository_rule_update_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


