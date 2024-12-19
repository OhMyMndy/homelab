# RepositoryRuleRequiredLinearHistory

Prevent merge commits from being pushed to matching refs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from github_openapi.models.repository_rule_required_linear_history import RepositoryRuleRequiredLinearHistory

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleRequiredLinearHistory from a JSON string
repository_rule_required_linear_history_instance = RepositoryRuleRequiredLinearHistory.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleRequiredLinearHistory.to_json())

# convert the object into a dict
repository_rule_required_linear_history_dict = repository_rule_required_linear_history_instance.to_dict()
# create an instance of RepositoryRuleRequiredLinearHistory from a dict
repository_rule_required_linear_history_from_dict = RepositoryRuleRequiredLinearHistory.from_dict(repository_rule_required_linear_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


