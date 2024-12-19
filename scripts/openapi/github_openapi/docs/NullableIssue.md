# NullableIssue

Issues are a great way to keep track of tasks, enhancements, and bugs for your projects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**node_id** | **str** |  | 
**url** | **str** | URL for the issue | 
**repository_url** | **str** |  | 
**labels_url** | **str** |  | 
**comments_url** | **str** |  | 
**events_url** | **str** |  | 
**html_url** | **str** |  | 
**number** | **int** | Number uniquely identifying the issue within its repository | 
**state** | **str** | State of the issue; either &#39;open&#39; or &#39;closed&#39; | 
**state_reason** | **str** | The reason for the current state | [optional] 
**title** | **str** | Title of the issue | 
**body** | **str** | Contents of the issue | [optional] 
**user** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**labels** | [**List[IssueLabelsInner]**](IssueLabelsInner.md) | Labels to associate with this issue; pass one or more label names to replace the set of labels on this issue; send an empty array to clear all labels from the issue; note that the labels are silently dropped for users without push access to the repository | 
**assignee** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**assignees** | [**List[SimpleUser]**](SimpleUser.md) |  | [optional] 
**milestone** | [**NullableMilestone**](NullableMilestone.md) |  | 
**locked** | **bool** |  | 
**active_lock_reason** | **str** |  | [optional] 
**comments** | **int** |  | 
**pull_request** | [**IssuePullRequest**](IssuePullRequest.md) |  | [optional] 
**closed_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**draft** | **bool** |  | [optional] 
**closed_by** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | [optional] 
**body_html** | **str** |  | [optional] 
**body_text** | **str** |  | [optional] 
**timeline_url** | **str** |  | [optional] 
**repository** | [**Repository**](Repository.md) |  | [optional] 
**performed_via_github_app** | [**NullableIntegration**](NullableIntegration.md) |  | [optional] 
**author_association** | [**AuthorAssociation**](AuthorAssociation.md) |  | 
**reactions** | [**ReactionRollup**](ReactionRollup.md) |  | [optional] 
**sub_issues_summary** | [**SubIssuesSummary**](SubIssuesSummary.md) |  | [optional] 

## Example

```python
from github_openapi.models.nullable_issue import NullableIssue

# TODO update the JSON string below
json = "{}"
# create an instance of NullableIssue from a JSON string
nullable_issue_instance = NullableIssue.from_json(json)
# print the JSON string representation of the object
print(NullableIssue.to_json())

# convert the object into a dict
nullable_issue_dict = nullable_issue_instance.to_dict()
# create an instance of NullableIssue from a dict
nullable_issue_from_dict = NullableIssue.from_dict(nullable_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


