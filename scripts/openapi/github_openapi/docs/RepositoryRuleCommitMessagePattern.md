# RepositoryRuleCommitMessagePattern

Parameters to be used for the commit_message_pattern rule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**parameters** | [**RepositoryRuleCommitMessagePatternParameters**](RepositoryRuleCommitMessagePatternParameters.md) |  | [optional] 

## Example

```python
from github_openapi.models.repository_rule_commit_message_pattern import RepositoryRuleCommitMessagePattern

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleCommitMessagePattern from a JSON string
repository_rule_commit_message_pattern_instance = RepositoryRuleCommitMessagePattern.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleCommitMessagePattern.to_json())

# convert the object into a dict
repository_rule_commit_message_pattern_dict = repository_rule_commit_message_pattern_instance.to_dict()
# create an instance of RepositoryRuleCommitMessagePattern from a dict
repository_rule_commit_message_pattern_from_dict = RepositoryRuleCommitMessagePattern.from_dict(repository_rule_commit_message_pattern_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


