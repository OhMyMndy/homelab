# LDAPPropertyMappingRequest

LDAP PropertyMapping Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**managed** | **str** | Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update. | [optional] 
**name** | **str** |  | 
**expression** | **str** |  | 
**object_field** | **str** |  | 

## Example

```python
from authentik_openapi.models.ldap_property_mapping_request import LDAPPropertyMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LDAPPropertyMappingRequest from a JSON string
ldap_property_mapping_request_instance = LDAPPropertyMappingRequest.from_json(json)
# print the JSON string representation of the object
print(LDAPPropertyMappingRequest.to_json())

# convert the object into a dict
ldap_property_mapping_request_dict = ldap_property_mapping_request_instance.to_dict()
# create an instance of LDAPPropertyMappingRequest from a dict
ldap_property_mapping_request_from_dict = LDAPPropertyMappingRequest.from_dict(ldap_property_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


