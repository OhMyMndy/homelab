# PullRequest11Base


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
from github_openapi.models.pull_request11_base import PullRequest11Base

# TODO update the JSON string below
json = "{}"
# create an instance of PullRequest11Base from a JSON string
pull_request11_base_instance = PullRequest11Base.from_json(json)
# print the JSON string representation of the object
print(PullRequest11Base.to_json())

# convert the object into a dict
pull_request11_base_dict = pull_request11_base_instance.to_dict()
# create an instance of PullRequest11Base from a dict
pull_request11_base_from_dict = PullRequest11Base.from_dict(pull_request11_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


