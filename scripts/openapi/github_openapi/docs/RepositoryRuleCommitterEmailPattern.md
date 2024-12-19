# RepositoryRuleCommitterEmailPattern

Parameters to be used for the committer_email_pattern rule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**parameters** | [**RepositoryRuleCommitMessagePatternParameters**](RepositoryRuleCommitMessagePatternParameters.md) |  | [optional] 

## Example

```python
from github_openapi.models.repository_rule_committer_email_pattern import RepositoryRuleCommitterEmailPattern

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleCommitterEmailPattern from a JSON string
repository_rule_committer_email_pattern_instance = RepositoryRuleCommitterEmailPattern.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleCommitterEmailPattern.to_json())

# convert the object into a dict
repository_rule_committer_email_pattern_dict = repository_rule_committer_email_pattern_instance.to_dict()
# create an instance of RepositoryRuleCommitterEmailPattern from a dict
repository_rule_committer_email_pattern_from_dict = RepositoryRuleCommitterEmailPattern.from_dict(repository_rule_committer_email_pattern_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


