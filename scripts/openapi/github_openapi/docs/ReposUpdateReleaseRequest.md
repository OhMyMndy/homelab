# ReposUpdateReleaseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_name** | **str** | The name of the tag. | [optional] 
**target_commitish** | **str** | Specifies the commitish value that determines where the Git tag is created from. Can be any branch or commit SHA. Unused if the Git tag already exists. Default: the repository&#39;s default branch. | [optional] 
**name** | **str** | The name of the release. | [optional] 
**body** | **str** | Text describing the contents of the tag. | [optional] 
**draft** | **bool** | &#x60;true&#x60; makes the release a draft, and &#x60;false&#x60; publishes the release. | [optional] 
**prerelease** | **bool** | &#x60;true&#x60; to identify the release as a prerelease, &#x60;false&#x60; to identify the release as a full release. | [optional] 
**make_latest** | **str** | Specifies whether this release should be set as the latest release for the repository. Drafts and prereleases cannot be set as latest. Defaults to &#x60;true&#x60; for newly published releases. &#x60;legacy&#x60; specifies that the latest release should be determined based on the release creation date and higher semantic version. | [optional] [default to 'true']
**discussion_category_name** | **str** | If specified, a discussion of the specified category is created and linked to the release. The value must be a category that already exists in the repository. If there is already a discussion linked to the release, this parameter is ignored. For more information, see \&quot;[Managing categories for discussions in your repository](https://docs.github.com/discussions/managing-discussions-for-your-community/managing-categories-for-discussions-in-your-repository).\&quot; | [optional] 

## Example

```python
from github_openapi.models.repos_update_release_request import ReposUpdateReleaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReposUpdateReleaseRequest from a JSON string
repos_update_release_request_instance = ReposUpdateReleaseRequest.from_json(json)
# print the JSON string representation of the object
print(ReposUpdateReleaseRequest.to_json())

# convert the object into a dict
repos_update_release_request_dict = repos_update_release_request_instance.to_dict()
# create an instance of ReposUpdateReleaseRequest from a dict
repos_update_release_request_from_dict = ReposUpdateReleaseRequest.from_dict(repos_update_release_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


