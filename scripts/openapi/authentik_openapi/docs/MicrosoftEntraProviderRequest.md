# MicrosoftEntraProviderRequest

MicrosoftEntraProvider Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**property_mappings** | **List[str]** |  | [optional] 
**property_mappings_group** | **List[str]** | Property mappings used for group creation/updating. | [optional] 
**client_id** | **str** |  | 
**client_secret** | **str** |  | 
**tenant_id** | **str** |  | 
**exclude_users_service_account** | **bool** |  | [optional] 
**filter_group** | **str** |  | [optional] 
**user_delete_action** | [**OutgoingSyncDeleteAction**](OutgoingSyncDeleteAction.md) |  | [optional] 
**group_delete_action** | [**OutgoingSyncDeleteAction**](OutgoingSyncDeleteAction.md) |  | [optional] 

## Example

```python
from authentik_openapi.models.microsoft_entra_provider_request import MicrosoftEntraProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftEntraProviderRequest from a JSON string
microsoft_entra_provider_request_instance = MicrosoftEntraProviderRequest.from_json(json)
# print the JSON string representation of the object
print(MicrosoftEntraProviderRequest.to_json())

# convert the object into a dict
microsoft_entra_provider_request_dict = microsoft_entra_provider_request_instance.to_dict()
# create an instance of MicrosoftEntraProviderRequest from a dict
microsoft_entra_provider_request_from_dict = MicrosoftEntraProviderRequest.from_dict(microsoft_entra_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


