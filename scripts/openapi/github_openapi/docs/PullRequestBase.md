# PullRequestBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**ref** | **str** |  | 
**repo** | [**Repository3**](Repository3.md) |  | 
**sha** | **str** |  | 
**user** | [**User1**](User1.md) |  | 

## Example

```python
from github_openapi.models.pull_request_base import PullRequestBase

# TODO update the JSON string below
json = "{}"
# create an instance of PullRequestBase from a JSON string
pull_request_base_instance = PullRequestBase.from_json(json)
# print the JSON string representation of the object
print(PullRequestBase.to_json())

# convert the object into a dict
pull_request_base_dict = pull_request_base_instance.to_dict()
# create an instance of PullRequestBase from a dict
pull_request_base_from_dict = PullRequestBase.from_dict(pull_request_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


