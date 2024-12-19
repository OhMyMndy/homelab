# Repository7

A git repository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_auto_merge** | **bool** | Whether to allow auto-merge for pull requests. | [optional] [default to False]
**allow_forking** | **bool** | Whether to allow private forks | [optional] 
**allow_merge_commit** | **bool** | Whether to allow merge commits for pull requests. | [optional] [default to True]
**allow_rebase_merge** | **bool** | Whether to allow rebase merges for pull requests. | [optional] [default to True]
**allow_squash_merge** | **bool** | Whether to allow squash merges for pull requests. | [optional] [default to True]
**allow_update_branch** | **bool** |  | [optional] 
**archive_url** | **str** |  | 
**archived** | **bool** | Whether the repository is archived. | [default to False]
**assignees_url** | **str** |  | 
**blobs_url** | **str** |  | 
**branches_url** | **str** |  | 
**clone_url** | **str** |  | 
**collaborators_url** | **str** |  | 
**comments_url** | **str** |  | 
**commits_url** | **str** |  | 
**compare_url** | **str** |  | 
**contents_url** | **str** |  | 
**contributors_url** | **str** |  | 
**created_at** | [**RepositoryCreatedAt**](RepositoryCreatedAt.md) |  | 
**default_branch** | **str** | The default branch of the repository. | 
**delete_branch_on_merge** | **bool** | Whether to delete head branches when pull requests are merged | [optional] [default to False]
**deployments_url** | **str** |  | 
**description** | **str** |  | 
**disabled** | **bool** | Returns whether or not this repository is disabled. | [optional] 
**downloads_url** | **str** |  | 
**events_url** | **str** |  | 
**fork** | **bool** |  | 
**forks** | **int** |  | 
**forks_count** | **int** |  | 
**forks_url** | **str** |  | 
**full_name** | **str** |  | 
**git_commits_url** | **str** |  | 
**git_refs_url** | **str** |  | 
**git_tags_url** | **str** |  | 
**git_url** | **str** |  | 
**has_downloads** | **bool** | Whether downloads are enabled. | [default to True]
**has_issues** | **bool** | Whether issues are enabled. | [default to True]
**has_pages** | **bool** |  | 
**has_projects** | **bool** | Whether projects are enabled. | [default to True]
**has_wiki** | **bool** | Whether the wiki is enabled. | [default to True]
**has_discussions** | **bool** | Whether discussions are enabled. | [optional] [default to False]
**homepage** | **str** |  | 
**hooks_url** | **str** |  | 
**html_url** | **str** |  | 
**id** | **int** | Unique identifier of the repository | 
**is_template** | **bool** |  | [optional] 
**issue_comment_url** | **str** |  | 
**issue_events_url** | **str** |  | 
**issues_url** | **str** |  | 
**keys_url** | **str** |  | 
**labels_url** | **str** |  | 
**language** | **str** |  | 
**languages_url** | **str** |  | 
**license** | [**License**](License.md) |  | 
**master_branch** | **str** |  | [optional] 
**merge_commit_message** | **str** | The default value for a merge commit message.  - &#x60;PR_TITLE&#x60; - default to the pull request&#39;s title. - &#x60;PR_BODY&#x60; - default to the pull request&#39;s body. - &#x60;BLANK&#x60; - default to a blank commit message. | [optional] 
**merge_commit_title** | **str** | The default value for a merge commit title.  - &#x60;PR_TITLE&#x60; - default to the pull request&#39;s title. - &#x60;MERGE_MESSAGE&#x60; - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name). | [optional] 
**merges_url** | **str** |  | 
**milestones_url** | **str** |  | 
**mirror_url** | **str** |  | 
**name** | **str** | The name of the repository. | 
**node_id** | **str** |  | 
**notifications_url** | **str** |  | 
**open_issues** | **int** |  | 
**open_issues_count** | **int** |  | 
**organization** | **str** |  | [optional] 
**owner** | [**User2**](User2.md) |  | 
**permissions** | [**RepositoryPermissions**](RepositoryPermissions.md) |  | [optional] 
**private** | **bool** | Whether the repository is private or public. | 
**public** | **bool** |  | [optional] 
**pulls_url** | **str** |  | 
**pushed_at** | [**RepositoryPushedAt**](RepositoryPushedAt.md) |  | 
**releases_url** | **str** |  | 
**role_name** | **str** |  | [optional] 
**size** | **int** |  | 
**squash_merge_commit_message** | **str** | The default value for a squash merge commit message:  - &#x60;PR_BODY&#x60; - default to the pull request&#39;s body. - &#x60;COMMIT_MESSAGES&#x60; - default to the branch&#39;s commit messages. - &#x60;BLANK&#x60; - default to a blank commit message. | [optional] 
**squash_merge_commit_title** | **str** | The default value for a squash merge commit title:  - &#x60;PR_TITLE&#x60; - default to the pull request&#39;s title. - &#x60;COMMIT_OR_PR_TITLE&#x60; - default to the commit&#39;s title (if only one commit) or the pull request&#39;s title (when more than one commit). | [optional] 
**ssh_url** | **str** |  | 
**stargazers** | **int** |  | [optional] 
**stargazers_count** | **int** |  | 
**stargazers_url** | **str** |  | 
**statuses_url** | **str** |  | 
**subscribers_url** | **str** |  | 
**subscription_url** | **str** |  | 
**svn_url** | **str** |  | 
**tags_url** | **str** |  | 
**teams_url** | **str** |  | 
**topics** | **List[str]** |  | 
**trees_url** | **str** |  | 
**updated_at** | **datetime** |  | 
**url** | **str** |  | 
**use_squash_pr_title_as_default** | **bool** | Whether a squash merge commit can use the pull request title as default. **This property is closing down. Please use &#x60;squash_merge_commit_title&#x60; instead. | [optional] [default to False]
**visibility** | **str** |  | 
**watchers** | **int** |  | 
**watchers_count** | **int** |  | 
**web_commit_signoff_required** | **bool** | Whether to require contributors to sign off on web-based commits | [optional] 

## Example

```python
from github_openapi.models.repository7 import Repository7

# TODO update the JSON string below
json = "{}"
# create an instance of Repository7 from a JSON string
repository7_instance = Repository7.from_json(json)
# print the JSON string representation of the object
print(Repository7.to_json())

# convert the object into a dict
repository7_dict = repository7_instance.to_dict()
# create an instance of Repository7 from a dict
repository7_from_dict = Repository7.from_dict(repository7_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


