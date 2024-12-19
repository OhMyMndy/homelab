# MilestonedIssueEvent

Milestoned Issue Event

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
**milestone** | [**MilestonedIssueEventMilestone**](MilestonedIssueEventMilestone.md) |  | 

## Example

```python
from github_openapi.models.milestoned_issue_event import MilestonedIssueEvent

# TODO update the JSON string below
json = "{}"
# create an instance of MilestonedIssueEvent from a JSON string
milestoned_issue_event_instance = MilestonedIssueEvent.from_json(json)
# print the JSON string representation of the object
print(MilestonedIssueEvent.to_json())

# convert the object into a dict
milestoned_issue_event_dict = milestoned_issue_event_instance.to_dict()
# create an instance of MilestonedIssueEvent from a dict
milestoned_issue_event_from_dict = MilestonedIssueEvent.from_dict(milestoned_issue_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


