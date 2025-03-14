# ProxyOutpostConfig

Proxy provider serializer for outposts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**name** | **str** |  | 
**internal_host** | **str** |  | [optional] 
**external_host** | **str** |  | 
**internal_host_ssl_validation** | **bool** | Validate SSL Certificates of upstream servers | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**oidc_configuration** | [**OpenIDConnectConfiguration**](OpenIDConnectConfiguration.md) |  | [readonly] 
**cookie_secret** | **str** |  | [optional] 
**certificate** | **str** |  | [optional] 
**skip_path_regex** | **str** | Regular expressions for which authentication is not required. Each new line is interpreted as a new Regular Expression. | [optional] 
**basic_auth_enabled** | **bool** | Set a custom HTTP-Basic Authentication header based on values from authentik. | [optional] 
**basic_auth_password_attribute** | **str** | User/Group Attribute used for the password part of the HTTP-Basic Header. | [optional] 
**basic_auth_user_attribute** | **str** | User/Group Attribute used for the user part of the HTTP-Basic Header. If not set, the user&#39;s Email address is used. | [optional] 
**mode** | [**ProxyMode**](ProxyMode.md) | Enable support for forwardAuth in traefik and nginx auth_request. Exclusive with internal_host. | [optional] 
**cookie_domain** | **str** |  | [optional] 
**access_token_validity** | **float** | Get token validity as second count | [readonly] 
**intercept_header_auth** | **bool** | When enabled, this provider will intercept the authorization header and authenticate requests based on its value. | [optional] 
**scopes_to_request** | **List[str]** | Get all the scope names the outpost should request, including custom-defined ones | [readonly] 
**assigned_application_slug** | **str** | Internal application name, used in URLs. | [readonly] 
**assigned_application_name** | **str** | Application&#39;s display Name. | [readonly] 

## Example

```python
from authentik_openapi.models.proxy_outpost_config import ProxyOutpostConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ProxyOutpostConfig from a JSON string
proxy_outpost_config_instance = ProxyOutpostConfig.from_json(json)
# print the JSON string representation of the object
print(ProxyOutpostConfig.to_json())

# convert the object into a dict
proxy_outpost_config_dict = proxy_outpost_config_instance.to_dict()
# create an instance of ProxyOutpostConfig from a dict
proxy_outpost_config_from_dict = ProxyOutpostConfig.from_dict(proxy_outpost_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


