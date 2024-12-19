# PaginatedLDAPProviderList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[LDAPProvider]**](LDAPProvider.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_ldap_provider_list import PaginatedLDAPProviderList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedLDAPProviderList from a JSON string
paginated_ldap_provider_list_instance = PaginatedLDAPProviderList.from_json(json)
# print the JSON string representation of the object
print(PaginatedLDAPProviderList.to_json())

# convert the object into a dict
paginated_ldap_provider_list_dict = paginated_ldap_provider_list_instance.to_dict()
# create an instance of PaginatedLDAPProviderList from a dict
paginated_ldap_provider_list_from_dict = PaginatedLDAPProviderList.from_dict(paginated_ldap_provider_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


