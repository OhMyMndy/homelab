# RepositoryRuleParamsRestrictedCommits

Restricted commit

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oid** | **str** | Full or abbreviated commit hash to reject | 
**reason** | **str** | Reason for restriction | [optional] 

## Example

```python
from github_openapi.models.repository_rule_params_restricted_commits import RepositoryRuleParamsRestrictedCommits

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleParamsRestrictedCommits from a JSON string
repository_rule_params_restricted_commits_instance = RepositoryRuleParamsRestrictedCommits.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleParamsRestrictedCommits.to_json())

# convert the object into a dict
repository_rule_params_restricted_commits_dict = repository_rule_params_restricted_commits_instance.to_dict()
# create an instance of RepositoryRuleParamsRestrictedCommits from a dict
repository_rule_params_restricted_commits_from_dict = RepositoryRuleParamsRestrictedCommits.from_dict(repository_rule_params_restricted_commits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


