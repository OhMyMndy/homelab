# ActionsSetSelectedRepositoriesEnabledGithubActionsOrganizationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_repository_ids** | **List[int]** | List of repository IDs to enable for GitHub Actions. | 

## Example

```python
from github_openapi.models.actions_set_selected_repositories_enabled_github_actions_organization_request import ActionsSetSelectedRepositoriesEnabledGithubActionsOrganizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsSetSelectedRepositoriesEnabledGithubActionsOrganizationRequest from a JSON string
actions_set_selected_repositories_enabled_github_actions_organization_request_instance = ActionsSetSelectedRepositoriesEnabledGithubActionsOrganizationRequest.from_json(json)
# print the JSON string representation of the object
print(ActionsSetSelectedRepositoriesEnabledGithubActionsOrganizationRequest.to_json())

# convert the object into a dict
actions_set_selected_repositories_enabled_github_actions_organization_request_dict = actions_set_selected_repositories_enabled_github_actions_organization_request_instance.to_dict()
# create an instance of ActionsSetSelectedRepositoriesEnabledGithubActionsOrganizationRequest from a dict
actions_set_selected_repositories_enabled_github_actions_organization_request_from_dict = ActionsSetSelectedRepositoriesEnabledGithubActionsOrganizationRequest.from_dict(actions_set_selected_repositories_enabled_github_actions_organization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


