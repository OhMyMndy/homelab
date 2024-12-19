# ActionsOrganizationPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled_repositories** | [**EnabledRepositories**](EnabledRepositories.md) |  | 
**selected_repositories_url** | **str** | The API URL to use to get or set the selected repositories that are allowed to run GitHub Actions, when &#x60;enabled_repositories&#x60; is set to &#x60;selected&#x60;. | [optional] 
**allowed_actions** | [**AllowedActions**](AllowedActions.md) |  | [optional] 
**selected_actions_url** | **str** | The API URL to use to get or set the actions and reusable workflows that are allowed to run, when &#x60;allowed_actions&#x60; is set to &#x60;selected&#x60;. | [optional] 

## Example

```python
from github_openapi.models.actions_organization_permissions import ActionsOrganizationPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsOrganizationPermissions from a JSON string
actions_organization_permissions_instance = ActionsOrganizationPermissions.from_json(json)
# print the JSON string representation of the object
print(ActionsOrganizationPermissions.to_json())

# convert the object into a dict
actions_organization_permissions_dict = actions_organization_permissions_instance.to_dict()
# create an instance of ActionsOrganizationPermissions from a dict
actions_organization_permissions_from_dict = ActionsOrganizationPermissions.from_dict(actions_organization_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


