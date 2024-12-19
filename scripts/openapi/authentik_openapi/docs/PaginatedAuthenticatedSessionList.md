# PaginatedAuthenticatedSessionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[AuthenticatedSession]**](AuthenticatedSession.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_authenticated_session_list import PaginatedAuthenticatedSessionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAuthenticatedSessionList from a JSON string
paginated_authenticated_session_list_instance = PaginatedAuthenticatedSessionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedAuthenticatedSessionList.to_json())

# convert the object into a dict
paginated_authenticated_session_list_dict = paginated_authenticated_session_list_instance.to_dict()
# create an instance of PaginatedAuthenticatedSessionList from a dict
paginated_authenticated_session_list_from_dict = PaginatedAuthenticatedSessionList.from_dict(paginated_authenticated_session_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


