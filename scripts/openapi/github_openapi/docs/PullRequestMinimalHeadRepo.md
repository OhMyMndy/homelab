# PullRequestMinimalHeadRepo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**url** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from github_openapi.models.pull_request_minimal_head_repo import PullRequestMinimalHeadRepo

# TODO update the JSON string below
json = "{}"
# create an instance of PullRequestMinimalHeadRepo from a JSON string
pull_request_minimal_head_repo_instance = PullRequestMinimalHeadRepo.from_json(json)
# print the JSON string representation of the object
print(PullRequestMinimalHeadRepo.to_json())

# convert the object into a dict
pull_request_minimal_head_repo_dict = pull_request_minimal_head_repo_instance.to_dict()
# create an instance of PullRequestMinimalHeadRepo from a dict
pull_request_minimal_head_repo_from_dict = PullRequestMinimalHeadRepo.from_dict(pull_request_minimal_head_repo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


