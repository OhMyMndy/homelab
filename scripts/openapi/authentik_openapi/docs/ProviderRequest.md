# ProviderRequest

Provider Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**authentication_flow** | **str** | Flow used for authentication when the associated application is accessed by an un-authenticated user. | [optional] 
**authorization_flow** | **str** | Flow used when authorizing this provider. | 
**property_mappings** | **List[str]** |  | [optional] 

## Example

```python
from authentik_openapi.models.provider_request import ProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderRequest from a JSON string
provider_request_instance = ProviderRequest.from_json(json)
# print the JSON string representation of the object
print(ProviderRequest.to_json())

# convert the object into a dict
provider_request_dict = provider_request_instance.to_dict()
# create an instance of ProviderRequest from a dict
provider_request_from_dict = ProviderRequest.from_dict(provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


