# PaginatedExpiringBaseGrantModelList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[ExpiringBaseGrantModel]**](ExpiringBaseGrantModel.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_expiring_base_grant_model_list import PaginatedExpiringBaseGrantModelList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedExpiringBaseGrantModelList from a JSON string
paginated_expiring_base_grant_model_list_instance = PaginatedExpiringBaseGrantModelList.from_json(json)
# print the JSON string representation of the object
print(PaginatedExpiringBaseGrantModelList.to_json())

# convert the object into a dict
paginated_expiring_base_grant_model_list_dict = paginated_expiring_base_grant_model_list_instance.to_dict()
# create an instance of PaginatedExpiringBaseGrantModelList from a dict
paginated_expiring_base_grant_model_list_from_dict = PaginatedExpiringBaseGrantModelList.from_dict(paginated_expiring_base_grant_model_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


