# CodespacesCreateForAuthenticatedUserRequestOneOf1PullRequest

Pull request number for this codespace

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pull_request_number** | **int** | Pull request number | 
**repository_id** | **int** | Repository id for this codespace | 

## Example

```python
from github_openapi.models.codespaces_create_for_authenticated_user_request_one_of1_pull_request import CodespacesCreateForAuthenticatedUserRequestOneOf1PullRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CodespacesCreateForAuthenticatedUserRequestOneOf1PullRequest from a JSON string
codespaces_create_for_authenticated_user_request_one_of1_pull_request_instance = CodespacesCreateForAuthenticatedUserRequestOneOf1PullRequest.from_json(json)
# print the JSON string representation of the object
print(CodespacesCreateForAuthenticatedUserRequestOneOf1PullRequest.to_json())

# convert the object into a dict
codespaces_create_for_authenticated_user_request_one_of1_pull_request_dict = codespaces_create_for_authenticated_user_request_one_of1_pull_request_instance.to_dict()
# create an instance of CodespacesCreateForAuthenticatedUserRequestOneOf1PullRequest from a dict
codespaces_create_for_authenticated_user_request_one_of1_pull_request_from_dict = CodespacesCreateForAuthenticatedUserRequestOneOf1PullRequest.from_dict(codespaces_create_for_authenticated_user_request_one_of1_pull_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


