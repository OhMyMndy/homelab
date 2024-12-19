# PullRequestAutoMerge1

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
from github_openapi.models.pull_request_auto_merge1 import PullRequestAutoMerge1

# TODO update the JSON string below
json = "{}"
# create an instance of PullRequestAutoMerge1 from a JSON string
pull_request_auto_merge1_instance = PullRequestAutoMerge1.from_json(json)
# print the JSON string representation of the object
print(PullRequestAutoMerge1.to_json())

# convert the object into a dict
pull_request_auto_merge1_dict = pull_request_auto_merge1_instance.to_dict()
# create an instance of PullRequestAutoMerge1 from a dict
pull_request_auto_merge1_from_dict = PullRequestAutoMerge1.from_dict(pull_request_auto_merge1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


