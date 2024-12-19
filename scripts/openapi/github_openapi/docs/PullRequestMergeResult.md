# PullRequestMergeResult

Pull Request Merge Result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sha** | **str** |  | 
**merged** | **bool** |  | 
**message** | **str** |  | 

## Example

```python
from github_openapi.models.pull_request_merge_result import PullRequestMergeResult

# TODO update the JSON string below
json = "{}"
# create an instance of PullRequestMergeResult from a JSON string
pull_request_merge_result_instance = PullRequestMergeResult.from_json(json)
# print the JSON string representation of the object
print(PullRequestMergeResult.to_json())

# convert the object into a dict
pull_request_merge_result_dict = pull_request_merge_result_instance.to_dict()
# create an instance of PullRequestMergeResult from a dict
pull_request_merge_result_from_dict = PullRequestMergeResult.from_dict(pull_request_merge_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


