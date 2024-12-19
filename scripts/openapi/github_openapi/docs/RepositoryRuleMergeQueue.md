# RepositoryRuleMergeQueue

Merges must be performed via a merge queue.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**parameters** | [**RepositoryRuleMergeQueueParameters**](RepositoryRuleMergeQueueParameters.md) |  | [optional] 

## Example

```python
from github_openapi.models.repository_rule_merge_queue import RepositoryRuleMergeQueue

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRuleMergeQueue from a JSON string
repository_rule_merge_queue_instance = RepositoryRuleMergeQueue.from_json(json)
# print the JSON string representation of the object
print(RepositoryRuleMergeQueue.to_json())

# convert the object into a dict
repository_rule_merge_queue_dict = repository_rule_merge_queue_instance.to_dict()
# create an instance of RepositoryRuleMergeQueue from a dict
repository_rule_merge_queue_from_dict = RepositoryRuleMergeQueue.from_dict(repository_rule_merge_queue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


