# FullRepository

Full Repository

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
**default_branch** | **str** |  | 
**open_issues_count** | **int** |  | 
**is_template** | **bool** |  | [optional] 
**topics** | **List[str]** |  | [optional] 
**has_issues** | **bool** |  | 
**has_projects** | **bool** |  | 
**has_wiki** | **bool** |  | 
**has_pages** | **bool** |  | 
**has_downloads** | **bool** |  | [optional] 
**has_discussions** | **bool** |  | 
**archived** | **bool** |  | 
**disabled** | **bool** | Returns whether or not this repository disabled. | 
**visibility** | **str** | The repository visibility: public, private, or internal. | [optional] 
**pushed_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**permissions** | [**FullRepositoryPermissions**](FullRepositoryPermissions.md) |  | [optional] 
**allow_rebase_merge** | **bool** |  | [optional] 
**template_repository** | [**NullableRepository**](NullableRepository.md) |  | [optional] 
**temp_clone_token** | **str** |  | [optional] 
**allow_squash_merge** | **bool** |  | [optional] 
**allow_auto_merge** | **bool** |  | [optional] 
**delete_branch_on_merge** | **bool** |  | [optional] 
**allow_merge_commit** | **bool** |  | [optional] 
**allow_update_branch** | **bool** |  | [optional] 
**use_squash_pr_title_as_default** | **bool** |  | [optional] 
**squash_merge_commit_title** | **str** | The default value for a squash merge commit title:  - &#x60;PR_TITLE&#x60; - default to the pull request&#39;s title. - &#x60;COMMIT_OR_PR_TITLE&#x60; - default to the commit&#39;s title (if only one commit) or the pull request&#39;s title (when more than one commit). | [optional] 
**squash_merge_commit_message** | **str** | The default value for a squash merge commit message:  - &#x60;PR_BODY&#x60; - default to the pull request&#39;s body. - &#x60;COMMIT_MESSAGES&#x60; - default to the branch&#39;s commit messages. - &#x60;BLANK&#x60; - default to a blank commit message. | [optional] 
**merge_commit_title** | **str** | The default value for a merge commit title.    - &#x60;PR_TITLE&#x60; - default to the pull request&#39;s title.   - &#x60;MERGE_MESSAGE&#x60; - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name). | [optional] 
**merge_commit_message** | **str** | The default value for a merge commit message.  - &#x60;PR_TITLE&#x60; - default to the pull request&#39;s title. - &#x60;PR_BODY&#x60; - default to the pull request&#39;s body. - &#x60;BLANK&#x60; - default to a blank commit message. | [optional] 
**allow_forking** | **bool** |  | [optional] 
**web_commit_signoff_required** | **bool** |  | [optional] 
**subscribers_count** | **int** |  | 
**network_count** | **int** |  | 
**license** | [**NullableLicenseSimple**](NullableLicenseSimple.md) |  | 
**organization** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | [optional] 
**parent** | [**Repository**](Repository.md) |  | [optional] 
**source** | [**Repository**](Repository.md) |  | [optional] 
**forks** | **int** |  | 
**master_branch** | **str** |  | [optional] 
**open_issues** | **int** |  | 
**watchers** | **int** |  | 
**anonymous_access_enabled** | **bool** | Whether anonymous git access is allowed. | [optional] [default to True]
**code_of_conduct** | [**CodeOfConductSimple**](CodeOfConductSimple.md) |  | [optional] 
**security_and_analysis** | [**SecurityAndAnalysis**](SecurityAndAnalysis.md) |  | [optional] 
**custom_properties** | **Dict[str, object]** | The custom properties that were defined for the repository. The keys are the custom property names, and the values are the corresponding custom property values. | [optional] 

## Example

```python
from github_openapi.models.full_repository import FullRepository

# TODO update the JSON string below
json = "{}"
# create an instance of FullRepository from a JSON string
full_repository_instance = FullRepository.from_json(json)
# print the JSON string representation of the object
print(FullRepository.to_json())

# convert the object into a dict
full_repository_dict = full_repository_instance.to_dict()
# create an instance of FullRepository from a dict
full_repository_from_dict = FullRepository.from_dict(full_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


