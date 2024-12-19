# PatchedGoogleWorkspaceProviderRequest

GoogleWorkspaceProvider Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**property_mappings** | **List[str]** |  | [optional] 
**property_mappings_group** | **List[str]** | Property mappings used for group creation/updating. | [optional] 
**delegated_subject** | **str** |  | [optional] 
**credentials** | **object** |  | [optional] 
**scopes** | **str** |  | [optional] 
**exclude_users_service_account** | **bool** |  | [optional] 
**filter_group** | **str** |  | [optional] 
**user_delete_action** | [**OutgoingSyncDeleteAction**](OutgoingSyncDeleteAction.md) |  | [optional] 
**group_delete_action** | [**OutgoingSyncDeleteAction**](OutgoingSyncDeleteAction.md) |  | [optional] 
**default_group_email_domain** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_google_workspace_provider_request import PatchedGoogleWorkspaceProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedGoogleWorkspaceProviderRequest from a JSON string
patched_google_workspace_provider_request_instance = PatchedGoogleWorkspaceProviderRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedGoogleWorkspaceProviderRequest.to_json())

# convert the object into a dict
patched_google_workspace_provider_request_dict = patched_google_workspace_provider_request_instance.to_dict()
# create an instance of PatchedGoogleWorkspaceProviderRequest from a dict
patched_google_workspace_provider_request_from_dict = PatchedGoogleWorkspaceProviderRequest.from_dict(patched_google_workspace_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


