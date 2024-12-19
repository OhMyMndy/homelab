# RACProvider

RACProvider Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**name** | **str** |  | 
**authentication_flow** | **str** | Flow used for authentication when the associated application is accessed by an un-authenticated user. | [optional] 
**authorization_flow** | **str** | Flow used when authorizing this provider. | 
**property_mappings** | **List[str]** |  | [optional] 
**component** | **str** | Get object component so that we know how to edit the object | [readonly] 
**assigned_application_slug** | **str** | Internal application name, used in URLs. | [readonly] 
**assigned_application_name** | **str** | Application&#39;s display Name. | [readonly] 
**assigned_backchannel_application_slug** | **str** | Internal application name, used in URLs. | [readonly] 
**assigned_backchannel_application_name** | **str** | Application&#39;s display Name. | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**settings** | **object** |  | [optional] 
**outpost_set** | **List[str]** |  | [readonly] 
**connection_expiry** | **str** | Determines how long a session lasts. Default of 0 means that the sessions lasts until the browser is closed. (Format: hours&#x3D;-1;minutes&#x3D;-2;seconds&#x3D;-3) | [optional] 
**delete_token_on_disconnect** | **bool** | When set to true, connection tokens will be deleted upon disconnect. | [optional] 

## Example

```python
from authentik_openapi.models.rac_provider import RACProvider

# TODO update the JSON string below
json = "{}"
# create an instance of RACProvider from a JSON string
rac_provider_instance = RACProvider.from_json(json)
# print the JSON string representation of the object
print(RACProvider.to_json())

# convert the object into a dict
rac_provider_dict = rac_provider_instance.to_dict()
# create an instance of RACProvider from a dict
rac_provider_from_dict = RACProvider.from_dict(rac_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


