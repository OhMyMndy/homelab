# PullsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the new pull request. Required unless &#x60;issue&#x60; is specified. | [optional] 
**head** | **str** | The name of the branch where your changes are implemented. For cross-repository pull requests in the same network, namespace &#x60;head&#x60; with a user like this: &#x60;username:branch&#x60;. | 
**head_repo** | **str** | The name of the repository where the changes in the pull request were made. This field is required for cross-repository pull requests if both repositories are owned by the same organization. | [optional] 
**base** | **str** | The name of the branch you want the changes pulled into. This should be an existing branch on the current repository. You cannot submit a pull request to one repository that requests a merge to a base of another repository. | 
**body** | **str** | The contents of the pull request. | [optional] 
**maintainer_can_modify** | **bool** | Indicates whether [maintainers can modify](https://docs.github.com/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork/) the pull request. | [optional] 
**draft** | **bool** | Indicates whether the pull request is a draft. See \&quot;[Draft Pull Requests](https://docs.github.com/articles/about-pull-requests#draft-pull-requests)\&quot; in the GitHub Help documentation to learn more. | [optional] 
**issue** | **int** | An issue in the repository to convert to a pull request. The issue title, body, and comments will become the title, body, and comments on the new pull request. Required unless &#x60;title&#x60; is specified. | [optional] 

## Example

```python
from github_openapi.models.pulls_create_request import PullsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PullsCreateRequest from a JSON string
pulls_create_request_instance = PullsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(PullsCreateRequest.to_json())

# convert the object into a dict
pulls_create_request_dict = pulls_create_request_instance.to_dict()
# create an instance of PullsCreateRequest from a dict
pulls_create_request_from_dict = PullsCreateRequest.from_dict(pulls_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


