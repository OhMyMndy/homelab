# AddedToProjectIssueEventProjectCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**url** | **str** |  | 
**project_id** | **int** |  | 
**project_url** | **str** |  | 
**column_name** | **str** |  | 
**previous_column_name** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.added_to_project_issue_event_project_card import AddedToProjectIssueEventProjectCard

# TODO update the JSON string below
json = "{}"
# create an instance of AddedToProjectIssueEventProjectCard from a JSON string
added_to_project_issue_event_project_card_instance = AddedToProjectIssueEventProjectCard.from_json(json)
# print the JSON string representation of the object
print(AddedToProjectIssueEventProjectCard.to_json())

# convert the object into a dict
added_to_project_issue_event_project_card_dict = added_to_project_issue_event_project_card_instance.to_dict()
# create an instance of AddedToProjectIssueEventProjectCard from a dict
added_to_project_issue_event_project_card_from_dict = AddedToProjectIssueEventProjectCard.from_dict(added_to_project_issue_event_project_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


