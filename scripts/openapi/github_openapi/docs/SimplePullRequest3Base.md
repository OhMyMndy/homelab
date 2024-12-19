# SimplePullRequest3Base


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**ref** | **str** |  | 
**repo** | [**Repository11**](Repository11.md) |  | 
**sha** | **str** |  | 
**user** | [**User1**](User1.md) |  | 

## Example

```python
from github_openapi.models.simple_pull_request3_base import SimplePullRequest3Base

# TODO update the JSON string below
json = "{}"
# create an instance of SimplePullRequest3Base from a JSON string
simple_pull_request3_base_instance = SimplePullRequest3Base.from_json(json)
# print the JSON string representation of the object
print(SimplePullRequest3Base.to_json())

# convert the object into a dict
simple_pull_request3_base_dict = simple_pull_request3_base_instance.to_dict()
# create an instance of SimplePullRequest3Base from a dict
simple_pull_request3_base_from_dict = SimplePullRequest3Base.from_dict(simple_pull_request3_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


