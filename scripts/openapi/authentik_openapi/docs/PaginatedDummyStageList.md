# PaginatedDummyStageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[DummyStage]**](DummyStage.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_dummy_stage_list import PaginatedDummyStageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedDummyStageList from a JSON string
paginated_dummy_stage_list_instance = PaginatedDummyStageList.from_json(json)
# print the JSON string representation of the object
print(PaginatedDummyStageList.to_json())

# convert the object into a dict
paginated_dummy_stage_list_dict = paginated_dummy_stage_list_instance.to_dict()
# create an instance of PaginatedDummyStageList from a dict
paginated_dummy_stage_list_from_dict = PaginatedDummyStageList.from_dict(paginated_dummy_stage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


