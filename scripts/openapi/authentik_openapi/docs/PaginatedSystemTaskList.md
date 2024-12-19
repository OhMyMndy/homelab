# PaginatedSystemTaskList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[SystemTask]**](SystemTask.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_system_task_list import PaginatedSystemTaskList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSystemTaskList from a JSON string
paginated_system_task_list_instance = PaginatedSystemTaskList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSystemTaskList.to_json())

# convert the object into a dict
paginated_system_task_list_dict = paginated_system_task_list_instance.to_dict()
# create an instance of PaginatedSystemTaskList from a dict
paginated_system_task_list_from_dict = PaginatedSystemTaskList.from_dict(paginated_system_task_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


