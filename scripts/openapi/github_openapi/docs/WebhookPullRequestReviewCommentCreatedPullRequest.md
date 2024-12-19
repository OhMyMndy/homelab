# WebhookPullRequestReviewCommentCreatedPullRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**WebhooksPullRequest5Links**](WebhooksPullRequest5Links.md) |  | 
**active_lock_reason** | **str** |  | 
**assignee** | [**User4**](User4.md) |  | 
**assignees** | [**List[User5]**](User5.md) |  | 
**author_association** | **str** | How the author is associated with the repository. | 
**auto_merge** | [**PullRequestAutoMerge**](PullRequestAutoMerge.md) |  | [optional] 
**base** | [**PullRequestBase**](PullRequestBase.md) |  | 
**body** | **str** |  | 
**closed_at** | **str** |  | 
**comments_url** | **str** |  | 
**commits_url** | **str** |  | 
**created_at** | **str** |  | 
**diff_url** | **str** |  | 
**draft** | **bool** |  | [optional] 
**head** | [**WebhookPullRequestReviewCommentCreatedPullRequestHead**](WebhookPullRequestReviewCommentCreatedPullRequestHead.md) |  | 
**html_url** | **str** |  | 
**id** | **int** |  | 
**issue_url** | **str** |  | 
**labels** | [**List[Label]**](Label.md) |  | 
**locked** | **bool** |  | 
**merge_commit_sha** | **str** |  | 
**merged_at** | **str** |  | 
**milestone** | [**Milestone**](Milestone.md) |  | 
**node_id** | **str** |  | 
**number** | **int** |  | 
**patch_url** | **str** |  | 
**requested_reviewers** | [**List[PullRequestRequestedReviewersInner]**](PullRequestRequestedReviewersInner.md) |  | 
**requested_teams** | [**List[Team]**](Team.md) |  | 
**review_comment_url** | **str** |  | 
**review_comments_url** | **str** |  | 
**state** | **str** |  | 
**statuses_url** | **str** |  | 
**title** | **str** |  | 
**updated_at** | **str** |  | 
**url** | **str** |  | 
**user** | [**User3**](User3.md) |  | 

## Example

```python
from github_openapi.models.webhook_pull_request_review_comment_created_pull_request import WebhookPullRequestReviewCommentCreatedPullRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPullRequestReviewCommentCreatedPullRequest from a JSON string
webhook_pull_request_review_comment_created_pull_request_instance = WebhookPullRequestReviewCommentCreatedPullRequest.from_json(json)
# print the JSON string representation of the object
print(WebhookPullRequestReviewCommentCreatedPullRequest.to_json())

# convert the object into a dict
webhook_pull_request_review_comment_created_pull_request_dict = webhook_pull_request_review_comment_created_pull_request_instance.to_dict()
# create an instance of WebhookPullRequestReviewCommentCreatedPullRequest from a dict
webhook_pull_request_review_comment_created_pull_request_from_dict = WebhookPullRequestReviewCommentCreatedPullRequest.from_dict(webhook_pull_request_review_comment_created_pull_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


