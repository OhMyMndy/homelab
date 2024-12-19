# PullsUpdateBranchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_head_sha** | **str** | The expected SHA of the pull request&#39;s HEAD ref. This is the most recent commit on the pull request&#39;s branch. If the expected SHA does not match the pull request&#39;s HEAD, you will receive a &#x60;422 Unprocessable Entity&#x60; status. You can use the \&quot;[List commits](https://docs.github.com/rest/commits/commits#list-commits)\&quot; endpoint to find the most recent commit SHA. Default: SHA of the pull request&#39;s current HEAD ref. | [optional] 

## Example

```python
from github_openapi.models.pulls_update_branch_request import PullsUpdateBranchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PullsUpdateBranchRequest from a JSON string
pulls_update_branch_request_instance = PullsUpdateBranchRequest.from_json(json)
# print the JSON string representation of the object
print(PullsUpdateBranchRequest.to_json())

# convert the object into a dict
pulls_update_branch_request_dict = pulls_update_branch_request_instance.to_dict()
# create an instance of PullsUpdateBranchRequest from a dict
pulls_update_branch_request_from_dict = PullsUpdateBranchRequest.from_dict(pulls_update_branch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


