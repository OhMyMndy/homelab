# RepositoryRulePullRequest

Require all commits be made to a non-target branch and submitted via a pull request before they can be merged.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**parameters** | [**RepositoryRulePullRequestParameters**](RepositoryRulePullRequestParameters.md) |  | [optional] 

## Example

```python
from github_openapi.models.repository_rule_pull_request import RepositoryRulePullRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRulePullRequest from a JSON string
repository_rule_pull_request_instance = RepositoryRulePullRequest.from_json(json)
# print the JSON string representation of the object
print(RepositoryRulePullRequest.to_json())

# convert the object into a dict
repository_rule_pull_request_dict = repository_rule_pull_request_instance.to_dict()
# create an instance of RepositoryRulePullRequest from a dict
repository_rule_pull_request_from_dict = RepositoryRulePullRequest.from_dict(repository_rule_pull_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


