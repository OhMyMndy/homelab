# WebhooksIssue

The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_lock_reason** | **str** |  | 
**assignee** | [**User4**](User4.md) |  | [optional] 
**assignees** | [**List[User4]**](User4.md) |  | 
**author_association** | **str** | How the author is associated with the repository. | 
**body** | **str** | Contents of the issue | 
**closed_at** | **datetime** |  | 
**comments** | **int** |  | 
**comments_url** | **str** |  | 
**created_at** | **datetime** |  | 
**draft** | **bool** |  | [optional] 
**events_url** | **str** |  | 
**html_url** | **str** |  | 
**id** | **int** |  | 
**labels** | [**List[Label]**](Label.md) |  | [optional] 
**labels_url** | **str** |  | 
**locked** | **bool** |  | [optional] 
**milestone** | [**Milestone**](Milestone.md) |  | 
**node_id** | **str** |  | 
**number** | **int** |  | 
**performed_via_github_app** | [**App**](App.md) |  | [optional] 
**pull_request** | [**WebhooksIssuePullRequest**](WebhooksIssuePullRequest.md) |  | [optional] 
**reactions** | [**Reactions**](Reactions.md) |  | 
**repository_url** | **str** |  | 
**sub_issues_summary** | [**SubIssuesSummary**](SubIssuesSummary.md) |  | [optional] 
**state** | **str** | State of the issue; either &#39;open&#39; or &#39;closed&#39; | [optional] 
**state_reason** | **str** |  | [optional] 
**timeline_url** | **str** |  | [optional] 
**title** | **str** | Title of the issue | 
**updated_at** | **datetime** |  | 
**url** | **str** | URL for the issue | 
**user** | [**User3**](User3.md) |  | 

## Example

```python
from github_openapi.models.webhooks_issue import WebhooksIssue

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksIssue from a JSON string
webhooks_issue_instance = WebhooksIssue.from_json(json)
# print the JSON string representation of the object
print(WebhooksIssue.to_json())

# convert the object into a dict
webhooks_issue_dict = webhooks_issue_instance.to_dict()
# create an instance of WebhooksIssue from a dict
webhooks_issue_from_dict = WebhooksIssue.from_dict(webhooks_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


