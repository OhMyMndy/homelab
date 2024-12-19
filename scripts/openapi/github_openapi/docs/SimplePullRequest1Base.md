# SimplePullRequest1Base


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**ref** | **str** |  | 
**repo** | [**Repository8**](Repository8.md) |  | 
**sha** | **str** |  | 
**user** | [**User1**](User1.md) |  | 

## Example

```python
from github_openapi.models.simple_pull_request1_base import SimplePullRequest1Base

# TODO update the JSON string below
json = "{}"
# create an instance of SimplePullRequest1Base from a JSON string
simple_pull_request1_base_instance = SimplePullRequest1Base.from_json(json)
# print the JSON string representation of the object
print(SimplePullRequest1Base.to_json())

# convert the object into a dict
simple_pull_request1_base_dict = simple_pull_request1_base_instance.to_dict()
# create an instance of SimplePullRequest1Base from a dict
simple_pull_request1_base_from_dict = SimplePullRequest1Base.from_dict(simple_pull_request1_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


