# ConvertedNoteToIssueIssueEvent

Converted Note to Issue Issue Event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**node_id** | **str** |  | 
**url** | **str** |  | 
**actor** | [**SimpleUser**](SimpleUser.md) |  | 
**event** | **str** |  | 
**commit_id** | **str** |  | 
**commit_url** | **str** |  | 
**created_at** | **str** |  | 
**performed_via_github_app** | [**Integration**](Integration.md) |  | 
**project_card** | [**AddedToProjectIssueEventProjectCard**](AddedToProjectIssueEventProjectCard.md) |  | [optional] 

## Example

```python
from github_openapi.models.converted_note_to_issue_issue_event import ConvertedNoteToIssueIssueEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertedNoteToIssueIssueEvent from a JSON string
converted_note_to_issue_issue_event_instance = ConvertedNoteToIssueIssueEvent.from_json(json)
# print the JSON string representation of the object
print(ConvertedNoteToIssueIssueEvent.to_json())

# convert the object into a dict
converted_note_to_issue_issue_event_dict = converted_note_to_issue_issue_event_instance.to_dict()
# create an instance of ConvertedNoteToIssueIssueEvent from a dict
converted_note_to_issue_issue_event_from_dict = ConvertedNoteToIssueIssueEvent.from_dict(converted_note_to_issue_issue_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


