# UnlabeledIssueEvent

Unlabeled Issue Event

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
**label** | [**LabeledIssueEventLabel**](LabeledIssueEventLabel.md) |  | 

## Example

```python
from github_openapi.models.unlabeled_issue_event import UnlabeledIssueEvent

# TODO update the JSON string below
json = "{}"
# create an instance of UnlabeledIssueEvent from a JSON string
unlabeled_issue_event_instance = UnlabeledIssueEvent.from_json(json)
# print the JSON string representation of the object
print(UnlabeledIssueEvent.to_json())

# convert the object into a dict
unlabeled_issue_event_dict = unlabeled_issue_event_instance.to_dict()
# create an instance of UnlabeledIssueEvent from a dict
unlabeled_issue_event_from_dict = UnlabeledIssueEvent.from_dict(unlabeled_issue_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


