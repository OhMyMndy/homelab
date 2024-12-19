# TeamRepository

A team's access to a repository.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the repository | 
**node_id** | **str** |  | 
**name** | **str** | The name of the repository. | 
**full_name** | **str** |  | 
**license** | [**NullableLicenseSimple**](NullableLicenseSimple.md) |  | 
**forks** | **int** |  | 
**permissions** | [**RepositoryPermissions**](RepositoryPermissions.md) |  | [optional] 
**role_name** | **str** |  | [optional] 
**owner** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
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
**size** | **int** |  | 
**default_branch** | **str** | The default branch of the repository. | 
**open_issues_count** | **int** |  | 
**is_template** | **bool** | Whether this repository acts as a template that can be used to generate new repositories. | [optional] [default to False]
**topics** | **List[str]** |  | [optional] 
**has_issues** | **bool** | Whether issues are enabled. | [default to True]
**has_projects** | **bool** | Whether projects are enabled. | [default to True]
**has_wiki** | **bool** | Whether the wiki is enabled. | [default to True]
**has_pages** | **bool** |  | 
**has_downloads** | **bool** | Whether downloads are enabled. | [default to True]
**archived** | **bool** | Whether the repository is archived. | [default to False]
**disabled** | **bool** | Returns whether or not this repository disabled. | 
**visibility** | **str** | The repository visibility: public, private, or internal. | [optional] [default to 'public']
**pushed_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**allow_rebase_merge** | **bool** | Whether to allow rebase merges for pull requests. | [optional] [default to True]
**temp_clone_token** | **str** |  | [optional] 
**allow_squash_merge** | **bool** | Whether to allow squash merges for pull requests. | [optional] [default to True]
**allow_auto_merge** | **bool** | Whether to allow Auto-merge to be used on pull requests. | [optional] [default to False]
**delete_branch_on_merge** | **bool** | Whether to delete head branches when pull requests are merged | [optional] [default to False]
**allow_merge_commit** | **bool** | Whether to allow merge commits for pull requests. | [optional] [default to True]
**allow_forking** | **bool** | Whether to allow forking this repo | [optional] [default to False]
**web_commit_signoff_required** | **bool** | Whether to require contributors to sign off on web-based commits | [optional] [default to False]
**subscribers_count** | **int** |  | [optional] 
**network_count** | **int** |  | [optional] 
**open_issues** | **int** |  | 
**watchers** | **int** |  | 
**master_branch** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.team_repository import TeamRepository

# TODO update the JSON string below
json = "{}"
# create an instance of TeamRepository from a JSON string
team_repository_instance = TeamRepository.from_json(json)
# print the JSON string representation of the object
print(TeamRepository.to_json())

# convert the object into a dict
team_repository_dict = team_repository_instance.to_dict()
# create an instance of TeamRepository from a dict
team_repository_from_dict = TeamRepository.from_dict(team_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


