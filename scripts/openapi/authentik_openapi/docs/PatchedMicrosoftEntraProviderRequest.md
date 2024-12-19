# PatchedMicrosoftEntraProviderRequest

MicrosoftEntraProvider Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**property_mappings** | **List[str]** |  | [optional] 
**property_mappings_group** | **List[str]** | Property mappings used for group creation/updating. | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**exclude_users_service_account** | **bool** |  | [optional] 
**filter_group** | **str** |  | [optional] 
**user_delete_action** | [**OutgoingSyncDeleteAction**](OutgoingSyncDeleteAction.md) |  | [optional] 
**group_delete_action** | [**OutgoingSyncDeleteAction**](OutgoingSyncDeleteAction.md) |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_microsoft_entra_provider_request import PatchedMicrosoftEntraProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedMicrosoftEntraProviderRequest from a JSON string
patched_microsoft_entra_provider_request_instance = PatchedMicrosoftEntraProviderRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedMicrosoftEntraProviderRequest.to_json())

# convert the object into a dict
patched_microsoft_entra_provider_request_dict = patched_microsoft_entra_provider_request_instance.to_dict()
# create an instance of PatchedMicrosoftEntraProviderRequest from a dict
patched_microsoft_entra_provider_request_from_dict = PatchedMicrosoftEntraProviderRequest.from_dict(patched_microsoft_entra_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


