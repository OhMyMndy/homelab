# PaginatedDuoDeviceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[DuoDevice]**](DuoDevice.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_duo_device_list import PaginatedDuoDeviceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedDuoDeviceList from a JSON string
paginated_duo_device_list_instance = PaginatedDuoDeviceList.from_json(json)
# print the JSON string representation of the object
print(PaginatedDuoDeviceList.to_json())

# convert the object into a dict
paginated_duo_device_list_dict = paginated_duo_device_list_instance.to_dict()
# create an instance of PaginatedDuoDeviceList from a dict
paginated_duo_device_list_from_dict = PaginatedDuoDeviceList.from_dict(paginated_duo_device_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


