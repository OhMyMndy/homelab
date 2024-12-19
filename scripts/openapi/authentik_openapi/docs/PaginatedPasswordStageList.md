# PaginatedPasswordStageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[PasswordStage]**](PasswordStage.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_password_stage_list import PaginatedPasswordStageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPasswordStageList from a JSON string
paginated_password_stage_list_instance = PaginatedPasswordStageList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPasswordStageList.to_json())

# convert the object into a dict
paginated_password_stage_list_dict = paginated_password_stage_list_instance.to_dict()
# create an instance of PaginatedPasswordStageList from a dict
paginated_password_stage_list_from_dict = PaginatedPasswordStageList.from_dict(paginated_password_stage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


