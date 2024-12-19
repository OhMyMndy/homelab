# ProjectsMoveCard403Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**documentation_url** | **str** |  | [optional] 
**errors** | [**List[ProjectsMoveCard403ResponseErrorsInner]**](ProjectsMoveCard403ResponseErrorsInner.md) |  | [optional] 

## Example

```python
from github_openapi.models.projects_move_card403_response import ProjectsMoveCard403Response

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsMoveCard403Response from a JSON string
projects_move_card403_response_instance = ProjectsMoveCard403Response.from_json(json)
# print the JSON string representation of the object
print(ProjectsMoveCard403Response.to_json())

# convert the object into a dict
projects_move_card403_response_dict = projects_move_card403_response_instance.to_dict()
# create an instance of ProjectsMoveCard403Response from a dict
projects_move_card403_response_from_dict = ProjectsMoveCard403Response.from_dict(projects_move_card403_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


