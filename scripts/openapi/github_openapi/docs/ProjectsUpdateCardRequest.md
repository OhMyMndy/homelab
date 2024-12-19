# ProjectsUpdateCardRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** | The project card&#39;s note | [optional] 
**archived** | **bool** | Whether or not the card is archived | [optional] 

## Example

```python
from github_openapi.models.projects_update_card_request import ProjectsUpdateCardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsUpdateCardRequest from a JSON string
projects_update_card_request_instance = ProjectsUpdateCardRequest.from_json(json)
# print the JSON string representation of the object
print(ProjectsUpdateCardRequest.to_json())

# convert the object into a dict
projects_update_card_request_dict = projects_update_card_request_instance.to_dict()
# create an instance of ProjectsUpdateCardRequest from a dict
projects_update_card_request_from_dict = ProjectsUpdateCardRequest.from_dict(projects_update_card_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


