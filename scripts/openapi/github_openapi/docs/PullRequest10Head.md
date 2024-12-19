# PullRequest10Head


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**ref** | **str** |  | 
**repo** | [**Repository13**](Repository13.md) |  | 
**sha** | **str** |  | 
**user** | [**User1**](User1.md) |  | 

## Example

```python
from github_openapi.models.pull_request10_head import PullRequest10Head

# TODO update the JSON string below
json = "{}"
# create an instance of PullRequest10Head from a JSON string
pull_request10_head_instance = PullRequest10Head.from_json(json)
# print the JSON string representation of the object
print(PullRequest10Head.to_json())

# convert the object into a dict
pull_request10_head_dict = pull_request10_head_instance.to_dict()
# create an instance of PullRequest10Head from a dict
pull_request10_head_from_dict = PullRequest10Head.from_dict(pull_request10_head_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


