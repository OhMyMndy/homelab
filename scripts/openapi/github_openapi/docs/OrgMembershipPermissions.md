# OrgMembershipPermissions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_create_repository** | **bool** |  | 

## Example

```python
from github_openapi.models.org_membership_permissions import OrgMembershipPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of OrgMembershipPermissions from a JSON string
org_membership_permissions_instance = OrgMembershipPermissions.from_json(json)
# print the JSON string representation of the object
print(OrgMembershipPermissions.to_json())

# convert the object into a dict
org_membership_permissions_dict = org_membership_permissions_instance.to_dict()
# create an instance of OrgMembershipPermissions from a dict
org_membership_permissions_from_dict = OrgMembershipPermissions.from_dict(org_membership_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


