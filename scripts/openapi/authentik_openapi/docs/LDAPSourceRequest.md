# LDAPSourceRequest

LDAP Source Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Source&#39;s display Name. | 
**slug** | **str** | Internal source name, used in URLs. | 
**enabled** | **bool** |  | [optional] 
**authentication_flow** | **str** | Flow to use when authenticating existing users. | [optional] 
**enrollment_flow** | **str** | Flow to use when enrolling new users. | [optional] 
**policy_engine_mode** | [**PolicyEngineMode**](PolicyEngineMode.md) |  | [optional] 
**user_matching_mode** | [**UserMatchingModeEnum**](UserMatchingModeEnum.md) | How the source determines if an existing user should be authenticated or a new user enrolled. | [optional] 
**user_path_template** | **str** |  | [optional] 
**server_uri** | **str** |  | 
**peer_certificate** | **str** | Optionally verify the LDAP Server&#39;s Certificate against the CA Chain in this keypair. | [optional] 
**client_certificate** | **str** | Client certificate to authenticate against the LDAP Server&#39;s Certificate. | [optional] 
**bind_cn** | **str** |  | [optional] 
**bind_password** | **str** |  | [optional] 
**start_tls** | **bool** |  | [optional] 
**sni** | **bool** |  | [optional] 
**base_dn** | **str** |  | 
**additional_user_dn** | **str** | Prepended to Base DN for User-queries. | [optional] 
**additional_group_dn** | **str** | Prepended to Base DN for Group-queries. | [optional] 
**user_object_filter** | **str** | Consider Objects matching this filter to be Users. | [optional] 
**group_object_filter** | **str** | Consider Objects matching this filter to be Groups. | [optional] 
**group_membership_field** | **str** | Field which contains members of a group. | [optional] 
**object_uniqueness_field** | **str** | Field which contains a unique Identifier. | [optional] 
**password_login_update_internal_password** | **bool** | Update internal authentik password when login succeeds with LDAP | [optional] 
**sync_users** | **bool** |  | [optional] 
**sync_users_password** | **bool** | When a user changes their password, sync it back to LDAP. This can only be enabled on a single LDAP source. | [optional] 
**sync_groups** | **bool** |  | [optional] 
**sync_parent_group** | **str** |  | [optional] 
**property_mappings** | **List[str]** |  | [optional] 
**property_mappings_group** | **List[str]** | Property mappings used for group creation/updating. | [optional] 

## Example

```python
from authentik_openapi.models.ldap_source_request import LDAPSourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LDAPSourceRequest from a JSON string
ldap_source_request_instance = LDAPSourceRequest.from_json(json)
# print the JSON string representation of the object
print(LDAPSourceRequest.to_json())

# convert the object into a dict
ldap_source_request_dict = ldap_source_request_instance.to_dict()
# create an instance of LDAPSourceRequest from a dict
ldap_source_request_from_dict = LDAPSourceRequest.from_dict(ldap_source_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


