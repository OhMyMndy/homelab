# PaginatedWebAuthnDeviceTypeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[WebAuthnDeviceType]**](WebAuthnDeviceType.md) |  | 

## Example

```python
from authentik_openapi.models.paginated_web_authn_device_type_list import PaginatedWebAuthnDeviceTypeList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedWebAuthnDeviceTypeList from a JSON string
paginated_web_authn_device_type_list_instance = PaginatedWebAuthnDeviceTypeList.from_json(json)
# print the JSON string representation of the object
print(PaginatedWebAuthnDeviceTypeList.to_json())

# convert the object into a dict
paginated_web_authn_device_type_list_dict = paginated_web_authn_device_type_list_instance.to_dict()
# create an instance of PaginatedWebAuthnDeviceTypeList from a dict
paginated_web_authn_device_type_list_from_dict = PaginatedWebAuthnDeviceTypeList.from_dict(paginated_web_authn_device_type_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


