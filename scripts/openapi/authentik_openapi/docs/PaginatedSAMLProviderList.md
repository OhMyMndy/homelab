# PaginatedSAMLProviderList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[SAMLProvider]**](SAMLProvider.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_saml_provider_list import PaginatedSAMLProviderList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSAMLProviderList from a JSON string
paginated_saml_provider_list_instance = PaginatedSAMLProviderList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSAMLProviderList.to_json())

# convert the object into a dict
paginated_saml_provider_list_dict = paginated_saml_provider_list_instance.to_dict()
# create an instance of PaginatedSAMLProviderList from a dict
paginated_saml_provider_list_from_dict = PaginatedSAMLProviderList.from_dict(paginated_saml_provider_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


