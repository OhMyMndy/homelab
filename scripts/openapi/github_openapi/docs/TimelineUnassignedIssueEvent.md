# TimelineUnassignedIssueEvent

Timeline Unassigned Issue Event

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
**assignee** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.timeline_unassigned_issue_event import TimelineUnassignedIssueEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineUnassignedIssueEvent from a JSON string
timeline_unassigned_issue_event_instance = TimelineUnassignedIssueEvent.from_json(json)
# print the JSON string representation of the object
print(TimelineUnassignedIssueEvent.to_json())

# convert the object into a dict
timeline_unassigned_issue_event_dict = timeline_unassigned_issue_event_instance.to_dict()
# create an instance of TimelineUnassignedIssueEvent from a dict
timeline_unassigned_issue_event_from_dict = TimelineUnassignedIssueEvent.from_dict(timeline_unassigned_issue_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


