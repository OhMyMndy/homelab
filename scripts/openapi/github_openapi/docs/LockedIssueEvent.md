# LockedIssueEvent

Locked Issue Event

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
**lock_reason** | **str** |  | 

## Example

```python
from github_openapi.models.locked_issue_event import LockedIssueEvent

# TODO update the JSON string below
json = "{}"
# create an instance of LockedIssueEvent from a JSON string
locked_issue_event_instance = LockedIssueEvent.from_json(json)
# print the JSON string representation of the object
print(LockedIssueEvent.to_json())

# convert the object into a dict
locked_issue_event_dict = locked_issue_event_instance.to_dict()
# create an instance of LockedIssueEvent from a dict
locked_issue_event_from_dict = LockedIssueEvent.from_dict(locked_issue_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


