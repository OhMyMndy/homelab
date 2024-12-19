# PaginatedIdentificationStageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[IdentificationStage]**](IdentificationStage.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_identification_stage_list import PaginatedIdentificationStageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedIdentificationStageList from a JSON string
paginated_identification_stage_list_instance = PaginatedIdentificationStageList.from_json(json)
# print the JSON string representation of the object
print(PaginatedIdentificationStageList.to_json())

# convert the object into a dict
paginated_identification_stage_list_dict = paginated_identification_stage_list_instance.to_dict()
# create an instance of PaginatedIdentificationStageList from a dict
paginated_identification_stage_list_from_dict = PaginatedIdentificationStageList.from_dict(paginated_identification_stage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


