# PaginatedUserDeleteStageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[UserDeleteStage]**](UserDeleteStage.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_user_delete_stage_list import PaginatedUserDeleteStageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUserDeleteStageList from a JSON string
paginated_user_delete_stage_list_instance = PaginatedUserDeleteStageList.from_json(json)
# print the JSON string representation of the object
print(PaginatedUserDeleteStageList.to_json())

# convert the object into a dict
paginated_user_delete_stage_list_dict = paginated_user_delete_stage_list_instance.to_dict()
# create an instance of PaginatedUserDeleteStageList from a dict
paginated_user_delete_stage_list_from_dict = PaginatedUserDeleteStageList.from_dict(paginated_user_delete_stage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


