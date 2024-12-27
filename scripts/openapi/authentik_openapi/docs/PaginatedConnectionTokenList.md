# PaginatedConnectionTokenList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[ConnectionToken]**](ConnectionToken.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_connection_token_list import PaginatedConnectionTokenList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedConnectionTokenList from a JSON string
paginated_connection_token_list_instance = PaginatedConnectionTokenList.from_json(json)
# print the JSON string representation of the object
print(PaginatedConnectionTokenList.to_json())

# convert the object into a dict
paginated_connection_token_list_dict = paginated_connection_token_list_instance.to_dict()
# create an instance of PaginatedConnectionTokenList from a dict
paginated_connection_token_list_from_dict = PaginatedConnectionTokenList.from_dict(paginated_connection_token_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

