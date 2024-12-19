# PaginatedLDAPOutpostConfigList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[LDAPOutpostConfig]**](LDAPOutpostConfig.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_ldap_outpost_config_list import PaginatedLDAPOutpostConfigList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedLDAPOutpostConfigList from a JSON string
paginated_ldap_outpost_config_list_instance = PaginatedLDAPOutpostConfigList.from_json(json)
# print the JSON string representation of the object
print(PaginatedLDAPOutpostConfigList.to_json())

# convert the object into a dict
paginated_ldap_outpost_config_list_dict = paginated_ldap_outpost_config_list_instance.to_dict()
# create an instance of PaginatedLDAPOutpostConfigList from a dict
paginated_ldap_outpost_config_list_from_dict = PaginatedLDAPOutpostConfigList.from_dict(paginated_ldap_outpost_config_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


