# RepositoryRuleMergeQueueParameters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_response_timeout_minutes** | **int** | Maximum time for a required status check to report a conclusion. After this much time has elapsed, checks that have not reported a conclusion will be assumed to have failed | 
**grouping_strategy** | **str** | When set to ALLGREEN, the merge commit created by merge queue for each PR in the group must pass all required checks to merge. When set to HEADGREEN, only the commit at the head of the merge group, i.e. the commit containing changes from all of the PRs in the group, must pass its required checks to merge. | 
**max_entries_to_build** | **int** | Limit the number of queued pull requests requesting checks and workflow runs at the same time. | 
**max_entries_to_merge** | **int** | The maximum number of PRs that will be merged together in a group. | 
**merge_method** | **str** | Method to use when merging changes from queued pull requests. | 
**min_entries_to_merge** | **int** | The minimum number of PRs that will be merged together in a group. | 
**min_entries_to_merge_wait_minutes** | **int** | The time merge queue should wait after the first PR is added to the queue for the minimum group size to be met. After this time has elapsed, the minimum group size will be ignored and a smaller group will be merged. | 

## Example

```python
from github_openapi.models.repository_rule_merge_queue_parameters import RepositoryRuleMergeQueueParameters

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleMergeQueueParameters from a JSON string
repository_rule_merge_queue_parameters_instance = RepositoryRuleMergeQueueParameters.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleMergeQueueParameters.to_json())

# convert the object into a dict
repository_rule_merge_queue_parameters_dict = repository_rule_merge_queue_parameters_instance.to_dict()
# create an instance of RepositoryRuleMergeQueueParameters from a dict
repository_rule_merge_queue_parameters_from_dict = RepositoryRuleMergeQueueParameters.from_dict(repository_rule_merge_queue_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


