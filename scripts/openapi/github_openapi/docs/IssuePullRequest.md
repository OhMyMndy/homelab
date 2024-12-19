# IssuePullRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merged_at** | **datetime** |  | [optional] 
**diff_url** | **str** |  | 
**html_url** | **str** |  | 
**patch_url** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.issue_pull_request import IssuePullRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IssuePullRequest from a JSON string
issue_pull_request_instance = IssuePullRequest.from_json(json)
# print the JSON string representation of the object
print(IssuePullRequest.to_json())

# convert the object into a dict
issue_pull_request_dict = issue_pull_request_instance.to_dict()
# create an instance of IssuePullRequest from a dict
issue_pull_request_from_dict = IssuePullRequest.from_dict(issue_pull_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


