# AssignedIssueEvent

Assigned Issue Event

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
**assignee** | [**SimpleUser**](SimpleUser.md) |  | 
**assigner** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.assigned_issue_event import AssignedIssueEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AssignedIssueEvent from a JSON string
assigned_issue_event_instance = AssignedIssueEvent.from_json(json)
# print the JSON string representation of the object
print(AssignedIssueEvent.to_json())

# convert the object into a dict
assigned_issue_event_dict = assigned_issue_event_instance.to_dict()
# create an instance of AssignedIssueEvent from a dict
assigned_issue_event_from_dict = AssignedIssueEvent.from_dict(assigned_issue_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


