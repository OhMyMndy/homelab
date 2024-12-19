# PaginatedSCIMProviderGroupList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[SCIMProviderGroup]**](SCIMProviderGroup.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_scim_provider_group_list import PaginatedSCIMProviderGroupList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSCIMProviderGroupList from a JSON string
paginated_scim_provider_group_list_instance = PaginatedSCIMProviderGroupList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSCIMProviderGroupList.to_json())

# convert the object into a dict
paginated_scim_provider_group_list_dict = paginated_scim_provider_group_list_instance.to_dict()
# create an instance of PaginatedSCIMProviderGroupList from a dict
paginated_scim_provider_group_list_from_dict = PaginatedSCIMProviderGroupList.from_dict(paginated_scim_provider_group_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


