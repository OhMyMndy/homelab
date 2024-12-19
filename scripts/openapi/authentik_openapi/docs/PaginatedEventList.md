# PaginatedEventList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[Event]**](Event.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_event_list import PaginatedEventList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedEventList from a JSON string
paginated_event_list_instance = PaginatedEventList.from_json(json)
# print the JSON string representation of the object
print(PaginatedEventList.to_json())

# convert the object into a dict
paginated_event_list_dict = paginated_event_list_instance.to_dict()
# create an instance of PaginatedEventList from a dict
paginated_event_list_from_dict = PaginatedEventList.from_dict(paginated_event_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


