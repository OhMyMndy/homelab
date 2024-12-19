# IssueSearchResultItem

Issue Search Result Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**repository_url** | **str** |  | 
**labels_url** | **str** |  | 
**comments_url** | **str** |  | 
**events_url** | **str** |  | 
**html_url** | **str** |  | 
**id** | **int** |  | 
**node_id** | **str** |  | 
**number** | **int** |  | 
**title** | **str** |  | 
**locked** | **bool** |  | 
**active_lock_reason** | **str** |  | [optional] 
**assignees** | [**List[SimpleUser]**](SimpleUser.md) |  | [optional] 
**user** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**labels** | [**List[IssueSearchResultItemLabelsInner]**](IssueSearchResultItemLabelsInner.md) |  | 
**sub_issues_summary** | [**SubIssuesSummary**](SubIssuesSummary.md) |  | [optional] 
**state** | **str** |  | 
**state_reason** | **str** |  | [optional] 
**assignee** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**milestone** | [**NullableMilestone**](NullableMilestone.md) |  | 
**comments** | **int** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**closed_at** | **datetime** |  | 
**text_matches** | [**List[SearchResultTextMatchesInner]**](SearchResultTextMatchesInner.md) |  | [optional] 
**pull_request** | [**IssuePullRequest**](IssuePullRequest.md) |  | [optional] 
**body** | **str** |  | [optional] 
**score** | **float** |  | 
**author_association** | [**AuthorAssociation**](AuthorAssociation.md) |  | 
**draft** | **bool** |  | [optional] 
**repository** | [**Repository**](Repository.md) |  | [optional] 
**body_html** | **str** |  | [optional] 
**body_text** | **str** |  | [optional] 
**timeline_url** | **str** |  | [optional] 
**performed_via_github_app** | [**NullableIntegration**](NullableIntegration.md) |  | [optional] 
**reactions** | [**ReactionRollup**](ReactionRollup.md) |  | [optional] 

## Example

```python
from github_openapi.models.issue_search_result_item import IssueSearchResultItem

# TODO update the JSON string below
json = "{}"
# create an instance of IssueSearchResultItem from a JSON string
issue_search_result_item_instance = IssueSearchResultItem.from_json(json)
# print the JSON string representation of the object
print(IssueSearchResultItem.to_json())

# convert the object into a dict
issue_search_result_item_dict = issue_search_result_item_instance.to_dict()
# create an instance of IssueSearchResultItem from a dict
issue_search_result_item_from_dict = IssueSearchResultItem.from_dict(issue_search_result_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


