# TimelineAssignedIssueEvent

Timeline Assigned Issue Event

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
from github_openapi.models.timeline_assigned_issue_event import TimelineAssignedIssueEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineAssignedIssueEvent from a JSON string
timeline_assigned_issue_event_instance = TimelineAssignedIssueEvent.from_json(json)
# print the JSON string representation of the object
print(TimelineAssignedIssueEvent.to_json())

# convert the object into a dict
timeline_assigned_issue_event_dict = timeline_assigned_issue_event_instance.to_dict()
# create an instance of TimelineAssignedIssueEvent from a dict
timeline_assigned_issue_event_from_dict = TimelineAssignedIssueEvent.from_dict(timeline_assigned_issue_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


