# OpenIDConnectConfiguration

rest_framework Serializer for OIDC Configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer** | **str** |  | 
**authorization_endpoint** | **str** |  | 
**token_endpoint** | **str** |  | 
**userinfo_endpoint** | **str** |  | 
**end_session_endpoint** | **str** |  | 
**introspection_endpoint** | **str** |  | 
**jwks_uri** | **str** |  | 
**response_types_supported** | **List[str]** |  | 
**id_token_signing_alg_values_supported** | **List[str]** |  | 
**subject_types_supported** | **List[str]** |  | 
**token_endpoint_auth_methods_supported** | **List[str]** |  | 

## Example

```python
from authentik_openapi.models.open_id_connect_configuration import OpenIDConnectConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of OpenIDConnectConfiguration from a JSON string
open_id_connect_configuration_instance = OpenIDConnectConfiguration.from_json(json)
# print the JSON string representation of the object
print(OpenIDConnectConfiguration.to_json())

# convert the object into a dict
open_id_connect_configuration_dict = open_id_connect_configuration_instance.to_dict()
# create an instance of OpenIDConnectConfiguration from a dict
open_id_connect_configuration_from_dict = OpenIDConnectConfiguration.from_dict(open_id_connect_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


