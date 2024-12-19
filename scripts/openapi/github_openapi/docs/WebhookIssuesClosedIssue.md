# WebhookIssuesClosedIssue

The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_lock_reason** | **str** |  | 
**assignee** | **object** |  | [optional] 
**assignees** | **List[Optional[object]]** |  | 
**author_association** | **str** |  | 
**body** | **str** |  | 
**closed_at** | **str** |  | 
**comments** | **int** |  | 
**comments_url** | **str** |  | 
**created_at** | **str** |  | 
**draft** | **bool** |  | [optional] 
**events_url** | **str** |  | 
**html_url** | **str** |  | 
**id** | **int** |  | 
**labels** | **List[Optional[object]]** |  | [optional] 
**labels_url** | **str** |  | 
**locked** | **bool** |  | [optional] 
**milestone** | **object** |  | 
**node_id** | **str** |  | 
**number** | **int** |  | 
**performed_via_github_app** | **object** |  | [optional] 
**pull_request** | [**WebhooksIssuePullRequest**](WebhooksIssuePullRequest.md) |  | [optional] 
**reactions** | [**WebhookIssueCommentCreatedIssueAllOfReactions**](WebhookIssueCommentCreatedIssueAllOfReactions.md) |  | 
**repository_url** | **str** |  | 
**sub_issues_summary** | [**SubIssuesSummary**](SubIssuesSummary.md) |  | [optional] 
**state** | **str** |  | 
**state_reason** | **str** |  | [optional] 
**timeline_url** | **str** |  | [optional] 
**title** | **str** |  | 
**updated_at** | **str** |  | 
**url** | **str** |  | 
**user** | [**WebhookIssueCommentDeletedIssueAllOfUser**](WebhookIssueCommentDeletedIssueAllOfUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_issues_closed_issue import WebhookIssuesClosedIssue

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookIssuesClosedIssue from a JSON string
webhook_issues_closed_issue_instance = WebhookIssuesClosedIssue.from_json(json)
# print the JSON string representation of the object
print(WebhookIssuesClosedIssue.to_json())

# convert the object into a dict
webhook_issues_closed_issue_dict = webhook_issues_closed_issue_instance.to_dict()
# create an instance of WebhookIssuesClosedIssue from a dict
webhook_issues_closed_issue_from_dict = WebhookIssuesClosedIssue.from_dict(webhook_issues_closed_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


