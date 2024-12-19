# LDAPPropertyMapping

LDAP PropertyMapping Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**managed** | **str** | Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update. | [optional] 
**name** | **str** |  | 
**expression** | **str** |  | 
**component** | **str** | Get object&#39;s component so that we know how to edit the object | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**object_field** | **str** |  | 

## Example

```python
from authentik_openapi.models.ldap_property_mapping import LDAPPropertyMapping

# TODO update the JSON string below
json = "{}"
# create an instance of LDAPPropertyMapping from a JSON string
ldap_property_mapping_instance = LDAPPropertyMapping.from_json(json)
# print the JSON string representation of the object
print(LDAPPropertyMapping.to_json())

# convert the object into a dict
ldap_property_mapping_dict = ldap_property_mapping_instance.to_dict()
# create an instance of LDAPPropertyMapping from a dict
ldap_property_mapping_from_dict = LDAPPropertyMapping.from_dict(ldap_property_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


