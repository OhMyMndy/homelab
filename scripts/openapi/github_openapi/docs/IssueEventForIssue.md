# IssueEventForIssue

Issue Event for Issue

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
**label** | [**LabeledIssueEventLabel**](LabeledIssueEventLabel.md) |  | 
**assignee** | [**SimpleUser**](SimpleUser.md) |  | 
**assigner** | [**SimpleUser**](SimpleUser.md) |  | 
**milestone** | [**MilestonedIssueEventMilestone**](MilestonedIssueEventMilestone.md) |  | 
**rename** | [**RenamedIssueEventRename**](RenamedIssueEventRename.md) |  | 
**review_requester** | [**SimpleUser**](SimpleUser.md) |  | 
**requested_team** | [**Team**](Team.md) |  | [optional] 
**requested_reviewer** | [**SimpleUser**](SimpleUser.md) |  | [optional] 
**dismissed_review** | [**ReviewDismissedIssueEventDismissedReview**](ReviewDismissedIssueEventDismissedReview.md) |  | 
**lock_reason** | **str** |  | 
**project_card** | [**AddedToProjectIssueEventProjectCard**](AddedToProjectIssueEventProjectCard.md) |  | [optional] 

## Example

```python
from github_openapi.models.issue_event_for_issue import IssueEventForIssue

# TODO update the JSON string below
json = "{}"
# create an instance of IssueEventForIssue from a JSON string
issue_event_for_issue_instance = IssueEventForIssue.from_json(json)
# print the JSON string representation of the object
print(IssueEventForIssue.to_json())

# convert the object into a dict
issue_event_for_issue_dict = issue_event_for_issue_instance.to_dict()
# create an instance of IssueEventForIssue from a dict
issue_event_for_issue_from_dict = IssueEventForIssue.from_dict(issue_event_for_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


