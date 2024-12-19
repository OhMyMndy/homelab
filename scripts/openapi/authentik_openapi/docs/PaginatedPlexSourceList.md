# PaginatedPlexSourceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[PlexSource]**](PlexSource.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_plex_source_list import PaginatedPlexSourceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedPlexSourceList from a JSON string
paginated_plex_source_list_instance = PaginatedPlexSourceList.from_json(json)
# print the JSON string representation of the object
print(PaginatedPlexSourceList.to_json())

# convert the object into a dict
paginated_plex_source_list_dict = paginated_plex_source_list_instance.to_dict()
# create an instance of PaginatedPlexSourceList from a dict
paginated_plex_source_list_from_dict = PaginatedPlexSourceList.from_dict(paginated_plex_source_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


