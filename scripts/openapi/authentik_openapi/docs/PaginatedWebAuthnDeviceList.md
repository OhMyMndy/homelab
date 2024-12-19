# PaginatedWebAuthnDeviceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[WebAuthnDevice]**](WebAuthnDevice.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_web_authn_device_list import PaginatedWebAuthnDeviceList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedWebAuthnDeviceList from a JSON string
paginated_web_authn_device_list_instance = PaginatedWebAuthnDeviceList.from_json(json)
# print the JSON string representation of the object
print(PaginatedWebAuthnDeviceList.to_json())

# convert the object into a dict
paginated_web_authn_device_list_dict = paginated_web_authn_device_list_instance.to_dict()
# create an instance of PaginatedWebAuthnDeviceList from a dict
paginated_web_authn_device_list_from_dict = PaginatedWebAuthnDeviceList.from_dict(paginated_web_authn_device_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


