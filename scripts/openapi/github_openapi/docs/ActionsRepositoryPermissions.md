# ActionsRepositoryPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether GitHub Actions is enabled on the repository. | 
**allowed_actions** | [**AllowedActions**](AllowedActions.md) |  | [optional] 
**selected_actions_url** | **str** | The API URL to use to get or set the actions and reusable workflows that are allowed to run, when &#x60;allowed_actions&#x60; is set to &#x60;selected&#x60;. | [optional] 

## Example

```python
from github_openapi.models.actions_repository_permissions import ActionsRepositoryPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of ActionsRepositoryPermissions from a JSON string
actions_repository_permissions_instance = ActionsRepositoryPermissions.from_json(json)
# print the JSON string representation of the object
print(ActionsRepositoryPermissions.to_json())

# convert the object into a dict
actions_repository_permissions_dict = actions_repository_permissions_instance.to_dict()
# create an instance of ActionsRepositoryPermissions from a dict
actions_repository_permissions_from_dict = ActionsRepositoryPermissions.from_dict(actions_repository_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


