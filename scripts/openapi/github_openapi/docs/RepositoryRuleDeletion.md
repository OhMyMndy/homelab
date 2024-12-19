# RepositoryRuleDeletion

Only allow users with bypass permissions to delete matching refs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from github_openapi.models.repository_rule_deletion import RepositoryRuleDeletion

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleDeletion from a JSON string
repository_rule_deletion_instance = RepositoryRuleDeletion.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleDeletion.to_json())

# convert the object into a dict
repository_rule_deletion_dict = repository_rule_deletion_instance.to_dict()
# create an instance of RepositoryRuleDeletion from a dict
repository_rule_deletion_from_dict = RepositoryRuleDeletion.from_dict(repository_rule_deletion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


