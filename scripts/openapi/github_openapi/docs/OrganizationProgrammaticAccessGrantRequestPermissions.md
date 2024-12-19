# OrganizationProgrammaticAccessGrantRequestPermissions

Permissions requested, categorized by type of permission.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization** | **Dict[str, str]** |  | [optional] 
**repository** | **Dict[str, str]** |  | [optional] 
**other** | **Dict[str, str]** |  | [optional] 

## Example

```python
from github_openapi.models.organization_programmatic_access_grant_request_permissions import OrganizationProgrammaticAccessGrantRequestPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationProgrammaticAccessGrantRequestPermissions from a JSON string
organization_programmatic_access_grant_request_permissions_instance = OrganizationProgrammaticAccessGrantRequestPermissions.from_json(json)
# print the JSON string representation of the object
print(OrganizationProgrammaticAccessGrantRequestPermissions.to_json())

# convert the object into a dict
organization_programmatic_access_grant_request_permissions_dict = organization_programmatic_access_grant_request_permissions_instance.to_dict()
# create an instance of OrganizationProgrammaticAccessGrantRequestPermissions from a dict
organization_programmatic_access_grant_request_permissions_from_dict = OrganizationProgrammaticAccessGrantRequestPermissions.from_dict(organization_programmatic_access_grant_request_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


