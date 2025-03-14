# Repository2

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
**custom_properties** | **Dict[str, object]** | The custom properties that were defined for the repository. The keys are the custom property names, and the values are the corresponding custom property values. | [optional] 
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
**has_discussions** | **bool** | Whether discussions are enabled. | [default to False]
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
**visibility** | **str** |  | 
**watchers** | **int** |  | 
**watchers_count** | **int** |  | 
**web_commit_signoff_required** | **bool** | Whether to require contributors to sign off on web-based commits | [optional] 

## Example

```python
from github_openapi.models.repository2 import Repository2

# TODO update the JSON string below
json = "{}"
# create an instance of Repository2 from a JSON string
repository2_instance = Repository2.from_json(json)
# print the JSON string representation of the object
print(Repository2.to_json())

# convert the object into a dict
repository2_dict = repository2_instance.to_dict()
# create an instance of Repository2 from a dict
repository2_from_dict = Repository2.from_dict(repository2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


