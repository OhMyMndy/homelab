# RepositoryRulePullRequestParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_merge_methods** | **List[str]** | When merging pull requests, you can allow any combination of merge commits, squashing, or rebasing. At least one option must be enabled. | [optional] 
**dismiss_stale_reviews_on_push** | **bool** | New, reviewable commits pushed will dismiss previous pull request review approvals. | 
**require_code_owner_review** | **bool** | Require an approving review in pull requests that modify files that have a designated code owner. | 
**require_last_push_approval** | **bool** | Whether the most recent reviewable push must be approved by someone other than the person who pushed it. | 
**required_approving_review_count** | **int** | The number of approving reviews that are required before a pull request can be merged. | 
**required_review_thread_resolution** | **bool** | All conversations on code must be resolved before a pull request can be merged. | 

## Example

```python
from github_openapi.models.repository_rule_pull_request_parameters import RepositoryRulePullRequestParameters

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRulePullRequestParameters from a JSON string
repository_rule_pull_request_parameters_instance = RepositoryRulePullRequestParameters.from_json(json)
# print the JSON string representation of the object
print(RepositoryRulePullRequestParameters.to_json())

# convert the object into a dict
repository_rule_pull_request_parameters_dict = repository_rule_pull_request_parameters_instance.to_dict()
# create an instance of RepositoryRulePullRequestParameters from a dict
repository_rule_pull_request_parameters_from_dict = RepositoryRulePullRequestParameters.from_dict(repository_rule_pull_request_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


