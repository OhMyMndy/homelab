# AddedToProjectIssueEvent

Added to Project Issue Event

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
**performed_via_github_app** | [**NullableIntegration**](NullableIntegration.md) |  | 
**project_card** | [**AddedToProjectIssueEventProjectCard**](AddedToProjectIssueEventProjectCard.md) |  | [optional] 

## Example

```python
from github_openapi.models.added_to_project_issue_event import AddedToProjectIssueEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AddedToProjectIssueEvent from a JSON string
added_to_project_issue_event_instance = AddedToProjectIssueEvent.from_json(json)
# print the JSON string representation of the object
print(AddedToProjectIssueEvent.to_json())

# convert the object into a dict
added_to_project_issue_event_dict = added_to_project_issue_event_instance.to_dict()
# create an instance of AddedToProjectIssueEvent from a dict
added_to_project_issue_event_from_dict = AddedToProjectIssueEvent.from_dict(added_to_project_issue_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


