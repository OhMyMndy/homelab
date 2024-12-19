# WebhookIssueCommentCreatedIssue

The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) the comment belongs to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_lock_reason** | **str** |  | 
**assignee** | [**User4**](User4.md) |  | 
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
**labels** | [**List[Label]**](Label.md) |  | 
**labels_url** | **str** |  | 
**locked** | **bool** |  | 
**milestone** | **object** |  | 
**node_id** | **str** |  | 
**number** | **int** |  | 
**performed_via_github_app** | **object** |  | [optional] 
**pull_request** | [**WebhooksIssuePullRequest**](WebhooksIssuePullRequest.md) |  | [optional] 
**reactions** | [**WebhookIssueCommentCreatedIssueAllOfReactions**](WebhookIssueCommentCreatedIssueAllOfReactions.md) |  | 
**repository_url** | **str** |  | 
**sub_issues_summary** | [**SubIssuesSummary**](SubIssuesSummary.md) |  | [optional] 
**state** | **str** | State of the issue; either &#39;open&#39; or &#39;closed&#39; | 
**state_reason** | **str** |  | [optional] 
**timeline_url** | **str** |  | [optional] 
**title** | **str** |  | 
**updated_at** | **str** |  | 
**url** | **str** |  | 
**user** | [**WebhookIssueCommentCreatedIssueAllOfUser**](WebhookIssueCommentCreatedIssueAllOfUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_issue_comment_created_issue import WebhookIssueCommentCreatedIssue

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookIssueCommentCreatedIssue from a JSON string
webhook_issue_comment_created_issue_instance = WebhookIssueCommentCreatedIssue.from_json(json)
# print the JSON string representation of the object
print(WebhookIssueCommentCreatedIssue.to_json())

# convert the object into a dict
webhook_issue_comment_created_issue_dict = webhook_issue_comment_created_issue_instance.to_dict()
# create an instance of WebhookIssueCommentCreatedIssue from a dict
webhook_issue_comment_created_issue_from_dict = WebhookIssueCommentCreatedIssue.from_dict(webhook_issue_comment_created_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


