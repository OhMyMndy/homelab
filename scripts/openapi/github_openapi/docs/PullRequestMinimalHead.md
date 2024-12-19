# PullRequestMinimalHead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | **str** |  | 
**sha** | **str** |  | 
**repo** | [**PullRequestMinimalHeadRepo**](PullRequestMinimalHeadRepo.md) |  | 

## Example

```python
from github_openapi.models.pull_request_minimal_head import PullRequestMinimalHead

# TODO update the JSON string below
json = "{}"
# create an instance of PullRequestMinimalHead from a JSON string
pull_request_minimal_head_instance = PullRequestMinimalHead.from_json(json)
# print the JSON string representation of the object
print(PullRequestMinimalHead.to_json())

# convert the object into a dict
pull_request_minimal_head_dict = pull_request_minimal_head_instance.to_dict()
# create an instance of PullRequestMinimalHead from a dict
pull_request_minimal_head_from_dict = PullRequestMinimalHead.from_dict(pull_request_minimal_head_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


