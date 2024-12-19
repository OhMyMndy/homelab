# RepositoryRuleTagNamePattern

Parameters to be used for the tag_name_pattern rule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**parameters** | [**RepositoryRuleCommitMessagePatternParameters**](RepositoryRuleCommitMessagePatternParameters.md) |  | [optional] 

## Example

```python
from github_openapi.models.repository_rule_tag_name_pattern import RepositoryRuleTagNamePattern

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleTagNamePattern from a JSON string
repository_rule_tag_name_pattern_instance = RepositoryRuleTagNamePattern.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleTagNamePattern.to_json())

# convert the object into a dict
repository_rule_tag_name_pattern_dict = repository_rule_tag_name_pattern_instance.to_dict()
# create an instance of RepositoryRuleTagNamePattern from a dict
repository_rule_tag_name_pattern_from_dict = RepositoryRuleTagNamePattern.from_dict(repository_rule_tag_name_pattern_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


