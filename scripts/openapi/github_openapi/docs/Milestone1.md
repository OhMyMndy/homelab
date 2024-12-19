# Milestone1

A collection of related issues and pull requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closed_at** | **datetime** |  | 
**closed_issues** | **int** |  | 
**created_at** | **datetime** |  | 
**creator** | [**User2**](User2.md) |  | 
**description** | **str** |  | 
**due_on** | **datetime** |  | 
**html_url** | **str** |  | 
**id** | **int** |  | 
**labels_url** | **str** |  | 
**node_id** | **str** |  | 
**number** | **int** | The number of the milestone. | 
**open_issues** | **int** |  | 
**state** | **str** | The state of the milestone. | 
**title** | **str** | The title of the milestone. | 
**updated_at** | **datetime** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.milestone1 import Milestone1

# TODO update the JSON string below
json = "{}"
# create an instance of Milestone1 from a JSON string
milestone1_instance = Milestone1.from_json(json)
# print the JSON string representation of the object
print(Milestone1.to_json())

# convert the object into a dict
milestone1_dict = milestone1_instance.to_dict()
# create an instance of Milestone1 from a dict
milestone1_from_dict = Milestone1.from_dict(milestone1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


