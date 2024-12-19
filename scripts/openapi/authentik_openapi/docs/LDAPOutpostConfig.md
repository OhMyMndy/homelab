# LDAPOutpostConfig

LDAPProvider Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**name** | **str** |  | 
**base_dn** | **str** | DN under which objects are accessible. | [optional] 
**bind_flow_slug** | **str** |  | 
**application_slug** | **str** | Prioritise backchannel slug over direct application slug | [readonly] 
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
from authentik_openapi.models.ldap_outpost_config import LDAPOutpostConfig

# TODO update the JSON string below
json = "{}"
# create an instance of LDAPOutpostConfig from a JSON string
ldap_outpost_config_instance = LDAPOutpostConfig.from_json(json)
# print the JSON string representation of the object
print(LDAPOutpostConfig.to_json())

# convert the object into a dict
ldap_outpost_config_dict = ldap_outpost_config_instance.to_dict()
# create an instance of LDAPOutpostConfig from a dict
ldap_outpost_config_from_dict = LDAPOutpostConfig.from_dict(ldap_outpost_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


