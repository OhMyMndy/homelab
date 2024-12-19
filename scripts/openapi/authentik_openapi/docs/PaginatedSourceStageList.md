# PaginatedSourceStageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[SourceStage]**](SourceStage.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_source_stage_list import PaginatedSourceStageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSourceStageList from a JSON string
paginated_source_stage_list_instance = PaginatedSourceStageList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSourceStageList.to_json())

# convert the object into a dict
paginated_source_stage_list_dict = paginated_source_stage_list_instance.to_dict()
# create an instance of PaginatedSourceStageList from a dict
paginated_source_stage_list_from_dict = PaginatedSourceStageList.from_dict(paginated_source_stage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


