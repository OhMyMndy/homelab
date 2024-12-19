# PaginatedRadiusOutpostConfigList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[RadiusOutpostConfig]**](RadiusOutpostConfig.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_radius_outpost_config_list import PaginatedRadiusOutpostConfigList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedRadiusOutpostConfigList from a JSON string
paginated_radius_outpost_config_list_instance = PaginatedRadiusOutpostConfigList.from_json(json)
# print the JSON string representation of the object
print(PaginatedRadiusOutpostConfigList.to_json())

# convert the object into a dict
paginated_radius_outpost_config_list_dict = paginated_radius_outpost_config_list_instance.to_dict()
# create an instance of PaginatedRadiusOutpostConfigList from a dict
paginated_radius_outpost_config_list_from_dict = PaginatedRadiusOutpostConfigList.from_dict(paginated_radius_outpost_config_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


