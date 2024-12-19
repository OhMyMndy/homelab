# authentik_openapi.ProvidersApi

All URIs are relative to *https://auth.home.ohmymndy.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**providers_all_destroy**](ProvidersApi.md#providers_all_destroy) | **DELETE** /providers/all/{id}/ | 
[**providers_all_list**](ProvidersApi.md#providers_all_list) | **GET** /providers/all/ | 
[**providers_all_retrieve**](ProvidersApi.md#providers_all_retrieve) | **GET** /providers/all/{id}/ | 
[**providers_all_types_list**](ProvidersApi.md#providers_all_types_list) | **GET** /providers/all/types/ | 
[**providers_all_used_by_list**](ProvidersApi.md#providers_all_used_by_list) | **GET** /providers/all/{id}/used_by/ | 
[**providers_google_workspace_create**](ProvidersApi.md#providers_google_workspace_create) | **POST** /providers/google_workspace/ | 
[**providers_google_workspace_destroy**](ProvidersApi.md#providers_google_workspace_destroy) | **DELETE** /providers/google_workspace/{id}/ | 
[**providers_google_workspace_groups_create**](ProvidersApi.md#providers_google_workspace_groups_create) | **POST** /providers/google_workspace_groups/ | 
[**providers_google_workspace_groups_destroy**](ProvidersApi.md#providers_google_workspace_groups_destroy) | **DELETE** /providers/google_workspace_groups/{id}/ | 
[**providers_google_workspace_groups_list**](ProvidersApi.md#providers_google_workspace_groups_list) | **GET** /providers/google_workspace_groups/ | 
[**providers_google_workspace_groups_retrieve**](ProvidersApi.md#providers_google_workspace_groups_retrieve) | **GET** /providers/google_workspace_groups/{id}/ | 
[**providers_google_workspace_groups_used_by_list**](ProvidersApi.md#providers_google_workspace_groups_used_by_list) | **GET** /providers/google_workspace_groups/{id}/used_by/ | 
[**providers_google_workspace_list**](ProvidersApi.md#providers_google_workspace_list) | **GET** /providers/google_workspace/ | 
[**providers_google_workspace_partial_update**](ProvidersApi.md#providers_google_workspace_partial_update) | **PATCH** /providers/google_workspace/{id}/ | 
[**providers_google_workspace_retrieve**](ProvidersApi.md#providers_google_workspace_retrieve) | **GET** /providers/google_workspace/{id}/ | 
[**providers_google_workspace_sync_status_retrieve**](ProvidersApi.md#providers_google_workspace_sync_status_retrieve) | **GET** /providers/google_workspace/{id}/sync/status/ | 
[**providers_google_workspace_update**](ProvidersApi.md#providers_google_workspace_update) | **PUT** /providers/google_workspace/{id}/ | 
[**providers_google_workspace_used_by_list**](ProvidersApi.md#providers_google_workspace_used_by_list) | **GET** /providers/google_workspace/{id}/used_by/ | 
[**providers_google_workspace_users_create**](ProvidersApi.md#providers_google_workspace_users_create) | **POST** /providers/google_workspace_users/ | 
[**providers_google_workspace_users_destroy**](ProvidersApi.md#providers_google_workspace_users_destroy) | **DELETE** /providers/google_workspace_users/{id}/ | 
[**providers_google_workspace_users_list**](ProvidersApi.md#providers_google_workspace_users_list) | **GET** /providers/google_workspace_users/ | 
[**providers_google_workspace_users_retrieve**](ProvidersApi.md#providers_google_workspace_users_retrieve) | **GET** /providers/google_workspace_users/{id}/ | 
[**providers_google_workspace_users_used_by_list**](ProvidersApi.md#providers_google_workspace_users_used_by_list) | **GET** /providers/google_workspace_users/{id}/used_by/ | 
[**providers_ldap_create**](ProvidersApi.md#providers_ldap_create) | **POST** /providers/ldap/ | 
[**providers_ldap_destroy**](ProvidersApi.md#providers_ldap_destroy) | **DELETE** /providers/ldap/{id}/ | 
[**providers_ldap_list**](ProvidersApi.md#providers_ldap_list) | **GET** /providers/ldap/ | 
[**providers_ldap_partial_update**](ProvidersApi.md#providers_ldap_partial_update) | **PATCH** /providers/ldap/{id}/ | 
[**providers_ldap_retrieve**](ProvidersApi.md#providers_ldap_retrieve) | **GET** /providers/ldap/{id}/ | 
[**providers_ldap_update**](ProvidersApi.md#providers_ldap_update) | **PUT** /providers/ldap/{id}/ | 
[**providers_ldap_used_by_list**](ProvidersApi.md#providers_ldap_used_by_list) | **GET** /providers/ldap/{id}/used_by/ | 
[**providers_microsoft_entra_create**](ProvidersApi.md#providers_microsoft_entra_create) | **POST** /providers/microsoft_entra/ | 
[**providers_microsoft_entra_destroy**](ProvidersApi.md#providers_microsoft_entra_destroy) | **DELETE** /providers/microsoft_entra/{id}/ | 
[**providers_microsoft_entra_groups_create**](ProvidersApi.md#providers_microsoft_entra_groups_create) | **POST** /providers/microsoft_entra_groups/ | 
[**providers_microsoft_entra_groups_destroy**](ProvidersApi.md#providers_microsoft_entra_groups_destroy) | **DELETE** /providers/microsoft_entra_groups/{id}/ | 
[**providers_microsoft_entra_groups_list**](ProvidersApi.md#providers_microsoft_entra_groups_list) | **GET** /providers/microsoft_entra_groups/ | 
[**providers_microsoft_entra_groups_retrieve**](ProvidersApi.md#providers_microsoft_entra_groups_retrieve) | **GET** /providers/microsoft_entra_groups/{id}/ | 
[**providers_microsoft_entra_groups_used_by_list**](ProvidersApi.md#providers_microsoft_entra_groups_used_by_list) | **GET** /providers/microsoft_entra_groups/{id}/used_by/ | 
[**providers_microsoft_entra_list**](ProvidersApi.md#providers_microsoft_entra_list) | **GET** /providers/microsoft_entra/ | 
[**providers_microsoft_entra_partial_update**](ProvidersApi.md#providers_microsoft_entra_partial_update) | **PATCH** /providers/microsoft_entra/{id}/ | 
[**providers_microsoft_entra_retrieve**](ProvidersApi.md#providers_microsoft_entra_retrieve) | **GET** /providers/microsoft_entra/{id}/ | 
[**providers_microsoft_entra_sync_status_retrieve**](ProvidersApi.md#providers_microsoft_entra_sync_status_retrieve) | **GET** /providers/microsoft_entra/{id}/sync/status/ | 
[**providers_microsoft_entra_update**](ProvidersApi.md#providers_microsoft_entra_update) | **PUT** /providers/microsoft_entra/{id}/ | 
[**providers_microsoft_entra_used_by_list**](ProvidersApi.md#providers_microsoft_entra_used_by_list) | **GET** /providers/microsoft_entra/{id}/used_by/ | 
[**providers_microsoft_entra_users_create**](ProvidersApi.md#providers_microsoft_entra_users_create) | **POST** /providers/microsoft_entra_users/ | 
[**providers_microsoft_entra_users_destroy**](ProvidersApi.md#providers_microsoft_entra_users_destroy) | **DELETE** /providers/microsoft_entra_users/{id}/ | 
[**providers_microsoft_entra_users_list**](ProvidersApi.md#providers_microsoft_entra_users_list) | **GET** /providers/microsoft_entra_users/ | 
[**providers_microsoft_entra_users_retrieve**](ProvidersApi.md#providers_microsoft_entra_users_retrieve) | **GET** /providers/microsoft_entra_users/{id}/ | 
[**providers_microsoft_entra_users_used_by_list**](ProvidersApi.md#providers_microsoft_entra_users_used_by_list) | **GET** /providers/microsoft_entra_users/{id}/used_by/ | 
[**providers_oauth2_create**](ProvidersApi.md#providers_oauth2_create) | **POST** /providers/oauth2/ | 
[**providers_oauth2_destroy**](ProvidersApi.md#providers_oauth2_destroy) | **DELETE** /providers/oauth2/{id}/ | 
[**providers_oauth2_list**](ProvidersApi.md#providers_oauth2_list) | **GET** /providers/oauth2/ | 
[**providers_oauth2_partial_update**](ProvidersApi.md#providers_oauth2_partial_update) | **PATCH** /providers/oauth2/{id}/ | 
[**providers_oauth2_preview_user_retrieve**](ProvidersApi.md#providers_oauth2_preview_user_retrieve) | **GET** /providers/oauth2/{id}/preview_user/ | 
[**providers_oauth2_retrieve**](ProvidersApi.md#providers_oauth2_retrieve) | **GET** /providers/oauth2/{id}/ | 
[**providers_oauth2_setup_urls_retrieve**](ProvidersApi.md#providers_oauth2_setup_urls_retrieve) | **GET** /providers/oauth2/{id}/setup_urls/ | 
[**providers_oauth2_update**](ProvidersApi.md#providers_oauth2_update) | **PUT** /providers/oauth2/{id}/ | 
[**providers_oauth2_used_by_list**](ProvidersApi.md#providers_oauth2_used_by_list) | **GET** /providers/oauth2/{id}/used_by/ | 
[**providers_proxy_create**](ProvidersApi.md#providers_proxy_create) | **POST** /providers/proxy/ | 
[**providers_proxy_destroy**](ProvidersApi.md#providers_proxy_destroy) | **DELETE** /providers/proxy/{id}/ | 
[**providers_proxy_list**](ProvidersApi.md#providers_proxy_list) | **GET** /providers/proxy/ | 
[**providers_proxy_partial_update**](ProvidersApi.md#providers_proxy_partial_update) | **PATCH** /providers/proxy/{id}/ | 
[**providers_proxy_retrieve**](ProvidersApi.md#providers_proxy_retrieve) | **GET** /providers/proxy/{id}/ | 
[**providers_proxy_update**](ProvidersApi.md#providers_proxy_update) | **PUT** /providers/proxy/{id}/ | 
[**providers_proxy_used_by_list**](ProvidersApi.md#providers_proxy_used_by_list) | **GET** /providers/proxy/{id}/used_by/ | 
[**providers_rac_create**](ProvidersApi.md#providers_rac_create) | **POST** /providers/rac/ | 
[**providers_rac_destroy**](ProvidersApi.md#providers_rac_destroy) | **DELETE** /providers/rac/{id}/ | 
[**providers_rac_list**](ProvidersApi.md#providers_rac_list) | **GET** /providers/rac/ | 
[**providers_rac_partial_update**](ProvidersApi.md#providers_rac_partial_update) | **PATCH** /providers/rac/{id}/ | 
[**providers_rac_retrieve**](ProvidersApi.md#providers_rac_retrieve) | **GET** /providers/rac/{id}/ | 
[**providers_rac_update**](ProvidersApi.md#providers_rac_update) | **PUT** /providers/rac/{id}/ | 
[**providers_rac_used_by_list**](ProvidersApi.md#providers_rac_used_by_list) | **GET** /providers/rac/{id}/used_by/ | 
[**providers_radius_create**](ProvidersApi.md#providers_radius_create) | **POST** /providers/radius/ | 
[**providers_radius_destroy**](ProvidersApi.md#providers_radius_destroy) | **DELETE** /providers/radius/{id}/ | 
[**providers_radius_list**](ProvidersApi.md#providers_radius_list) | **GET** /providers/radius/ | 
[**providers_radius_partial_update**](ProvidersApi.md#providers_radius_partial_update) | **PATCH** /providers/radius/{id}/ | 
[**providers_radius_retrieve**](ProvidersApi.md#providers_radius_retrieve) | **GET** /providers/radius/{id}/ | 
[**providers_radius_update**](ProvidersApi.md#providers_radius_update) | **PUT** /providers/radius/{id}/ | 
[**providers_radius_used_by_list**](ProvidersApi.md#providers_radius_used_by_list) | **GET** /providers/radius/{id}/used_by/ | 
[**providers_saml_create**](ProvidersApi.md#providers_saml_create) | **POST** /providers/saml/ | 
[**providers_saml_destroy**](ProvidersApi.md#providers_saml_destroy) | **DELETE** /providers/saml/{id}/ | 
[**providers_saml_import_metadata_create**](ProvidersApi.md#providers_saml_import_metadata_create) | **POST** /providers/saml/import_metadata/ | 
[**providers_saml_list**](ProvidersApi.md#providers_saml_list) | **GET** /providers/saml/ | 
[**providers_saml_metadata_retrieve**](ProvidersApi.md#providers_saml_metadata_retrieve) | **GET** /providers/saml/{id}/metadata/ | 
[**providers_saml_partial_update**](ProvidersApi.md#providers_saml_partial_update) | **PATCH** /providers/saml/{id}/ | 
[**providers_saml_preview_user_retrieve**](ProvidersApi.md#providers_saml_preview_user_retrieve) | **GET** /providers/saml/{id}/preview_user/ | 
[**providers_saml_retrieve**](ProvidersApi.md#providers_saml_retrieve) | **GET** /providers/saml/{id}/ | 
[**providers_saml_update**](ProvidersApi.md#providers_saml_update) | **PUT** /providers/saml/{id}/ | 
[**providers_saml_used_by_list**](ProvidersApi.md#providers_saml_used_by_list) | **GET** /providers/saml/{id}/used_by/ | 
[**providers_scim_create**](ProvidersApi.md#providers_scim_create) | **POST** /providers/scim/ | 
[**providers_scim_destroy**](ProvidersApi.md#providers_scim_destroy) | **DELETE** /providers/scim/{id}/ | 
[**providers_scim_groups_create**](ProvidersApi.md#providers_scim_groups_create) | **POST** /providers/scim_groups/ | 
[**providers_scim_groups_destroy**](ProvidersApi.md#providers_scim_groups_destroy) | **DELETE** /providers/scim_groups/{id}/ | 
[**providers_scim_groups_list**](ProvidersApi.md#providers_scim_groups_list) | **GET** /providers/scim_groups/ | 
[**providers_scim_groups_retrieve**](ProvidersApi.md#providers_scim_groups_retrieve) | **GET** /providers/scim_groups/{id}/ | 
[**providers_scim_groups_used_by_list**](ProvidersApi.md#providers_scim_groups_used_by_list) | **GET** /providers/scim_groups/{id}/used_by/ | 
[**providers_scim_list**](ProvidersApi.md#providers_scim_list) | **GET** /providers/scim/ | 
[**providers_scim_partial_update**](ProvidersApi.md#providers_scim_partial_update) | **PATCH** /providers/scim/{id}/ | 
[**providers_scim_retrieve**](ProvidersApi.md#providers_scim_retrieve) | **GET** /providers/scim/{id}/ | 
[**providers_scim_sync_status_retrieve**](ProvidersApi.md#providers_scim_sync_status_retrieve) | **GET** /providers/scim/{id}/sync/status/ | 
[**providers_scim_update**](ProvidersApi.md#providers_scim_update) | **PUT** /providers/scim/{id}/ | 
[**providers_scim_used_by_list**](ProvidersApi.md#providers_scim_used_by_list) | **GET** /providers/scim/{id}/used_by/ | 
[**providers_scim_users_create**](ProvidersApi.md#providers_scim_users_create) | **POST** /providers/scim_users/ | 
[**providers_scim_users_destroy**](ProvidersApi.md#providers_scim_users_destroy) | **DELETE** /providers/scim_users/{id}/ | 
[**providers_scim_users_list**](ProvidersApi.md#providers_scim_users_list) | **GET** /providers/scim_users/ | 
[**providers_scim_users_retrieve**](ProvidersApi.md#providers_scim_users_retrieve) | **GET** /providers/scim_users/{id}/ | 
[**providers_scim_users_used_by_list**](ProvidersApi.md#providers_scim_users_used_by_list) | **GET** /providers/scim_users/{id}/used_by/ | 


# **providers_all_destroy**
> providers_all_destroy(id)



Provider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this provider.

    try:
        api_instance.providers_all_destroy(id)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_all_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this provider. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_all_list**
> PaginatedProviderList providers_all_list(application__isnull=application__isnull, backchannel=backchannel, ordering=ordering, page=page, page_size=page_size, search=search)



Provider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_provider_list import PaginatedProviderList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    application__isnull = True # bool |  (optional)
    backchannel = True # bool | When not set all providers are returned. When set to true, only backchannel providers are returned. When set to false, backchannel providers are excluded (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.providers_all_list(application__isnull=application__isnull, backchannel=backchannel, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of ProvidersApi->providers_all_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_all_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application__isnull** | **bool**|  | [optional] 
 **backchannel** | **bool**| When not set all providers are returned. When set to true, only backchannel providers are returned. When set to false, backchannel providers are excluded | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedProviderList**](PaginatedProviderList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_all_retrieve**
> Provider providers_all_retrieve(id)



Provider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.provider import Provider
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this provider.

    try:
        api_response = api_instance.providers_all_retrieve(id)
        print("The response of ProvidersApi->providers_all_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_all_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this provider. | 

### Return type

[**Provider**](Provider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_all_types_list**
> List[TypeCreate] providers_all_types_list()



Get all creatable types

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.type_create import TypeCreate
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)

    try:
        api_response = api_instance.providers_all_types_list()
        print("The response of ProvidersApi->providers_all_types_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_all_types_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[TypeCreate]**](TypeCreate.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_all_used_by_list**
> List[UsedBy] providers_all_used_by_list(id)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this provider.

    try:
        api_response = api_instance.providers_all_used_by_list(id)
        print("The response of ProvidersApi->providers_all_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_all_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this provider. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_google_workspace_create**
> GoogleWorkspaceProvider providers_google_workspace_create(google_workspace_provider_request)



GoogleWorkspaceProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.google_workspace_provider import GoogleWorkspaceProvider
from authentik_openapi.models.google_workspace_provider_request import GoogleWorkspaceProviderRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    google_workspace_provider_request = authentik_openapi.GoogleWorkspaceProviderRequest() # GoogleWorkspaceProviderRequest | 

    try:
        api_response = api_instance.providers_google_workspace_create(google_workspace_provider_request)
        print("The response of ProvidersApi->providers_google_workspace_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_google_workspace_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_workspace_provider_request** | [**GoogleWorkspaceProviderRequest**](GoogleWorkspaceProviderRequest.md)|  | 

### Return type

[**GoogleWorkspaceProvider**](GoogleWorkspaceProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_google_workspace_destroy**
> providers_google_workspace_destroy(id)



GoogleWorkspaceProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this Google Workspace Provider.

    try:
        api_instance.providers_google_workspace_destroy(id)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_google_workspace_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Google Workspace Provider. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_google_workspace_groups_create**
> GoogleWorkspaceProviderGroup providers_google_workspace_groups_create(google_workspace_provider_group_request)



GoogleWorkspaceProviderGroup Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.google_workspace_provider_group import GoogleWorkspaceProviderGroup
from authentik_openapi.models.google_workspace_provider_group_request import GoogleWorkspaceProviderGroupRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    google_workspace_provider_group_request = authentik_openapi.GoogleWorkspaceProviderGroupRequest() # GoogleWorkspaceProviderGroupRequest | 

    try:
        api_response = api_instance.providers_google_workspace_groups_create(google_workspace_provider_group_request)
        print("The response of ProvidersApi->providers_google_workspace_groups_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_google_workspace_groups_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_workspace_provider_group_request** | [**GoogleWorkspaceProviderGroupRequest**](GoogleWorkspaceProviderGroupRequest.md)|  | 

### Return type

[**GoogleWorkspaceProviderGroup**](GoogleWorkspaceProviderGroup.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_google_workspace_groups_destroy**
> providers_google_workspace_groups_destroy(id)



GoogleWorkspaceProviderGroup Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 'id_example' # str | A UUID string identifying this Google Workspace Provider Group.

    try:
        api_instance.providers_google_workspace_groups_destroy(id)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_google_workspace_groups_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this Google Workspace Provider Group. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_google_workspace_groups_list**
> PaginatedGoogleWorkspaceProviderGroupList providers_google_workspace_groups_list(group__group_uuid=group__group_uuid, group__name=group__name, ordering=ordering, page=page, page_size=page_size, provider__id=provider__id, search=search)



GoogleWorkspaceProviderGroup Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_google_workspace_provider_group_list import PaginatedGoogleWorkspaceProviderGroupList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    group__group_uuid = 'group__group_uuid_example' # str |  (optional)
    group__name = 'group__name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    provider__id = 56 # int |  (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.providers_google_workspace_groups_list(group__group_uuid=group__group_uuid, group__name=group__name, ordering=ordering, page=page, page_size=page_size, provider__id=provider__id, search=search)
        print("The response of ProvidersApi->providers_google_workspace_groups_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_google_workspace_groups_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group__group_uuid** | **str**|  | [optional] 
 **group__name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **provider__id** | **int**|  | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedGoogleWorkspaceProviderGroupList**](PaginatedGoogleWorkspaceProviderGroupList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_google_workspace_groups_retrieve**
> GoogleWorkspaceProviderGroup providers_google_workspace_groups_retrieve(id)



GoogleWorkspaceProviderGroup Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.google_workspace_provider_group import GoogleWorkspaceProviderGroup
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 'id_example' # str | A UUID string identifying this Google Workspace Provider Group.

    try:
        api_response = api_instance.providers_google_workspace_groups_retrieve(id)
        print("The response of ProvidersApi->providers_google_workspace_groups_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_google_workspace_groups_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this Google Workspace Provider Group. | 

### Return type

[**GoogleWorkspaceProviderGroup**](GoogleWorkspaceProviderGroup.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_google_workspace_groups_used_by_list**
> List[UsedBy] providers_google_workspace_groups_used_by_list(id)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 'id_example' # str | A UUID string identifying this Google Workspace Provider Group.

    try:
        api_response = api_instance.providers_google_workspace_groups_used_by_list(id)
        print("The response of ProvidersApi->providers_google_workspace_groups_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_google_workspace_groups_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this Google Workspace Provider Group. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_google_workspace_list**
> PaginatedGoogleWorkspaceProviderList providers_google_workspace_list(delegated_subject=delegated_subject, exclude_users_service_account=exclude_users_service_account, filter_group=filter_group, name=name, ordering=ordering, page=page, page_size=page_size, search=search)



GoogleWorkspaceProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_google_workspace_provider_list import PaginatedGoogleWorkspaceProviderList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    delegated_subject = 'delegated_subject_example' # str |  (optional)
    exclude_users_service_account = True # bool |  (optional)
    filter_group = 'filter_group_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.providers_google_workspace_list(delegated_subject=delegated_subject, exclude_users_service_account=exclude_users_service_account, filter_group=filter_group, name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of ProvidersApi->providers_google_workspace_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_google_workspace_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delegated_subject** | **str**|  | [optional] 
 **exclude_users_service_account** | **bool**|  | [optional] 
 **filter_group** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedGoogleWorkspaceProviderList**](PaginatedGoogleWorkspaceProviderList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_google_workspace_partial_update**
> GoogleWorkspaceProvider providers_google_workspace_partial_update(id, patched_google_workspace_provider_request=patched_google_workspace_provider_request)



GoogleWorkspaceProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.google_workspace_provider import GoogleWorkspaceProvider
from authentik_openapi.models.patched_google_workspace_provider_request import PatchedGoogleWorkspaceProviderRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this Google Workspace Provider.
    patched_google_workspace_provider_request = authentik_openapi.PatchedGoogleWorkspaceProviderRequest() # PatchedGoogleWorkspaceProviderRequest |  (optional)

    try:
        api_response = api_instance.providers_google_workspace_partial_update(id, patched_google_workspace_provider_request=patched_google_workspace_provider_request)
        print("The response of ProvidersApi->providers_google_workspace_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_google_workspace_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Google Workspace Provider. | 
 **patched_google_workspace_provider_request** | [**PatchedGoogleWorkspaceProviderRequest**](PatchedGoogleWorkspaceProviderRequest.md)|  | [optional] 

### Return type

[**GoogleWorkspaceProvider**](GoogleWorkspaceProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_google_workspace_retrieve**
> GoogleWorkspaceProvider providers_google_workspace_retrieve(id)



GoogleWorkspaceProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.google_workspace_provider import GoogleWorkspaceProvider
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this Google Workspace Provider.

    try:
        api_response = api_instance.providers_google_workspace_retrieve(id)
        print("The response of ProvidersApi->providers_google_workspace_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_google_workspace_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Google Workspace Provider. | 

### Return type

[**GoogleWorkspaceProvider**](GoogleWorkspaceProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_google_workspace_sync_status_retrieve**
> SyncStatus providers_google_workspace_sync_status_retrieve(id)



Get provider's sync status

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.sync_status import SyncStatus
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this Google Workspace Provider.

    try:
        api_response = api_instance.providers_google_workspace_sync_status_retrieve(id)
        print("The response of ProvidersApi->providers_google_workspace_sync_status_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_google_workspace_sync_status_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Google Workspace Provider. | 

### Return type

[**SyncStatus**](SyncStatus.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Task not found |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_google_workspace_update**
> GoogleWorkspaceProvider providers_google_workspace_update(id, google_workspace_provider_request)



GoogleWorkspaceProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.google_workspace_provider import GoogleWorkspaceProvider
from authentik_openapi.models.google_workspace_provider_request import GoogleWorkspaceProviderRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this Google Workspace Provider.
    google_workspace_provider_request = authentik_openapi.GoogleWorkspaceProviderRequest() # GoogleWorkspaceProviderRequest | 

    try:
        api_response = api_instance.providers_google_workspace_update(id, google_workspace_provider_request)
        print("The response of ProvidersApi->providers_google_workspace_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_google_workspace_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Google Workspace Provider. | 
 **google_workspace_provider_request** | [**GoogleWorkspaceProviderRequest**](GoogleWorkspaceProviderRequest.md)|  | 

### Return type

[**GoogleWorkspaceProvider**](GoogleWorkspaceProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_google_workspace_used_by_list**
> List[UsedBy] providers_google_workspace_used_by_list(id)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this Google Workspace Provider.

    try:
        api_response = api_instance.providers_google_workspace_used_by_list(id)
        print("The response of ProvidersApi->providers_google_workspace_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_google_workspace_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Google Workspace Provider. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_google_workspace_users_create**
> GoogleWorkspaceProviderUser providers_google_workspace_users_create(google_workspace_provider_user_request)



GoogleWorkspaceProviderUser Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.google_workspace_provider_user import GoogleWorkspaceProviderUser
from authentik_openapi.models.google_workspace_provider_user_request import GoogleWorkspaceProviderUserRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    google_workspace_provider_user_request = authentik_openapi.GoogleWorkspaceProviderUserRequest() # GoogleWorkspaceProviderUserRequest | 

    try:
        api_response = api_instance.providers_google_workspace_users_create(google_workspace_provider_user_request)
        print("The response of ProvidersApi->providers_google_workspace_users_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_google_workspace_users_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_workspace_provider_user_request** | [**GoogleWorkspaceProviderUserRequest**](GoogleWorkspaceProviderUserRequest.md)|  | 

### Return type

[**GoogleWorkspaceProviderUser**](GoogleWorkspaceProviderUser.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_google_workspace_users_destroy**
> providers_google_workspace_users_destroy(id)



GoogleWorkspaceProviderUser Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 'id_example' # str | A UUID string identifying this Google Workspace Provider User.

    try:
        api_instance.providers_google_workspace_users_destroy(id)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_google_workspace_users_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this Google Workspace Provider User. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_google_workspace_users_list**
> PaginatedGoogleWorkspaceProviderUserList providers_google_workspace_users_list(ordering=ordering, page=page, page_size=page_size, provider__id=provider__id, search=search, user__id=user__id, user__username=user__username)



GoogleWorkspaceProviderUser Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_google_workspace_provider_user_list import PaginatedGoogleWorkspaceProviderUserList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    provider__id = 56 # int |  (optional)
    search = 'search_example' # str | A search term. (optional)
    user__id = 56 # int |  (optional)
    user__username = 'user__username_example' # str |  (optional)

    try:
        api_response = api_instance.providers_google_workspace_users_list(ordering=ordering, page=page, page_size=page_size, provider__id=provider__id, search=search, user__id=user__id, user__username=user__username)
        print("The response of ProvidersApi->providers_google_workspace_users_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_google_workspace_users_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **provider__id** | **int**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **user__id** | **int**|  | [optional] 
 **user__username** | **str**|  | [optional] 

### Return type

[**PaginatedGoogleWorkspaceProviderUserList**](PaginatedGoogleWorkspaceProviderUserList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_google_workspace_users_retrieve**
> GoogleWorkspaceProviderUser providers_google_workspace_users_retrieve(id)



GoogleWorkspaceProviderUser Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.google_workspace_provider_user import GoogleWorkspaceProviderUser
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 'id_example' # str | A UUID string identifying this Google Workspace Provider User.

    try:
        api_response = api_instance.providers_google_workspace_users_retrieve(id)
        print("The response of ProvidersApi->providers_google_workspace_users_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_google_workspace_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this Google Workspace Provider User. | 

### Return type

[**GoogleWorkspaceProviderUser**](GoogleWorkspaceProviderUser.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_google_workspace_users_used_by_list**
> List[UsedBy] providers_google_workspace_users_used_by_list(id)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 'id_example' # str | A UUID string identifying this Google Workspace Provider User.

    try:
        api_response = api_instance.providers_google_workspace_users_used_by_list(id)
        print("The response of ProvidersApi->providers_google_workspace_users_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_google_workspace_users_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this Google Workspace Provider User. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_ldap_create**
> LDAPProvider providers_ldap_create(ldap_provider_request)



LDAPProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.ldap_provider import LDAPProvider
from authentik_openapi.models.ldap_provider_request import LDAPProviderRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    ldap_provider_request = authentik_openapi.LDAPProviderRequest() # LDAPProviderRequest | 

    try:
        api_response = api_instance.providers_ldap_create(ldap_provider_request)
        print("The response of ProvidersApi->providers_ldap_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_ldap_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldap_provider_request** | [**LDAPProviderRequest**](LDAPProviderRequest.md)|  | 

### Return type

[**LDAPProvider**](LDAPProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_ldap_destroy**
> providers_ldap_destroy(id)



LDAPProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this LDAP Provider.

    try:
        api_instance.providers_ldap_destroy(id)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_ldap_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this LDAP Provider. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_ldap_list**
> PaginatedLDAPProviderList providers_ldap_list(application__isnull=application__isnull, authorization_flow__slug__iexact=authorization_flow__slug__iexact, base_dn__iexact=base_dn__iexact, certificate__kp_uuid__iexact=certificate__kp_uuid__iexact, certificate__name__iexact=certificate__name__iexact, gid_start_number__iexact=gid_start_number__iexact, name__iexact=name__iexact, ordering=ordering, page=page, page_size=page_size, search=search, search_group__group_uuid__iexact=search_group__group_uuid__iexact, search_group__name__iexact=search_group__name__iexact, tls_server_name__iexact=tls_server_name__iexact, uid_start_number__iexact=uid_start_number__iexact)



LDAPProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_ldap_provider_list import PaginatedLDAPProviderList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    application__isnull = True # bool |  (optional)
    authorization_flow__slug__iexact = 'authorization_flow__slug__iexact_example' # str |  (optional)
    base_dn__iexact = 'base_dn__iexact_example' # str |  (optional)
    certificate__kp_uuid__iexact = 'certificate__kp_uuid__iexact_example' # str |  (optional)
    certificate__name__iexact = 'certificate__name__iexact_example' # str |  (optional)
    gid_start_number__iexact = 56 # int |  (optional)
    name__iexact = 'name__iexact_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    search_group__group_uuid__iexact = 'search_group__group_uuid__iexact_example' # str |  (optional)
    search_group__name__iexact = 'search_group__name__iexact_example' # str |  (optional)
    tls_server_name__iexact = 'tls_server_name__iexact_example' # str |  (optional)
    uid_start_number__iexact = 56 # int |  (optional)

    try:
        api_response = api_instance.providers_ldap_list(application__isnull=application__isnull, authorization_flow__slug__iexact=authorization_flow__slug__iexact, base_dn__iexact=base_dn__iexact, certificate__kp_uuid__iexact=certificate__kp_uuid__iexact, certificate__name__iexact=certificate__name__iexact, gid_start_number__iexact=gid_start_number__iexact, name__iexact=name__iexact, ordering=ordering, page=page, page_size=page_size, search=search, search_group__group_uuid__iexact=search_group__group_uuid__iexact, search_group__name__iexact=search_group__name__iexact, tls_server_name__iexact=tls_server_name__iexact, uid_start_number__iexact=uid_start_number__iexact)
        print("The response of ProvidersApi->providers_ldap_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_ldap_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application__isnull** | **bool**|  | [optional] 
 **authorization_flow__slug__iexact** | **str**|  | [optional] 
 **base_dn__iexact** | **str**|  | [optional] 
 **certificate__kp_uuid__iexact** | **str**|  | [optional] 
 **certificate__name__iexact** | **str**|  | [optional] 
 **gid_start_number__iexact** | **int**|  | [optional] 
 **name__iexact** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **search_group__group_uuid__iexact** | **str**|  | [optional] 
 **search_group__name__iexact** | **str**|  | [optional] 
 **tls_server_name__iexact** | **str**|  | [optional] 
 **uid_start_number__iexact** | **int**|  | [optional] 

### Return type

[**PaginatedLDAPProviderList**](PaginatedLDAPProviderList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_ldap_partial_update**
> LDAPProvider providers_ldap_partial_update(id, patched_ldap_provider_request=patched_ldap_provider_request)



LDAPProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.ldap_provider import LDAPProvider
from authentik_openapi.models.patched_ldap_provider_request import PatchedLDAPProviderRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this LDAP Provider.
    patched_ldap_provider_request = authentik_openapi.PatchedLDAPProviderRequest() # PatchedLDAPProviderRequest |  (optional)

    try:
        api_response = api_instance.providers_ldap_partial_update(id, patched_ldap_provider_request=patched_ldap_provider_request)
        print("The response of ProvidersApi->providers_ldap_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_ldap_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this LDAP Provider. | 
 **patched_ldap_provider_request** | [**PatchedLDAPProviderRequest**](PatchedLDAPProviderRequest.md)|  | [optional] 

### Return type

[**LDAPProvider**](LDAPProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_ldap_retrieve**
> LDAPProvider providers_ldap_retrieve(id)



LDAPProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.ldap_provider import LDAPProvider
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this LDAP Provider.

    try:
        api_response = api_instance.providers_ldap_retrieve(id)
        print("The response of ProvidersApi->providers_ldap_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_ldap_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this LDAP Provider. | 

### Return type

[**LDAPProvider**](LDAPProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_ldap_update**
> LDAPProvider providers_ldap_update(id, ldap_provider_request)



LDAPProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.ldap_provider import LDAPProvider
from authentik_openapi.models.ldap_provider_request import LDAPProviderRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this LDAP Provider.
    ldap_provider_request = authentik_openapi.LDAPProviderRequest() # LDAPProviderRequest | 

    try:
        api_response = api_instance.providers_ldap_update(id, ldap_provider_request)
        print("The response of ProvidersApi->providers_ldap_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_ldap_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this LDAP Provider. | 
 **ldap_provider_request** | [**LDAPProviderRequest**](LDAPProviderRequest.md)|  | 

### Return type

[**LDAPProvider**](LDAPProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_ldap_used_by_list**
> List[UsedBy] providers_ldap_used_by_list(id)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this LDAP Provider.

    try:
        api_response = api_instance.providers_ldap_used_by_list(id)
        print("The response of ProvidersApi->providers_ldap_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_ldap_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this LDAP Provider. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_microsoft_entra_create**
> MicrosoftEntraProvider providers_microsoft_entra_create(microsoft_entra_provider_request)



MicrosoftEntraProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.microsoft_entra_provider import MicrosoftEntraProvider
from authentik_openapi.models.microsoft_entra_provider_request import MicrosoftEntraProviderRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    microsoft_entra_provider_request = authentik_openapi.MicrosoftEntraProviderRequest() # MicrosoftEntraProviderRequest | 

    try:
        api_response = api_instance.providers_microsoft_entra_create(microsoft_entra_provider_request)
        print("The response of ProvidersApi->providers_microsoft_entra_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_microsoft_entra_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **microsoft_entra_provider_request** | [**MicrosoftEntraProviderRequest**](MicrosoftEntraProviderRequest.md)|  | 

### Return type

[**MicrosoftEntraProvider**](MicrosoftEntraProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_microsoft_entra_destroy**
> providers_microsoft_entra_destroy(id)



MicrosoftEntraProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this Microsoft Entra Provider.

    try:
        api_instance.providers_microsoft_entra_destroy(id)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_microsoft_entra_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Microsoft Entra Provider. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_microsoft_entra_groups_create**
> MicrosoftEntraProviderGroup providers_microsoft_entra_groups_create(microsoft_entra_provider_group_request)



MicrosoftEntraProviderGroup Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.microsoft_entra_provider_group import MicrosoftEntraProviderGroup
from authentik_openapi.models.microsoft_entra_provider_group_request import MicrosoftEntraProviderGroupRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    microsoft_entra_provider_group_request = authentik_openapi.MicrosoftEntraProviderGroupRequest() # MicrosoftEntraProviderGroupRequest | 

    try:
        api_response = api_instance.providers_microsoft_entra_groups_create(microsoft_entra_provider_group_request)
        print("The response of ProvidersApi->providers_microsoft_entra_groups_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_microsoft_entra_groups_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **microsoft_entra_provider_group_request** | [**MicrosoftEntraProviderGroupRequest**](MicrosoftEntraProviderGroupRequest.md)|  | 

### Return type

[**MicrosoftEntraProviderGroup**](MicrosoftEntraProviderGroup.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_microsoft_entra_groups_destroy**
> providers_microsoft_entra_groups_destroy(id)



MicrosoftEntraProviderGroup Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 'id_example' # str | A UUID string identifying this Microsoft Entra Provider Group.

    try:
        api_instance.providers_microsoft_entra_groups_destroy(id)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_microsoft_entra_groups_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this Microsoft Entra Provider Group. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_microsoft_entra_groups_list**
> PaginatedMicrosoftEntraProviderGroupList providers_microsoft_entra_groups_list(group__group_uuid=group__group_uuid, group__name=group__name, ordering=ordering, page=page, page_size=page_size, provider__id=provider__id, search=search)



MicrosoftEntraProviderGroup Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_microsoft_entra_provider_group_list import PaginatedMicrosoftEntraProviderGroupList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    group__group_uuid = 'group__group_uuid_example' # str |  (optional)
    group__name = 'group__name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    provider__id = 56 # int |  (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.providers_microsoft_entra_groups_list(group__group_uuid=group__group_uuid, group__name=group__name, ordering=ordering, page=page, page_size=page_size, provider__id=provider__id, search=search)
        print("The response of ProvidersApi->providers_microsoft_entra_groups_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_microsoft_entra_groups_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group__group_uuid** | **str**|  | [optional] 
 **group__name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **provider__id** | **int**|  | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedMicrosoftEntraProviderGroupList**](PaginatedMicrosoftEntraProviderGroupList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_microsoft_entra_groups_retrieve**
> MicrosoftEntraProviderGroup providers_microsoft_entra_groups_retrieve(id)



MicrosoftEntraProviderGroup Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.microsoft_entra_provider_group import MicrosoftEntraProviderGroup
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 'id_example' # str | A UUID string identifying this Microsoft Entra Provider Group.

    try:
        api_response = api_instance.providers_microsoft_entra_groups_retrieve(id)
        print("The response of ProvidersApi->providers_microsoft_entra_groups_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_microsoft_entra_groups_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this Microsoft Entra Provider Group. | 

### Return type

[**MicrosoftEntraProviderGroup**](MicrosoftEntraProviderGroup.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_microsoft_entra_groups_used_by_list**
> List[UsedBy] providers_microsoft_entra_groups_used_by_list(id)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 'id_example' # str | A UUID string identifying this Microsoft Entra Provider Group.

    try:
        api_response = api_instance.providers_microsoft_entra_groups_used_by_list(id)
        print("The response of ProvidersApi->providers_microsoft_entra_groups_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_microsoft_entra_groups_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this Microsoft Entra Provider Group. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_microsoft_entra_list**
> PaginatedMicrosoftEntraProviderList providers_microsoft_entra_list(exclude_users_service_account=exclude_users_service_account, filter_group=filter_group, name=name, ordering=ordering, page=page, page_size=page_size, search=search)



MicrosoftEntraProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_microsoft_entra_provider_list import PaginatedMicrosoftEntraProviderList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    exclude_users_service_account = True # bool |  (optional)
    filter_group = 'filter_group_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.providers_microsoft_entra_list(exclude_users_service_account=exclude_users_service_account, filter_group=filter_group, name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of ProvidersApi->providers_microsoft_entra_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_microsoft_entra_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exclude_users_service_account** | **bool**|  | [optional] 
 **filter_group** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedMicrosoftEntraProviderList**](PaginatedMicrosoftEntraProviderList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_microsoft_entra_partial_update**
> MicrosoftEntraProvider providers_microsoft_entra_partial_update(id, patched_microsoft_entra_provider_request=patched_microsoft_entra_provider_request)



MicrosoftEntraProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.microsoft_entra_provider import MicrosoftEntraProvider
from authentik_openapi.models.patched_microsoft_entra_provider_request import PatchedMicrosoftEntraProviderRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this Microsoft Entra Provider.
    patched_microsoft_entra_provider_request = authentik_openapi.PatchedMicrosoftEntraProviderRequest() # PatchedMicrosoftEntraProviderRequest |  (optional)

    try:
        api_response = api_instance.providers_microsoft_entra_partial_update(id, patched_microsoft_entra_provider_request=patched_microsoft_entra_provider_request)
        print("The response of ProvidersApi->providers_microsoft_entra_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_microsoft_entra_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Microsoft Entra Provider. | 
 **patched_microsoft_entra_provider_request** | [**PatchedMicrosoftEntraProviderRequest**](PatchedMicrosoftEntraProviderRequest.md)|  | [optional] 

### Return type

[**MicrosoftEntraProvider**](MicrosoftEntraProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_microsoft_entra_retrieve**
> MicrosoftEntraProvider providers_microsoft_entra_retrieve(id)



MicrosoftEntraProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.microsoft_entra_provider import MicrosoftEntraProvider
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this Microsoft Entra Provider.

    try:
        api_response = api_instance.providers_microsoft_entra_retrieve(id)
        print("The response of ProvidersApi->providers_microsoft_entra_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_microsoft_entra_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Microsoft Entra Provider. | 

### Return type

[**MicrosoftEntraProvider**](MicrosoftEntraProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_microsoft_entra_sync_status_retrieve**
> SyncStatus providers_microsoft_entra_sync_status_retrieve(id)



Get provider's sync status

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.sync_status import SyncStatus
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this Microsoft Entra Provider.

    try:
        api_response = api_instance.providers_microsoft_entra_sync_status_retrieve(id)
        print("The response of ProvidersApi->providers_microsoft_entra_sync_status_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_microsoft_entra_sync_status_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Microsoft Entra Provider. | 

### Return type

[**SyncStatus**](SyncStatus.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Task not found |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_microsoft_entra_update**
> MicrosoftEntraProvider providers_microsoft_entra_update(id, microsoft_entra_provider_request)



MicrosoftEntraProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.microsoft_entra_provider import MicrosoftEntraProvider
from authentik_openapi.models.microsoft_entra_provider_request import MicrosoftEntraProviderRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this Microsoft Entra Provider.
    microsoft_entra_provider_request = authentik_openapi.MicrosoftEntraProviderRequest() # MicrosoftEntraProviderRequest | 

    try:
        api_response = api_instance.providers_microsoft_entra_update(id, microsoft_entra_provider_request)
        print("The response of ProvidersApi->providers_microsoft_entra_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_microsoft_entra_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Microsoft Entra Provider. | 
 **microsoft_entra_provider_request** | [**MicrosoftEntraProviderRequest**](MicrosoftEntraProviderRequest.md)|  | 

### Return type

[**MicrosoftEntraProvider**](MicrosoftEntraProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_microsoft_entra_used_by_list**
> List[UsedBy] providers_microsoft_entra_used_by_list(id)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this Microsoft Entra Provider.

    try:
        api_response = api_instance.providers_microsoft_entra_used_by_list(id)
        print("The response of ProvidersApi->providers_microsoft_entra_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_microsoft_entra_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Microsoft Entra Provider. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_microsoft_entra_users_create**
> MicrosoftEntraProviderUser providers_microsoft_entra_users_create(microsoft_entra_provider_user_request)



MicrosoftEntraProviderUser Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.microsoft_entra_provider_user import MicrosoftEntraProviderUser
from authentik_openapi.models.microsoft_entra_provider_user_request import MicrosoftEntraProviderUserRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    microsoft_entra_provider_user_request = authentik_openapi.MicrosoftEntraProviderUserRequest() # MicrosoftEntraProviderUserRequest | 

    try:
        api_response = api_instance.providers_microsoft_entra_users_create(microsoft_entra_provider_user_request)
        print("The response of ProvidersApi->providers_microsoft_entra_users_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_microsoft_entra_users_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **microsoft_entra_provider_user_request** | [**MicrosoftEntraProviderUserRequest**](MicrosoftEntraProviderUserRequest.md)|  | 

### Return type

[**MicrosoftEntraProviderUser**](MicrosoftEntraProviderUser.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_microsoft_entra_users_destroy**
> providers_microsoft_entra_users_destroy(id)



MicrosoftEntraProviderUser Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 'id_example' # str | A UUID string identifying this Microsoft Entra Provider User.

    try:
        api_instance.providers_microsoft_entra_users_destroy(id)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_microsoft_entra_users_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this Microsoft Entra Provider User. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_microsoft_entra_users_list**
> PaginatedMicrosoftEntraProviderUserList providers_microsoft_entra_users_list(ordering=ordering, page=page, page_size=page_size, provider__id=provider__id, search=search, user__id=user__id, user__username=user__username)



MicrosoftEntraProviderUser Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_microsoft_entra_provider_user_list import PaginatedMicrosoftEntraProviderUserList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    provider__id = 56 # int |  (optional)
    search = 'search_example' # str | A search term. (optional)
    user__id = 56 # int |  (optional)
    user__username = 'user__username_example' # str |  (optional)

    try:
        api_response = api_instance.providers_microsoft_entra_users_list(ordering=ordering, page=page, page_size=page_size, provider__id=provider__id, search=search, user__id=user__id, user__username=user__username)
        print("The response of ProvidersApi->providers_microsoft_entra_users_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_microsoft_entra_users_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **provider__id** | **int**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **user__id** | **int**|  | [optional] 
 **user__username** | **str**|  | [optional] 

### Return type

[**PaginatedMicrosoftEntraProviderUserList**](PaginatedMicrosoftEntraProviderUserList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_microsoft_entra_users_retrieve**
> MicrosoftEntraProviderUser providers_microsoft_entra_users_retrieve(id)



MicrosoftEntraProviderUser Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.microsoft_entra_provider_user import MicrosoftEntraProviderUser
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 'id_example' # str | A UUID string identifying this Microsoft Entra Provider User.

    try:
        api_response = api_instance.providers_microsoft_entra_users_retrieve(id)
        print("The response of ProvidersApi->providers_microsoft_entra_users_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_microsoft_entra_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this Microsoft Entra Provider User. | 

### Return type

[**MicrosoftEntraProviderUser**](MicrosoftEntraProviderUser.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_microsoft_entra_users_used_by_list**
> List[UsedBy] providers_microsoft_entra_users_used_by_list(id)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 'id_example' # str | A UUID string identifying this Microsoft Entra Provider User.

    try:
        api_response = api_instance.providers_microsoft_entra_users_used_by_list(id)
        print("The response of ProvidersApi->providers_microsoft_entra_users_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_microsoft_entra_users_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this Microsoft Entra Provider User. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_oauth2_create**
> OAuth2Provider providers_oauth2_create(o_auth2_provider_request)



OAuth2Provider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.o_auth2_provider import OAuth2Provider
from authentik_openapi.models.o_auth2_provider_request import OAuth2ProviderRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    o_auth2_provider_request = authentik_openapi.OAuth2ProviderRequest() # OAuth2ProviderRequest | 

    try:
        api_response = api_instance.providers_oauth2_create(o_auth2_provider_request)
        print("The response of ProvidersApi->providers_oauth2_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_oauth2_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_auth2_provider_request** | [**OAuth2ProviderRequest**](OAuth2ProviderRequest.md)|  | 

### Return type

[**OAuth2Provider**](OAuth2Provider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_oauth2_destroy**
> providers_oauth2_destroy(id)



OAuth2Provider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this OAuth2/OpenID Provider.

    try:
        api_instance.providers_oauth2_destroy(id)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_oauth2_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this OAuth2/OpenID Provider. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_oauth2_list**
> PaginatedOAuth2ProviderList providers_oauth2_list(access_code_validity=access_code_validity, access_token_validity=access_token_validity, application=application, authorization_flow=authorization_flow, client_id=client_id, client_type=client_type, include_claims_in_id_token=include_claims_in_id_token, issuer_mode=issuer_mode, name=name, ordering=ordering, page=page, page_size=page_size, property_mappings=property_mappings, redirect_uris=redirect_uris, refresh_token_validity=refresh_token_validity, search=search, signing_key=signing_key, sub_mode=sub_mode)



OAuth2Provider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_o_auth2_provider_list import PaginatedOAuth2ProviderList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    access_code_validity = 'access_code_validity_example' # str |  (optional)
    access_token_validity = 'access_token_validity_example' # str |  (optional)
    application = 'application_example' # str |  (optional)
    authorization_flow = 'authorization_flow_example' # str |  (optional)
    client_id = 'client_id_example' # str |  (optional)
    client_type = 'client_type_example' # str | Confidential clients are capable of maintaining the confidentiality of their credentials. Public clients are incapable   (optional)
    include_claims_in_id_token = True # bool |  (optional)
    issuer_mode = 'issuer_mode_example' # str | Configure how the issuer field of the ID Token should be filled.   (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    property_mappings = ['property_mappings_example'] # List[str] |  (optional)
    redirect_uris = 'redirect_uris_example' # str |  (optional)
    refresh_token_validity = 'refresh_token_validity_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)
    signing_key = 'signing_key_example' # str |  (optional)
    sub_mode = 'sub_mode_example' # str | Configure what data should be used as unique User Identifier. For most cases, the default should be fine.   (optional)

    try:
        api_response = api_instance.providers_oauth2_list(access_code_validity=access_code_validity, access_token_validity=access_token_validity, application=application, authorization_flow=authorization_flow, client_id=client_id, client_type=client_type, include_claims_in_id_token=include_claims_in_id_token, issuer_mode=issuer_mode, name=name, ordering=ordering, page=page, page_size=page_size, property_mappings=property_mappings, redirect_uris=redirect_uris, refresh_token_validity=refresh_token_validity, search=search, signing_key=signing_key, sub_mode=sub_mode)
        print("The response of ProvidersApi->providers_oauth2_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_oauth2_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_code_validity** | **str**|  | [optional] 
 **access_token_validity** | **str**|  | [optional] 
 **application** | **str**|  | [optional] 
 **authorization_flow** | **str**|  | [optional] 
 **client_id** | **str**|  | [optional] 
 **client_type** | **str**| Confidential clients are capable of maintaining the confidentiality of their credentials. Public clients are incapable   | [optional] 
 **include_claims_in_id_token** | **bool**|  | [optional] 
 **issuer_mode** | **str**| Configure how the issuer field of the ID Token should be filled.   | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **property_mappings** | [**List[str]**](str.md)|  | [optional] 
 **redirect_uris** | **str**|  | [optional] 
 **refresh_token_validity** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **signing_key** | **str**|  | [optional] 
 **sub_mode** | **str**| Configure what data should be used as unique User Identifier. For most cases, the default should be fine.   | [optional] 

### Return type

[**PaginatedOAuth2ProviderList**](PaginatedOAuth2ProviderList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_oauth2_partial_update**
> OAuth2Provider providers_oauth2_partial_update(id, patched_o_auth2_provider_request=patched_o_auth2_provider_request)



OAuth2Provider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.o_auth2_provider import OAuth2Provider
from authentik_openapi.models.patched_o_auth2_provider_request import PatchedOAuth2ProviderRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this OAuth2/OpenID Provider.
    patched_o_auth2_provider_request = authentik_openapi.PatchedOAuth2ProviderRequest() # PatchedOAuth2ProviderRequest |  (optional)

    try:
        api_response = api_instance.providers_oauth2_partial_update(id, patched_o_auth2_provider_request=patched_o_auth2_provider_request)
        print("The response of ProvidersApi->providers_oauth2_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_oauth2_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this OAuth2/OpenID Provider. | 
 **patched_o_auth2_provider_request** | [**PatchedOAuth2ProviderRequest**](PatchedOAuth2ProviderRequest.md)|  | [optional] 

### Return type

[**OAuth2Provider**](OAuth2Provider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_oauth2_preview_user_retrieve**
> PropertyMappingPreview providers_oauth2_preview_user_retrieve(id, for_user=for_user)



Preview user data for provider

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.property_mapping_preview import PropertyMappingPreview
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this OAuth2/OpenID Provider.
    for_user = 56 # int |  (optional)

    try:
        api_response = api_instance.providers_oauth2_preview_user_retrieve(id, for_user=for_user)
        print("The response of ProvidersApi->providers_oauth2_preview_user_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_oauth2_preview_user_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this OAuth2/OpenID Provider. | 
 **for_user** | **int**|  | [optional] 

### Return type

[**PropertyMappingPreview**](PropertyMappingPreview.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_oauth2_retrieve**
> OAuth2Provider providers_oauth2_retrieve(id)



OAuth2Provider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.o_auth2_provider import OAuth2Provider
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this OAuth2/OpenID Provider.

    try:
        api_response = api_instance.providers_oauth2_retrieve(id)
        print("The response of ProvidersApi->providers_oauth2_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_oauth2_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this OAuth2/OpenID Provider. | 

### Return type

[**OAuth2Provider**](OAuth2Provider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_oauth2_setup_urls_retrieve**
> OAuth2ProviderSetupURLs providers_oauth2_setup_urls_retrieve(id)



Get Providers setup URLs

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.o_auth2_provider_setup_urls import OAuth2ProviderSetupURLs
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this OAuth2/OpenID Provider.

    try:
        api_response = api_instance.providers_oauth2_setup_urls_retrieve(id)
        print("The response of ProvidersApi->providers_oauth2_setup_urls_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_oauth2_setup_urls_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this OAuth2/OpenID Provider. | 

### Return type

[**OAuth2ProviderSetupURLs**](OAuth2ProviderSetupURLs.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Provider has no application assigned |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_oauth2_update**
> OAuth2Provider providers_oauth2_update(id, o_auth2_provider_request)



OAuth2Provider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.o_auth2_provider import OAuth2Provider
from authentik_openapi.models.o_auth2_provider_request import OAuth2ProviderRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this OAuth2/OpenID Provider.
    o_auth2_provider_request = authentik_openapi.OAuth2ProviderRequest() # OAuth2ProviderRequest | 

    try:
        api_response = api_instance.providers_oauth2_update(id, o_auth2_provider_request)
        print("The response of ProvidersApi->providers_oauth2_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_oauth2_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this OAuth2/OpenID Provider. | 
 **o_auth2_provider_request** | [**OAuth2ProviderRequest**](OAuth2ProviderRequest.md)|  | 

### Return type

[**OAuth2Provider**](OAuth2Provider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_oauth2_used_by_list**
> List[UsedBy] providers_oauth2_used_by_list(id)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this OAuth2/OpenID Provider.

    try:
        api_response = api_instance.providers_oauth2_used_by_list(id)
        print("The response of ProvidersApi->providers_oauth2_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_oauth2_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this OAuth2/OpenID Provider. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_proxy_create**
> ProxyProvider providers_proxy_create(proxy_provider_request)



ProxyProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.proxy_provider import ProxyProvider
from authentik_openapi.models.proxy_provider_request import ProxyProviderRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    proxy_provider_request = authentik_openapi.ProxyProviderRequest() # ProxyProviderRequest | 

    try:
        api_response = api_instance.providers_proxy_create(proxy_provider_request)
        print("The response of ProvidersApi->providers_proxy_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_proxy_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **proxy_provider_request** | [**ProxyProviderRequest**](ProxyProviderRequest.md)|  | 

### Return type

[**ProxyProvider**](ProxyProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_proxy_destroy**
> providers_proxy_destroy(id)



ProxyProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this Proxy Provider.

    try:
        api_instance.providers_proxy_destroy(id)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_proxy_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Proxy Provider. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_proxy_list**
> PaginatedProxyProviderList providers_proxy_list(application__isnull=application__isnull, authorization_flow__slug__iexact=authorization_flow__slug__iexact, basic_auth_enabled__iexact=basic_auth_enabled__iexact, basic_auth_password_attribute__iexact=basic_auth_password_attribute__iexact, basic_auth_user_attribute__iexact=basic_auth_user_attribute__iexact, certificate__kp_uuid__iexact=certificate__kp_uuid__iexact, certificate__name__iexact=certificate__name__iexact, cookie_domain__iexact=cookie_domain__iexact, external_host__iexact=external_host__iexact, internal_host__iexact=internal_host__iexact, internal_host_ssl_validation__iexact=internal_host_ssl_validation__iexact, mode__iexact=mode__iexact, name__iexact=name__iexact, ordering=ordering, page=page, page_size=page_size, property_mappings__iexact=property_mappings__iexact, redirect_uris__iexact=redirect_uris__iexact, search=search, skip_path_regex__iexact=skip_path_regex__iexact)



ProxyProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_proxy_provider_list import PaginatedProxyProviderList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    application__isnull = True # bool |  (optional)
    authorization_flow__slug__iexact = 'authorization_flow__slug__iexact_example' # str |  (optional)
    basic_auth_enabled__iexact = True # bool |  (optional)
    basic_auth_password_attribute__iexact = 'basic_auth_password_attribute__iexact_example' # str |  (optional)
    basic_auth_user_attribute__iexact = 'basic_auth_user_attribute__iexact_example' # str |  (optional)
    certificate__kp_uuid__iexact = 'certificate__kp_uuid__iexact_example' # str |  (optional)
    certificate__name__iexact = 'certificate__name__iexact_example' # str |  (optional)
    cookie_domain__iexact = 'cookie_domain__iexact_example' # str |  (optional)
    external_host__iexact = 'external_host__iexact_example' # str |  (optional)
    internal_host__iexact = 'internal_host__iexact_example' # str |  (optional)
    internal_host_ssl_validation__iexact = True # bool |  (optional)
    mode__iexact = 'mode__iexact_example' # str |  (optional)
    name__iexact = 'name__iexact_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    property_mappings__iexact = ['property_mappings__iexact_example'] # List[str] |  (optional)
    redirect_uris__iexact = 'redirect_uris__iexact_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)
    skip_path_regex__iexact = 'skip_path_regex__iexact_example' # str |  (optional)

    try:
        api_response = api_instance.providers_proxy_list(application__isnull=application__isnull, authorization_flow__slug__iexact=authorization_flow__slug__iexact, basic_auth_enabled__iexact=basic_auth_enabled__iexact, basic_auth_password_attribute__iexact=basic_auth_password_attribute__iexact, basic_auth_user_attribute__iexact=basic_auth_user_attribute__iexact, certificate__kp_uuid__iexact=certificate__kp_uuid__iexact, certificate__name__iexact=certificate__name__iexact, cookie_domain__iexact=cookie_domain__iexact, external_host__iexact=external_host__iexact, internal_host__iexact=internal_host__iexact, internal_host_ssl_validation__iexact=internal_host_ssl_validation__iexact, mode__iexact=mode__iexact, name__iexact=name__iexact, ordering=ordering, page=page, page_size=page_size, property_mappings__iexact=property_mappings__iexact, redirect_uris__iexact=redirect_uris__iexact, search=search, skip_path_regex__iexact=skip_path_regex__iexact)
        print("The response of ProvidersApi->providers_proxy_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_proxy_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application__isnull** | **bool**|  | [optional] 
 **authorization_flow__slug__iexact** | **str**|  | [optional] 
 **basic_auth_enabled__iexact** | **bool**|  | [optional] 
 **basic_auth_password_attribute__iexact** | **str**|  | [optional] 
 **basic_auth_user_attribute__iexact** | **str**|  | [optional] 
 **certificate__kp_uuid__iexact** | **str**|  | [optional] 
 **certificate__name__iexact** | **str**|  | [optional] 
 **cookie_domain__iexact** | **str**|  | [optional] 
 **external_host__iexact** | **str**|  | [optional] 
 **internal_host__iexact** | **str**|  | [optional] 
 **internal_host_ssl_validation__iexact** | **bool**|  | [optional] 
 **mode__iexact** | **str**|  | [optional] 
 **name__iexact** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **property_mappings__iexact** | [**List[str]**](str.md)|  | [optional] 
 **redirect_uris__iexact** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **skip_path_regex__iexact** | **str**|  | [optional] 

### Return type

[**PaginatedProxyProviderList**](PaginatedProxyProviderList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_proxy_partial_update**
> ProxyProvider providers_proxy_partial_update(id, patched_proxy_provider_request=patched_proxy_provider_request)



ProxyProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_proxy_provider_request import PatchedProxyProviderRequest
from authentik_openapi.models.proxy_provider import ProxyProvider
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this Proxy Provider.
    patched_proxy_provider_request = authentik_openapi.PatchedProxyProviderRequest() # PatchedProxyProviderRequest |  (optional)

    try:
        api_response = api_instance.providers_proxy_partial_update(id, patched_proxy_provider_request=patched_proxy_provider_request)
        print("The response of ProvidersApi->providers_proxy_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_proxy_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Proxy Provider. | 
 **patched_proxy_provider_request** | [**PatchedProxyProviderRequest**](PatchedProxyProviderRequest.md)|  | [optional] 

### Return type

[**ProxyProvider**](ProxyProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_proxy_retrieve**
> ProxyProvider providers_proxy_retrieve(id)



ProxyProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.proxy_provider import ProxyProvider
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this Proxy Provider.

    try:
        api_response = api_instance.providers_proxy_retrieve(id)
        print("The response of ProvidersApi->providers_proxy_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_proxy_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Proxy Provider. | 

### Return type

[**ProxyProvider**](ProxyProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_proxy_update**
> ProxyProvider providers_proxy_update(id, proxy_provider_request)



ProxyProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.proxy_provider import ProxyProvider
from authentik_openapi.models.proxy_provider_request import ProxyProviderRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this Proxy Provider.
    proxy_provider_request = authentik_openapi.ProxyProviderRequest() # ProxyProviderRequest | 

    try:
        api_response = api_instance.providers_proxy_update(id, proxy_provider_request)
        print("The response of ProvidersApi->providers_proxy_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_proxy_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Proxy Provider. | 
 **proxy_provider_request** | [**ProxyProviderRequest**](ProxyProviderRequest.md)|  | 

### Return type

[**ProxyProvider**](ProxyProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_proxy_used_by_list**
> List[UsedBy] providers_proxy_used_by_list(id)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this Proxy Provider.

    try:
        api_response = api_instance.providers_proxy_used_by_list(id)
        print("The response of ProvidersApi->providers_proxy_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_proxy_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Proxy Provider. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_rac_create**
> RACProvider providers_rac_create(rac_provider_request)



RACProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.rac_provider import RACProvider
from authentik_openapi.models.rac_provider_request import RACProviderRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    rac_provider_request = authentik_openapi.RACProviderRequest() # RACProviderRequest | 

    try:
        api_response = api_instance.providers_rac_create(rac_provider_request)
        print("The response of ProvidersApi->providers_rac_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_rac_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rac_provider_request** | [**RACProviderRequest**](RACProviderRequest.md)|  | 

### Return type

[**RACProvider**](RACProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_rac_destroy**
> providers_rac_destroy(id)



RACProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this RAC Provider.

    try:
        api_instance.providers_rac_destroy(id)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_rac_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this RAC Provider. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_rac_list**
> PaginatedRACProviderList providers_rac_list(application__isnull=application__isnull, name__iexact=name__iexact, ordering=ordering, page=page, page_size=page_size, search=search)



RACProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_rac_provider_list import PaginatedRACProviderList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    application__isnull = True # bool |  (optional)
    name__iexact = 'name__iexact_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.providers_rac_list(application__isnull=application__isnull, name__iexact=name__iexact, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of ProvidersApi->providers_rac_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_rac_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application__isnull** | **bool**|  | [optional] 
 **name__iexact** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedRACProviderList**](PaginatedRACProviderList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_rac_partial_update**
> RACProvider providers_rac_partial_update(id, patched_rac_provider_request=patched_rac_provider_request)



RACProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_rac_provider_request import PatchedRACProviderRequest
from authentik_openapi.models.rac_provider import RACProvider
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this RAC Provider.
    patched_rac_provider_request = authentik_openapi.PatchedRACProviderRequest() # PatchedRACProviderRequest |  (optional)

    try:
        api_response = api_instance.providers_rac_partial_update(id, patched_rac_provider_request=patched_rac_provider_request)
        print("The response of ProvidersApi->providers_rac_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_rac_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this RAC Provider. | 
 **patched_rac_provider_request** | [**PatchedRACProviderRequest**](PatchedRACProviderRequest.md)|  | [optional] 

### Return type

[**RACProvider**](RACProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_rac_retrieve**
> RACProvider providers_rac_retrieve(id)



RACProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.rac_provider import RACProvider
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this RAC Provider.

    try:
        api_response = api_instance.providers_rac_retrieve(id)
        print("The response of ProvidersApi->providers_rac_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_rac_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this RAC Provider. | 

### Return type

[**RACProvider**](RACProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_rac_update**
> RACProvider providers_rac_update(id, rac_provider_request)



RACProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.rac_provider import RACProvider
from authentik_openapi.models.rac_provider_request import RACProviderRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this RAC Provider.
    rac_provider_request = authentik_openapi.RACProviderRequest() # RACProviderRequest | 

    try:
        api_response = api_instance.providers_rac_update(id, rac_provider_request)
        print("The response of ProvidersApi->providers_rac_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_rac_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this RAC Provider. | 
 **rac_provider_request** | [**RACProviderRequest**](RACProviderRequest.md)|  | 

### Return type

[**RACProvider**](RACProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_rac_used_by_list**
> List[UsedBy] providers_rac_used_by_list(id)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this RAC Provider.

    try:
        api_response = api_instance.providers_rac_used_by_list(id)
        print("The response of ProvidersApi->providers_rac_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_rac_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this RAC Provider. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_radius_create**
> RadiusProvider providers_radius_create(radius_provider_request)



RadiusProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.radius_provider import RadiusProvider
from authentik_openapi.models.radius_provider_request import RadiusProviderRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    radius_provider_request = authentik_openapi.RadiusProviderRequest() # RadiusProviderRequest | 

    try:
        api_response = api_instance.providers_radius_create(radius_provider_request)
        print("The response of ProvidersApi->providers_radius_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_radius_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **radius_provider_request** | [**RadiusProviderRequest**](RadiusProviderRequest.md)|  | 

### Return type

[**RadiusProvider**](RadiusProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_radius_destroy**
> providers_radius_destroy(id)



RadiusProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this Radius Provider.

    try:
        api_instance.providers_radius_destroy(id)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_radius_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Radius Provider. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_radius_list**
> PaginatedRadiusProviderList providers_radius_list(application__isnull=application__isnull, authorization_flow__slug__iexact=authorization_flow__slug__iexact, client_networks__iexact=client_networks__iexact, name__iexact=name__iexact, ordering=ordering, page=page, page_size=page_size, search=search)



RadiusProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_radius_provider_list import PaginatedRadiusProviderList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    application__isnull = True # bool |  (optional)
    authorization_flow__slug__iexact = 'authorization_flow__slug__iexact_example' # str |  (optional)
    client_networks__iexact = 'client_networks__iexact_example' # str |  (optional)
    name__iexact = 'name__iexact_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.providers_radius_list(application__isnull=application__isnull, authorization_flow__slug__iexact=authorization_flow__slug__iexact, client_networks__iexact=client_networks__iexact, name__iexact=name__iexact, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of ProvidersApi->providers_radius_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_radius_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application__isnull** | **bool**|  | [optional] 
 **authorization_flow__slug__iexact** | **str**|  | [optional] 
 **client_networks__iexact** | **str**|  | [optional] 
 **name__iexact** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedRadiusProviderList**](PaginatedRadiusProviderList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_radius_partial_update**
> RadiusProvider providers_radius_partial_update(id, patched_radius_provider_request=patched_radius_provider_request)



RadiusProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_radius_provider_request import PatchedRadiusProviderRequest
from authentik_openapi.models.radius_provider import RadiusProvider
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this Radius Provider.
    patched_radius_provider_request = authentik_openapi.PatchedRadiusProviderRequest() # PatchedRadiusProviderRequest |  (optional)

    try:
        api_response = api_instance.providers_radius_partial_update(id, patched_radius_provider_request=patched_radius_provider_request)
        print("The response of ProvidersApi->providers_radius_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_radius_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Radius Provider. | 
 **patched_radius_provider_request** | [**PatchedRadiusProviderRequest**](PatchedRadiusProviderRequest.md)|  | [optional] 

### Return type

[**RadiusProvider**](RadiusProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_radius_retrieve**
> RadiusProvider providers_radius_retrieve(id)



RadiusProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.radius_provider import RadiusProvider
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this Radius Provider.

    try:
        api_response = api_instance.providers_radius_retrieve(id)
        print("The response of ProvidersApi->providers_radius_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_radius_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Radius Provider. | 

### Return type

[**RadiusProvider**](RadiusProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_radius_update**
> RadiusProvider providers_radius_update(id, radius_provider_request)



RadiusProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.radius_provider import RadiusProvider
from authentik_openapi.models.radius_provider_request import RadiusProviderRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this Radius Provider.
    radius_provider_request = authentik_openapi.RadiusProviderRequest() # RadiusProviderRequest | 

    try:
        api_response = api_instance.providers_radius_update(id, radius_provider_request)
        print("The response of ProvidersApi->providers_radius_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_radius_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Radius Provider. | 
 **radius_provider_request** | [**RadiusProviderRequest**](RadiusProviderRequest.md)|  | 

### Return type

[**RadiusProvider**](RadiusProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_radius_used_by_list**
> List[UsedBy] providers_radius_used_by_list(id)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this Radius Provider.

    try:
        api_response = api_instance.providers_radius_used_by_list(id)
        print("The response of ProvidersApi->providers_radius_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_radius_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Radius Provider. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_saml_create**
> SAMLProvider providers_saml_create(saml_provider_request)



SAMLProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.saml_provider import SAMLProvider
from authentik_openapi.models.saml_provider_request import SAMLProviderRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    saml_provider_request = authentik_openapi.SAMLProviderRequest() # SAMLProviderRequest | 

    try:
        api_response = api_instance.providers_saml_create(saml_provider_request)
        print("The response of ProvidersApi->providers_saml_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_saml_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saml_provider_request** | [**SAMLProviderRequest**](SAMLProviderRequest.md)|  | 

### Return type

[**SAMLProvider**](SAMLProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_saml_destroy**
> providers_saml_destroy(id)



SAMLProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this SAML Provider.

    try:
        api_instance.providers_saml_destroy(id)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_saml_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SAML Provider. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_saml_import_metadata_create**
> providers_saml_import_metadata_create(name, authorization_flow, file)



Create provider from SAML Metadata

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    name = 'name_example' # str | 
    authorization_flow = 'authorization_flow_example' # str | 
    file = None # bytearray | 

    try:
        api_instance.providers_saml_import_metadata_create(name, authorization_flow, file)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_saml_import_metadata_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **authorization_flow** | **str**|  | 
 **file** | **bytearray**|  | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully imported provider |  -  |
**400** | Bad request |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_saml_list**
> PaginatedSAMLProviderList providers_saml_list(acs_url=acs_url, assertion_valid_not_before=assertion_valid_not_before, assertion_valid_not_on_or_after=assertion_valid_not_on_or_after, audience=audience, authentication_flow=authentication_flow, authorization_flow=authorization_flow, backchannel_application=backchannel_application, default_relay_state=default_relay_state, digest_algorithm=digest_algorithm, is_backchannel=is_backchannel, issuer=issuer, name=name, name_id_mapping=name_id_mapping, ordering=ordering, page=page, page_size=page_size, property_mappings=property_mappings, search=search, session_valid_not_on_or_after=session_valid_not_on_or_after, signature_algorithm=signature_algorithm, signing_kp=signing_kp, sp_binding=sp_binding, verification_kp=verification_kp)



SAMLProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_saml_provider_list import PaginatedSAMLProviderList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    acs_url = 'acs_url_example' # str |  (optional)
    assertion_valid_not_before = 'assertion_valid_not_before_example' # str |  (optional)
    assertion_valid_not_on_or_after = 'assertion_valid_not_on_or_after_example' # str |  (optional)
    audience = 'audience_example' # str |  (optional)
    authentication_flow = 'authentication_flow_example' # str |  (optional)
    authorization_flow = 'authorization_flow_example' # str |  (optional)
    backchannel_application = 'backchannel_application_example' # str |  (optional)
    default_relay_state = 'default_relay_state_example' # str |  (optional)
    digest_algorithm = 'digest_algorithm_example' # str |  (optional)
    is_backchannel = True # bool |  (optional)
    issuer = 'issuer_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    name_id_mapping = 'name_id_mapping_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    property_mappings = ['property_mappings_example'] # List[str] |  (optional)
    search = 'search_example' # str | A search term. (optional)
    session_valid_not_on_or_after = 'session_valid_not_on_or_after_example' # str |  (optional)
    signature_algorithm = 'signature_algorithm_example' # str |  (optional)
    signing_kp = 'signing_kp_example' # str |  (optional)
    sp_binding = 'sp_binding_example' # str | This determines how authentik sends the response back to the Service Provider.   (optional)
    verification_kp = 'verification_kp_example' # str |  (optional)

    try:
        api_response = api_instance.providers_saml_list(acs_url=acs_url, assertion_valid_not_before=assertion_valid_not_before, assertion_valid_not_on_or_after=assertion_valid_not_on_or_after, audience=audience, authentication_flow=authentication_flow, authorization_flow=authorization_flow, backchannel_application=backchannel_application, default_relay_state=default_relay_state, digest_algorithm=digest_algorithm, is_backchannel=is_backchannel, issuer=issuer, name=name, name_id_mapping=name_id_mapping, ordering=ordering, page=page, page_size=page_size, property_mappings=property_mappings, search=search, session_valid_not_on_or_after=session_valid_not_on_or_after, signature_algorithm=signature_algorithm, signing_kp=signing_kp, sp_binding=sp_binding, verification_kp=verification_kp)
        print("The response of ProvidersApi->providers_saml_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_saml_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acs_url** | **str**|  | [optional] 
 **assertion_valid_not_before** | **str**|  | [optional] 
 **assertion_valid_not_on_or_after** | **str**|  | [optional] 
 **audience** | **str**|  | [optional] 
 **authentication_flow** | **str**|  | [optional] 
 **authorization_flow** | **str**|  | [optional] 
 **backchannel_application** | **str**|  | [optional] 
 **default_relay_state** | **str**|  | [optional] 
 **digest_algorithm** | **str**|  | [optional] 
 **is_backchannel** | **bool**|  | [optional] 
 **issuer** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **name_id_mapping** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **property_mappings** | [**List[str]**](str.md)|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **session_valid_not_on_or_after** | **str**|  | [optional] 
 **signature_algorithm** | **str**|  | [optional] 
 **signing_kp** | **str**|  | [optional] 
 **sp_binding** | **str**| This determines how authentik sends the response back to the Service Provider.   | [optional] 
 **verification_kp** | **str**|  | [optional] 

### Return type

[**PaginatedSAMLProviderList**](PaginatedSAMLProviderList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_saml_metadata_retrieve**
> SAMLMetadata providers_saml_metadata_retrieve(id, download=download, force_binding=force_binding)



Return metadata as XML string

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.saml_metadata import SAMLMetadata
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this SAML Provider.
    download = True # bool |  (optional)
    force_binding = 'force_binding_example' # str | Optionally force the metadata to only include one binding. (optional)

    try:
        api_response = api_instance.providers_saml_metadata_retrieve(id, download=download, force_binding=force_binding)
        print("The response of ProvidersApi->providers_saml_metadata_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_saml_metadata_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SAML Provider. | 
 **download** | **bool**|  | [optional] 
 **force_binding** | **str**| Optionally force the metadata to only include one binding. | [optional] 

### Return type

[**SAMLMetadata**](SAMLMetadata.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Provider has no application assigned |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_saml_partial_update**
> SAMLProvider providers_saml_partial_update(id, patched_saml_provider_request=patched_saml_provider_request)



SAMLProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_saml_provider_request import PatchedSAMLProviderRequest
from authentik_openapi.models.saml_provider import SAMLProvider
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this SAML Provider.
    patched_saml_provider_request = authentik_openapi.PatchedSAMLProviderRequest() # PatchedSAMLProviderRequest |  (optional)

    try:
        api_response = api_instance.providers_saml_partial_update(id, patched_saml_provider_request=patched_saml_provider_request)
        print("The response of ProvidersApi->providers_saml_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_saml_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SAML Provider. | 
 **patched_saml_provider_request** | [**PatchedSAMLProviderRequest**](PatchedSAMLProviderRequest.md)|  | [optional] 

### Return type

[**SAMLProvider**](SAMLProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_saml_preview_user_retrieve**
> PropertyMappingPreview providers_saml_preview_user_retrieve(id, for_user=for_user)



Preview user data for provider

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.property_mapping_preview import PropertyMappingPreview
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this SAML Provider.
    for_user = 56 # int |  (optional)

    try:
        api_response = api_instance.providers_saml_preview_user_retrieve(id, for_user=for_user)
        print("The response of ProvidersApi->providers_saml_preview_user_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_saml_preview_user_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SAML Provider. | 
 **for_user** | **int**|  | [optional] 

### Return type

[**PropertyMappingPreview**](PropertyMappingPreview.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_saml_retrieve**
> SAMLProvider providers_saml_retrieve(id)



SAMLProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.saml_provider import SAMLProvider
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this SAML Provider.

    try:
        api_response = api_instance.providers_saml_retrieve(id)
        print("The response of ProvidersApi->providers_saml_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_saml_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SAML Provider. | 

### Return type

[**SAMLProvider**](SAMLProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_saml_update**
> SAMLProvider providers_saml_update(id, saml_provider_request)



SAMLProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.saml_provider import SAMLProvider
from authentik_openapi.models.saml_provider_request import SAMLProviderRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this SAML Provider.
    saml_provider_request = authentik_openapi.SAMLProviderRequest() # SAMLProviderRequest | 

    try:
        api_response = api_instance.providers_saml_update(id, saml_provider_request)
        print("The response of ProvidersApi->providers_saml_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_saml_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SAML Provider. | 
 **saml_provider_request** | [**SAMLProviderRequest**](SAMLProviderRequest.md)|  | 

### Return type

[**SAMLProvider**](SAMLProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_saml_used_by_list**
> List[UsedBy] providers_saml_used_by_list(id)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this SAML Provider.

    try:
        api_response = api_instance.providers_saml_used_by_list(id)
        print("The response of ProvidersApi->providers_saml_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_saml_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SAML Provider. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_scim_create**
> SCIMProvider providers_scim_create(scim_provider_request)



SCIMProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.scim_provider import SCIMProvider
from authentik_openapi.models.scim_provider_request import SCIMProviderRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    scim_provider_request = authentik_openapi.SCIMProviderRequest() # SCIMProviderRequest | 

    try:
        api_response = api_instance.providers_scim_create(scim_provider_request)
        print("The response of ProvidersApi->providers_scim_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_scim_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scim_provider_request** | [**SCIMProviderRequest**](SCIMProviderRequest.md)|  | 

### Return type

[**SCIMProvider**](SCIMProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_scim_destroy**
> providers_scim_destroy(id)



SCIMProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this SCIM Provider.

    try:
        api_instance.providers_scim_destroy(id)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_scim_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SCIM Provider. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_scim_groups_create**
> SCIMProviderGroup providers_scim_groups_create(scim_provider_group_request)



SCIMProviderGroup Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.scim_provider_group import SCIMProviderGroup
from authentik_openapi.models.scim_provider_group_request import SCIMProviderGroupRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    scim_provider_group_request = authentik_openapi.SCIMProviderGroupRequest() # SCIMProviderGroupRequest | 

    try:
        api_response = api_instance.providers_scim_groups_create(scim_provider_group_request)
        print("The response of ProvidersApi->providers_scim_groups_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_scim_groups_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scim_provider_group_request** | [**SCIMProviderGroupRequest**](SCIMProviderGroupRequest.md)|  | 

### Return type

[**SCIMProviderGroup**](SCIMProviderGroup.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_scim_groups_destroy**
> providers_scim_groups_destroy(id)



SCIMProviderGroup Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 'id_example' # str | A UUID string identifying this scim provider group.

    try:
        api_instance.providers_scim_groups_destroy(id)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_scim_groups_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this scim provider group. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_scim_groups_list**
> PaginatedSCIMProviderGroupList providers_scim_groups_list(group__group_uuid=group__group_uuid, group__name=group__name, ordering=ordering, page=page, page_size=page_size, provider__id=provider__id, search=search)



SCIMProviderGroup Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_scim_provider_group_list import PaginatedSCIMProviderGroupList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    group__group_uuid = 'group__group_uuid_example' # str |  (optional)
    group__name = 'group__name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    provider__id = 56 # int |  (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.providers_scim_groups_list(group__group_uuid=group__group_uuid, group__name=group__name, ordering=ordering, page=page, page_size=page_size, provider__id=provider__id, search=search)
        print("The response of ProvidersApi->providers_scim_groups_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_scim_groups_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group__group_uuid** | **str**|  | [optional] 
 **group__name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **provider__id** | **int**|  | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedSCIMProviderGroupList**](PaginatedSCIMProviderGroupList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_scim_groups_retrieve**
> SCIMProviderGroup providers_scim_groups_retrieve(id)



SCIMProviderGroup Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.scim_provider_group import SCIMProviderGroup
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 'id_example' # str | A UUID string identifying this scim provider group.

    try:
        api_response = api_instance.providers_scim_groups_retrieve(id)
        print("The response of ProvidersApi->providers_scim_groups_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_scim_groups_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this scim provider group. | 

### Return type

[**SCIMProviderGroup**](SCIMProviderGroup.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_scim_groups_used_by_list**
> List[UsedBy] providers_scim_groups_used_by_list(id)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 'id_example' # str | A UUID string identifying this scim provider group.

    try:
        api_response = api_instance.providers_scim_groups_used_by_list(id)
        print("The response of ProvidersApi->providers_scim_groups_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_scim_groups_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this scim provider group. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_scim_list**
> PaginatedSCIMProviderList providers_scim_list(exclude_users_service_account=exclude_users_service_account, filter_group=filter_group, name=name, ordering=ordering, page=page, page_size=page_size, search=search, url=url)



SCIMProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_scim_provider_list import PaginatedSCIMProviderList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    exclude_users_service_account = True # bool |  (optional)
    filter_group = 'filter_group_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    url = 'url_example' # str |  (optional)

    try:
        api_response = api_instance.providers_scim_list(exclude_users_service_account=exclude_users_service_account, filter_group=filter_group, name=name, ordering=ordering, page=page, page_size=page_size, search=search, url=url)
        print("The response of ProvidersApi->providers_scim_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_scim_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exclude_users_service_account** | **bool**|  | [optional] 
 **filter_group** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **url** | **str**|  | [optional] 

### Return type

[**PaginatedSCIMProviderList**](PaginatedSCIMProviderList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_scim_partial_update**
> SCIMProvider providers_scim_partial_update(id, patched_scim_provider_request=patched_scim_provider_request)



SCIMProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_scim_provider_request import PatchedSCIMProviderRequest
from authentik_openapi.models.scim_provider import SCIMProvider
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this SCIM Provider.
    patched_scim_provider_request = authentik_openapi.PatchedSCIMProviderRequest() # PatchedSCIMProviderRequest |  (optional)

    try:
        api_response = api_instance.providers_scim_partial_update(id, patched_scim_provider_request=patched_scim_provider_request)
        print("The response of ProvidersApi->providers_scim_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_scim_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SCIM Provider. | 
 **patched_scim_provider_request** | [**PatchedSCIMProviderRequest**](PatchedSCIMProviderRequest.md)|  | [optional] 

### Return type

[**SCIMProvider**](SCIMProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_scim_retrieve**
> SCIMProvider providers_scim_retrieve(id)



SCIMProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.scim_provider import SCIMProvider
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this SCIM Provider.

    try:
        api_response = api_instance.providers_scim_retrieve(id)
        print("The response of ProvidersApi->providers_scim_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_scim_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SCIM Provider. | 

### Return type

[**SCIMProvider**](SCIMProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_scim_sync_status_retrieve**
> SyncStatus providers_scim_sync_status_retrieve(id)



Get provider's sync status

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.sync_status import SyncStatus
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this SCIM Provider.

    try:
        api_response = api_instance.providers_scim_sync_status_retrieve(id)
        print("The response of ProvidersApi->providers_scim_sync_status_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_scim_sync_status_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SCIM Provider. | 

### Return type

[**SyncStatus**](SyncStatus.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Task not found |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_scim_update**
> SCIMProvider providers_scim_update(id, scim_provider_request)



SCIMProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.scim_provider import SCIMProvider
from authentik_openapi.models.scim_provider_request import SCIMProviderRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this SCIM Provider.
    scim_provider_request = authentik_openapi.SCIMProviderRequest() # SCIMProviderRequest | 

    try:
        api_response = api_instance.providers_scim_update(id, scim_provider_request)
        print("The response of ProvidersApi->providers_scim_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_scim_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SCIM Provider. | 
 **scim_provider_request** | [**SCIMProviderRequest**](SCIMProviderRequest.md)|  | 

### Return type

[**SCIMProvider**](SCIMProvider.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_scim_used_by_list**
> List[UsedBy] providers_scim_used_by_list(id)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 56 # int | A unique integer value identifying this SCIM Provider.

    try:
        api_response = api_instance.providers_scim_used_by_list(id)
        print("The response of ProvidersApi->providers_scim_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_scim_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SCIM Provider. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_scim_users_create**
> SCIMProviderUser providers_scim_users_create(scim_provider_user_request)



SCIMProviderUser Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.scim_provider_user import SCIMProviderUser
from authentik_openapi.models.scim_provider_user_request import SCIMProviderUserRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    scim_provider_user_request = authentik_openapi.SCIMProviderUserRequest() # SCIMProviderUserRequest | 

    try:
        api_response = api_instance.providers_scim_users_create(scim_provider_user_request)
        print("The response of ProvidersApi->providers_scim_users_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_scim_users_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scim_provider_user_request** | [**SCIMProviderUserRequest**](SCIMProviderUserRequest.md)|  | 

### Return type

[**SCIMProviderUser**](SCIMProviderUser.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_scim_users_destroy**
> providers_scim_users_destroy(id)



SCIMProviderUser Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 'id_example' # str | A UUID string identifying this scim provider user.

    try:
        api_instance.providers_scim_users_destroy(id)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_scim_users_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this scim provider user. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_scim_users_list**
> PaginatedSCIMProviderUserList providers_scim_users_list(ordering=ordering, page=page, page_size=page_size, provider__id=provider__id, search=search, user__id=user__id, user__username=user__username)



SCIMProviderUser Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_scim_provider_user_list import PaginatedSCIMProviderUserList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    provider__id = 56 # int |  (optional)
    search = 'search_example' # str | A search term. (optional)
    user__id = 56 # int |  (optional)
    user__username = 'user__username_example' # str |  (optional)

    try:
        api_response = api_instance.providers_scim_users_list(ordering=ordering, page=page, page_size=page_size, provider__id=provider__id, search=search, user__id=user__id, user__username=user__username)
        print("The response of ProvidersApi->providers_scim_users_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_scim_users_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **provider__id** | **int**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **user__id** | **int**|  | [optional] 
 **user__username** | **str**|  | [optional] 

### Return type

[**PaginatedSCIMProviderUserList**](PaginatedSCIMProviderUserList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_scim_users_retrieve**
> SCIMProviderUser providers_scim_users_retrieve(id)



SCIMProviderUser Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.scim_provider_user import SCIMProviderUser
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 'id_example' # str | A UUID string identifying this scim provider user.

    try:
        api_response = api_instance.providers_scim_users_retrieve(id)
        print("The response of ProvidersApi->providers_scim_users_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_scim_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this scim provider user. | 

### Return type

[**SCIMProviderUser**](SCIMProviderUser.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_scim_users_used_by_list**
> List[UsedBy] providers_scim_users_used_by_list(id)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ProvidersApi(api_client)
    id = 'id_example' # str | A UUID string identifying this scim provider user.

    try:
        api_response = api_instance.providers_scim_users_used_by_list(id)
        print("The response of ProvidersApi->providers_scim_users_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProvidersApi->providers_scim_users_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A UUID string identifying this scim provider user. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

