# Issue2

The [issue](https://docs.github.com/rest/issues/issues#get-an-issue) itself.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_lock_reason** | **str** |  | 
**assignee** | [**User4**](User4.md) |  | [optional] 
**assignees** | [**List[User5]**](User5.md) |  | 
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
**user** | [**User3**](User3.md) |  | 

## Example

```python
from github_openapi.models.issue2 import Issue2

# TODO update the JSON string below
json = "{}"
# create an instance of Issue2 from a JSON string
issue2_instance = Issue2.from_json(json)
# print the JSON string representation of the object
print(Issue2.to_json())

# convert the object into a dict
issue2_dict = issue2_instance.to_dict()
# create an instance of Issue2 from a dict
issue2_from_dict = Issue2.from_dict(issue2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


