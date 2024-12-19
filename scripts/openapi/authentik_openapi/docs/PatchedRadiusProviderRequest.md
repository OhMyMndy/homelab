# PatchedRadiusProviderRequest

RadiusProvider Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**authentication_flow** | **str** | Flow used for authentication when the associated application is accessed by an un-authenticated user. | [optional] 
**authorization_flow** | **str** | Flow used when authorizing this provider. | [optional] 
**property_mappings** | **List[str]** |  | [optional] 
**client_networks** | **str** | List of CIDRs (comma-separated) that clients can connect from. A more specific CIDR will match before a looser one. Clients connecting from a non-specified CIDR will be dropped. | [optional] 
**shared_secret** | **str** | Shared secret between clients and server to hash packets. | [optional] 
**mfa_support** | **bool** | When enabled, code-based multi-factor authentication can be used by appending a semicolon and the TOTP code to the password. This should only be enabled if all users that will bind to this provider have a TOTP device configured, as otherwise a password may incorrectly be rejected if it contains a semicolon. | [optional] 

## Example

```python
from authentik_openapi.models.patched_radius_provider_request import PatchedRadiusProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedRadiusProviderRequest from a JSON string
patched_radius_provider_request_instance = PatchedRadiusProviderRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedRadiusProviderRequest.to_json())

# convert the object into a dict
patched_radius_provider_request_dict = patched_radius_provider_request_instance.to_dict()
# create an instance of PatchedRadiusProviderRequest from a dict
patched_radius_provider_request_from_dict = PatchedRadiusProviderRequest.from_dict(patched_radius_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


