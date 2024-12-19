# PaginatedEndpointList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[Endpoint]**](Endpoint.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_endpoint_list import PaginatedEndpointList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedEndpointList from a JSON string
paginated_endpoint_list_instance = PaginatedEndpointList.from_json(json)
# print the JSON string representation of the object
print(PaginatedEndpointList.to_json())

# convert the object into a dict
paginated_endpoint_list_dict = paginated_endpoint_list_instance.to_dict()
# create an instance of PaginatedEndpointList from a dict
paginated_endpoint_list_from_dict = PaginatedEndpointList.from_dict(paginated_endpoint_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


