# RepositoryRuleCommitMessagePatternParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | How this rule will appear to users. | [optional] 
**negate** | **bool** | If true, the rule will fail if the pattern matches. | [optional] 
**operator** | **str** | The operator to use for matching. | 
**pattern** | **str** | The pattern to match with. | 

## Example

```python
from github_openapi.models.repository_rule_commit_message_pattern_parameters import RepositoryRuleCommitMessagePatternParameters

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleCommitMessagePatternParameters from a JSON string
repository_rule_commit_message_pattern_parameters_instance = RepositoryRuleCommitMessagePatternParameters.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleCommitMessagePatternParameters.to_json())

# convert the object into a dict
repository_rule_commit_message_pattern_parameters_dict = repository_rule_commit_message_pattern_parameters_instance.to_dict()
# create an instance of RepositoryRuleCommitMessagePatternParameters from a dict
repository_rule_commit_message_pattern_parameters_from_dict = RepositoryRuleCommitMessagePatternParameters.from_dict(repository_rule_commit_message_pattern_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


