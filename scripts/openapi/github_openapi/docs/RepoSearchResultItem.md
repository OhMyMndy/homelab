# RepoSearchResultItem

Repo Search Result Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**node_id** | **str** |  | 
**name** | **str** |  | 
**full_name** | **str** |  | 
**owner** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**private** | **bool** |  | 
**html_url** | **str** |  | 
**description** | **str** |  | 
**fork** | **bool** |  | 
**url** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**pushed_at** | **datetime** |  | 
**homepage** | **str** |  | 
**size** | **int** |  | 
**stargazers_count** | **int** |  | 
**watchers_count** | **int** |  | 
**language** | **str** |  | 
**forks_count** | **int** |  | 
**open_issues_count** | **int** |  | 
**master_branch** | **str** |  | [optional] 
**default_branch** | **str** |  | 
**score** | **float** |  | 
**forks_url** | **str** |  | 
**keys_url** | **str** |  | 
**collaborators_url** | **str** |  | 
**teams_url** | **str** |  | 
**hooks_url** | **str** |  | 
**issue_events_url** | **str** |  | 
**events_url** | **str** |  | 
**assignees_url** | **str** |  | 
**branches_url** | **str** |  | 
**tags_url** | **str** |  | 
**blobs_url** | **str** |  | 
**git_tags_url** | **str** |  | 
**git_refs_url** | **str** |  | 
**trees_url** | **str** |  | 
**statuses_url** | **str** |  | 
**languages_url** | **str** |  | 
**stargazers_url** | **str** |  | 
**contributors_url** | **str** |  | 
**subscribers_url** | **str** |  | 
**subscription_url** | **str** |  | 
**commits_url** | **str** |  | 
**git_commits_url** | **str** |  | 
**comments_url** | **str** |  | 
**issue_comment_url** | **str** |  | 
**contents_url** | **str** |  | 
**compare_url** | **str** |  | 
**merges_url** | **str** |  | 
**archive_url** | **str** |  | 
**downloads_url** | **str** |  | 
**issues_url** | **str** |  | 
**pulls_url** | **str** |  | 
**milestones_url** | **str** |  | 
**notifications_url** | **str** |  | 
**labels_url** | **str** |  | 
**releases_url** | **str** |  | 
**deployments_url** | **str** |  | 
**git_url** | **str** |  | 
**ssh_url** | **str** |  | 
**clone_url** | **str** |  | 
**svn_url** | **str** |  | 
**forks** | **int** |  | 
**open_issues** | **int** |  | 
**watchers** | **int** |  | 
**topics** | **List[str]** |  | [optional] 
**mirror_url** | **str** |  | 
**has_issues** | **bool** |  | 
**has_projects** | **bool** |  | 
**has_pages** | **bool** |  | 
**has_wiki** | **bool** |  | 
**has_downloads** | **bool** |  | 
**has_discussions** | **bool** |  | [optional] 
**archived** | **bool** |  | 
**disabled** | **bool** | Returns whether or not this repository disabled. | 
**visibility** | **str** | The repository visibility: public, private, or internal. | [optional] 
**license** | [**NullableLicenseSimple**](NullableLicenseSimple.md) |  | 
**permissions** | [**FullRepositoryPermissions**](FullRepositoryPermissions.md) |  | [optional] 
**text_matches** | [**List[SearchResultTextMatchesInner]**](SearchResultTextMatchesInner.md) |  | [optional] 
**temp_clone_token** | **str** |  | [optional] 
**allow_merge_commit** | **bool** |  | [optional] 
**allow_squash_merge** | **bool** |  | [optional] 
**allow_rebase_merge** | **bool** |  | [optional] 
**allow_auto_merge** | **bool** |  | [optional] 
**delete_branch_on_merge** | **bool** |  | [optional] 
**allow_forking** | **bool** |  | [optional] 
**is_template** | **bool** |  | [optional] 
**web_commit_signoff_required** | **bool** |  | [optional] 

## Example

```python
from github_openapi.models.repo_search_result_item import RepoSearchResultItem

# TODO update the JSON string below
json = "{}"
# create an instance of RepoSearchResultItem from a JSON string
repo_search_result_item_instance = RepoSearchResultItem.from_json(json)
# print the JSON string representation of the object
print(RepoSearchResultItem.to_json())

# convert the object into a dict
repo_search_result_item_dict = repo_search_result_item_instance.to_dict()
# create an instance of RepoSearchResultItem from a dict
repo_search_result_item_from_dict = RepoSearchResultItem.from_dict(repo_search_result_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


