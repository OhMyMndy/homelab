# ActionsSetGithubActionsPermissionsOrganizationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled_repositories** | [**EnabledRepositories**](EnabledRepositories.md) |  | 
**allowed_actions** | [**AllowedActions**](AllowedActions.md) |  | [optional] 

## Example

```python
from github_openapi.models.actions_set_github_actions_permissions_organization_request import ActionsSetGithubActionsPermissionsOrganizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsSetGithubActionsPermissionsOrganizationRequest from a JSON string
actions_set_github_actions_permissions_organization_request_instance = ActionsSetGithubActionsPermissionsOrganizationRequest.from_json(json)
# print the JSON string representation of the object
print(ActionsSetGithubActionsPermissionsOrganizationRequest.to_json())

# convert the object into a dict
actions_set_github_actions_permissions_organization_request_dict = actions_set_github_actions_permissions_organization_request_instance.to_dict()
# create an instance of ActionsSetGithubActionsPermissionsOrganizationRequest from a dict
actions_set_github_actions_permissions_organization_request_from_dict = ActionsSetGithubActionsPermissionsOrganizationRequest.from_dict(actions_set_github_actions_permissions_organization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


