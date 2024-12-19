# PaginatedStaticDeviceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[StaticDevice]**](StaticDevice.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_static_device_list import PaginatedStaticDeviceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedStaticDeviceList from a JSON string
paginated_static_device_list_instance = PaginatedStaticDeviceList.from_json(json)
# print the JSON string representation of the object
print(PaginatedStaticDeviceList.to_json())

# convert the object into a dict
paginated_static_device_list_dict = paginated_static_device_list_instance.to_dict()
# create an instance of PaginatedStaticDeviceList from a dict
paginated_static_device_list_from_dict = PaginatedStaticDeviceList.from_dict(paginated_static_device_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


