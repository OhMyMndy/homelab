# UnassignedIssueEvent

Unassigned Issue Event

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
**assigner** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.unassigned_issue_event import UnassignedIssueEvent

# TODO update the JSON string below
json = "{}"
# create an instance of UnassignedIssueEvent from a JSON string
unassigned_issue_event_instance = UnassignedIssueEvent.from_json(json)
# print the JSON string representation of the object
print(UnassignedIssueEvent.to_json())

# convert the object into a dict
unassigned_issue_event_dict = unassigned_issue_event_instance.to_dict()
# create an instance of UnassignedIssueEvent from a dict
unassigned_issue_event_from_dict = UnassignedIssueEvent.from_dict(unassigned_issue_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


