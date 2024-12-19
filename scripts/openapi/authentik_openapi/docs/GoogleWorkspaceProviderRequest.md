# GoogleWorkspaceProviderRequest

GoogleWorkspaceProvider Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**property_mappings** | **List[str]** |  | [optional] 
**property_mappings_group** | **List[str]** | Property mappings used for group creation/updating. | [optional] 
**delegated_subject** | **str** |  | 
**credentials** | **object** |  | 
**scopes** | **str** |  | [optional] 
**exclude_users_service_account** | **bool** |  | [optional] 
**filter_group** | **str** |  | [optional] 
**user_delete_action** | [**OutgoingSyncDeleteAction**](OutgoingSyncDeleteAction.md) |  | [optional] 
**group_delete_action** | [**OutgoingSyncDeleteAction**](OutgoingSyncDeleteAction.md) |  | [optional] 
**default_group_email_domain** | **str** |  | 

## Example

```python
from authentik_openapi.models.google_workspace_provider_request import GoogleWorkspaceProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleWorkspaceProviderRequest from a JSON string
google_workspace_provider_request_instance = GoogleWorkspaceProviderRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleWorkspaceProviderRequest.to_json())

# convert the object into a dict
google_workspace_provider_request_dict = google_workspace_provider_request_instance.to_dict()
# create an instance of GoogleWorkspaceProviderRequest from a dict
google_workspace_provider_request_from_dict = GoogleWorkspaceProviderRequest.from_dict(google_workspace_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


