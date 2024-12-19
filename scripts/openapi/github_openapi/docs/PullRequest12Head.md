# PullRequest12Head


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**ref** | **str** |  | 
**repo** | [**Repository14**](Repository14.md) |  | 
**sha** | **str** |  | 
**user** | [**User1**](User1.md) |  | 

## Example

```python
from github_openapi.models.pull_request12_head import PullRequest12Head

# TODO update the JSON string below
json = "{}"
# create an instance of PullRequest12Head from a JSON string
pull_request12_head_instance = PullRequest12Head.from_json(json)
# print the JSON string representation of the object
print(PullRequest12Head.to_json())

# convert the object into a dict
pull_request12_head_dict = pull_request12_head_instance.to_dict()
# create an instance of PullRequest12Head from a dict
pull_request12_head_from_dict = PullRequest12Head.from_dict(pull_request12_head_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


