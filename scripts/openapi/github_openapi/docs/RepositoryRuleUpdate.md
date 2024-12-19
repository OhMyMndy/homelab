# RepositoryRuleUpdate

Only allow users with bypass permission to update matching refs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**parameters** | [**RepositoryRuleUpdateParameters**](RepositoryRuleUpdateParameters.md) |  | [optional] 

## Example

```python
from github_openapi.models.repository_rule_update import RepositoryRuleUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleUpdate from a JSON string
repository_rule_update_instance = RepositoryRuleUpdate.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleUpdate.to_json())

# convert the object into a dict
repository_rule_update_dict = repository_rule_update_instance.to_dict()
# create an instance of RepositoryRuleUpdate from a dict
repository_rule_update_from_dict = RepositoryRuleUpdate.from_dict(repository_rule_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


