# StateChangeIssueEvent

State Change Issue Event

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
**state_reason** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.state_change_issue_event import StateChangeIssueEvent

# TODO update the JSON string below
json = "{}"
# create an instance of StateChangeIssueEvent from a JSON string
state_change_issue_event_instance = StateChangeIssueEvent.from_json(json)
# print the JSON string representation of the object
print(StateChangeIssueEvent.to_json())

# convert the object into a dict
state_change_issue_event_dict = state_change_issue_event_instance.to_dict()
# create an instance of StateChangeIssueEvent from a dict
state_change_issue_event_from_dict = StateChangeIssueEvent.from_dict(state_change_issue_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


