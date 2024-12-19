# RACProviderRequest

RACProvider Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**authentication_flow** | **str** | Flow used for authentication when the associated application is accessed by an un-authenticated user. | [optional] 
**authorization_flow** | **str** | Flow used when authorizing this provider. | 
**property_mappings** | **List[str]** |  | [optional] 
**settings** | **object** |  | [optional] 
**connection_expiry** | **str** | Determines how long a session lasts. Default of 0 means that the sessions lasts until the browser is closed. (Format: hours&#x3D;-1;minutes&#x3D;-2;seconds&#x3D;-3) | [optional] 
**delete_token_on_disconnect** | **bool** | When set to true, connection tokens will be deleted upon disconnect. | [optional] 

## Example

```python
from authentik_openapi.models.rac_provider_request import RACProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RACProviderRequest from a JSON string
rac_provider_request_instance = RACProviderRequest.from_json(json)
# print the JSON string representation of the object
print(RACProviderRequest.to_json())

# convert the object into a dict
rac_provider_request_dict = rac_provider_request_instance.to_dict()
# create an instance of RACProviderRequest from a dict
rac_provider_request_from_dict = RACProviderRequest.from_dict(rac_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


