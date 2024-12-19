# MicrosoftEntraProvider

MicrosoftEntraProvider Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**name** | **str** |  | 
**property_mappings** | **List[str]** |  | [optional] 
**property_mappings_group** | **List[str]** | Property mappings used for group creation/updating. | [optional] 
**component** | **str** | Get object component so that we know how to edit the object | [readonly] 
**assigned_backchannel_application_slug** | **str** | Internal application name, used in URLs. | [readonly] 
**assigned_backchannel_application_name** | **str** | Application&#39;s display Name. | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**client_id** | **str** |  | 
**client_secret** | **str** |  | 
**tenant_id** | **str** |  | 
**exclude_users_service_account** | **bool** |  | [optional] 
**filter_group** | **str** |  | [optional] 
**user_delete_action** | [**OutgoingSyncDeleteAction**](OutgoingSyncDeleteAction.md) |  | [optional] 
**group_delete_action** | [**OutgoingSyncDeleteAction**](OutgoingSyncDeleteAction.md) |  | [optional] 

## Example

```python
from authentik_openapi.models.microsoft_entra_provider import MicrosoftEntraProvider

# TODO update the JSON string below
json = "{}"
# create an instance of MicrosoftEntraProvider from a JSON string
microsoft_entra_provider_instance = MicrosoftEntraProvider.from_json(json)
# print the JSON string representation of the object
print(MicrosoftEntraProvider.to_json())

# convert the object into a dict
microsoft_entra_provider_dict = microsoft_entra_provider_instance.to_dict()
# create an instance of MicrosoftEntraProvider from a dict
microsoft_entra_provider_from_dict = MicrosoftEntraProvider.from_dict(microsoft_entra_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


