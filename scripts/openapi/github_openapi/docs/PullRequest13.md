# PullRequest13


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**WebhooksPullRequest5Links**](WebhooksPullRequest5Links.md) |  | 
**active_lock_reason** | **str** |  | 
**additions** | **int** |  | [optional] 
**assignee** | [**User2**](User2.md) |  | 
**assignees** | [**List[User]**](User.md) |  | 
**author_association** | **str** | How the author is associated with the repository. | 
**auto_merge** | [**PullRequestAutoMerge1**](PullRequestAutoMerge1.md) |  | 
**base** | [**PullRequestBase**](PullRequestBase.md) |  | 
**body** | **str** |  | 
**changed_files** | **int** |  | [optional] 
**closed_at** | **datetime** |  | 
**comments** | **int** |  | [optional] 
**comments_url** | **str** |  | 
**commits** | **int** |  | [optional] 
**commits_url** | **str** |  | 
**created_at** | **datetime** |  | 
**deletions** | **int** |  | [optional] 
**diff_url** | **str** |  | 
**draft** | **bool** | Indicates whether or not the pull request is a draft. | 
**head** | [**WebhookPullRequestReviewCommentDeletedPullRequestHead**](WebhookPullRequestReviewCommentDeletedPullRequestHead.md) |  | 
**html_url** | **str** |  | 
**id** | **int** |  | 
**issue_url** | **str** |  | 
**labels** | [**List[Label]**](Label.md) |  | 
**locked** | **bool** |  | 
**maintainer_can_modify** | **bool** | Indicates whether maintainers can modify the pull request. | [optional] 
**merge_commit_sha** | **str** |  | 
**mergeable** | **bool** |  | [optional] 
**mergeable_state** | **str** |  | [optional] 
**merged** | **bool** |  | [optional] 
**merged_at** | **datetime** |  | 
**merged_by** | [**User2**](User2.md) |  | [optional] 
**milestone** | [**Milestone1**](Milestone1.md) |  | 
**node_id** | **str** |  | 
**number** | **int** | Number uniquely identifying the pull request within its repository. | 
**patch_url** | **str** |  | 
**rebaseable** | **bool** |  | [optional] 
**requested_reviewers** | [**List[PullRequest3RequestedReviewersInner]**](PullRequest3RequestedReviewersInner.md) |  | 
**requested_teams** | [**List[Team]**](Team.md) |  | 
**review_comment_url** | **str** |  | 
**review_comments** | **int** |  | [optional] 
**review_comments_url** | **str** |  | 
**state** | **str** | State of this Pull Request. Either &#x60;open&#x60; or &#x60;closed&#x60;. | 
**statuses_url** | **str** |  | 
**title** | **str** | The title of the pull request. | 
**updated_at** | **datetime** |  | 
**url** | **str** |  | 
**user** | [**User1**](User1.md) |  | 

## Example

```python
from github_openapi.models.pull_request13 import PullRequest13

# TODO update the JSON string below
json = "{}"
# create an instance of PullRequest13 from a JSON string
pull_request13_instance = PullRequest13.from_json(json)
# print the JSON string representation of the object
print(PullRequest13.to_json())

# convert the object into a dict
pull_request13_dict = pull_request13_instance.to_dict()
# create an instance of PullRequest13 from a dict
pull_request13_from_dict = PullRequest13.from_dict(pull_request13_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


