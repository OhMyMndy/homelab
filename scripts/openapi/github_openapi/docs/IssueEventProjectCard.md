# IssueEventProjectCard

Issue Event Project Card

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**id** | **int** |  | 
**project_url** | **str** |  | 
**project_id** | **int** |  | 
**column_name** | **str** |  | 
**previous_column_name** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.issue_event_project_card import IssueEventProjectCard

# TODO update the JSON string below
json = "{}"
# create an instance of IssueEventProjectCard from a JSON string
issue_event_project_card_instance = IssueEventProjectCard.from_json(json)
# print the JSON string representation of the object
print(IssueEventProjectCard.to_json())

# convert the object into a dict
issue_event_project_card_dict = issue_event_project_card_instance.to_dict()
# create an instance of IssueEventProjectCard from a dict
issue_event_project_card_from_dict = IssueEventProjectCard.from_dict(issue_event_project_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


