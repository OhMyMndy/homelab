# CodespacesPermissionsCheckForDevcontainer

Permission check result for a given devcontainer config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted** | **bool** | Whether the user has accepted the permissions defined by the devcontainer config | 

## Example

```python
from github_openapi.models.codespaces_permissions_check_for_devcontainer import CodespacesPermissionsCheckForDevcontainer

# TODO update the JSON string below
json = "{}"
# create an instance of CodespacesPermissionsCheckForDevcontainer from a JSON string
codespaces_permissions_check_for_devcontainer_instance = CodespacesPermissionsCheckForDevcontainer.from_json(json)
# print the JSON string representation of the object
print(CodespacesPermissionsCheckForDevcontainer.to_json())

# convert the object into a dict
codespaces_permissions_check_for_devcontainer_dict = codespaces_permissions_check_for_devcontainer_instance.to_dict()
# create an instance of CodespacesPermissionsCheckForDevcontainer from a dict
codespaces_permissions_check_for_devcontainer_from_dict = CodespacesPermissionsCheckForDevcontainer.from_dict(codespaces_permissions_check_for_devcontainer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


