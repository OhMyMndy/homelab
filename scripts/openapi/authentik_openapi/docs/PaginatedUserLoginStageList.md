# PaginatedUserLoginStageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[UserLoginStage]**](UserLoginStage.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_user_login_stage_list import PaginatedUserLoginStageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedUserLoginStageList from a JSON string
paginated_user_login_stage_list_instance = PaginatedUserLoginStageList.from_json(json)
# print the JSON string representation of the object
print(PaginatedUserLoginStageList.to_json())

# convert the object into a dict
paginated_user_login_stage_list_dict = paginated_user_login_stage_list_instance.to_dict()
# create an instance of PaginatedUserLoginStageList from a dict
paginated_user_login_stage_list_from_dict = PaginatedUserLoginStageList.from_dict(paginated_user_login_stage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


