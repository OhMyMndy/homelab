# RepositoryRuleCreation

Only allow users with bypass permission to create matching refs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from github_openapi.models.repository_rule_creation import RepositoryRuleCreation

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleCreation from a JSON string
repository_rule_creation_instance = RepositoryRuleCreation.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleCreation.to_json())

# convert the object into a dict
repository_rule_creation_dict = repository_rule_creation_instance.to_dict()
# create an instance of RepositoryRuleCreation from a dict
repository_rule_creation_from_dict = RepositoryRuleCreation.from_dict(repository_rule_creation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


