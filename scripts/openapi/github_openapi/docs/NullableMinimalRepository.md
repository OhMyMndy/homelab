# NullableMinimalRepository

Minimal Repository

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**node_id** | **str** |  | 
**name** | **str** |  | 
**full_name** | **str** |  | 
**owner** | [**SimpleUser**](SimpleUser.md) |  | 
**private** | **bool** |  | 
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
**git_url** | **str** |  | [optional] 
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
**ssh_url** | **str** |  | [optional] 
**stargazers_url** | **str** |  | 
**statuses_url** | **str** |  | 
**subscribers_url** | **str** |  | 
**subscription_url** | **str** |  | 
**tags_url** | **str** |  | 
**teams_url** | **str** |  | 
**trees_url** | **str** |  | 
**clone_url** | **str** |  | [optional] 
**mirror_url** | **str** |  | [optional] 
**hooks_url** | **str** |  | 
**svn_url** | **str** |  | [optional] 
**homepage** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**forks_count** | **int** |  | [optional] 
**stargazers_count** | **int** |  | [optional] 
**watchers_count** | **int** |  | [optional] 
**size** | **int** | The size of the repository, in kilobytes. Size is calculated hourly. When a repository is initially created, the size is 0. | [optional] 
**default_branch** | **str** |  | [optional] 
**open_issues_count** | **int** |  | [optional] 
**is_template** | **bool** |  | [optional] 
**topics** | **List[str]** |  | [optional] 
**has_issues** | **bool** |  | [optional] 
**has_projects** | **bool** |  | [optional] 
**has_wiki** | **bool** |  | [optional] 
**has_pages** | **bool** |  | [optional] 
**has_downloads** | **bool** |  | [optional] 
**has_discussions** | **bool** |  | [optional] 
**archived** | **bool** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**visibility** | **str** |  | [optional] 
**pushed_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**permissions** | [**MinimalRepositoryPermissions**](MinimalRepositoryPermissions.md) |  | [optional] 
**role_name** | **str** |  | [optional] 
**temp_clone_token** | **str** |  | [optional] 
**delete_branch_on_merge** | **bool** |  | [optional] 
**subscribers_count** | **int** |  | [optional] 
**network_count** | **int** |  | [optional] 
**code_of_conduct** | [**CodeOfConduct**](CodeOfConduct.md) |  | [optional] 
**license** | [**MinimalRepositoryLicense**](MinimalRepositoryLicense.md) |  | [optional] 
**forks** | **int** |  | [optional] 
**open_issues** | **int** |  | [optional] 
**watchers** | **int** |  | [optional] 
**allow_forking** | **bool** |  | [optional] 
**web_commit_signoff_required** | **bool** |  | [optional] 
**security_and_analysis** | [**SecurityAndAnalysis**](SecurityAndAnalysis.md) |  | [optional] 

## Example

```python
from github_openapi.models.nullable_minimal_repository import NullableMinimalRepository

# TODO update the JSON string below
json = "{}"
# create an instance of NullableMinimalRepository from a JSON string
nullable_minimal_repository_instance = NullableMinimalRepository.from_json(json)
# print the JSON string representation of the object
print(NullableMinimalRepository.to_json())

# convert the object into a dict
nullable_minimal_repository_dict = nullable_minimal_repository_instance.to_dict()
# create an instance of NullableMinimalRepository from a dict
nullable_minimal_repository_from_dict = NullableMinimalRepository.from_dict(nullable_minimal_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


