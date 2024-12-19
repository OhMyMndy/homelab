# ReposCreateInOrgRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the repository. | 
**description** | **str** | A short description of the repository. | [optional] 
**homepage** | **str** | A URL with more information about the repository. | [optional] 
**private** | **bool** | Whether the repository is private. | [optional] [default to False]
**visibility** | **str** | The visibility of the repository. | [optional] 
**has_issues** | **bool** | Either &#x60;true&#x60; to enable issues for this repository or &#x60;false&#x60; to disable them. | [optional] [default to True]
**has_projects** | **bool** | Either &#x60;true&#x60; to enable projects for this repository or &#x60;false&#x60; to disable them. **Note:** If you&#39;re creating a repository in an organization that has disabled repository projects, the default is &#x60;false&#x60;, and if you pass &#x60;true&#x60;, the API returns an error. | [optional] [default to True]
**has_wiki** | **bool** | Either &#x60;true&#x60; to enable the wiki for this repository or &#x60;false&#x60; to disable it. | [optional] [default to True]
**has_downloads** | **bool** | Whether downloads are enabled. | [optional] [default to True]
**is_template** | **bool** | Either &#x60;true&#x60; to make this repo available as a template repository or &#x60;false&#x60; to prevent it. | [optional] [default to False]
**team_id** | **int** | The id of the team that will be granted access to this repository. This is only valid when creating a repository in an organization. | [optional] 
**auto_init** | **bool** | Pass &#x60;true&#x60; to create an initial commit with empty README. | [optional] [default to False]
**gitignore_template** | **str** | Desired language or platform [.gitignore template](https://github.com/github/gitignore) to apply. Use the name of the template without the extension. For example, \&quot;Haskell\&quot;. | [optional] 
**license_template** | **str** | Choose an [open source license template](https://choosealicense.com/) that best suits your needs, and then use the [license keyword](https://docs.github.com/articles/licensing-a-repository/#searching-github-by-license-type) as the &#x60;license_template&#x60; string. For example, \&quot;mit\&quot; or \&quot;mpl-2.0\&quot;. | [optional] 
**allow_squash_merge** | **bool** | Either &#x60;true&#x60; to allow squash-merging pull requests, or &#x60;false&#x60; to prevent squash-merging. | [optional] [default to True]
**allow_merge_commit** | **bool** | Either &#x60;true&#x60; to allow merging pull requests with a merge commit, or &#x60;false&#x60; to prevent merging pull requests with merge commits. | [optional] [default to True]
**allow_rebase_merge** | **bool** | Either &#x60;true&#x60; to allow rebase-merging pull requests, or &#x60;false&#x60; to prevent rebase-merging. | [optional] [default to True]
**allow_auto_merge** | **bool** | Either &#x60;true&#x60; to allow auto-merge on pull requests, or &#x60;false&#x60; to disallow auto-merge. | [optional] [default to False]
**delete_branch_on_merge** | **bool** | Either &#x60;true&#x60; to allow automatically deleting head branches when pull requests are merged, or &#x60;false&#x60; to prevent automatic deletion. **The authenticated user must be an organization owner to set this property to &#x60;true&#x60;.** | [optional] [default to False]
**use_squash_pr_title_as_default** | **bool** | Either &#x60;true&#x60; to allow squash-merge commits to use pull request title, or &#x60;false&#x60; to use commit message. **This property is closing down. Please use &#x60;squash_merge_commit_title&#x60; instead. | [optional] [default to False]
**squash_merge_commit_title** | **str** | Required when using &#x60;squash_merge_commit_message&#x60;.  The default value for a squash merge commit title:  - &#x60;PR_TITLE&#x60; - default to the pull request&#39;s title. - &#x60;COMMIT_OR_PR_TITLE&#x60; - default to the commit&#39;s title (if only one commit) or the pull request&#39;s title (when more than one commit). | [optional] 
**squash_merge_commit_message** | **str** | The default value for a squash merge commit message:  - &#x60;PR_BODY&#x60; - default to the pull request&#39;s body. - &#x60;COMMIT_MESSAGES&#x60; - default to the branch&#39;s commit messages. - &#x60;BLANK&#x60; - default to a blank commit message. | [optional] 
**merge_commit_title** | **str** | Required when using &#x60;merge_commit_message&#x60;.  The default value for a merge commit title.  - &#x60;PR_TITLE&#x60; - default to the pull request&#39;s title. - &#x60;MERGE_MESSAGE&#x60; - default to the classic title for a merge message (e.g., Merge pull request #123 from branch-name). | [optional] 
**merge_commit_message** | **str** | The default value for a merge commit message.  - &#x60;PR_TITLE&#x60; - default to the pull request&#39;s title. - &#x60;PR_BODY&#x60; - default to the pull request&#39;s body. - &#x60;BLANK&#x60; - default to a blank commit message. | [optional] 
**custom_properties** | **Dict[str, object]** | The custom properties for the new repository. The keys are the custom property names, and the values are the corresponding custom property values. | [optional] 

## Example

```python
from github_openapi.models.repos_create_in_org_request import ReposCreateInOrgRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposCreateInOrgRequest from a JSON string
repos_create_in_org_request_instance = ReposCreateInOrgRequest.from_json(json)
# print the JSON string representation of the object
print(ReposCreateInOrgRequest.to_json())

# convert the object into a dict
repos_create_in_org_request_dict = repos_create_in_org_request_instance.to_dict()
# create an instance of ReposCreateInOrgRequest from a dict
repos_create_in_org_request_from_dict = ReposCreateInOrgRequest.from_dict(repos_create_in_org_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


