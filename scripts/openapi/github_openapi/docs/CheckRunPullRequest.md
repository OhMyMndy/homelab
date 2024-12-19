# CheckRunPullRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base** | [**CheckRunPullRequestBase**](CheckRunPullRequestBase.md) |  | 
**head** | [**CheckRunPullRequestBase**](CheckRunPullRequestBase.md) |  | 
**id** | **int** |  | 
**number** | **int** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.check_run_pull_request import CheckRunPullRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CheckRunPullRequest from a JSON string
check_run_pull_request_instance = CheckRunPullRequest.from_json(json)
# print the JSON string representation of the object
print(CheckRunPullRequest.to_json())

# convert the object into a dict
check_run_pull_request_dict = check_run_pull_request_instance.to_dict()
# create an instance of CheckRunPullRequest from a dict
check_run_pull_request_from_dict = CheckRunPullRequest.from_dict(check_run_pull_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


