# ActionsListSelectedRepositoriesEnabledGithubActionsOrganization200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **float** |  | 
**repositories** | [**List[Repository]**](Repository.md) |  | 

## Example

```python
from github_openapi.models.actions_list_selected_repositories_enabled_github_actions_organization200_response import ActionsListSelectedRepositoriesEnabledGithubActionsOrganization200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsListSelectedRepositoriesEnabledGithubActionsOrganization200Response from a JSON string
actions_list_selected_repositories_enabled_github_actions_organization200_response_instance = ActionsListSelectedRepositoriesEnabledGithubActionsOrganization200Response.from_json(json)
# print the JSON string representation of the object
print(ActionsListSelectedRepositoriesEnabledGithubActionsOrganization200Response.to_json())

# convert the object into a dict
actions_list_selected_repositories_enabled_github_actions_organization200_response_dict = actions_list_selected_repositories_enabled_github_actions_organization200_response_instance.to_dict()
# create an instance of ActionsListSelectedRepositoriesEnabledGithubActionsOrganization200Response from a dict
actions_list_selected_repositories_enabled_github_actions_organization200_response_from_dict = ActionsListSelectedRepositoriesEnabledGithubActionsOrganization200Response.from_dict(actions_list_selected_repositories_enabled_github_actions_organization200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


