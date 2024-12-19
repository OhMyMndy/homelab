# TimelineIssueEvents

Timeline Event

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
**milestone** | [**MilestonedIssueEventMilestone**](MilestonedIssueEventMilestone.md) |  | 
**rename** | [**RenamedIssueEventRename**](RenamedIssueEventRename.md) |  | 
**review_requester** | [**SimpleUser**](SimpleUser.md) |  | 
**requested_team** | [**Team**](Team.md) |  | [optional] 
**requested_reviewer** | [**SimpleUser**](SimpleUser.md) |  | [optional] 
**dismissed_review** | [**ReviewDismissedIssueEventDismissedReview**](ReviewDismissedIssueEventDismissedReview.md) |  | 
**lock_reason** | **str** |  | 
**project_card** | [**AddedToProjectIssueEventProjectCard**](AddedToProjectIssueEventProjectCard.md) |  | [optional] 
**body** | **str** | The text of the review. | 
**body_text** | **str** |  | [optional] 
**body_html** | **str** |  | [optional] 
**html_url** | **str** |  | 
**user** | [**SimpleUser**](SimpleUser.md) |  | 
**updated_at** | **datetime** |  | 
**issue_url** | **str** |  | 
**author_association** | [**AuthorAssociation**](AuthorAssociation.md) |  | 
**reactions** | [**ReactionRollup**](ReactionRollup.md) |  | [optional] 
**source** | [**TimelineCrossReferencedEventSource**](TimelineCrossReferencedEventSource.md) |  | 
**sha** | **str** | SHA for the commit | 
**author** | [**GitCommitAuthor**](GitCommitAuthor.md) |  | 
**committer** | [**GitCommitAuthor**](GitCommitAuthor.md) |  | 
**message** | **str** | Message describing the purpose of the commit | 
**tree** | [**GitCommitTree**](GitCommitTree.md) |  | 
**parents** | [**List[GitCommitParentsInner]**](GitCommitParentsInner.md) |  | 
**verification** | [**GitCommitVerification**](GitCommitVerification.md) |  | 
**state** | **str** |  | 
**pull_request_url** | **str** |  | 
**links** | [**TimelineReviewedEventLinks**](TimelineReviewedEventLinks.md) |  | 
**submitted_at** | **datetime** |  | [optional] 
**comments** | [**List[CommitComment]**](CommitComment.md) |  | [optional] 
**assignee** | [**SimpleUser**](SimpleUser.md) |  | 
**state_reason** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.timeline_issue_events import TimelineIssueEvents

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineIssueEvents from a JSON string
timeline_issue_events_instance = TimelineIssueEvents.from_json(json)
# print the JSON string representation of the object
print(TimelineIssueEvents.to_json())

# convert the object into a dict
timeline_issue_events_dict = timeline_issue_events_instance.to_dict()
# create an instance of TimelineIssueEvents from a dict
timeline_issue_events_from_dict = TimelineIssueEvents.from_dict(timeline_issue_events_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


