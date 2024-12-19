# PaginatedLDAPSourceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[LDAPSource]**](LDAPSource.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_ldap_source_list import PaginatedLDAPSourceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedLDAPSourceList from a JSON string
paginated_ldap_source_list_instance = PaginatedLDAPSourceList.from_json(json)
# print the JSON string representation of the object
print(PaginatedLDAPSourceList.to_json())

# convert the object into a dict
paginated_ldap_source_list_dict = paginated_ldap_source_list_instance.to_dict()
# create an instance of PaginatedLDAPSourceList from a dict
paginated_ldap_source_list_from_dict = PaginatedLDAPSourceList.from_dict(paginated_ldap_source_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


