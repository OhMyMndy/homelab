# ProxyProvider

ProxyProvider Serializer

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
**client_id** | **str** |  | [readonly] 
**internal_host** | **str** |  | [optional] 
**external_host** | **str** |  | 
**internal_host_ssl_validation** | **bool** | Validate SSL Certificates of upstream servers | [optional] 
**certificate** | **str** |  | [optional] 
**skip_path_regex** | **str** | Regular expressions for which authentication is not required. Each new line is interpreted as a new Regular Expression. | [optional] 
**basic_auth_enabled** | **bool** | Set a custom HTTP-Basic Authentication header based on values from authentik. | [optional] 
**basic_auth_password_attribute** | **str** | User/Group Attribute used for the password part of the HTTP-Basic Header. | [optional] 
**basic_auth_user_attribute** | **str** | User/Group Attribute used for the user part of the HTTP-Basic Header. If not set, the user&#39;s Email address is used. | [optional] 
**mode** | [**ProxyMode**](ProxyMode.md) | Enable support for forwardAuth in traefik and nginx auth_request. Exclusive with internal_host. | [optional] 
**intercept_header_auth** | **bool** | When enabled, this provider will intercept the authorization header and authenticate requests based on its value. | [optional] 
**redirect_uris** | **str** |  | [readonly] 
**cookie_domain** | **str** |  | [optional] 
**jwks_sources** | **List[str]** |  | [optional] 
**access_token_validity** | **str** | Tokens not valid on or after current time + this value (Format: hours&#x3D;1;minutes&#x3D;2;seconds&#x3D;3). | [optional] 
**refresh_token_validity** | **str** | Tokens not valid on or after current time + this value (Format: hours&#x3D;1;minutes&#x3D;2;seconds&#x3D;3). | [optional] 
**outpost_set** | **List[str]** |  | [readonly] 

## Example

```python
from authentik_openapi.models.proxy_provider import ProxyProvider

# TODO update the JSON string below
json = "{}"
# create an instance of ProxyProvider from a JSON string
proxy_provider_instance = ProxyProvider.from_json(json)
# print the JSON string representation of the object
print(ProxyProvider.to_json())

# convert the object into a dict
proxy_provider_dict = proxy_provider_instance.to_dict()
# create an instance of ProxyProvider from a dict
proxy_provider_from_dict = ProxyProvider.from_dict(proxy_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


