# RepositoryRuleNonFastForward

Prevent users with push access from force pushing to refs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from github_openapi.models.repository_rule_non_fast_forward import RepositoryRuleNonFastForward

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleNonFastForward from a JSON string
repository_rule_non_fast_forward_instance = RepositoryRuleNonFastForward.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleNonFastForward.to_json())

# convert the object into a dict
repository_rule_non_fast_forward_dict = repository_rule_non_fast_forward_instance.to_dict()
# create an instance of RepositoryRuleNonFastForward from a dict
repository_rule_non_fast_forward_from_dict = RepositoryRuleNonFastForward.from_dict(repository_rule_non_fast_forward_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


