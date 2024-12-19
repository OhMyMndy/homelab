# RepositoryWebhooksTemplateRepository


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**node_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**owner** | [**RepositoryWebhooksTemplateRepositoryOwner**](RepositoryWebhooksTemplateRepositoryOwner.md) |  | [optional] 
**private** | **bool** |  | [optional] 
**html_url** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**fork** | **bool** |  | [optional] 
**url** | **str** |  | [optional] 
**archive_url** | **str** |  | [optional] 
**assignees_url** | **str** |  | [optional] 
**blobs_url** | **str** |  | [optional] 
**branches_url** | **str** |  | [optional] 
**collaborators_url** | **str** |  | [optional] 
**comments_url** | **str** |  | [optional] 
**commits_url** | **str** |  | [optional] 
**compare_url** | **str** |  | [optional] 
**contents_url** | **str** |  | [optional] 
**contributors_url** | **str** |  | [optional] 
**deployments_url** | **str** |  | [optional] 
**downloads_url** | **str** |  | [optional] 
**events_url** | **str** |  | [optional] 
**forks_url** | **str** |  | [optional] 
**git_commits_url** | **str** |  | [optional] 
**git_refs_url** | **str** |  | [optional] 
**git_tags_url** | **str** |  | [optional] 
**git_url** | **str** |  | [optional] 
**issue_comment_url** | **str** |  | [optional] 
**issue_events_url** | **str** |  | [optional] 
**issues_url** | **str** |  | [optional] 
**keys_url** | **str** |  | [optional] 
**labels_url** | **str** |  | [optional] 
**languages_url** | **str** |  | [optional] 
**merges_url** | **str** |  | [optional] 
**milestones_url** | **str** |  | [optional] 
**notifications_url** | **str** |  | [optional] 
**pulls_url** | **str** |  | [optional] 
**releases_url** | **str** |  | [optional] 
**ssh_url** | **str** |  | [optional] 
**stargazers_url** | **str** |  | [optional] 
**statuses_url** | **str** |  | [optional] 
**subscribers_url** | **str** |  | [optional] 
**subscription_url** | **str** |  | [optional] 
**tags_url** | **str** |  | [optional] 
**teams_url** | **str** |  | [optional] 
**trees_url** | **str** |  | [optional] 
**clone_url** | **str** |  | [optional] 
**mirror_url** | **str** |  | [optional] 
**hooks_url** | **str** |  | [optional] 
**svn_url** | **str** |  | [optional] 
**homepage** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**forks_count** | **int** |  | [optional] 
**stargazers_count** | **int** |  | [optional] 
**watchers_count** | **int** |  | [optional] 
**size** | **int** |  | [optional] 
**default_branch** | **str** |  | [optional] 
**open_issues_count** | **int** |  | [optional] 
**is_template** | **bool** |  | [optional] 
**topics** | **List[str]** |  | [optional] 
**has_issues** | **bool** |  | [optional] 
**has_projects** | **bool** |  | [optional] 
**has_wiki** | **bool** |  | [optional] 
**has_pages** | **bool** |  | [optional] 
**has_downloads** | **bool** |  | [optional] 
**archived** | **bool** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**visibility** | **str** |  | [optional] 
**pushed_at** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**permissions** | [**MinimalRepositoryPermissions**](MinimalRepositoryPermissions.md) |  | [optional] 
**allow_rebase_merge** | **bool** |  | [optional] 
**temp_clone_token** | **str** |  | [optional] 
**allow_squash_merge** | **bool** |  | [optional] 
**allow_auto_merge** | **bool** |  | [optional] 
**delete_branch_on_merge** | **bool** |  | [optional] 
**allow_update_branch** | **bool** |  | [optional] 
**use_squash_pr_title_as_default** | **bool** |  | [optional] 
**squash_merge_commit_title** | **str** | The default value for a squash merge commit title:  - &#x60;PR_TITLE&#x60; - default to the pull request&#39;s title. - &#x60;COMMIT_OR_PR_TITLE&#x60; - default to the commit&#39;s title (if only one commit) or the pull request&#39;s title (when more than one commit). | [optional] 
**squash_merge_commit_message** | **str** | The default value for a squash merge commit message:  - &#x60;PR_BODY&#x60; - default to the pull request&#39;s body. - &#x60;COMMIT_MESSAGES&#x60; - default to the branch&#39;s commit messages. - &#x60;BLANK&#x60; - default to a blank commit message. | [optional] 
**merge_commit_title** | **str** | The default value for a merge commit title.  - &#x60;PR_TITLE&#x60; - default to the pull request&#39;s title. - &#x60;MERGE_MESSAGE&#x60; - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name). | [optional] 
**merge_commit_message** | **str** | The default value for a merge commit message.  - &#x60;PR_TITLE&#x60; - default to the pull request&#39;s title. - &#x60;PR_BODY&#x60; - default to the pull request&#39;s body. - &#x60;BLANK&#x60; - default to a blank commit message. | [optional] 
**allow_merge_commit** | **bool** |  | [optional] 
**subscribers_count** | **int** |  | [optional] 
**network_count** | **int** |  | [optional] 

## Example

```python
from github_openapi.models.repository_webhooks_template_repository import RepositoryWebhooksTemplateRepository

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryWebhooksTemplateRepository from a JSON string
repository_webhooks_template_repository_instance = RepositoryWebhooksTemplateRepository.from_json(json)
# print the JSON string representation of the object
print(RepositoryWebhooksTemplateRepository.to_json())

# convert the object into a dict
repository_webhooks_template_repository_dict = repository_webhooks_template_repository_instance.to_dict()
# create an instance of RepositoryWebhooksTemplateRepository from a dict
repository_webhooks_template_repository_from_dict = RepositoryWebhooksTemplateRepository.from_dict(repository_webhooks_template_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


