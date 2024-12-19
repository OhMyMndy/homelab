# SAMLPropertyMapping

SAMLPropertyMapping Serializer

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
**saml_name** | **str** |  | 
**friendly_name** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.saml_property_mapping import SAMLPropertyMapping

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLPropertyMapping from a JSON string
saml_property_mapping_instance = SAMLPropertyMapping.from_json(json)
# print the JSON string representation of the object
print(SAMLPropertyMapping.to_json())

# convert the object into a dict
saml_property_mapping_dict = saml_property_mapping_instance.to_dict()
# create an instance of SAMLPropertyMapping from a dict
saml_property_mapping_from_dict = SAMLPropertyMapping.from_dict(saml_property_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


