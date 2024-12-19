# ProjectCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after_id** | **int** |  | [optional] 
**archived** | **bool** | Whether or not the card is archived | 
**column_id** | **int** |  | 
**column_url** | **str** |  | 
**content_url** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**creator** | [**User4**](User4.md) |  | 
**id** | **int** | The project card&#39;s ID | 
**node_id** | **str** |  | 
**note** | **str** |  | 
**project_url** | **str** |  | 
**updated_at** | **datetime** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.project_card import ProjectCard

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCard from a JSON string
project_card_instance = ProjectCard.from_json(json)
# print the JSON string representation of the object
print(ProjectCard.to_json())

# convert the object into a dict
project_card_dict = project_card_instance.to_dict()
# create an instance of ProjectCard from a dict
project_card_from_dict = ProjectCard.from_dict(project_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


