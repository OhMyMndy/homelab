# CheckRunPullRequestBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | **str** |  | 
**repo** | [**RepoRef**](RepoRef.md) |  | 
**sha** | **str** |  | 

## Example

```python
from github_openapi.models.check_run_pull_request_base import CheckRunPullRequestBase

# TODO update the JSON string below
json = "{}"
# create an instance of CheckRunPullRequestBase from a JSON string
check_run_pull_request_base_instance = CheckRunPullRequestBase.from_json(json)
# print the JSON string representation of the object
print(CheckRunPullRequestBase.to_json())

# convert the object into a dict
check_run_pull_request_base_dict = check_run_pull_request_base_instance.to_dict()
# create an instance of CheckRunPullRequestBase from a dict
check_run_pull_request_base_from_dict = CheckRunPullRequestBase.from_dict(check_run_pull_request_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


