# PullRequest2Head


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**ref** | **str** |  | 
**repo** | [**Repository6**](Repository6.md) |  | 
**sha** | **str** |  | 
**user** | [**User1**](User1.md) |  | 

## Example

```python
from github_openapi.models.pull_request2_head import PullRequest2Head

# TODO update the JSON string below
json = "{}"
# create an instance of PullRequest2Head from a JSON string
pull_request2_head_instance = PullRequest2Head.from_json(json)
# print the JSON string representation of the object
print(PullRequest2Head.to_json())

# convert the object into a dict
pull_request2_head_dict = pull_request2_head_instance.to_dict()
# create an instance of PullRequest2Head from a dict
pull_request2_head_from_dict = PullRequest2Head.from_dict(pull_request2_head_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


