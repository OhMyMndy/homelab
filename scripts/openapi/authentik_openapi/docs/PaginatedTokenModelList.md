# PaginatedTokenModelList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[TokenModel]**](TokenModel.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_token_model_list import PaginatedTokenModelList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTokenModelList from a JSON string
paginated_token_model_list_instance = PaginatedTokenModelList.from_json(json)
# print the JSON string representation of the object
print(PaginatedTokenModelList.to_json())

# convert the object into a dict
paginated_token_model_list_dict = paginated_token_model_list_instance.to_dict()
# create an instance of PaginatedTokenModelList from a dict
paginated_token_model_list_from_dict = PaginatedTokenModelList.from_dict(paginated_token_model_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


