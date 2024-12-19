# SimpleCommitStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**id** | **int** |  | 
**node_id** | **str** |  | 
**state** | **str** |  | 
**context** | **str** |  | 
**target_url** | **str** |  | 
**required** | **bool** |  | [optional] 
**avatar_url** | **str** |  | 
**url** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from github_openapi.models.simple_commit_status import SimpleCommitStatus

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleCommitStatus from a JSON string
simple_commit_status_instance = SimpleCommitStatus.from_json(json)
# print the JSON string representation of the object
print(SimpleCommitStatus.to_json())

# convert the object into a dict
simple_commit_status_dict = simple_commit_status_instance.to_dict()
# create an instance of SimpleCommitStatus from a dict
simple_commit_status_from_dict = SimpleCommitStatus.from_dict(simple_commit_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


