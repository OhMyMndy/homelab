# ProjectsCreateCardRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** | The project card&#39;s note | 
**content_id** | **int** | The unique identifier of the content associated with the card | 
**content_type** | **str** | The piece of content associated with the card | 

## Example

```python
from github_openapi.models.projects_create_card_request import ProjectsCreateCardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsCreateCardRequest from a JSON string
projects_create_card_request_instance = ProjectsCreateCardRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectsCreateCardRequest.to_json())

# convert the object into a dict
projects_create_card_request_dict = projects_create_card_request_instance.to_dict()
# create an instance of ProjectsCreateCardRequest from a dict
projects_create_card_request_from_dict = ProjectsCreateCardRequest.from_dict(projects_create_card_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


