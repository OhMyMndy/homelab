# RepositoryRuleRequiredStatusChecks

Choose which status checks must pass before the ref is updated. When enabled, commits must first be pushed to another ref where the checks pass.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**parameters** | [**RepositoryRuleRequiredStatusChecksParameters**](RepositoryRuleRequiredStatusChecksParameters.md) |  | [optional] 

## Example

```python
from github_openapi.models.repository_rule_required_status_checks import RepositoryRuleRequiredStatusChecks

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleRequiredStatusChecks from a JSON string
repository_rule_required_status_checks_instance = RepositoryRuleRequiredStatusChecks.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleRequiredStatusChecks.to_json())

# convert the object into a dict
repository_rule_required_status_checks_dict = repository_rule_required_status_checks_instance.to_dict()
# create an instance of RepositoryRuleRequiredStatusChecks from a dict
repository_rule_required_status_checks_from_dict = RepositoryRuleRequiredStatusChecks.from_dict(repository_rule_required_status_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


