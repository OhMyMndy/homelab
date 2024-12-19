# RenamedIssueEvent

Renamed Issue Event

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
**rename** | [**RenamedIssueEventRename**](RenamedIssueEventRename.md) |  | 

## Example

```python
from github_openapi.models.renamed_issue_event import RenamedIssueEvent

# TODO update the JSON string below
json = "{}"
# create an instance of RenamedIssueEvent from a JSON string
renamed_issue_event_instance = RenamedIssueEvent.from_json(json)
# print the JSON string representation of the object
print(RenamedIssueEvent.to_json())

# convert the object into a dict
renamed_issue_event_dict = renamed_issue_event_instance.to_dict()
# create an instance of RenamedIssueEvent from a dict
renamed_issue_event_from_dict = RenamedIssueEvent.from_dict(renamed_issue_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


