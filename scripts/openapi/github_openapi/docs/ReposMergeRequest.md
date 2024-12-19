# ReposMergeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | **str** | The name of the base branch that the head will be merged into. | 
**head** | **str** | The head to merge. This can be a branch name or a commit SHA1. | 
**commit_message** | **str** | Commit message to use for the merge commit. If omitted, a default message will be used. | [optional] 

## Example

```python
from github_openapi.models.repos_merge_request import ReposMergeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposMergeRequest from a JSON string
repos_merge_request_instance = ReposMergeRequest.from_json(json)
# print the JSON string representation of the object
print(ReposMergeRequest.to_json())

# convert the object into a dict
repos_merge_request_dict = repos_merge_request_instance.to_dict()
# create an instance of ReposMergeRequest from a dict
repos_merge_request_from_dict = ReposMergeRequest.from_dict(repos_merge_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


