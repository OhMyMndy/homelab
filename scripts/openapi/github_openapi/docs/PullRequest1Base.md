# PullRequest1Base


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**ref** | **str** |  | 
**repo** | [**Repository5**](Repository5.md) |  | 
**sha** | **str** |  | 
**user** | [**User1**](User1.md) |  | 

## Example

```python
from github_openapi.models.pull_request1_base import PullRequest1Base

# TODO update the JSON string below
json = "{}"
# create an instance of PullRequest1Base from a JSON string
pull_request1_base_instance = PullRequest1Base.from_json(json)
# print the JSON string representation of the object
print(PullRequest1Base.to_json())

# convert the object into a dict
pull_request1_base_dict = pull_request1_base_instance.to_dict()
# create an instance of PullRequest1Base from a dict
pull_request1_base_from_dict = PullRequest1Base.from_dict(pull_request1_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


