# PaginatedFlowStageBindingList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[FlowStageBinding]**](FlowStageBinding.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_flow_stage_binding_list import PaginatedFlowStageBindingList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedFlowStageBindingList from a JSON string
paginated_flow_stage_binding_list_instance = PaginatedFlowStageBindingList.from_json(json)
# print the JSON string representation of the object
print(PaginatedFlowStageBindingList.to_json())

# convert the object into a dict
paginated_flow_stage_binding_list_dict = paginated_flow_stage_binding_list_instance.to_dict()
# create an instance of PaginatedFlowStageBindingList from a dict
paginated_flow_stage_binding_list_from_dict = PaginatedFlowStageBindingList.from_dict(paginated_flow_stage_binding_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


