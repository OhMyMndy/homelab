# PatchedLDAPProviderRequest

LDAPProvider Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**authentication_flow** | **str** | Flow used for authentication when the associated application is accessed by an un-authenticated user. | [optional] 
**authorization_flow** | **str** | Flow used when authorizing this provider. | [optional] 
**property_mappings** | **List[str]** |  | [optional] 
**base_dn** | **str** | DN under which objects are accessible. | [optional] 
**search_group** | **str** | Users in this group can do search queries. If not set, every user can execute search queries. | [optional] 
**certificate** | **str** |  | [optional] 
**tls_server_name** | **str** |  | [optional] 
**uid_start_number** | **int** | The start for uidNumbers, this number is added to the user.pk to make sure that the numbers aren&#39;t too low for POSIX users. Default is 2000 to ensure that we don&#39;t collide with local users uidNumber | [optional] 
**gid_start_number** | **int** | The start for gidNumbers, this number is added to a number generated from the group.pk to make sure that the numbers aren&#39;t too low for POSIX groups. Default is 4000 to ensure that we don&#39;t collide with local groups or users primary groups gidNumber | [optional] 
**search_mode** | [**LDAPAPIAccessMode**](LDAPAPIAccessMode.md) |  | [optional] 
**bind_mode** | [**LDAPAPIAccessMode**](LDAPAPIAccessMode.md) |  | [optional] 
**mfa_support** | **bool** | When enabled, code-based multi-factor authentication can be used by appending a semicolon and the TOTP code to the password. This should only be enabled if all users that will bind to this provider have a TOTP device configured, as otherwise a password may incorrectly be rejected if it contains a semicolon. | [optional] 

## Example

```python
from authentik_openapi.models.patched_ldap_provider_request import PatchedLDAPProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedLDAPProviderRequest from a JSON string
patched_ldap_provider_request_instance = PatchedLDAPProviderRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedLDAPProviderRequest.to_json())

# convert the object into a dict
patched_ldap_provider_request_dict = patched_ldap_provider_request_instance.to_dict()
# create an instance of PatchedLDAPProviderRequest from a dict
patched_ldap_provider_request_from_dict = PatchedLDAPProviderRequest.from_dict(patched_ldap_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


