# PullsMergeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit_title** | **str** | Title for the automatic commit message. | [optional] 
**commit_message** | **str** | Extra detail to append to automatic commit message. | [optional] 
**sha** | **str** | SHA that pull request head must match to allow merge. | [optional] 
**merge_method** | **str** | The merge method to use. | [optional] 

## Example

```python
from github_openapi.models.pulls_merge_request import PullsMergeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PullsMergeRequest from a JSON string
pulls_merge_request_instance = PullsMergeRequest.from_json(json)
# print the JSON string representation of the object
print(PullsMergeRequest.to_json())

# convert the object into a dict
pulls_merge_request_dict = pulls_merge_request_instance.to_dict()
# create an instance of PullsMergeRequest from a dict
pulls_merge_request_from_dict = PullsMergeRequest.from_dict(pulls_merge_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


