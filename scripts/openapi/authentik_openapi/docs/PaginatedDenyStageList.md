# PaginatedDenyStageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[DenyStage]**](DenyStage.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_deny_stage_list import PaginatedDenyStageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedDenyStageList from a JSON string
paginated_deny_stage_list_instance = PaginatedDenyStageList.from_json(json)
# print the JSON string representation of the object
print(PaginatedDenyStageList.to_json())

# convert the object into a dict
paginated_deny_stage_list_dict = paginated_deny_stage_list_instance.to_dict()
# create an instance of PaginatedDenyStageList from a dict
paginated_deny_stage_list_from_dict = PaginatedDenyStageList.from_dict(paginated_deny_stage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


