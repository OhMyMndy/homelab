# WebhookForkForkee

The created [`repository`](https://docs.github.com/rest/repos/repos#get-a-repository) resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_auto_merge** | **bool** | Whether to allow auto-merge for pull requests. | [optional] [default to False]
**allow_forking** | **bool** |  | [optional] 
**allow_merge_commit** | **bool** | Whether to allow merge commits for pull requests. | [optional] [default to True]
**allow_rebase_merge** | **bool** | Whether to allow rebase merges for pull requests. | [optional] [default to True]
**allow_squash_merge** | **bool** | Whether to allow squash merges for pull requests. | [optional] [default to True]
**allow_update_branch** | **bool** |  | [optional] 
**archive_url** | **str** |  | 
**archived** | **bool** |  | 
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
**created_at** | **str** |  | 
**default_branch** | **str** |  | 
**delete_branch_on_merge** | **bool** | Whether to delete head branches when pull requests are merged | [optional] [default to False]
**deployments_url** | **str** |  | 
**description** | **str** |  | 
**disabled** | **bool** |  | [optional] 
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
**has_downloads** | **bool** |  | 
**has_issues** | **bool** |  | 
**has_pages** | **bool** |  | 
**has_projects** | **bool** |  | 
**has_wiki** | **bool** |  | 
**homepage** | **str** |  | 
**hooks_url** | **str** |  | 
**html_url** | **str** |  | 
**id** | **int** |  | 
**is_template** | **bool** |  | [optional] 
**issue_comment_url** | **str** |  | 
**issue_events_url** | **str** |  | 
**issues_url** | **str** |  | 
**keys_url** | **str** |  | 
**labels_url** | **str** |  | 
**language** | **object** |  | 
**languages_url** | **str** |  | 
**license** | **object** |  | 
**master_branch** | **str** |  | [optional] 
**merges_url** | **str** |  | 
**milestones_url** | **str** |  | 
**mirror_url** | **object** |  | 
**name** | **str** |  | 
**node_id** | **str** |  | 
**notifications_url** | **str** |  | 
**open_issues** | **int** |  | 
**open_issues_count** | **int** |  | 
**organization** | **str** |  | [optional] 
**owner** | [**DeploymentWorkflowRunHeadRepositoryOwner**](DeploymentWorkflowRunHeadRepositoryOwner.md) |  | 
**permissions** | [**RepositoryPermissions**](RepositoryPermissions.md) |  | [optional] 
**private** | **bool** |  | 
**public** | **bool** |  | [optional] 
**pulls_url** | **str** |  | 
**pushed_at** | **str** |  | 
**releases_url** | **str** |  | 
**role_name** | **str** |  | [optional] 
**size** | **int** |  | 
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
**topics** | **List[Optional[object]]** |  | 
**trees_url** | **str** |  | 
**updated_at** | **str** |  | 
**url** | **str** |  | 
**visibility** | **str** |  | 
**watchers** | **int** |  | 
**watchers_count** | **int** |  | 
**web_commit_signoff_required** | **bool** | Whether to require contributors to sign off on web-based commits | [optional] 

## Example

```python
from github_openapi.models.webhook_fork_forkee import WebhookForkForkee

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookForkForkee from a JSON string
webhook_fork_forkee_instance = WebhookForkForkee.from_json(json)
# print the JSON string representation of the object
print(WebhookForkForkee.to_json())

# convert the object into a dict
webhook_fork_forkee_dict = webhook_fork_forkee_instance.to_dict()
# create an instance of WebhookForkForkee from a dict
webhook_fork_forkee_from_dict = WebhookForkForkee.from_dict(webhook_fork_forkee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


