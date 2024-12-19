# SimplePullRequest3Head


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**ref** | **str** |  | 
**repo** | [**Repository12**](Repository12.md) |  | 
**sha** | **str** |  | 
**user** | [**User1**](User1.md) |  | 

## Example

```python
from github_openapi.models.simple_pull_request3_head import SimplePullRequest3Head

# TODO update the JSON string below
json = "{}"
# create an instance of SimplePullRequest3Head from a JSON string
simple_pull_request3_head_instance = SimplePullRequest3Head.from_json(json)
# print the JSON string representation of the object
print(SimplePullRequest3Head.to_json())

# convert the object into a dict
simple_pull_request3_head_dict = simple_pull_request3_head_instance.to_dict()
# create an instance of SimplePullRequest3Head from a dict
simple_pull_request3_head_from_dict = SimplePullRequest3Head.from_dict(simple_pull_request3_head_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


