# PaginatedSAMLPropertyMappingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[SAMLPropertyMapping]**](SAMLPropertyMapping.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_saml_property_mapping_list import PaginatedSAMLPropertyMappingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSAMLPropertyMappingList from a JSON string
paginated_saml_property_mapping_list_instance = PaginatedSAMLPropertyMappingList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSAMLPropertyMappingList.to_json())

# convert the object into a dict
paginated_saml_property_mapping_list_dict = paginated_saml_property_mapping_list_instance.to_dict()
# create an instance of PaginatedSAMLPropertyMappingList from a dict
paginated_saml_property_mapping_list_from_dict = PaginatedSAMLPropertyMappingList.from_dict(paginated_saml_property_mapping_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


