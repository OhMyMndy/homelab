# SimplePullRequest1Head


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**ref** | **str** |  | 
**repo** | [**Repository9**](Repository9.md) |  | 
**sha** | **str** |  | 
**user** | [**User1**](User1.md) |  | 

## Example

```python
from github_openapi.models.simple_pull_request1_head import SimplePullRequest1Head

# TODO update the JSON string below
json = "{}"
# create an instance of SimplePullRequest1Head from a JSON string
simple_pull_request1_head_instance = SimplePullRequest1Head.from_json(json)
# print the JSON string representation of the object
print(SimplePullRequest1Head.to_json())

# convert the object into a dict
simple_pull_request1_head_dict = simple_pull_request1_head_instance.to_dict()
# create an instance of SimplePullRequest1Head from a dict
simple_pull_request1_head_from_dict = SimplePullRequest1Head.from_dict(simple_pull_request1_head_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


