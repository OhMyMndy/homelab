# RepositoryRuleCommitAuthorEmailPattern

Parameters to be used for the commit_author_email_pattern rule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**parameters** | [**RepositoryRuleCommitMessagePatternParameters**](RepositoryRuleCommitMessagePatternParameters.md) |  | [optional] 

## Example

```python
from github_openapi.models.repository_rule_commit_author_email_pattern import RepositoryRuleCommitAuthorEmailPattern

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleCommitAuthorEmailPattern from a JSON string
repository_rule_commit_author_email_pattern_instance = RepositoryRuleCommitAuthorEmailPattern.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleCommitAuthorEmailPattern.to_json())

# convert the object into a dict
repository_rule_commit_author_email_pattern_dict = repository_rule_commit_author_email_pattern_instance.to_dict()
# create an instance of RepositoryRuleCommitAuthorEmailPattern from a dict
repository_rule_commit_author_email_pattern_from_dict = RepositoryRuleCommitAuthorEmailPattern.from_dict(repository_rule_commit_author_email_pattern_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


