# ActionsSetGithubActionsPermissionsRepositoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether GitHub Actions is enabled on the repository. | 
**allowed_actions** | [**AllowedActions**](AllowedActions.md) |  | [optional] 

## Example

```python
from github_openapi.models.actions_set_github_actions_permissions_repository_request import ActionsSetGithubActionsPermissionsRepositoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsSetGithubActionsPermissionsRepositoryRequest from a JSON string
actions_set_github_actions_permissions_repository_request_instance = ActionsSetGithubActionsPermissionsRepositoryRequest.from_json(json)
# print the JSON string representation of the object
print(ActionsSetGithubActionsPermissionsRepositoryRequest.to_json())

# convert the object into a dict
actions_set_github_actions_permissions_repository_request_dict = actions_set_github_actions_permissions_repository_request_instance.to_dict()
# create an instance of ActionsSetGithubActionsPermissionsRepositoryRequest from a dict
actions_set_github_actions_permissions_repository_request_from_dict = ActionsSetGithubActionsPermissionsRepositoryRequest.from_dict(actions_set_github_actions_permissions_repository_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


