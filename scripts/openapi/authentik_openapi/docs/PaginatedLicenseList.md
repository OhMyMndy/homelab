# PaginatedLicenseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[License]**](License.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_license_list import PaginatedLicenseList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedLicenseList from a JSON string
paginated_license_list_instance = PaginatedLicenseList.from_json(json)
# print the JSON string representation of the object
print(PaginatedLicenseList.to_json())

# convert the object into a dict
paginated_license_list_dict = paginated_license_list_instance.to_dict()
# create an instance of PaginatedLicenseList from a dict
paginated_license_list_from_dict = PaginatedLicenseList.from_dict(paginated_license_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


