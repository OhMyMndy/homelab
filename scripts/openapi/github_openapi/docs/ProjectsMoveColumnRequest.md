# ProjectsMoveColumnRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **str** | The position of the column in a project. Can be one of: &#x60;first&#x60;, &#x60;last&#x60;, or &#x60;after:&lt;column_id&gt;&#x60; to place after the specified column. | 

## Example

```python
from github_openapi.models.projects_move_column_request import ProjectsMoveColumnRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsMoveColumnRequest from a JSON string
projects_move_column_request_instance = ProjectsMoveColumnRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectsMoveColumnRequest.to_json())

# convert the object into a dict
projects_move_column_request_dict = projects_move_column_request_instance.to_dict()
# create an instance of ProjectsMoveColumnRequest from a dict
projects_move_column_request_from_dict = ProjectsMoveColumnRequest.from_dict(projects_move_column_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


