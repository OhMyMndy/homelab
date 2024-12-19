# PatchedSCIMProviderRequest

SCIMProvider Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**property_mappings** | **List[str]** |  | [optional] 
**property_mappings_group** | **List[str]** | Property mappings used for group creation/updating. | [optional] 
**url** | **str** | Base URL to SCIM requests, usually ends in /v2 | [optional] 
**token** | **str** | Authentication token | [optional] 
**exclude_users_service_account** | **bool** |  | [optional] 
**filter_group** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_scim_provider_request import PatchedSCIMProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedSCIMProviderRequest from a JSON string
patched_scim_provider_request_instance = PatchedSCIMProviderRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedSCIMProviderRequest.to_json())

# convert the object into a dict
patched_scim_provider_request_dict = patched_scim_provider_request_instance.to_dict()
# create an instance of PatchedSCIMProviderRequest from a dict
patched_scim_provider_request_from_dict = PatchedSCIMProviderRequest.from_dict(patched_scim_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


