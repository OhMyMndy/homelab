# OrgMembership

Org Membership

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**state** | **str** | The state of the member in the organization. The &#x60;pending&#x60; state indicates the user has not yet accepted an invitation. | 
**role** | **str** | The user&#39;s membership type in the organization. | 
**organization_url** | **str** |  | 
**organization** | [**OrganizationSimple**](OrganizationSimple.md) |  | 
**user** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 
**permissions** | [**OrgMembershipPermissions**](OrgMembershipPermissions.md) |  | [optional] 

## Example

```python
from github_openapi.models.org_membership import OrgMembership

# TODO update the JSON string below
json = "{}"
# create an instance of OrgMembership from a JSON string
org_membership_instance = OrgMembership.from_json(json)
# print the JSON string representation of the object
print(OrgMembership.to_json())

# convert the object into a dict
org_membership_dict = org_membership_instance.to_dict()
# create an instance of OrgMembership from a dict
org_membership_from_dict = OrgMembership.from_dict(org_membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


