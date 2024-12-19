# PullRequestSimpleHead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**ref** | **str** |  | 
**repo** | [**Repository**](Repository.md) |  | 
**sha** | **str** |  | 
**user** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 

## Example

```python
from github_openapi.models.pull_request_simple_head import PullRequestSimpleHead

# TODO update the JSON string below
json = "{}"
# create an instance of PullRequestSimpleHead from a JSON string
pull_request_simple_head_instance = PullRequestSimpleHead.from_json(json)
# print the JSON string representation of the object
print(PullRequestSimpleHead.to_json())

# convert the object into a dict
pull_request_simple_head_dict = pull_request_simple_head_instance.to_dict()
# create an instance of PullRequestSimpleHead from a dict
pull_request_simple_head_from_dict = PullRequestSimpleHead.from_dict(pull_request_simple_head_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


