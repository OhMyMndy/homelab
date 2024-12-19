# ReposCreateForAuthenticatedUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the repository. | 
**description** | **str** | A short description of the repository. | [optional] 
**homepage** | **str** | A URL with more information about the repository. | [optional] 
**private** | **bool** | Whether the repository is private. | [optional] [default to False]
**has_issues** | **bool** | Whether issues are enabled. | [optional] [default to True]
**has_projects** | **bool** | Whether projects are enabled. | [optional] [default to True]
**has_wiki** | **bool** | Whether the wiki is enabled. | [optional] [default to True]
**has_discussions** | **bool** | Whether discussions are enabled. | [optional] [default to False]
**team_id** | **int** | The id of the team that will be granted access to this repository. This is only valid when creating a repository in an organization. | [optional] 
**auto_init** | **bool** | Whether the repository is initialized with a minimal README. | [optional] [default to False]
**gitignore_template** | **str** | The desired language or platform to apply to the .gitignore. | [optional] 
**license_template** | **str** | The license keyword of the open source license for this repository. | [optional] 
**allow_squash_merge** | **bool** | Whether to allow squash merges for pull requests. | [optional] [default to True]
**allow_merge_commit** | **bool** | Whether to allow merge commits for pull requests. | [optional] [default to True]
**allow_rebase_merge** | **bool** | Whether to allow rebase merges for pull requests. | [optional] [default to True]
**allow_auto_merge** | **bool** | Whether to allow Auto-merge to be used on pull requests. | [optional] [default to False]
**delete_branch_on_merge** | **bool** | Whether to delete head branches when pull requests are merged | [optional] [default to False]
**squash_merge_commit_title** | **str** | Required when using &#x60;squash_merge_commit_message&#x60;.  The default value for a squash merge commit title:  - &#x60;PR_TITLE&#x60; - default to the pull request&#39;s title. - &#x60;COMMIT_OR_PR_TITLE&#x60; - default to the commit&#39;s title (if only one commit) or the pull request&#39;s title (when more than one commit). | [optional] 
**squash_merge_commit_message** | **str** | The default value for a squash merge commit message:  - &#x60;PR_BODY&#x60; - default to the pull request&#39;s body. - &#x60;COMMIT_MESSAGES&#x60; - default to the branch&#39;s commit messages. - &#x60;BLANK&#x60; - default to a blank commit message. | [optional] 
**merge_commit_title** | **str** | Required when using &#x60;merge_commit_message&#x60;.  The default value for a merge commit title.  - &#x60;PR_TITLE&#x60; - default to the pull request&#39;s title. - &#x60;MERGE_MESSAGE&#x60; - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name). | [optional] 
**merge_commit_message** | **str** | The default value for a merge commit message.  - &#x60;PR_TITLE&#x60; - default to the pull request&#39;s title. - &#x60;PR_BODY&#x60; - default to the pull request&#39;s body. - &#x60;BLANK&#x60; - default to a blank commit message. | [optional] 
**has_downloads** | **bool** | Whether downloads are enabled. | [optional] [default to True]
**is_template** | **bool** | Whether this repository acts as a template that can be used to generate new repositories. | [optional] [default to False]

## Example

```python
from github_openapi.models.repos_create_for_authenticated_user_request import ReposCreateForAuthenticatedUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposCreateForAuthenticatedUserRequest from a JSON string
repos_create_for_authenticated_user_request_instance = ReposCreateForAuthenticatedUserRequest.from_json(json)
# print the JSON string representation of the object
print(ReposCreateForAuthenticatedUserRequest.to_json())

# convert the object into a dict
repos_create_for_authenticated_user_request_dict = repos_create_for_authenticated_user_request_instance.to_dict()
# create an instance of ReposCreateForAuthenticatedUserRequest from a dict
repos_create_for_authenticated_user_request_from_dict = ReposCreateForAuthenticatedUserRequest.from_dict(repos_create_for_authenticated_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


