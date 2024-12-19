# RepositoryRuleRequiredSignatures

Commits pushed to matching refs must have verified signatures.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from github_openapi.models.repository_rule_required_signatures import RepositoryRuleRequiredSignatures

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleRequiredSignatures from a JSON string
repository_rule_required_signatures_instance = RepositoryRuleRequiredSignatures.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleRequiredSignatures.to_json())

# convert the object into a dict
repository_rule_required_signatures_dict = repository_rule_required_signatures_instance.to_dict()
# create an instance of RepositoryRuleRequiredSignatures from a dict
repository_rule_required_signatures_from_dict = RepositoryRuleRequiredSignatures.from_dict(repository_rule_required_signatures_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


