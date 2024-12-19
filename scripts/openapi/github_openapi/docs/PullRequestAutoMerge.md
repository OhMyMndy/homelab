# PullRequestAutoMerge

The status of auto merging a pull request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit_message** | **str** | Commit message for the merge commit. | 
**commit_title** | **str** | Title for the merge commit message. | 
**enabled_by** | [**User2**](User2.md) |  | 
**merge_method** | **str** | The merge method to use. | 

## Example

```python
from github_openapi.models.pull_request_auto_merge import PullRequestAutoMerge

# TODO update the JSON string below
json = "{}"
# create an instance of PullRequestAutoMerge from a JSON string
pull_request_auto_merge_instance = PullRequestAutoMerge.from_json(json)
# print the JSON string representation of the object
print(PullRequestAutoMerge.to_json())

# convert the object into a dict
pull_request_auto_merge_dict = pull_request_auto_merge_instance.to_dict()
# create an instance of PullRequestAutoMerge from a dict
pull_request_auto_merge_from_dict = PullRequestAutoMerge.from_dict(pull_request_auto_merge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


