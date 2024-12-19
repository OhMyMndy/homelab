# PullRequestWebhook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**id** | **int** |  | 
**node_id** | **str** |  | 
**html_url** | **str** |  | 
**diff_url** | **str** |  | 
**patch_url** | **str** |  | 
**issue_url** | **str** |  | 
**commits_url** | **str** |  | 
**review_comments_url** | **str** |  | 
**review_comment_url** | **str** |  | 
**comments_url** | **str** |  | 
**statuses_url** | **str** |  | 
**number** | **int** | Number uniquely identifying the pull request within its repository. | 
**state** | **str** | State of this Pull Request. Either &#x60;open&#x60; or &#x60;closed&#x60;. | 
**locked** | **bool** |  | 
**title** | **str** | The title of the pull request. | 
**user** | [**SimpleUser**](SimpleUser.md) |  | 
**body** | **str** |  | 
**labels** | [**List[PullRequestLabelsInner]**](PullRequestLabelsInner.md) |  | 
**milestone** | [**NullableMilestone**](NullableMilestone.md) |  | 
**active_lock_reason** | **str** |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**closed_at** | **datetime** |  | 
**merged_at** | **datetime** |  | 
**merge_commit_sha** | **str** |  | 
**assignee** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**assignees** | [**List[SimpleUser]**](SimpleUser.md) |  | [optional] 
**requested_reviewers** | [**List[SimpleUser]**](SimpleUser.md) |  | [optional] 
**requested_teams** | [**List[TeamSimple]**](TeamSimple.md) |  | [optional] 
**head** | [**PullRequestHead**](PullRequestHead.md) |  | 
**base** | [**PullRequestHead**](PullRequestHead.md) |  | 
**links** | [**PullRequestSimpleLinks**](PullRequestSimpleLinks.md) |  | 
**author_association** | [**AuthorAssociation**](AuthorAssociation.md) |  | 
**auto_merge** | [**AutoMerge**](AutoMerge.md) |  | 
**draft** | **bool** | Indicates whether or not the pull request is a draft. | [optional] 
**merged** | **bool** |  | 
**mergeable** | **bool** |  | 
**rebaseable** | **bool** |  | [optional] 
**mergeable_state** | **str** |  | 
**merged_by** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**comments** | **int** |  | 
**review_comments** | **int** |  | 
**maintainer_can_modify** | **bool** | Indicates whether maintainers can modify the pull request. | 
**commits** | **int** |  | 
**additions** | **int** |  | 
**deletions** | **int** |  | 
**changed_files** | **int** |  | 
**allow_auto_merge** | **bool** | Whether to allow auto-merge for pull requests. | [optional] [default to False]
**allow_update_branch** | **bool** | Whether to allow updating the pull request&#39;s branch. | [optional] 
**delete_branch_on_merge** | **bool** | Whether to delete head branches when pull requests are merged. | [optional] [default to False]
**merge_commit_message** | **str** | The default value for a merge commit message. - &#x60;PR_TITLE&#x60; - default to the pull request&#39;s title. - &#x60;PR_BODY&#x60; - default to the pull request&#39;s body. - &#x60;BLANK&#x60; - default to a blank commit message. | [optional] 
**merge_commit_title** | **str** | The default value for a merge commit title. - &#x60;PR_TITLE&#x60; - default to the pull request&#39;s title. - &#x60;MERGE_MESSAGE&#x60; - default to the classic title for a merge message (e.g., \&quot;Merge pull request #123 from branch-name\&quot;). | [optional] 
**squash_merge_commit_message** | **str** | The default value for a squash merge commit message: - &#x60;PR_BODY&#x60; - default to the pull request&#39;s body. - &#x60;COMMIT_MESSAGES&#x60; - default to the branch&#39;s commit messages. - &#x60;BLANK&#x60; - default to a blank commit message. | [optional] 
**squash_merge_commit_title** | **str** | The default value for a squash merge commit title: - &#x60;PR_TITLE&#x60; - default to the pull request&#39;s title. - &#x60;COMMIT_OR_PR_TITLE&#x60; - default to the commit&#39;s title (if only one commit) or the pull request&#39;s title (when more than one commit). | [optional] 
**use_squash_pr_title_as_default** | **bool** | Whether a squash merge commit can use the pull request title as default. **This property is closing down. Please use &#x60;squash_merge_commit_title&#x60; instead.** | [optional] [default to False]

## Example

```python
from github_openapi.models.pull_request_webhook import PullRequestWebhook

# TODO update the JSON string below
json = "{}"
# create an instance of PullRequestWebhook from a JSON string
pull_request_webhook_instance = PullRequestWebhook.from_json(json)
# print the JSON string representation of the object
print(PullRequestWebhook.to_json())

# convert the object into a dict
pull_request_webhook_dict = pull_request_webhook_instance.to_dict()
# create an instance of PullRequestWebhook from a dict
pull_request_webhook_from_dict = PullRequestWebhook.from_dict(pull_request_webhook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


