# PaginatedFlowList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[Flow]**](Flow.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_flow_list import PaginatedFlowList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedFlowList from a JSON string
paginated_flow_list_instance = PaginatedFlowList.from_json(json)
# print the JSON string representation of the object
print(PaginatedFlowList.to_json())

# convert the object into a dict
paginated_flow_list_dict = paginated_flow_list_instance.to_dict()
# create an instance of PaginatedFlowList from a dict
paginated_flow_list_from_dict = PaginatedFlowList.from_dict(paginated_flow_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


