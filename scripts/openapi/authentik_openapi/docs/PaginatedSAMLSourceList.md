# PaginatedSAMLSourceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[SAMLSource]**](SAMLSource.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_saml_source_list import PaginatedSAMLSourceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSAMLSourceList from a JSON string
paginated_saml_source_list_instance = PaginatedSAMLSourceList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSAMLSourceList.to_json())

# convert the object into a dict
paginated_saml_source_list_dict = paginated_saml_source_list_instance.to_dict()
# create an instance of PaginatedSAMLSourceList from a dict
paginated_saml_source_list_from_dict = PaginatedSAMLSourceList.from_dict(paginated_saml_source_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


