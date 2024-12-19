# PaginatedSMSDeviceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[SMSDevice]**](SMSDevice.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_sms_device_list import PaginatedSMSDeviceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSMSDeviceList from a JSON string
paginated_sms_device_list_instance = PaginatedSMSDeviceList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSMSDeviceList.to_json())

# convert the object into a dict
paginated_sms_device_list_dict = paginated_sms_device_list_instance.to_dict()
# create an instance of PaginatedSMSDeviceList from a dict
paginated_sms_device_list_from_dict = PaginatedSMSDeviceList.from_dict(paginated_sms_device_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


