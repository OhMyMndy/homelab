# PaginatedOAuthSourceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[OAuthSource]**](OAuthSource.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_o_auth_source_list import PaginatedOAuthSourceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedOAuthSourceList from a JSON string
paginated_o_auth_source_list_instance = PaginatedOAuthSourceList.from_json(json)
# print the JSON string representation of the object
print(PaginatedOAuthSourceList.to_json())

# convert the object into a dict
paginated_o_auth_source_list_dict = paginated_o_auth_source_list_instance.to_dict()
# create an instance of PaginatedOAuthSourceList from a dict
paginated_o_auth_source_list_from_dict = PaginatedOAuthSourceList.from_dict(paginated_o_auth_source_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


