# PaginatedTokenList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[Token]**](Token.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_token_list import PaginatedTokenList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTokenList from a JSON string
paginated_token_list_instance = PaginatedTokenList.from_json(json)
# print the JSON string representation of the object
print(PaginatedTokenList.to_json())

# convert the object into a dict
paginated_token_list_dict = paginated_token_list_instance.to_dict()
# create an instance of PaginatedTokenList from a dict
paginated_token_list_from_dict = PaginatedTokenList.from_dict(paginated_token_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


