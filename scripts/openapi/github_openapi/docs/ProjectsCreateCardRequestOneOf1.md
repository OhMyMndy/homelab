# ProjectsCreateCardRequestOneOf1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_id** | **int** | The unique identifier of the content associated with the card | 
**content_type** | **str** | The piece of content associated with the card | 

## Example

```python
from github_openapi.models.projects_create_card_request_one_of1 import ProjectsCreateCardRequestOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectsCreateCardRequestOneOf1 from a JSON string
projects_create_card_request_one_of1_instance = ProjectsCreateCardRequestOneOf1.from_json(json)
# print the JSON string representation of the object
print(ProjectsCreateCardRequestOneOf1.to_json())

# convert the object into a dict
projects_create_card_request_one_of1_dict = projects_create_card_request_one_of1_instance.to_dict()
# create an instance of ProjectsCreateCardRequestOneOf1 from a dict
projects_create_card_request_one_of1_from_dict = ProjectsCreateCardRequestOneOf1.from_dict(projects_create_card_request_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


