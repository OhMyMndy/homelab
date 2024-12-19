# authentik_openapi.SourcesApi

All URIs are relative to *https://auth.home.ohmymndy.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sources_all_destroy**](SourcesApi.md#sources_all_destroy) | **DELETE** /sources/all/{slug}/ | 
[**sources_all_list**](SourcesApi.md#sources_all_list) | **GET** /sources/all/ | 
[**sources_all_retrieve**](SourcesApi.md#sources_all_retrieve) | **GET** /sources/all/{slug}/ | 
[**sources_all_set_icon_create**](SourcesApi.md#sources_all_set_icon_create) | **POST** /sources/all/{slug}/set_icon/ | 
[**sources_all_set_icon_url_create**](SourcesApi.md#sources_all_set_icon_url_create) | **POST** /sources/all/{slug}/set_icon_url/ | 
[**sources_all_types_list**](SourcesApi.md#sources_all_types_list) | **GET** /sources/all/types/ | 
[**sources_all_used_by_list**](SourcesApi.md#sources_all_used_by_list) | **GET** /sources/all/{slug}/used_by/ | 
[**sources_all_user_settings_list**](SourcesApi.md#sources_all_user_settings_list) | **GET** /sources/all/user_settings/ | 
[**sources_ldap_create**](SourcesApi.md#sources_ldap_create) | **POST** /sources/ldap/ | 
[**sources_ldap_debug_retrieve**](SourcesApi.md#sources_ldap_debug_retrieve) | **GET** /sources/ldap/{slug}/debug/ | 
[**sources_ldap_destroy**](SourcesApi.md#sources_ldap_destroy) | **DELETE** /sources/ldap/{slug}/ | 
[**sources_ldap_list**](SourcesApi.md#sources_ldap_list) | **GET** /sources/ldap/ | 
[**sources_ldap_partial_update**](SourcesApi.md#sources_ldap_partial_update) | **PATCH** /sources/ldap/{slug}/ | 
[**sources_ldap_retrieve**](SourcesApi.md#sources_ldap_retrieve) | **GET** /sources/ldap/{slug}/ | 
[**sources_ldap_sync_status_retrieve**](SourcesApi.md#sources_ldap_sync_status_retrieve) | **GET** /sources/ldap/{slug}/sync/status/ | 
[**sources_ldap_update**](SourcesApi.md#sources_ldap_update) | **PUT** /sources/ldap/{slug}/ | 
[**sources_ldap_used_by_list**](SourcesApi.md#sources_ldap_used_by_list) | **GET** /sources/ldap/{slug}/used_by/ | 
[**sources_oauth_create**](SourcesApi.md#sources_oauth_create) | **POST** /sources/oauth/ | 
[**sources_oauth_destroy**](SourcesApi.md#sources_oauth_destroy) | **DELETE** /sources/oauth/{slug}/ | 
[**sources_oauth_list**](SourcesApi.md#sources_oauth_list) | **GET** /sources/oauth/ | 
[**sources_oauth_partial_update**](SourcesApi.md#sources_oauth_partial_update) | **PATCH** /sources/oauth/{slug}/ | 
[**sources_oauth_retrieve**](SourcesApi.md#sources_oauth_retrieve) | **GET** /sources/oauth/{slug}/ | 
[**sources_oauth_source_types_list**](SourcesApi.md#sources_oauth_source_types_list) | **GET** /sources/oauth/source_types/ | 
[**sources_oauth_update**](SourcesApi.md#sources_oauth_update) | **PUT** /sources/oauth/{slug}/ | 
[**sources_oauth_used_by_list**](SourcesApi.md#sources_oauth_used_by_list) | **GET** /sources/oauth/{slug}/used_by/ | 
[**sources_plex_create**](SourcesApi.md#sources_plex_create) | **POST** /sources/plex/ | 
[**sources_plex_destroy**](SourcesApi.md#sources_plex_destroy) | **DELETE** /sources/plex/{slug}/ | 
[**sources_plex_list**](SourcesApi.md#sources_plex_list) | **GET** /sources/plex/ | 
[**sources_plex_partial_update**](SourcesApi.md#sources_plex_partial_update) | **PATCH** /sources/plex/{slug}/ | 
[**sources_plex_redeem_token_authenticated_create**](SourcesApi.md#sources_plex_redeem_token_authenticated_create) | **POST** /sources/plex/redeem_token_authenticated/ | 
[**sources_plex_redeem_token_create**](SourcesApi.md#sources_plex_redeem_token_create) | **POST** /sources/plex/redeem_token/ | 
[**sources_plex_retrieve**](SourcesApi.md#sources_plex_retrieve) | **GET** /sources/plex/{slug}/ | 
[**sources_plex_update**](SourcesApi.md#sources_plex_update) | **PUT** /sources/plex/{slug}/ | 
[**sources_plex_used_by_list**](SourcesApi.md#sources_plex_used_by_list) | **GET** /sources/plex/{slug}/used_by/ | 
[**sources_saml_create**](SourcesApi.md#sources_saml_create) | **POST** /sources/saml/ | 
[**sources_saml_destroy**](SourcesApi.md#sources_saml_destroy) | **DELETE** /sources/saml/{slug}/ | 
[**sources_saml_list**](SourcesApi.md#sources_saml_list) | **GET** /sources/saml/ | 
[**sources_saml_metadata_retrieve**](SourcesApi.md#sources_saml_metadata_retrieve) | **GET** /sources/saml/{slug}/metadata/ | 
[**sources_saml_partial_update**](SourcesApi.md#sources_saml_partial_update) | **PATCH** /sources/saml/{slug}/ | 
[**sources_saml_retrieve**](SourcesApi.md#sources_saml_retrieve) | **GET** /sources/saml/{slug}/ | 
[**sources_saml_update**](SourcesApi.md#sources_saml_update) | **PUT** /sources/saml/{slug}/ | 
[**sources_saml_used_by_list**](SourcesApi.md#sources_saml_used_by_list) | **GET** /sources/saml/{slug}/used_by/ | 
[**sources_scim_create**](SourcesApi.md#sources_scim_create) | **POST** /sources/scim/ | 
[**sources_scim_destroy**](SourcesApi.md#sources_scim_destroy) | **DELETE** /sources/scim/{slug}/ | 
[**sources_scim_groups_create**](SourcesApi.md#sources_scim_groups_create) | **POST** /sources/scim_groups/ | 
[**sources_scim_groups_destroy**](SourcesApi.md#sources_scim_groups_destroy) | **DELETE** /sources/scim_groups/{id}/ | 
[**sources_scim_groups_list**](SourcesApi.md#sources_scim_groups_list) | **GET** /sources/scim_groups/ | 
[**sources_scim_groups_partial_update**](SourcesApi.md#sources_scim_groups_partial_update) | **PATCH** /sources/scim_groups/{id}/ | 
[**sources_scim_groups_retrieve**](SourcesApi.md#sources_scim_groups_retrieve) | **GET** /sources/scim_groups/{id}/ | 
[**sources_scim_groups_update**](SourcesApi.md#sources_scim_groups_update) | **PUT** /sources/scim_groups/{id}/ | 
[**sources_scim_groups_used_by_list**](SourcesApi.md#sources_scim_groups_used_by_list) | **GET** /sources/scim_groups/{id}/used_by/ | 
[**sources_scim_list**](SourcesApi.md#sources_scim_list) | **GET** /sources/scim/ | 
[**sources_scim_partial_update**](SourcesApi.md#sources_scim_partial_update) | **PATCH** /sources/scim/{slug}/ | 
[**sources_scim_retrieve**](SourcesApi.md#sources_scim_retrieve) | **GET** /sources/scim/{slug}/ | 
[**sources_scim_update**](SourcesApi.md#sources_scim_update) | **PUT** /sources/scim/{slug}/ | 
[**sources_scim_used_by_list**](SourcesApi.md#sources_scim_used_by_list) | **GET** /sources/scim/{slug}/used_by/ | 
[**sources_scim_users_create**](SourcesApi.md#sources_scim_users_create) | **POST** /sources/scim_users/ | 
[**sources_scim_users_destroy**](SourcesApi.md#sources_scim_users_destroy) | **DELETE** /sources/scim_users/{id}/ | 
[**sources_scim_users_list**](SourcesApi.md#sources_scim_users_list) | **GET** /sources/scim_users/ | 
[**sources_scim_users_partial_update**](SourcesApi.md#sources_scim_users_partial_update) | **PATCH** /sources/scim_users/{id}/ | 
[**sources_scim_users_retrieve**](SourcesApi.md#sources_scim_users_retrieve) | **GET** /sources/scim_users/{id}/ | 
[**sources_scim_users_update**](SourcesApi.md#sources_scim_users_update) | **PUT** /sources/scim_users/{id}/ | 
[**sources_scim_users_used_by_list**](SourcesApi.md#sources_scim_users_used_by_list) | **GET** /sources/scim_users/{id}/used_by/ | 
[**sources_user_connections_all_destroy**](SourcesApi.md#sources_user_connections_all_destroy) | **DELETE** /sources/user_connections/all/{id}/ | 
[**sources_user_connections_all_list**](SourcesApi.md#sources_user_connections_all_list) | **GET** /sources/user_connections/all/ | 
[**sources_user_connections_all_partial_update**](SourcesApi.md#sources_user_connections_all_partial_update) | **PATCH** /sources/user_connections/all/{id}/ | 
[**sources_user_connections_all_retrieve**](SourcesApi.md#sources_user_connections_all_retrieve) | **GET** /sources/user_connections/all/{id}/ | 
[**sources_user_connections_all_update**](SourcesApi.md#sources_user_connections_all_update) | **PUT** /sources/user_connections/all/{id}/ | 
[**sources_user_connections_all_used_by_list**](SourcesApi.md#sources_user_connections_all_used_by_list) | **GET** /sources/user_connections/all/{id}/used_by/ | 
[**sources_user_connections_oauth_create**](SourcesApi.md#sources_user_connections_oauth_create) | **POST** /sources/user_connections/oauth/ | 
[**sources_user_connections_oauth_destroy**](SourcesApi.md#sources_user_connections_oauth_destroy) | **DELETE** /sources/user_connections/oauth/{id}/ | 
[**sources_user_connections_oauth_list**](SourcesApi.md#sources_user_connections_oauth_list) | **GET** /sources/user_connections/oauth/ | 
[**sources_user_connections_oauth_partial_update**](SourcesApi.md#sources_user_connections_oauth_partial_update) | **PATCH** /sources/user_connections/oauth/{id}/ | 
[**sources_user_connections_oauth_retrieve**](SourcesApi.md#sources_user_connections_oauth_retrieve) | **GET** /sources/user_connections/oauth/{id}/ | 
[**sources_user_connections_oauth_update**](SourcesApi.md#sources_user_connections_oauth_update) | **PUT** /sources/user_connections/oauth/{id}/ | 
[**sources_user_connections_oauth_used_by_list**](SourcesApi.md#sources_user_connections_oauth_used_by_list) | **GET** /sources/user_connections/oauth/{id}/used_by/ | 
[**sources_user_connections_plex_create**](SourcesApi.md#sources_user_connections_plex_create) | **POST** /sources/user_connections/plex/ | 
[**sources_user_connections_plex_destroy**](SourcesApi.md#sources_user_connections_plex_destroy) | **DELETE** /sources/user_connections/plex/{id}/ | 
[**sources_user_connections_plex_list**](SourcesApi.md#sources_user_connections_plex_list) | **GET** /sources/user_connections/plex/ | 
[**sources_user_connections_plex_partial_update**](SourcesApi.md#sources_user_connections_plex_partial_update) | **PATCH** /sources/user_connections/plex/{id}/ | 
[**sources_user_connections_plex_retrieve**](SourcesApi.md#sources_user_connections_plex_retrieve) | **GET** /sources/user_connections/plex/{id}/ | 
[**sources_user_connections_plex_update**](SourcesApi.md#sources_user_connections_plex_update) | **PUT** /sources/user_connections/plex/{id}/ | 
[**sources_user_connections_plex_used_by_list**](SourcesApi.md#sources_user_connections_plex_used_by_list) | **GET** /sources/user_connections/plex/{id}/used_by/ | 
[**sources_user_connections_saml_create**](SourcesApi.md#sources_user_connections_saml_create) | **POST** /sources/user_connections/saml/ | 
[**sources_user_connections_saml_destroy**](SourcesApi.md#sources_user_connections_saml_destroy) | **DELETE** /sources/user_connections/saml/{id}/ | 
[**sources_user_connections_saml_list**](SourcesApi.md#sources_user_connections_saml_list) | **GET** /sources/user_connections/saml/ | 
[**sources_user_connections_saml_partial_update**](SourcesApi.md#sources_user_connections_saml_partial_update) | **PATCH** /sources/user_connections/saml/{id}/ | 
[**sources_user_connections_saml_retrieve**](SourcesApi.md#sources_user_connections_saml_retrieve) | **GET** /sources/user_connections/saml/{id}/ | 
[**sources_user_connections_saml_update**](SourcesApi.md#sources_user_connections_saml_update) | **PUT** /sources/user_connections/saml/{id}/ | 
[**sources_user_connections_saml_used_by_list**](SourcesApi.md#sources_user_connections_saml_used_by_list) | **GET** /sources/user_connections/saml/{id}/used_by/ | 


# **sources_all_destroy**
> sources_all_destroy(slug)



Source Viewset

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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_instance.sources_all_destroy(slug)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_all_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

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

# **sources_all_list**
> PaginatedSourceList sources_all_list(managed=managed, name=name, ordering=ordering, page=page, page_size=page_size, search=search, slug=slug)



Source Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_source_list import PaginatedSourceList
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    managed = 'managed_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    slug = 'slug_example' # str |  (optional)

    try:
        api_response = api_instance.sources_all_list(managed=managed, name=name, ordering=ordering, page=page, page_size=page_size, search=search, slug=slug)
        print("The response of SourcesApi->sources_all_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_all_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **slug** | **str**|  | [optional] 

### Return type

[**PaginatedSourceList**](PaginatedSourceList.md)

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

# **sources_all_retrieve**
> Source sources_all_retrieve(slug)



Source Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.source import Source
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.sources_all_retrieve(slug)
        print("The response of SourcesApi->sources_all_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_all_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**Source**](Source.md)

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

# **sources_all_set_icon_create**
> sources_all_set_icon_create(slug, file=file, clear=clear)



Set source icon

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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 
    file = None # bytearray |  (optional)
    clear = False # bool |  (optional) (default to False)

    try:
        api_instance.sources_all_set_icon_create(slug, file=file, clear=clear)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_all_set_icon_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **file** | **bytearray**|  | [optional] 
 **clear** | **bool**|  | [optional] [default to False]

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
**200** | Success |  -  |
**400** | Bad request |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_all_set_icon_url_create**
> sources_all_set_icon_url_create(slug, file_path_request)



Set source icon (as URL)

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.file_path_request import FilePathRequest
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 
    file_path_request = authentik_openapi.FilePathRequest() # FilePathRequest | 

    try:
        api_instance.sources_all_set_icon_url_create(slug, file_path_request)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_all_set_icon_url_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **file_path_request** | [**FilePathRequest**](FilePathRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_all_types_list**
> List[TypeCreate] sources_all_types_list()



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
    api_instance = authentik_openapi.SourcesApi(api_client)

    try:
        api_response = api_instance.sources_all_types_list()
        print("The response of SourcesApi->sources_all_types_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_all_types_list: %s\n" % e)
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

# **sources_all_used_by_list**
> List[UsedBy] sources_all_used_by_list(slug)



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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.sources_all_used_by_list(slug)
        print("The response of SourcesApi->sources_all_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_all_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

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

# **sources_all_user_settings_list**
> List[UserSetting] sources_all_user_settings_list()



Get all sources the user can configure

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user_setting import UserSetting
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
    api_instance = authentik_openapi.SourcesApi(api_client)

    try:
        api_response = api_instance.sources_all_user_settings_list()
        print("The response of SourcesApi->sources_all_user_settings_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_all_user_settings_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[UserSetting]**](UserSetting.md)

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

# **sources_ldap_create**
> LDAPSource sources_ldap_create(ldap_source_request)



LDAP Source Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.ldap_source import LDAPSource
from authentik_openapi.models.ldap_source_request import LDAPSourceRequest
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    ldap_source_request = authentik_openapi.LDAPSourceRequest() # LDAPSourceRequest | 

    try:
        api_response = api_instance.sources_ldap_create(ldap_source_request)
        print("The response of SourcesApi->sources_ldap_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_ldap_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldap_source_request** | [**LDAPSourceRequest**](LDAPSourceRequest.md)|  | 

### Return type

[**LDAPSource**](LDAPSource.md)

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

# **sources_ldap_debug_retrieve**
> LDAPDebug sources_ldap_debug_retrieve(slug)



Get raw LDAP data to debug

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.ldap_debug import LDAPDebug
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.sources_ldap_debug_retrieve(slug)
        print("The response of SourcesApi->sources_ldap_debug_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_ldap_debug_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**LDAPDebug**](LDAPDebug.md)

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

# **sources_ldap_destroy**
> sources_ldap_destroy(slug)



LDAP Source Viewset

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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_instance.sources_ldap_destroy(slug)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_ldap_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

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

# **sources_ldap_list**
> PaginatedLDAPSourceList sources_ldap_list(additional_group_dn=additional_group_dn, additional_user_dn=additional_user_dn, base_dn=base_dn, bind_cn=bind_cn, client_certificate=client_certificate, enabled=enabled, group_membership_field=group_membership_field, group_object_filter=group_object_filter, name=name, object_uniqueness_field=object_uniqueness_field, ordering=ordering, page=page, page_size=page_size, password_login_update_internal_password=password_login_update_internal_password, peer_certificate=peer_certificate, property_mappings=property_mappings, property_mappings_group=property_mappings_group, search=search, server_uri=server_uri, slug=slug, sni=sni, start_tls=start_tls, sync_groups=sync_groups, sync_parent_group=sync_parent_group, sync_users=sync_users, sync_users_password=sync_users_password, user_object_filter=user_object_filter)



LDAP Source Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_ldap_source_list import PaginatedLDAPSourceList
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    additional_group_dn = 'additional_group_dn_example' # str |  (optional)
    additional_user_dn = 'additional_user_dn_example' # str |  (optional)
    base_dn = 'base_dn_example' # str |  (optional)
    bind_cn = 'bind_cn_example' # str |  (optional)
    client_certificate = 'client_certificate_example' # str |  (optional)
    enabled = True # bool |  (optional)
    group_membership_field = 'group_membership_field_example' # str |  (optional)
    group_object_filter = 'group_object_filter_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    object_uniqueness_field = 'object_uniqueness_field_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    password_login_update_internal_password = True # bool |  (optional)
    peer_certificate = 'peer_certificate_example' # str |  (optional)
    property_mappings = ['property_mappings_example'] # List[str] |  (optional)
    property_mappings_group = ['property_mappings_group_example'] # List[str] |  (optional)
    search = 'search_example' # str | A search term. (optional)
    server_uri = 'server_uri_example' # str |  (optional)
    slug = 'slug_example' # str |  (optional)
    sni = True # bool |  (optional)
    start_tls = True # bool |  (optional)
    sync_groups = True # bool |  (optional)
    sync_parent_group = 'sync_parent_group_example' # str |  (optional)
    sync_users = True # bool |  (optional)
    sync_users_password = True # bool |  (optional)
    user_object_filter = 'user_object_filter_example' # str |  (optional)

    try:
        api_response = api_instance.sources_ldap_list(additional_group_dn=additional_group_dn, additional_user_dn=additional_user_dn, base_dn=base_dn, bind_cn=bind_cn, client_certificate=client_certificate, enabled=enabled, group_membership_field=group_membership_field, group_object_filter=group_object_filter, name=name, object_uniqueness_field=object_uniqueness_field, ordering=ordering, page=page, page_size=page_size, password_login_update_internal_password=password_login_update_internal_password, peer_certificate=peer_certificate, property_mappings=property_mappings, property_mappings_group=property_mappings_group, search=search, server_uri=server_uri, slug=slug, sni=sni, start_tls=start_tls, sync_groups=sync_groups, sync_parent_group=sync_parent_group, sync_users=sync_users, sync_users_password=sync_users_password, user_object_filter=user_object_filter)
        print("The response of SourcesApi->sources_ldap_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_ldap_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **additional_group_dn** | **str**|  | [optional] 
 **additional_user_dn** | **str**|  | [optional] 
 **base_dn** | **str**|  | [optional] 
 **bind_cn** | **str**|  | [optional] 
 **client_certificate** | **str**|  | [optional] 
 **enabled** | **bool**|  | [optional] 
 **group_membership_field** | **str**|  | [optional] 
 **group_object_filter** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **object_uniqueness_field** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **password_login_update_internal_password** | **bool**|  | [optional] 
 **peer_certificate** | **str**|  | [optional] 
 **property_mappings** | [**List[str]**](str.md)|  | [optional] 
 **property_mappings_group** | [**List[str]**](str.md)|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **server_uri** | **str**|  | [optional] 
 **slug** | **str**|  | [optional] 
 **sni** | **bool**|  | [optional] 
 **start_tls** | **bool**|  | [optional] 
 **sync_groups** | **bool**|  | [optional] 
 **sync_parent_group** | **str**|  | [optional] 
 **sync_users** | **bool**|  | [optional] 
 **sync_users_password** | **bool**|  | [optional] 
 **user_object_filter** | **str**|  | [optional] 

### Return type

[**PaginatedLDAPSourceList**](PaginatedLDAPSourceList.md)

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

# **sources_ldap_partial_update**
> LDAPSource sources_ldap_partial_update(slug, patched_ldap_source_request=patched_ldap_source_request)



LDAP Source Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.ldap_source import LDAPSource
from authentik_openapi.models.patched_ldap_source_request import PatchedLDAPSourceRequest
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 
    patched_ldap_source_request = authentik_openapi.PatchedLDAPSourceRequest() # PatchedLDAPSourceRequest |  (optional)

    try:
        api_response = api_instance.sources_ldap_partial_update(slug, patched_ldap_source_request=patched_ldap_source_request)
        print("The response of SourcesApi->sources_ldap_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_ldap_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **patched_ldap_source_request** | [**PatchedLDAPSourceRequest**](PatchedLDAPSourceRequest.md)|  | [optional] 

### Return type

[**LDAPSource**](LDAPSource.md)

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

# **sources_ldap_retrieve**
> LDAPSource sources_ldap_retrieve(slug)



LDAP Source Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.ldap_source import LDAPSource
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.sources_ldap_retrieve(slug)
        print("The response of SourcesApi->sources_ldap_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_ldap_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**LDAPSource**](LDAPSource.md)

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

# **sources_ldap_sync_status_retrieve**
> SyncStatus sources_ldap_sync_status_retrieve(slug)



Get source's sync status

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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.sources_ldap_sync_status_retrieve(slug)
        print("The response of SourcesApi->sources_ldap_sync_status_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_ldap_sync_status_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

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
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_ldap_update**
> LDAPSource sources_ldap_update(slug, ldap_source_request)



LDAP Source Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.ldap_source import LDAPSource
from authentik_openapi.models.ldap_source_request import LDAPSourceRequest
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 
    ldap_source_request = authentik_openapi.LDAPSourceRequest() # LDAPSourceRequest | 

    try:
        api_response = api_instance.sources_ldap_update(slug, ldap_source_request)
        print("The response of SourcesApi->sources_ldap_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_ldap_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **ldap_source_request** | [**LDAPSourceRequest**](LDAPSourceRequest.md)|  | 

### Return type

[**LDAPSource**](LDAPSource.md)

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

# **sources_ldap_used_by_list**
> List[UsedBy] sources_ldap_used_by_list(slug)



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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.sources_ldap_used_by_list(slug)
        print("The response of SourcesApi->sources_ldap_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_ldap_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

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

# **sources_oauth_create**
> OAuthSource sources_oauth_create(o_auth_source_request)



Source Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.o_auth_source import OAuthSource
from authentik_openapi.models.o_auth_source_request import OAuthSourceRequest
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    o_auth_source_request = authentik_openapi.OAuthSourceRequest() # OAuthSourceRequest | 

    try:
        api_response = api_instance.sources_oauth_create(o_auth_source_request)
        print("The response of SourcesApi->sources_oauth_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_oauth_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_auth_source_request** | [**OAuthSourceRequest**](OAuthSourceRequest.md)|  | 

### Return type

[**OAuthSource**](OAuthSource.md)

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

# **sources_oauth_destroy**
> sources_oauth_destroy(slug)



Source Viewset

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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_instance.sources_oauth_destroy(slug)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_oauth_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

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

# **sources_oauth_list**
> PaginatedOAuthSourceList sources_oauth_list(access_token_url=access_token_url, additional_scopes=additional_scopes, authentication_flow=authentication_flow, authorization_url=authorization_url, consumer_key=consumer_key, enabled=enabled, enrollment_flow=enrollment_flow, has_jwks=has_jwks, name=name, ordering=ordering, page=page, page_size=page_size, policy_engine_mode=policy_engine_mode, profile_url=profile_url, provider_type=provider_type, request_token_url=request_token_url, search=search, slug=slug, user_matching_mode=user_matching_mode)



Source Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_o_auth_source_list import PaginatedOAuthSourceList
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    access_token_url = 'access_token_url_example' # str |  (optional)
    additional_scopes = 'additional_scopes_example' # str |  (optional)
    authentication_flow = 'authentication_flow_example' # str |  (optional)
    authorization_url = 'authorization_url_example' # str |  (optional)
    consumer_key = 'consumer_key_example' # str |  (optional)
    enabled = True # bool |  (optional)
    enrollment_flow = 'enrollment_flow_example' # str |  (optional)
    has_jwks = True # bool | Only return sources with JWKS data (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    policy_engine_mode = 'policy_engine_mode_example' # str |  (optional)
    profile_url = 'profile_url_example' # str |  (optional)
    provider_type = 'provider_type_example' # str |  (optional)
    request_token_url = 'request_token_url_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)
    slug = 'slug_example' # str |  (optional)
    user_matching_mode = 'user_matching_mode_example' # str | How the source determines if an existing user should be authenticated or a new user enrolled.   (optional)

    try:
        api_response = api_instance.sources_oauth_list(access_token_url=access_token_url, additional_scopes=additional_scopes, authentication_flow=authentication_flow, authorization_url=authorization_url, consumer_key=consumer_key, enabled=enabled, enrollment_flow=enrollment_flow, has_jwks=has_jwks, name=name, ordering=ordering, page=page, page_size=page_size, policy_engine_mode=policy_engine_mode, profile_url=profile_url, provider_type=provider_type, request_token_url=request_token_url, search=search, slug=slug, user_matching_mode=user_matching_mode)
        print("The response of SourcesApi->sources_oauth_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_oauth_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token_url** | **str**|  | [optional] 
 **additional_scopes** | **str**|  | [optional] 
 **authentication_flow** | **str**|  | [optional] 
 **authorization_url** | **str**|  | [optional] 
 **consumer_key** | **str**|  | [optional] 
 **enabled** | **bool**|  | [optional] 
 **enrollment_flow** | **str**|  | [optional] 
 **has_jwks** | **bool**| Only return sources with JWKS data | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **policy_engine_mode** | **str**|  | [optional] 
 **profile_url** | **str**|  | [optional] 
 **provider_type** | **str**|  | [optional] 
 **request_token_url** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **slug** | **str**|  | [optional] 
 **user_matching_mode** | **str**| How the source determines if an existing user should be authenticated or a new user enrolled.   | [optional] 

### Return type

[**PaginatedOAuthSourceList**](PaginatedOAuthSourceList.md)

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

# **sources_oauth_partial_update**
> OAuthSource sources_oauth_partial_update(slug, patched_o_auth_source_request=patched_o_auth_source_request)



Source Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.o_auth_source import OAuthSource
from authentik_openapi.models.patched_o_auth_source_request import PatchedOAuthSourceRequest
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 
    patched_o_auth_source_request = authentik_openapi.PatchedOAuthSourceRequest() # PatchedOAuthSourceRequest |  (optional)

    try:
        api_response = api_instance.sources_oauth_partial_update(slug, patched_o_auth_source_request=patched_o_auth_source_request)
        print("The response of SourcesApi->sources_oauth_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_oauth_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **patched_o_auth_source_request** | [**PatchedOAuthSourceRequest**](PatchedOAuthSourceRequest.md)|  | [optional] 

### Return type

[**OAuthSource**](OAuthSource.md)

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

# **sources_oauth_retrieve**
> OAuthSource sources_oauth_retrieve(slug)



Source Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.o_auth_source import OAuthSource
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.sources_oauth_retrieve(slug)
        print("The response of SourcesApi->sources_oauth_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_oauth_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**OAuthSource**](OAuthSource.md)

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

# **sources_oauth_source_types_list**
> List[SourceType] sources_oauth_source_types_list(name=name)



Get all creatable source types. If ?name is set, only returns the type for <name>. If <name> isn't found, returns the default type.

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.source_type import SourceType
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    name = 'name_example' # str |  (optional)

    try:
        api_response = api_instance.sources_oauth_source_types_list(name=name)
        print("The response of SourcesApi->sources_oauth_source_types_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_oauth_source_types_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 

### Return type

[**List[SourceType]**](SourceType.md)

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

# **sources_oauth_update**
> OAuthSource sources_oauth_update(slug, o_auth_source_request)



Source Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.o_auth_source import OAuthSource
from authentik_openapi.models.o_auth_source_request import OAuthSourceRequest
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 
    o_auth_source_request = authentik_openapi.OAuthSourceRequest() # OAuthSourceRequest | 

    try:
        api_response = api_instance.sources_oauth_update(slug, o_auth_source_request)
        print("The response of SourcesApi->sources_oauth_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_oauth_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **o_auth_source_request** | [**OAuthSourceRequest**](OAuthSourceRequest.md)|  | 

### Return type

[**OAuthSource**](OAuthSource.md)

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

# **sources_oauth_used_by_list**
> List[UsedBy] sources_oauth_used_by_list(slug)



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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.sources_oauth_used_by_list(slug)
        print("The response of SourcesApi->sources_oauth_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_oauth_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

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

# **sources_plex_create**
> PlexSource sources_plex_create(plex_source_request)



Plex source Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.plex_source import PlexSource
from authentik_openapi.models.plex_source_request import PlexSourceRequest
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    plex_source_request = authentik_openapi.PlexSourceRequest() # PlexSourceRequest | 

    try:
        api_response = api_instance.sources_plex_create(plex_source_request)
        print("The response of SourcesApi->sources_plex_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_plex_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plex_source_request** | [**PlexSourceRequest**](PlexSourceRequest.md)|  | 

### Return type

[**PlexSource**](PlexSource.md)

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

# **sources_plex_destroy**
> sources_plex_destroy(slug)



Plex source Viewset

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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_instance.sources_plex_destroy(slug)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_plex_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

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

# **sources_plex_list**
> PaginatedPlexSourceList sources_plex_list(allow_friends=allow_friends, authentication_flow=authentication_flow, client_id=client_id, enabled=enabled, enrollment_flow=enrollment_flow, name=name, ordering=ordering, page=page, page_size=page_size, policy_engine_mode=policy_engine_mode, search=search, slug=slug, user_matching_mode=user_matching_mode)



Plex source Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_plex_source_list import PaginatedPlexSourceList
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    allow_friends = True # bool |  (optional)
    authentication_flow = 'authentication_flow_example' # str |  (optional)
    client_id = 'client_id_example' # str |  (optional)
    enabled = True # bool |  (optional)
    enrollment_flow = 'enrollment_flow_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    policy_engine_mode = 'policy_engine_mode_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)
    slug = 'slug_example' # str |  (optional)
    user_matching_mode = 'user_matching_mode_example' # str | How the source determines if an existing user should be authenticated or a new user enrolled.   (optional)

    try:
        api_response = api_instance.sources_plex_list(allow_friends=allow_friends, authentication_flow=authentication_flow, client_id=client_id, enabled=enabled, enrollment_flow=enrollment_flow, name=name, ordering=ordering, page=page, page_size=page_size, policy_engine_mode=policy_engine_mode, search=search, slug=slug, user_matching_mode=user_matching_mode)
        print("The response of SourcesApi->sources_plex_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_plex_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allow_friends** | **bool**|  | [optional] 
 **authentication_flow** | **str**|  | [optional] 
 **client_id** | **str**|  | [optional] 
 **enabled** | **bool**|  | [optional] 
 **enrollment_flow** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **policy_engine_mode** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **slug** | **str**|  | [optional] 
 **user_matching_mode** | **str**| How the source determines if an existing user should be authenticated or a new user enrolled.   | [optional] 

### Return type

[**PaginatedPlexSourceList**](PaginatedPlexSourceList.md)

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

# **sources_plex_partial_update**
> PlexSource sources_plex_partial_update(slug, patched_plex_source_request=patched_plex_source_request)



Plex source Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_plex_source_request import PatchedPlexSourceRequest
from authentik_openapi.models.plex_source import PlexSource
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 
    patched_plex_source_request = authentik_openapi.PatchedPlexSourceRequest() # PatchedPlexSourceRequest |  (optional)

    try:
        api_response = api_instance.sources_plex_partial_update(slug, patched_plex_source_request=patched_plex_source_request)
        print("The response of SourcesApi->sources_plex_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_plex_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **patched_plex_source_request** | [**PatchedPlexSourceRequest**](PatchedPlexSourceRequest.md)|  | [optional] 

### Return type

[**PlexSource**](PlexSource.md)

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

# **sources_plex_redeem_token_authenticated_create**
> sources_plex_redeem_token_authenticated_create(plex_token_redeem_request, slug=slug)



Redeem a plex token for an authenticated user, creating a connection

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.plex_token_redeem_request import PlexTokenRedeemRequest
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    plex_token_redeem_request = authentik_openapi.PlexTokenRedeemRequest() # PlexTokenRedeemRequest | 
    slug = 'slug_example' # str |  (optional)

    try:
        api_instance.sources_plex_redeem_token_authenticated_create(plex_token_redeem_request, slug=slug)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_plex_redeem_token_authenticated_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plex_token_redeem_request** | [**PlexTokenRedeemRequest**](PlexTokenRedeemRequest.md)|  | 
 **slug** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** | Token not found |  -  |
**403** | Access denied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_plex_redeem_token_create**
> RedirectChallenge sources_plex_redeem_token_create(plex_token_redeem_request, slug=slug)



Redeem a plex token, check it's access to resources against what's allowed for the source, and redirect to an authentication/enrollment flow.

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.plex_token_redeem_request import PlexTokenRedeemRequest
from authentik_openapi.models.redirect_challenge import RedirectChallenge
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    plex_token_redeem_request = authentik_openapi.PlexTokenRedeemRequest() # PlexTokenRedeemRequest | 
    slug = 'slug_example' # str |  (optional)

    try:
        api_response = api_instance.sources_plex_redeem_token_create(plex_token_redeem_request, slug=slug)
        print("The response of SourcesApi->sources_plex_redeem_token_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_plex_redeem_token_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plex_token_redeem_request** | [**PlexTokenRedeemRequest**](PlexTokenRedeemRequest.md)|  | 
 **slug** | **str**|  | [optional] 

### Return type

[**RedirectChallenge**](RedirectChallenge.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Token not found |  -  |
**403** | Access denied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_plex_retrieve**
> PlexSource sources_plex_retrieve(slug)



Plex source Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.plex_source import PlexSource
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.sources_plex_retrieve(slug)
        print("The response of SourcesApi->sources_plex_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_plex_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**PlexSource**](PlexSource.md)

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

# **sources_plex_update**
> PlexSource sources_plex_update(slug, plex_source_request)



Plex source Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.plex_source import PlexSource
from authentik_openapi.models.plex_source_request import PlexSourceRequest
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 
    plex_source_request = authentik_openapi.PlexSourceRequest() # PlexSourceRequest | 

    try:
        api_response = api_instance.sources_plex_update(slug, plex_source_request)
        print("The response of SourcesApi->sources_plex_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_plex_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **plex_source_request** | [**PlexSourceRequest**](PlexSourceRequest.md)|  | 

### Return type

[**PlexSource**](PlexSource.md)

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

# **sources_plex_used_by_list**
> List[UsedBy] sources_plex_used_by_list(slug)



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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.sources_plex_used_by_list(slug)
        print("The response of SourcesApi->sources_plex_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_plex_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

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

# **sources_saml_create**
> SAMLSource sources_saml_create(saml_source_request)



SAMLSource Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.saml_source import SAMLSource
from authentik_openapi.models.saml_source_request import SAMLSourceRequest
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    saml_source_request = authentik_openapi.SAMLSourceRequest() # SAMLSourceRequest | 

    try:
        api_response = api_instance.sources_saml_create(saml_source_request)
        print("The response of SourcesApi->sources_saml_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_saml_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saml_source_request** | [**SAMLSourceRequest**](SAMLSourceRequest.md)|  | 

### Return type

[**SAMLSource**](SAMLSource.md)

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

# **sources_saml_destroy**
> sources_saml_destroy(slug)



SAMLSource Viewset

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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_instance.sources_saml_destroy(slug)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_saml_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

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

# **sources_saml_list**
> PaginatedSAMLSourceList sources_saml_list(allow_idp_initiated=allow_idp_initiated, authentication_flow=authentication_flow, binding_type=binding_type, digest_algorithm=digest_algorithm, enabled=enabled, enrollment_flow=enrollment_flow, issuer=issuer, managed=managed, name=name, name_id_policy=name_id_policy, ordering=ordering, page=page, page_size=page_size, policy_engine_mode=policy_engine_mode, pre_authentication_flow=pre_authentication_flow, search=search, signature_algorithm=signature_algorithm, signing_kp=signing_kp, slo_url=slo_url, slug=slug, sso_url=sso_url, temporary_user_delete_after=temporary_user_delete_after, user_matching_mode=user_matching_mode, verification_kp=verification_kp)



SAMLSource Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_saml_source_list import PaginatedSAMLSourceList
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    allow_idp_initiated = True # bool |  (optional)
    authentication_flow = 'authentication_flow_example' # str |  (optional)
    binding_type = 'binding_type_example' # str |  (optional)
    digest_algorithm = 'digest_algorithm_example' # str |  (optional)
    enabled = True # bool |  (optional)
    enrollment_flow = 'enrollment_flow_example' # str |  (optional)
    issuer = 'issuer_example' # str |  (optional)
    managed = 'managed_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    name_id_policy = 'name_id_policy_example' # str | NameID Policy sent to the IdP. Can be unset, in which case no Policy is sent.   (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    policy_engine_mode = 'policy_engine_mode_example' # str |  (optional)
    pre_authentication_flow = 'pre_authentication_flow_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)
    signature_algorithm = 'signature_algorithm_example' # str |  (optional)
    signing_kp = 'signing_kp_example' # str |  (optional)
    slo_url = 'slo_url_example' # str |  (optional)
    slug = 'slug_example' # str |  (optional)
    sso_url = 'sso_url_example' # str |  (optional)
    temporary_user_delete_after = 'temporary_user_delete_after_example' # str |  (optional)
    user_matching_mode = 'user_matching_mode_example' # str | How the source determines if an existing user should be authenticated or a new user enrolled.   (optional)
    verification_kp = 'verification_kp_example' # str |  (optional)

    try:
        api_response = api_instance.sources_saml_list(allow_idp_initiated=allow_idp_initiated, authentication_flow=authentication_flow, binding_type=binding_type, digest_algorithm=digest_algorithm, enabled=enabled, enrollment_flow=enrollment_flow, issuer=issuer, managed=managed, name=name, name_id_policy=name_id_policy, ordering=ordering, page=page, page_size=page_size, policy_engine_mode=policy_engine_mode, pre_authentication_flow=pre_authentication_flow, search=search, signature_algorithm=signature_algorithm, signing_kp=signing_kp, slo_url=slo_url, slug=slug, sso_url=sso_url, temporary_user_delete_after=temporary_user_delete_after, user_matching_mode=user_matching_mode, verification_kp=verification_kp)
        print("The response of SourcesApi->sources_saml_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_saml_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allow_idp_initiated** | **bool**|  | [optional] 
 **authentication_flow** | **str**|  | [optional] 
 **binding_type** | **str**|  | [optional] 
 **digest_algorithm** | **str**|  | [optional] 
 **enabled** | **bool**|  | [optional] 
 **enrollment_flow** | **str**|  | [optional] 
 **issuer** | **str**|  | [optional] 
 **managed** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **name_id_policy** | **str**| NameID Policy sent to the IdP. Can be unset, in which case no Policy is sent.   | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **policy_engine_mode** | **str**|  | [optional] 
 **pre_authentication_flow** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **signature_algorithm** | **str**|  | [optional] 
 **signing_kp** | **str**|  | [optional] 
 **slo_url** | **str**|  | [optional] 
 **slug** | **str**|  | [optional] 
 **sso_url** | **str**|  | [optional] 
 **temporary_user_delete_after** | **str**|  | [optional] 
 **user_matching_mode** | **str**| How the source determines if an existing user should be authenticated or a new user enrolled.   | [optional] 
 **verification_kp** | **str**|  | [optional] 

### Return type

[**PaginatedSAMLSourceList**](PaginatedSAMLSourceList.md)

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

# **sources_saml_metadata_retrieve**
> SAMLMetadata sources_saml_metadata_retrieve(slug)



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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.sources_saml_metadata_retrieve(slug)
        print("The response of SourcesApi->sources_saml_metadata_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_saml_metadata_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

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
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_saml_partial_update**
> SAMLSource sources_saml_partial_update(slug, patched_saml_source_request=patched_saml_source_request)



SAMLSource Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_saml_source_request import PatchedSAMLSourceRequest
from authentik_openapi.models.saml_source import SAMLSource
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 
    patched_saml_source_request = authentik_openapi.PatchedSAMLSourceRequest() # PatchedSAMLSourceRequest |  (optional)

    try:
        api_response = api_instance.sources_saml_partial_update(slug, patched_saml_source_request=patched_saml_source_request)
        print("The response of SourcesApi->sources_saml_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_saml_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **patched_saml_source_request** | [**PatchedSAMLSourceRequest**](PatchedSAMLSourceRequest.md)|  | [optional] 

### Return type

[**SAMLSource**](SAMLSource.md)

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

# **sources_saml_retrieve**
> SAMLSource sources_saml_retrieve(slug)



SAMLSource Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.saml_source import SAMLSource
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.sources_saml_retrieve(slug)
        print("The response of SourcesApi->sources_saml_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_saml_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**SAMLSource**](SAMLSource.md)

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

# **sources_saml_update**
> SAMLSource sources_saml_update(slug, saml_source_request)



SAMLSource Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.saml_source import SAMLSource
from authentik_openapi.models.saml_source_request import SAMLSourceRequest
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 
    saml_source_request = authentik_openapi.SAMLSourceRequest() # SAMLSourceRequest | 

    try:
        api_response = api_instance.sources_saml_update(slug, saml_source_request)
        print("The response of SourcesApi->sources_saml_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_saml_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **saml_source_request** | [**SAMLSourceRequest**](SAMLSourceRequest.md)|  | 

### Return type

[**SAMLSource**](SAMLSource.md)

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

# **sources_saml_used_by_list**
> List[UsedBy] sources_saml_used_by_list(slug)



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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.sources_saml_used_by_list(slug)
        print("The response of SourcesApi->sources_saml_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_saml_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

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

# **sources_scim_create**
> SCIMSource sources_scim_create(scim_source_request)



SCIMSource Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.scim_source import SCIMSource
from authentik_openapi.models.scim_source_request import SCIMSourceRequest
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    scim_source_request = authentik_openapi.SCIMSourceRequest() # SCIMSourceRequest | 

    try:
        api_response = api_instance.sources_scim_create(scim_source_request)
        print("The response of SourcesApi->sources_scim_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_scim_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scim_source_request** | [**SCIMSourceRequest**](SCIMSourceRequest.md)|  | 

### Return type

[**SCIMSource**](SCIMSource.md)

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

# **sources_scim_destroy**
> sources_scim_destroy(slug)



SCIMSource Viewset

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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_instance.sources_scim_destroy(slug)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_scim_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

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

# **sources_scim_groups_create**
> SCIMSourceGroup sources_scim_groups_create(scim_source_group_request)



SCIMSourceGroup Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.scim_source_group import SCIMSourceGroup
from authentik_openapi.models.scim_source_group_request import SCIMSourceGroupRequest
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    scim_source_group_request = authentik_openapi.SCIMSourceGroupRequest() # SCIMSourceGroupRequest | 

    try:
        api_response = api_instance.sources_scim_groups_create(scim_source_group_request)
        print("The response of SourcesApi->sources_scim_groups_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_scim_groups_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scim_source_group_request** | [**SCIMSourceGroupRequest**](SCIMSourceGroupRequest.md)|  | 

### Return type

[**SCIMSourceGroup**](SCIMSourceGroup.md)

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

# **sources_scim_groups_destroy**
> sources_scim_groups_destroy(id)



SCIMSourceGroup Viewset

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
    api_instance = authentik_openapi.SourcesApi(api_client)
    id = 'id_example' # str | A unique value identifying this scim source group.

    try:
        api_instance.sources_scim_groups_destroy(id)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_scim_groups_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this scim source group. | 

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

# **sources_scim_groups_list**
> PaginatedSCIMSourceGroupList sources_scim_groups_list(group__group_uuid=group__group_uuid, group__name=group__name, ordering=ordering, page=page, page_size=page_size, search=search, source__slug=source__slug)



SCIMSourceGroup Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_scim_source_group_list import PaginatedSCIMSourceGroupList
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    group__group_uuid = 'group__group_uuid_example' # str |  (optional)
    group__name = 'group__name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    source__slug = 'source__slug_example' # str |  (optional)

    try:
        api_response = api_instance.sources_scim_groups_list(group__group_uuid=group__group_uuid, group__name=group__name, ordering=ordering, page=page, page_size=page_size, search=search, source__slug=source__slug)
        print("The response of SourcesApi->sources_scim_groups_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_scim_groups_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group__group_uuid** | **str**|  | [optional] 
 **group__name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **source__slug** | **str**|  | [optional] 

### Return type

[**PaginatedSCIMSourceGroupList**](PaginatedSCIMSourceGroupList.md)

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

# **sources_scim_groups_partial_update**
> SCIMSourceGroup sources_scim_groups_partial_update(id, patched_scim_source_group_request=patched_scim_source_group_request)



SCIMSourceGroup Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_scim_source_group_request import PatchedSCIMSourceGroupRequest
from authentik_openapi.models.scim_source_group import SCIMSourceGroup
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    id = 'id_example' # str | A unique value identifying this scim source group.
    patched_scim_source_group_request = authentik_openapi.PatchedSCIMSourceGroupRequest() # PatchedSCIMSourceGroupRequest |  (optional)

    try:
        api_response = api_instance.sources_scim_groups_partial_update(id, patched_scim_source_group_request=patched_scim_source_group_request)
        print("The response of SourcesApi->sources_scim_groups_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_scim_groups_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this scim source group. | 
 **patched_scim_source_group_request** | [**PatchedSCIMSourceGroupRequest**](PatchedSCIMSourceGroupRequest.md)|  | [optional] 

### Return type

[**SCIMSourceGroup**](SCIMSourceGroup.md)

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

# **sources_scim_groups_retrieve**
> SCIMSourceGroup sources_scim_groups_retrieve(id)



SCIMSourceGroup Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.scim_source_group import SCIMSourceGroup
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    id = 'id_example' # str | A unique value identifying this scim source group.

    try:
        api_response = api_instance.sources_scim_groups_retrieve(id)
        print("The response of SourcesApi->sources_scim_groups_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_scim_groups_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this scim source group. | 

### Return type

[**SCIMSourceGroup**](SCIMSourceGroup.md)

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

# **sources_scim_groups_update**
> SCIMSourceGroup sources_scim_groups_update(id, scim_source_group_request)



SCIMSourceGroup Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.scim_source_group import SCIMSourceGroup
from authentik_openapi.models.scim_source_group_request import SCIMSourceGroupRequest
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    id = 'id_example' # str | A unique value identifying this scim source group.
    scim_source_group_request = authentik_openapi.SCIMSourceGroupRequest() # SCIMSourceGroupRequest | 

    try:
        api_response = api_instance.sources_scim_groups_update(id, scim_source_group_request)
        print("The response of SourcesApi->sources_scim_groups_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_scim_groups_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this scim source group. | 
 **scim_source_group_request** | [**SCIMSourceGroupRequest**](SCIMSourceGroupRequest.md)|  | 

### Return type

[**SCIMSourceGroup**](SCIMSourceGroup.md)

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

# **sources_scim_groups_used_by_list**
> List[UsedBy] sources_scim_groups_used_by_list(id)



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
    api_instance = authentik_openapi.SourcesApi(api_client)
    id = 'id_example' # str | A unique value identifying this scim source group.

    try:
        api_response = api_instance.sources_scim_groups_used_by_list(id)
        print("The response of SourcesApi->sources_scim_groups_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_scim_groups_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this scim source group. | 

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

# **sources_scim_list**
> PaginatedSCIMSourceList sources_scim_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search, slug=slug)



SCIMSource Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_scim_source_list import PaginatedSCIMSourceList
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    slug = 'slug_example' # str |  (optional)

    try:
        api_response = api_instance.sources_scim_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search, slug=slug)
        print("The response of SourcesApi->sources_scim_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_scim_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **slug** | **str**|  | [optional] 

### Return type

[**PaginatedSCIMSourceList**](PaginatedSCIMSourceList.md)

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

# **sources_scim_partial_update**
> SCIMSource sources_scim_partial_update(slug, patched_scim_source_request=patched_scim_source_request)



SCIMSource Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_scim_source_request import PatchedSCIMSourceRequest
from authentik_openapi.models.scim_source import SCIMSource
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 
    patched_scim_source_request = authentik_openapi.PatchedSCIMSourceRequest() # PatchedSCIMSourceRequest |  (optional)

    try:
        api_response = api_instance.sources_scim_partial_update(slug, patched_scim_source_request=patched_scim_source_request)
        print("The response of SourcesApi->sources_scim_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_scim_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **patched_scim_source_request** | [**PatchedSCIMSourceRequest**](PatchedSCIMSourceRequest.md)|  | [optional] 

### Return type

[**SCIMSource**](SCIMSource.md)

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

# **sources_scim_retrieve**
> SCIMSource sources_scim_retrieve(slug)



SCIMSource Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.scim_source import SCIMSource
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.sources_scim_retrieve(slug)
        print("The response of SourcesApi->sources_scim_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_scim_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**SCIMSource**](SCIMSource.md)

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

# **sources_scim_update**
> SCIMSource sources_scim_update(slug, scim_source_request)



SCIMSource Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.scim_source import SCIMSource
from authentik_openapi.models.scim_source_request import SCIMSourceRequest
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 
    scim_source_request = authentik_openapi.SCIMSourceRequest() # SCIMSourceRequest | 

    try:
        api_response = api_instance.sources_scim_update(slug, scim_source_request)
        print("The response of SourcesApi->sources_scim_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_scim_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **scim_source_request** | [**SCIMSourceRequest**](SCIMSourceRequest.md)|  | 

### Return type

[**SCIMSource**](SCIMSource.md)

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

# **sources_scim_used_by_list**
> List[UsedBy] sources_scim_used_by_list(slug)



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
    api_instance = authentik_openapi.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.sources_scim_used_by_list(slug)
        print("The response of SourcesApi->sources_scim_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_scim_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

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

# **sources_scim_users_create**
> SCIMSourceUser sources_scim_users_create(scim_source_user_request)



SCIMSourceUser Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.scim_source_user import SCIMSourceUser
from authentik_openapi.models.scim_source_user_request import SCIMSourceUserRequest
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    scim_source_user_request = authentik_openapi.SCIMSourceUserRequest() # SCIMSourceUserRequest | 

    try:
        api_response = api_instance.sources_scim_users_create(scim_source_user_request)
        print("The response of SourcesApi->sources_scim_users_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_scim_users_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scim_source_user_request** | [**SCIMSourceUserRequest**](SCIMSourceUserRequest.md)|  | 

### Return type

[**SCIMSourceUser**](SCIMSourceUser.md)

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

# **sources_scim_users_destroy**
> sources_scim_users_destroy(id)



SCIMSourceUser Viewset

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
    api_instance = authentik_openapi.SourcesApi(api_client)
    id = 'id_example' # str | A unique value identifying this scim source user.

    try:
        api_instance.sources_scim_users_destroy(id)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_scim_users_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this scim source user. | 

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

# **sources_scim_users_list**
> PaginatedSCIMSourceUserList sources_scim_users_list(ordering=ordering, page=page, page_size=page_size, search=search, source__slug=source__slug, user__id=user__id, user__username=user__username)



SCIMSourceUser Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_scim_source_user_list import PaginatedSCIMSourceUserList
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    source__slug = 'source__slug_example' # str |  (optional)
    user__id = 56 # int |  (optional)
    user__username = 'user__username_example' # str |  (optional)

    try:
        api_response = api_instance.sources_scim_users_list(ordering=ordering, page=page, page_size=page_size, search=search, source__slug=source__slug, user__id=user__id, user__username=user__username)
        print("The response of SourcesApi->sources_scim_users_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_scim_users_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **source__slug** | **str**|  | [optional] 
 **user__id** | **int**|  | [optional] 
 **user__username** | **str**|  | [optional] 

### Return type

[**PaginatedSCIMSourceUserList**](PaginatedSCIMSourceUserList.md)

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

# **sources_scim_users_partial_update**
> SCIMSourceUser sources_scim_users_partial_update(id, patched_scim_source_user_request=patched_scim_source_user_request)



SCIMSourceUser Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_scim_source_user_request import PatchedSCIMSourceUserRequest
from authentik_openapi.models.scim_source_user import SCIMSourceUser
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    id = 'id_example' # str | A unique value identifying this scim source user.
    patched_scim_source_user_request = authentik_openapi.PatchedSCIMSourceUserRequest() # PatchedSCIMSourceUserRequest |  (optional)

    try:
        api_response = api_instance.sources_scim_users_partial_update(id, patched_scim_source_user_request=patched_scim_source_user_request)
        print("The response of SourcesApi->sources_scim_users_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_scim_users_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this scim source user. | 
 **patched_scim_source_user_request** | [**PatchedSCIMSourceUserRequest**](PatchedSCIMSourceUserRequest.md)|  | [optional] 

### Return type

[**SCIMSourceUser**](SCIMSourceUser.md)

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

# **sources_scim_users_retrieve**
> SCIMSourceUser sources_scim_users_retrieve(id)



SCIMSourceUser Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.scim_source_user import SCIMSourceUser
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    id = 'id_example' # str | A unique value identifying this scim source user.

    try:
        api_response = api_instance.sources_scim_users_retrieve(id)
        print("The response of SourcesApi->sources_scim_users_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_scim_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this scim source user. | 

### Return type

[**SCIMSourceUser**](SCIMSourceUser.md)

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

# **sources_scim_users_update**
> SCIMSourceUser sources_scim_users_update(id, scim_source_user_request)



SCIMSourceUser Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.scim_source_user import SCIMSourceUser
from authentik_openapi.models.scim_source_user_request import SCIMSourceUserRequest
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    id = 'id_example' # str | A unique value identifying this scim source user.
    scim_source_user_request = authentik_openapi.SCIMSourceUserRequest() # SCIMSourceUserRequest | 

    try:
        api_response = api_instance.sources_scim_users_update(id, scim_source_user_request)
        print("The response of SourcesApi->sources_scim_users_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_scim_users_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this scim source user. | 
 **scim_source_user_request** | [**SCIMSourceUserRequest**](SCIMSourceUserRequest.md)|  | 

### Return type

[**SCIMSourceUser**](SCIMSourceUser.md)

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

# **sources_scim_users_used_by_list**
> List[UsedBy] sources_scim_users_used_by_list(id)



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
    api_instance = authentik_openapi.SourcesApi(api_client)
    id = 'id_example' # str | A unique value identifying this scim source user.

    try:
        api_response = api_instance.sources_scim_users_used_by_list(id)
        print("The response of SourcesApi->sources_scim_users_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_scim_users_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| A unique value identifying this scim source user. | 

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

# **sources_user_connections_all_destroy**
> sources_user_connections_all_destroy(id)



User-source connection Viewset

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
    api_instance = authentik_openapi.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this user source connection.

    try:
        api_instance.sources_user_connections_all_destroy(id)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_all_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user source connection. | 

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

# **sources_user_connections_all_list**
> PaginatedUserSourceConnectionList sources_user_connections_all_list(ordering=ordering, page=page, page_size=page_size, search=search, user=user)



User-source connection Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_user_source_connection_list import PaginatedUserSourceConnectionList
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    user = 56 # int |  (optional)

    try:
        api_response = api_instance.sources_user_connections_all_list(ordering=ordering, page=page, page_size=page_size, search=search, user=user)
        print("The response of SourcesApi->sources_user_connections_all_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_all_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **user** | **int**|  | [optional] 

### Return type

[**PaginatedUserSourceConnectionList**](PaginatedUserSourceConnectionList.md)

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

# **sources_user_connections_all_partial_update**
> UserSourceConnection sources_user_connections_all_partial_update(id)



User-source connection Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user_source_connection import UserSourceConnection
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this user source connection.

    try:
        api_response = api_instance.sources_user_connections_all_partial_update(id)
        print("The response of SourcesApi->sources_user_connections_all_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_all_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user source connection. | 

### Return type

[**UserSourceConnection**](UserSourceConnection.md)

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

# **sources_user_connections_all_retrieve**
> UserSourceConnection sources_user_connections_all_retrieve(id)



User-source connection Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user_source_connection import UserSourceConnection
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this user source connection.

    try:
        api_response = api_instance.sources_user_connections_all_retrieve(id)
        print("The response of SourcesApi->sources_user_connections_all_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_all_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user source connection. | 

### Return type

[**UserSourceConnection**](UserSourceConnection.md)

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

# **sources_user_connections_all_update**
> UserSourceConnection sources_user_connections_all_update(id)



User-source connection Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user_source_connection import UserSourceConnection
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this user source connection.

    try:
        api_response = api_instance.sources_user_connections_all_update(id)
        print("The response of SourcesApi->sources_user_connections_all_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_all_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user source connection. | 

### Return type

[**UserSourceConnection**](UserSourceConnection.md)

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

# **sources_user_connections_all_used_by_list**
> List[UsedBy] sources_user_connections_all_used_by_list(id)



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
    api_instance = authentik_openapi.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this user source connection.

    try:
        api_response = api_instance.sources_user_connections_all_used_by_list(id)
        print("The response of SourcesApi->sources_user_connections_all_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_all_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user source connection. | 

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

# **sources_user_connections_oauth_create**
> UserOAuthSourceConnection sources_user_connections_oauth_create(user_o_auth_source_connection_request)



Source Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user_o_auth_source_connection import UserOAuthSourceConnection
from authentik_openapi.models.user_o_auth_source_connection_request import UserOAuthSourceConnectionRequest
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    user_o_auth_source_connection_request = authentik_openapi.UserOAuthSourceConnectionRequest() # UserOAuthSourceConnectionRequest | 

    try:
        api_response = api_instance.sources_user_connections_oauth_create(user_o_auth_source_connection_request)
        print("The response of SourcesApi->sources_user_connections_oauth_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_oauth_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_o_auth_source_connection_request** | [**UserOAuthSourceConnectionRequest**](UserOAuthSourceConnectionRequest.md)|  | 

### Return type

[**UserOAuthSourceConnection**](UserOAuthSourceConnection.md)

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

# **sources_user_connections_oauth_destroy**
> sources_user_connections_oauth_destroy(id)



Source Viewset

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
    api_instance = authentik_openapi.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this User OAuth Source Connection.

    try:
        api_instance.sources_user_connections_oauth_destroy(id)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_oauth_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User OAuth Source Connection. | 

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

# **sources_user_connections_oauth_list**
> PaginatedUserOAuthSourceConnectionList sources_user_connections_oauth_list(ordering=ordering, page=page, page_size=page_size, search=search, source__slug=source__slug)



Source Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_user_o_auth_source_connection_list import PaginatedUserOAuthSourceConnectionList
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    source__slug = 'source__slug_example' # str |  (optional)

    try:
        api_response = api_instance.sources_user_connections_oauth_list(ordering=ordering, page=page, page_size=page_size, search=search, source__slug=source__slug)
        print("The response of SourcesApi->sources_user_connections_oauth_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_oauth_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **source__slug** | **str**|  | [optional] 

### Return type

[**PaginatedUserOAuthSourceConnectionList**](PaginatedUserOAuthSourceConnectionList.md)

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

# **sources_user_connections_oauth_partial_update**
> UserOAuthSourceConnection sources_user_connections_oauth_partial_update(id, patched_user_o_auth_source_connection_request=patched_user_o_auth_source_connection_request)



Source Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_user_o_auth_source_connection_request import PatchedUserOAuthSourceConnectionRequest
from authentik_openapi.models.user_o_auth_source_connection import UserOAuthSourceConnection
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this User OAuth Source Connection.
    patched_user_o_auth_source_connection_request = authentik_openapi.PatchedUserOAuthSourceConnectionRequest() # PatchedUserOAuthSourceConnectionRequest |  (optional)

    try:
        api_response = api_instance.sources_user_connections_oauth_partial_update(id, patched_user_o_auth_source_connection_request=patched_user_o_auth_source_connection_request)
        print("The response of SourcesApi->sources_user_connections_oauth_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_oauth_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User OAuth Source Connection. | 
 **patched_user_o_auth_source_connection_request** | [**PatchedUserOAuthSourceConnectionRequest**](PatchedUserOAuthSourceConnectionRequest.md)|  | [optional] 

### Return type

[**UserOAuthSourceConnection**](UserOAuthSourceConnection.md)

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

# **sources_user_connections_oauth_retrieve**
> UserOAuthSourceConnection sources_user_connections_oauth_retrieve(id)



Source Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user_o_auth_source_connection import UserOAuthSourceConnection
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this User OAuth Source Connection.

    try:
        api_response = api_instance.sources_user_connections_oauth_retrieve(id)
        print("The response of SourcesApi->sources_user_connections_oauth_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_oauth_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User OAuth Source Connection. | 

### Return type

[**UserOAuthSourceConnection**](UserOAuthSourceConnection.md)

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

# **sources_user_connections_oauth_update**
> UserOAuthSourceConnection sources_user_connections_oauth_update(id, user_o_auth_source_connection_request)



Source Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user_o_auth_source_connection import UserOAuthSourceConnection
from authentik_openapi.models.user_o_auth_source_connection_request import UserOAuthSourceConnectionRequest
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this User OAuth Source Connection.
    user_o_auth_source_connection_request = authentik_openapi.UserOAuthSourceConnectionRequest() # UserOAuthSourceConnectionRequest | 

    try:
        api_response = api_instance.sources_user_connections_oauth_update(id, user_o_auth_source_connection_request)
        print("The response of SourcesApi->sources_user_connections_oauth_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_oauth_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User OAuth Source Connection. | 
 **user_o_auth_source_connection_request** | [**UserOAuthSourceConnectionRequest**](UserOAuthSourceConnectionRequest.md)|  | 

### Return type

[**UserOAuthSourceConnection**](UserOAuthSourceConnection.md)

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

# **sources_user_connections_oauth_used_by_list**
> List[UsedBy] sources_user_connections_oauth_used_by_list(id)



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
    api_instance = authentik_openapi.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this User OAuth Source Connection.

    try:
        api_response = api_instance.sources_user_connections_oauth_used_by_list(id)
        print("The response of SourcesApi->sources_user_connections_oauth_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_oauth_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User OAuth Source Connection. | 

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

# **sources_user_connections_plex_create**
> PlexSourceConnection sources_user_connections_plex_create(plex_source_connection_request)



Plex Source connection Serializer

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.plex_source_connection import PlexSourceConnection
from authentik_openapi.models.plex_source_connection_request import PlexSourceConnectionRequest
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    plex_source_connection_request = authentik_openapi.PlexSourceConnectionRequest() # PlexSourceConnectionRequest | 

    try:
        api_response = api_instance.sources_user_connections_plex_create(plex_source_connection_request)
        print("The response of SourcesApi->sources_user_connections_plex_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_plex_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plex_source_connection_request** | [**PlexSourceConnectionRequest**](PlexSourceConnectionRequest.md)|  | 

### Return type

[**PlexSourceConnection**](PlexSourceConnection.md)

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

# **sources_user_connections_plex_destroy**
> sources_user_connections_plex_destroy(id)



Plex Source connection Serializer

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
    api_instance = authentik_openapi.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this User Plex Source Connection.

    try:
        api_instance.sources_user_connections_plex_destroy(id)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_plex_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User Plex Source Connection. | 

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

# **sources_user_connections_plex_list**
> PaginatedPlexSourceConnectionList sources_user_connections_plex_list(ordering=ordering, page=page, page_size=page_size, search=search, source__slug=source__slug)



Plex Source connection Serializer

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_plex_source_connection_list import PaginatedPlexSourceConnectionList
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    source__slug = 'source__slug_example' # str |  (optional)

    try:
        api_response = api_instance.sources_user_connections_plex_list(ordering=ordering, page=page, page_size=page_size, search=search, source__slug=source__slug)
        print("The response of SourcesApi->sources_user_connections_plex_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_plex_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **source__slug** | **str**|  | [optional] 

### Return type

[**PaginatedPlexSourceConnectionList**](PaginatedPlexSourceConnectionList.md)

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

# **sources_user_connections_plex_partial_update**
> PlexSourceConnection sources_user_connections_plex_partial_update(id, patched_plex_source_connection_request=patched_plex_source_connection_request)



Plex Source connection Serializer

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_plex_source_connection_request import PatchedPlexSourceConnectionRequest
from authentik_openapi.models.plex_source_connection import PlexSourceConnection
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this User Plex Source Connection.
    patched_plex_source_connection_request = authentik_openapi.PatchedPlexSourceConnectionRequest() # PatchedPlexSourceConnectionRequest |  (optional)

    try:
        api_response = api_instance.sources_user_connections_plex_partial_update(id, patched_plex_source_connection_request=patched_plex_source_connection_request)
        print("The response of SourcesApi->sources_user_connections_plex_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_plex_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User Plex Source Connection. | 
 **patched_plex_source_connection_request** | [**PatchedPlexSourceConnectionRequest**](PatchedPlexSourceConnectionRequest.md)|  | [optional] 

### Return type

[**PlexSourceConnection**](PlexSourceConnection.md)

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

# **sources_user_connections_plex_retrieve**
> PlexSourceConnection sources_user_connections_plex_retrieve(id)



Plex Source connection Serializer

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.plex_source_connection import PlexSourceConnection
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this User Plex Source Connection.

    try:
        api_response = api_instance.sources_user_connections_plex_retrieve(id)
        print("The response of SourcesApi->sources_user_connections_plex_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_plex_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User Plex Source Connection. | 

### Return type

[**PlexSourceConnection**](PlexSourceConnection.md)

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

# **sources_user_connections_plex_update**
> PlexSourceConnection sources_user_connections_plex_update(id, plex_source_connection_request)



Plex Source connection Serializer

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.plex_source_connection import PlexSourceConnection
from authentik_openapi.models.plex_source_connection_request import PlexSourceConnectionRequest
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this User Plex Source Connection.
    plex_source_connection_request = authentik_openapi.PlexSourceConnectionRequest() # PlexSourceConnectionRequest | 

    try:
        api_response = api_instance.sources_user_connections_plex_update(id, plex_source_connection_request)
        print("The response of SourcesApi->sources_user_connections_plex_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_plex_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User Plex Source Connection. | 
 **plex_source_connection_request** | [**PlexSourceConnectionRequest**](PlexSourceConnectionRequest.md)|  | 

### Return type

[**PlexSourceConnection**](PlexSourceConnection.md)

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

# **sources_user_connections_plex_used_by_list**
> List[UsedBy] sources_user_connections_plex_used_by_list(id)



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
    api_instance = authentik_openapi.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this User Plex Source Connection.

    try:
        api_response = api_instance.sources_user_connections_plex_used_by_list(id)
        print("The response of SourcesApi->sources_user_connections_plex_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_plex_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User Plex Source Connection. | 

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

# **sources_user_connections_saml_create**
> UserSAMLSourceConnection sources_user_connections_saml_create(user_saml_source_connection_request)



Source Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user_saml_source_connection import UserSAMLSourceConnection
from authentik_openapi.models.user_saml_source_connection_request import UserSAMLSourceConnectionRequest
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    user_saml_source_connection_request = authentik_openapi.UserSAMLSourceConnectionRequest() # UserSAMLSourceConnectionRequest | 

    try:
        api_response = api_instance.sources_user_connections_saml_create(user_saml_source_connection_request)
        print("The response of SourcesApi->sources_user_connections_saml_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_saml_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_saml_source_connection_request** | [**UserSAMLSourceConnectionRequest**](UserSAMLSourceConnectionRequest.md)|  | 

### Return type

[**UserSAMLSourceConnection**](UserSAMLSourceConnection.md)

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

# **sources_user_connections_saml_destroy**
> sources_user_connections_saml_destroy(id)



Source Viewset

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
    api_instance = authentik_openapi.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this User SAML Source Connection.

    try:
        api_instance.sources_user_connections_saml_destroy(id)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_saml_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User SAML Source Connection. | 

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

# **sources_user_connections_saml_list**
> PaginatedUserSAMLSourceConnectionList sources_user_connections_saml_list(ordering=ordering, page=page, page_size=page_size, search=search, source__slug=source__slug)



Source Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_user_saml_source_connection_list import PaginatedUserSAMLSourceConnectionList
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    source__slug = 'source__slug_example' # str |  (optional)

    try:
        api_response = api_instance.sources_user_connections_saml_list(ordering=ordering, page=page, page_size=page_size, search=search, source__slug=source__slug)
        print("The response of SourcesApi->sources_user_connections_saml_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_saml_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **source__slug** | **str**|  | [optional] 

### Return type

[**PaginatedUserSAMLSourceConnectionList**](PaginatedUserSAMLSourceConnectionList.md)

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

# **sources_user_connections_saml_partial_update**
> UserSAMLSourceConnection sources_user_connections_saml_partial_update(id, patched_user_saml_source_connection_request=patched_user_saml_source_connection_request)



Source Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_user_saml_source_connection_request import PatchedUserSAMLSourceConnectionRequest
from authentik_openapi.models.user_saml_source_connection import UserSAMLSourceConnection
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this User SAML Source Connection.
    patched_user_saml_source_connection_request = authentik_openapi.PatchedUserSAMLSourceConnectionRequest() # PatchedUserSAMLSourceConnectionRequest |  (optional)

    try:
        api_response = api_instance.sources_user_connections_saml_partial_update(id, patched_user_saml_source_connection_request=patched_user_saml_source_connection_request)
        print("The response of SourcesApi->sources_user_connections_saml_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_saml_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User SAML Source Connection. | 
 **patched_user_saml_source_connection_request** | [**PatchedUserSAMLSourceConnectionRequest**](PatchedUserSAMLSourceConnectionRequest.md)|  | [optional] 

### Return type

[**UserSAMLSourceConnection**](UserSAMLSourceConnection.md)

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

# **sources_user_connections_saml_retrieve**
> UserSAMLSourceConnection sources_user_connections_saml_retrieve(id)



Source Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user_saml_source_connection import UserSAMLSourceConnection
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this User SAML Source Connection.

    try:
        api_response = api_instance.sources_user_connections_saml_retrieve(id)
        print("The response of SourcesApi->sources_user_connections_saml_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_saml_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User SAML Source Connection. | 

### Return type

[**UserSAMLSourceConnection**](UserSAMLSourceConnection.md)

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

# **sources_user_connections_saml_update**
> UserSAMLSourceConnection sources_user_connections_saml_update(id, user_saml_source_connection_request)



Source Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user_saml_source_connection import UserSAMLSourceConnection
from authentik_openapi.models.user_saml_source_connection_request import UserSAMLSourceConnectionRequest
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
    api_instance = authentik_openapi.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this User SAML Source Connection.
    user_saml_source_connection_request = authentik_openapi.UserSAMLSourceConnectionRequest() # UserSAMLSourceConnectionRequest | 

    try:
        api_response = api_instance.sources_user_connections_saml_update(id, user_saml_source_connection_request)
        print("The response of SourcesApi->sources_user_connections_saml_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_saml_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User SAML Source Connection. | 
 **user_saml_source_connection_request** | [**UserSAMLSourceConnectionRequest**](UserSAMLSourceConnectionRequest.md)|  | 

### Return type

[**UserSAMLSourceConnection**](UserSAMLSourceConnection.md)

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

# **sources_user_connections_saml_used_by_list**
> List[UsedBy] sources_user_connections_saml_used_by_list(id)



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
    api_instance = authentik_openapi.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this User SAML Source Connection.

    try:
        api_response = api_instance.sources_user_connections_saml_used_by_list(id)
        print("The response of SourcesApi->sources_user_connections_saml_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_saml_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User SAML Source Connection. | 

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

