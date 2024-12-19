# PaginatedUserSAMLSourceConnectionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[UserSAMLSourceConnection]**](UserSAMLSourceConnection.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_user_saml_source_connection_list import PaginatedUserSAMLSourceConnectionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUserSAMLSourceConnectionList from a JSON string
paginated_user_saml_source_connection_list_instance = PaginatedUserSAMLSourceConnectionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedUserSAMLSourceConnectionList.to_json())

# convert the object into a dict
paginated_user_saml_source_connection_list_dict = paginated_user_saml_source_connection_list_instance.to_dict()
# create an instance of PaginatedUserSAMLSourceConnectionList from a dict
paginated_user_saml_source_connection_list_from_dict = PaginatedUserSAMLSourceConnectionList.from_dict(paginated_user_saml_source_connection_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


