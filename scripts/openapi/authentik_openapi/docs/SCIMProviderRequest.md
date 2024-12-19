# SCIMProviderRequest

SCIMProvider Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**property_mappings** | **List[str]** |  | [optional] 
**property_mappings_group** | **List[str]** | Property mappings used for group creation/updating. | [optional] 
**url** | **str** | Base URL to SCIM requests, usually ends in /v2 | 
**token** | **str** | Authentication token | 
**exclude_users_service_account** | **bool** |  | [optional] 
**filter_group** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.scim_provider_request import SCIMProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SCIMProviderRequest from a JSON string
scim_provider_request_instance = SCIMProviderRequest.from_json(json)
# print the JSON string representation of the object
print(SCIMProviderRequest.to_json())

# convert the object into a dict
scim_provider_request_dict = scim_provider_request_instance.to_dict()
# create an instance of SCIMProviderRequest from a dict
scim_provider_request_from_dict = SCIMProviderRequest.from_dict(scim_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


