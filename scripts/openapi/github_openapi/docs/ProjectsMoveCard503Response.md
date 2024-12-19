# ProjectsMoveCard503Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**documentation_url** | **str** |  | [optional] 
**errors** | [**List[ProjectsMoveCard503ResponseErrorsInner]**](ProjectsMoveCard503ResponseErrorsInner.md) |  | [optional] 

## Example

```python
from github_openapi.models.projects_move_card503_response import ProjectsMoveCard503Response

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsMoveCard503Response from a JSON string
projects_move_card503_response_instance = ProjectsMoveCard503Response.from_json(json)
# print the JSON string representation of the object
print(ProjectsMoveCard503Response.to_json())

# convert the object into a dict
projects_move_card503_response_dict = projects_move_card503_response_instance.to_dict()
# create an instance of ProjectsMoveCard503Response from a dict
projects_move_card503_response_from_dict = ProjectsMoveCard503Response.from_dict(projects_move_card503_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


