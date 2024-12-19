# Issue7

The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_lock_reason** | **str** |  | 
**assignee** | [**User2**](User2.md) |  | [optional] 
**assignees** | [**List[User2]**](User2.md) |  | 
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
**performed_via_github_app** | [**App12**](App12.md) |  | [optional] 
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
**user** | [**User1**](User1.md) |  | 

## Example

```python
from github_openapi.models.issue7 import Issue7

# TODO update the JSON string below
json = "{}"
# create an instance of Issue7 from a JSON string
issue7_instance = Issue7.from_json(json)
# print the JSON string representation of the object
print(Issue7.to_json())

# convert the object into a dict
issue7_dict = issue7_instance.to_dict()
# create an instance of Issue7 from a dict
issue7_from_dict = Issue7.from_dict(issue7_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


