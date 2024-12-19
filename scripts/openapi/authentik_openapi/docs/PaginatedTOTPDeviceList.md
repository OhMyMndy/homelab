# PaginatedTOTPDeviceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[TOTPDevice]**](TOTPDevice.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_totp_device_list import PaginatedTOTPDeviceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTOTPDeviceList from a JSON string
paginated_totp_device_list_instance = PaginatedTOTPDeviceList.from_json(json)
# print the JSON string representation of the object
print(PaginatedTOTPDeviceList.to_json())

# convert the object into a dict
paginated_totp_device_list_dict = paginated_totp_device_list_instance.to_dict()
# create an instance of PaginatedTOTPDeviceList from a dict
paginated_totp_device_list_from_dict = PaginatedTOTPDeviceList.from_dict(paginated_totp_device_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


