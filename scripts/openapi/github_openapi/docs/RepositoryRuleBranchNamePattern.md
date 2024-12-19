# RepositoryRuleBranchNamePattern

Parameters to be used for the branch_name_pattern rule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**parameters** | [**RepositoryRuleCommitMessagePatternParameters**](RepositoryRuleCommitMessagePatternParameters.md) |  | [optional] 

## Example

```python
from github_openapi.models.repository_rule_branch_name_pattern import RepositoryRuleBranchNamePattern

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleBranchNamePattern from a JSON string
repository_rule_branch_name_pattern_instance = RepositoryRuleBranchNamePattern.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleBranchNamePattern.to_json())

# convert the object into a dict
repository_rule_branch_name_pattern_dict = repository_rule_branch_name_pattern_instance.to_dict()
# create an instance of RepositoryRuleBranchNamePattern from a dict
repository_rule_branch_name_pattern_from_dict = RepositoryRuleBranchNamePattern.from_dict(repository_rule_branch_name_pattern_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


