# RepositoryRule

A repository rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**parameters** | [**RepositoryRuleCodeScanningParameters**](RepositoryRuleCodeScanningParameters.md) |  | [optional] 

## Example

```python
from github_openapi.models.repository_rule import RepositoryRule

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRule from a JSON string
repository_rule_instance = RepositoryRule.from_json(json)
# print the JSON string representation of the object
print(RepositoryRule.to_json())

# convert the object into a dict
repository_rule_dict = repository_rule_instance.to_dict()
# create an instance of RepositoryRule from a dict
repository_rule_from_dict = RepositoryRule.from_dict(repository_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


