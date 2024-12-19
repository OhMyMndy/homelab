# PullRequestHead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**ref** | **str** |  | 
**repo** | [**Repository4**](Repository4.md) |  | 
**sha** | **str** |  | 
**user** | [**User1**](User1.md) |  | 

## Example

```python
from github_openapi.models.pull_request_head import PullRequestHead

# TODO update the JSON string below
json = "{}"
# create an instance of PullRequestHead from a JSON string
pull_request_head_instance = PullRequestHead.from_json(json)
# print the JSON string representation of the object
print(PullRequestHead.to_json())

# convert the object into a dict
pull_request_head_dict = pull_request_head_instance.to_dict()
# create an instance of PullRequestHead from a dict
pull_request_head_from_dict = PullRequestHead.from_dict(pull_request_head_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


