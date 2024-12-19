# RepositoryWebhooks

The repository on GitHub where the event occurred. Webhook payloads contain the `repository` property when the event occurs from activity in a repository.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the repository | 
**node_id** | **str** |  | 
**name** | **str** | The name of the repository. | 
**full_name** | **str** |  | 
**license** | [**NullableLicenseSimple**](NullableLicenseSimple.md) |  | 
**organization** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | [optional] 
**forks** | **int** |  | 
**permissions** | [**RepositoryPermissions**](RepositoryPermissions.md) |  | [optional] 
**owner** | [**SimpleUser**](SimpleUser.md) |  | 
**private** | **bool** | Whether the repository is private or public. | [default to False]
**html_url** | **str** |  | 
**description** | **str** |  | 
**fork** | **bool** |  | 
**url** | **str** |  | 
**archive_url** | **str** |  | 
**assignees_url** | **str** |  | 
**blobs_url** | **str** |  | 
**branches_url** | **str** |  | 
**collaborators_url** | **str** |  | 
**comments_url** | **str** |  | 
**commits_url** | **str** |  | 
**compare_url** | **str** |  | 
**contents_url** | **str** |  | 
**contributors_url** | **str** |  | 
**deployments_url** | **str** |  | 
**downloads_url** | **str** |  | 
**events_url** | **str** |  | 
**forks_url** | **str** |  | 
**git_commits_url** | **str** |  | 
**git_refs_url** | **str** |  | 
**git_tags_url** | **str** |  | 
**git_url** | **str** |  | 
**issue_comment_url** | **str** |  | 
**issue_events_url** | **str** |  | 
**issues_url** | **str** |  | 
**keys_url** | **str** |  | 
**labels_url** | **str** |  | 
**languages_url** | **str** |  | 
**merges_url** | **str** |  | 
**milestones_url** | **str** |  | 
**notifications_url** | **str** |  | 
**pulls_url** | **str** |  | 
**releases_url** | **str** |  | 
**ssh_url** | **str** |  | 
**stargazers_url** | **str** |  | 
**statuses_url** | **str** |  | 
**subscribers_url** | **str** |  | 
**subscription_url** | **str** |  | 
**tags_url** | **str** |  | 
**teams_url** | **str** |  | 
**trees_url** | **str** |  | 
**clone_url** | **str** |  | 
**mirror_url** | **str** |  | 
**hooks_url** | **str** |  | 
**svn_url** | **str** |  | 
**homepage** | **str** |  | 
**language** | **str** |  | 
**forks_count** | **int** |  | 
**stargazers_count** | **int** |  | 
**watchers_count** | **int** |  | 
**size** | **int** | The size of the repository, in kilobytes. Size is calculated hourly. When a repository is initially created, the size is 0. | 
**default_branch** | **str** | The default branch of the repository. | 
**open_issues_count** | **int** |  | 
**is_template** | **bool** | Whether this repository acts as a template that can be used to generate new repositories. | [optional] [default to False]
**topics** | **List[str]** |  | [optional] 
**custom_properties** | **Dict[str, object]** | The custom properties that were defined for the repository. The keys are the custom property names, and the values are the corresponding custom property values. | [optional] 
**has_issues** | **bool** | Whether issues are enabled. | [default to True]
**has_projects** | **bool** | Whether projects are enabled. | [default to True]
**has_wiki** | **bool** | Whether the wiki is enabled. | [default to True]
**has_pages** | **bool** |  | 
**has_downloads** | **bool** | Whether downloads are enabled. | [default to True]
**has_discussions** | **bool** | Whether discussions are enabled. | [optional] [default to False]
**archived** | **bool** | Whether the repository is archived. | [default to False]
**disabled** | **bool** | Returns whether or not this repository disabled. | 
**visibility** | **str** | The repository visibility: public, private, or internal. | [optional] [default to 'public']
**pushed_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**allow_rebase_merge** | **bool** | Whether to allow rebase merges for pull requests. | [optional] [default to True]
**template_repository** | [**RepositoryWebhooksTemplateRepository**](RepositoryWebhooksTemplateRepository.md) |  | [optional] 
**temp_clone_token** | **str** |  | [optional] 
**allow_squash_merge** | **bool** | Whether to allow squash merges for pull requests. | [optional] [default to True]
**allow_auto_merge** | **bool** | Whether to allow Auto-merge to be used on pull requests. | [optional] [default to False]
**delete_branch_on_merge** | **bool** | Whether to delete head branches when pull requests are merged | [optional] [default to False]
**allow_update_branch** | **bool** | Whether or not a pull request head branch that is behind its base branch can always be updated even if it is not required to be up to date before merging. | [optional] [default to False]
**use_squash_pr_title_as_default** | **bool** | Whether a squash merge commit can use the pull request title as default. **This property is closing down. Please use &#x60;squash_merge_commit_title&#x60; instead. | [optional] [default to False]
**squash_merge_commit_title** | **str** | The default value for a squash merge commit title:  - &#x60;PR_TITLE&#x60; - default to the pull request&#39;s title. - &#x60;COMMIT_OR_PR_TITLE&#x60; - default to the commit&#39;s title (if only one commit) or the pull request&#39;s title (when more than one commit). | [optional] 
**squash_merge_commit_message** | **str** | The default value for a squash merge commit message:  - &#x60;PR_BODY&#x60; - default to the pull request&#39;s body. - &#x60;COMMIT_MESSAGES&#x60; - default to the branch&#39;s commit messages. - &#x60;BLANK&#x60; - default to a blank commit message. | [optional] 
**merge_commit_title** | **str** | The default value for a merge commit title.  - &#x60;PR_TITLE&#x60; - default to the pull request&#39;s title. - &#x60;MERGE_MESSAGE&#x60; - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name). | [optional] 
**merge_commit_message** | **str** | The default value for a merge commit message.  - &#x60;PR_TITLE&#x60; - default to the pull request&#39;s title. - &#x60;PR_BODY&#x60; - default to the pull request&#39;s body. - &#x60;BLANK&#x60; - default to a blank commit message. | [optional] 
**allow_merge_commit** | **bool** | Whether to allow merge commits for pull requests. | [optional] [default to True]
**allow_forking** | **bool** | Whether to allow forking this repo | [optional] 
**web_commit_signoff_required** | **bool** | Whether to require contributors to sign off on web-based commits | [optional] [default to False]
**subscribers_count** | **int** |  | [optional] 
**network_count** | **int** |  | [optional] 
**open_issues** | **int** |  | 
**watchers** | **int** |  | 
**master_branch** | **str** |  | [optional] 
**starred_at** | **str** |  | [optional] 
**anonymous_access_enabled** | **bool** | Whether anonymous git access is enabled for this repository | [optional] 

## Example

```python
from github_openapi.models.repository_webhooks import RepositoryWebhooks

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryWebhooks from a JSON string
repository_webhooks_instance = RepositoryWebhooks.from_json(json)
# print the JSON string representation of the object
print(RepositoryWebhooks.to_json())

# convert the object into a dict
repository_webhooks_dict = repository_webhooks_instance.to_dict()
# create an instance of RepositoryWebhooks from a dict
repository_webhooks_from_dict = RepositoryWebhooks.from_dict(repository_webhooks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


