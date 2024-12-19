# IssueEvent

Issue Event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**node_id** | **str** |  | 
**url** | **str** |  | 
**actor** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**event** | **str** |  | 
**commit_id** | **str** |  | 
**commit_url** | **str** |  | 
**created_at** | **datetime** |  | 
**issue** | [**NullableIssue**](NullableIssue.md) |  | [optional] 
**label** | [**IssueEventLabel**](IssueEventLabel.md) |  | [optional] 
**assignee** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | [optional] 
**assigner** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | [optional] 
**review_requester** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | [optional] 
**requested_reviewer** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | [optional] 
**requested_team** | [**Team**](Team.md) |  | [optional] 
**dismissed_review** | [**IssueEventDismissedReview**](IssueEventDismissedReview.md) |  | [optional] 
**milestone** | [**IssueEventMilestone**](IssueEventMilestone.md) |  | [optional] 
**project_card** | [**IssueEventProjectCard**](IssueEventProjectCard.md) |  | [optional] 
**rename** | [**IssueEventRename**](IssueEventRename.md) |  | [optional] 
**author_association** | [**AuthorAssociation**](AuthorAssociation.md) |  | [optional] 
**lock_reason** | **str** |  | [optional] 
**performed_via_github_app** | [**NullableIntegration**](NullableIntegration.md) |  | [optional] 

## Example

```python
from github_openapi.models.issue_event import IssueEvent

# TODO update the JSON string below
json = "{}"
# create an instance of IssueEvent from a JSON string
issue_event_instance = IssueEvent.from_json(json)
# print the JSON string representation of the object
print(IssueEvent.to_json())

# convert the object into a dict
issue_event_dict = issue_event_instance.to_dict()
# create an instance of IssueEvent from a dict
issue_event_from_dict = IssueEvent.from_dict(issue_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


