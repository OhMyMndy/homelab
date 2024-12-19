# RadiusOutpostConfig

RadiusProvider Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**name** | **str** |  | 
**application_slug** | **str** |  | 
**auth_flow_slug** | **str** |  | 
**client_networks** | **str** | List of CIDRs (comma-separated) that clients can connect from. A more specific CIDR will match before a looser one. Clients connecting from a non-specified CIDR will be dropped. | [optional] 
**shared_secret** | **str** | Shared secret between clients and server to hash packets. | [optional] 
**mfa_support** | **bool** | When enabled, code-based multi-factor authentication can be used by appending a semicolon and the TOTP code to the password. This should only be enabled if all users that will bind to this provider have a TOTP device configured, as otherwise a password may incorrectly be rejected if it contains a semicolon. | [optional] 

## Example

```python
from authentik_openapi.models.radius_outpost_config import RadiusOutpostConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RadiusOutpostConfig from a JSON string
radius_outpost_config_instance = RadiusOutpostConfig.from_json(json)
# print the JSON string representation of the object
print(RadiusOutpostConfig.to_json())

# convert the object into a dict
radius_outpost_config_dict = radius_outpost_config_instance.to_dict()
# create an instance of RadiusOutpostConfig from a dict
radius_outpost_config_from_dict = RadiusOutpostConfig.from_dict(radius_outpost_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


