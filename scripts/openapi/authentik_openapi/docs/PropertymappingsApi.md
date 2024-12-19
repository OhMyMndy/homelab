# authentik_openapi.PropertymappingsApi

All URIs are relative to *https://auth.home.ohmymndy.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**propertymappings_all_destroy**](PropertymappingsApi.md#propertymappings_all_destroy) | **DELETE** /propertymappings/all/{pm_uuid}/ | 
[**propertymappings_all_list**](PropertymappingsApi.md#propertymappings_all_list) | **GET** /propertymappings/all/ | 
[**propertymappings_all_retrieve**](PropertymappingsApi.md#propertymappings_all_retrieve) | **GET** /propertymappings/all/{pm_uuid}/ | 
[**propertymappings_all_test_create**](PropertymappingsApi.md#propertymappings_all_test_create) | **POST** /propertymappings/all/{pm_uuid}/test/ | 
[**propertymappings_all_types_list**](PropertymappingsApi.md#propertymappings_all_types_list) | **GET** /propertymappings/all/types/ | 
[**propertymappings_all_used_by_list**](PropertymappingsApi.md#propertymappings_all_used_by_list) | **GET** /propertymappings/all/{pm_uuid}/used_by/ | 
[**propertymappings_ldap_create**](PropertymappingsApi.md#propertymappings_ldap_create) | **POST** /propertymappings/ldap/ | 
[**propertymappings_ldap_destroy**](PropertymappingsApi.md#propertymappings_ldap_destroy) | **DELETE** /propertymappings/ldap/{pm_uuid}/ | 
[**propertymappings_ldap_list**](PropertymappingsApi.md#propertymappings_ldap_list) | **GET** /propertymappings/ldap/ | 
[**propertymappings_ldap_partial_update**](PropertymappingsApi.md#propertymappings_ldap_partial_update) | **PATCH** /propertymappings/ldap/{pm_uuid}/ | 
[**propertymappings_ldap_retrieve**](PropertymappingsApi.md#propertymappings_ldap_retrieve) | **GET** /propertymappings/ldap/{pm_uuid}/ | 
[**propertymappings_ldap_update**](PropertymappingsApi.md#propertymappings_ldap_update) | **PUT** /propertymappings/ldap/{pm_uuid}/ | 
[**propertymappings_ldap_used_by_list**](PropertymappingsApi.md#propertymappings_ldap_used_by_list) | **GET** /propertymappings/ldap/{pm_uuid}/used_by/ | 
[**propertymappings_notification_create**](PropertymappingsApi.md#propertymappings_notification_create) | **POST** /propertymappings/notification/ | 
[**propertymappings_notification_destroy**](PropertymappingsApi.md#propertymappings_notification_destroy) | **DELETE** /propertymappings/notification/{pm_uuid}/ | 
[**propertymappings_notification_list**](PropertymappingsApi.md#propertymappings_notification_list) | **GET** /propertymappings/notification/ | 
[**propertymappings_notification_partial_update**](PropertymappingsApi.md#propertymappings_notification_partial_update) | **PATCH** /propertymappings/notification/{pm_uuid}/ | 
[**propertymappings_notification_retrieve**](PropertymappingsApi.md#propertymappings_notification_retrieve) | **GET** /propertymappings/notification/{pm_uuid}/ | 
[**propertymappings_notification_update**](PropertymappingsApi.md#propertymappings_notification_update) | **PUT** /propertymappings/notification/{pm_uuid}/ | 
[**propertymappings_notification_used_by_list**](PropertymappingsApi.md#propertymappings_notification_used_by_list) | **GET** /propertymappings/notification/{pm_uuid}/used_by/ | 
[**propertymappings_provider_google_workspace_create**](PropertymappingsApi.md#propertymappings_provider_google_workspace_create) | **POST** /propertymappings/provider/google_workspace/ | 
[**propertymappings_provider_google_workspace_destroy**](PropertymappingsApi.md#propertymappings_provider_google_workspace_destroy) | **DELETE** /propertymappings/provider/google_workspace/{pm_uuid}/ | 
[**propertymappings_provider_google_workspace_list**](PropertymappingsApi.md#propertymappings_provider_google_workspace_list) | **GET** /propertymappings/provider/google_workspace/ | 
[**propertymappings_provider_google_workspace_partial_update**](PropertymappingsApi.md#propertymappings_provider_google_workspace_partial_update) | **PATCH** /propertymappings/provider/google_workspace/{pm_uuid}/ | 
[**propertymappings_provider_google_workspace_retrieve**](PropertymappingsApi.md#propertymappings_provider_google_workspace_retrieve) | **GET** /propertymappings/provider/google_workspace/{pm_uuid}/ | 
[**propertymappings_provider_google_workspace_update**](PropertymappingsApi.md#propertymappings_provider_google_workspace_update) | **PUT** /propertymappings/provider/google_workspace/{pm_uuid}/ | 
[**propertymappings_provider_google_workspace_used_by_list**](PropertymappingsApi.md#propertymappings_provider_google_workspace_used_by_list) | **GET** /propertymappings/provider/google_workspace/{pm_uuid}/used_by/ | 
[**propertymappings_provider_microsoft_entra_create**](PropertymappingsApi.md#propertymappings_provider_microsoft_entra_create) | **POST** /propertymappings/provider/microsoft_entra/ | 
[**propertymappings_provider_microsoft_entra_destroy**](PropertymappingsApi.md#propertymappings_provider_microsoft_entra_destroy) | **DELETE** /propertymappings/provider/microsoft_entra/{pm_uuid}/ | 
[**propertymappings_provider_microsoft_entra_list**](PropertymappingsApi.md#propertymappings_provider_microsoft_entra_list) | **GET** /propertymappings/provider/microsoft_entra/ | 
[**propertymappings_provider_microsoft_entra_partial_update**](PropertymappingsApi.md#propertymappings_provider_microsoft_entra_partial_update) | **PATCH** /propertymappings/provider/microsoft_entra/{pm_uuid}/ | 
[**propertymappings_provider_microsoft_entra_retrieve**](PropertymappingsApi.md#propertymappings_provider_microsoft_entra_retrieve) | **GET** /propertymappings/provider/microsoft_entra/{pm_uuid}/ | 
[**propertymappings_provider_microsoft_entra_update**](PropertymappingsApi.md#propertymappings_provider_microsoft_entra_update) | **PUT** /propertymappings/provider/microsoft_entra/{pm_uuid}/ | 
[**propertymappings_provider_microsoft_entra_used_by_list**](PropertymappingsApi.md#propertymappings_provider_microsoft_entra_used_by_list) | **GET** /propertymappings/provider/microsoft_entra/{pm_uuid}/used_by/ | 
[**propertymappings_rac_create**](PropertymappingsApi.md#propertymappings_rac_create) | **POST** /propertymappings/rac/ | 
[**propertymappings_rac_destroy**](PropertymappingsApi.md#propertymappings_rac_destroy) | **DELETE** /propertymappings/rac/{pm_uuid}/ | 
[**propertymappings_rac_list**](PropertymappingsApi.md#propertymappings_rac_list) | **GET** /propertymappings/rac/ | 
[**propertymappings_rac_partial_update**](PropertymappingsApi.md#propertymappings_rac_partial_update) | **PATCH** /propertymappings/rac/{pm_uuid}/ | 
[**propertymappings_rac_retrieve**](PropertymappingsApi.md#propertymappings_rac_retrieve) | **GET** /propertymappings/rac/{pm_uuid}/ | 
[**propertymappings_rac_update**](PropertymappingsApi.md#propertymappings_rac_update) | **PUT** /propertymappings/rac/{pm_uuid}/ | 
[**propertymappings_rac_used_by_list**](PropertymappingsApi.md#propertymappings_rac_used_by_list) | **GET** /propertymappings/rac/{pm_uuid}/used_by/ | 
[**propertymappings_saml_create**](PropertymappingsApi.md#propertymappings_saml_create) | **POST** /propertymappings/saml/ | 
[**propertymappings_saml_destroy**](PropertymappingsApi.md#propertymappings_saml_destroy) | **DELETE** /propertymappings/saml/{pm_uuid}/ | 
[**propertymappings_saml_list**](PropertymappingsApi.md#propertymappings_saml_list) | **GET** /propertymappings/saml/ | 
[**propertymappings_saml_partial_update**](PropertymappingsApi.md#propertymappings_saml_partial_update) | **PATCH** /propertymappings/saml/{pm_uuid}/ | 
[**propertymappings_saml_retrieve**](PropertymappingsApi.md#propertymappings_saml_retrieve) | **GET** /propertymappings/saml/{pm_uuid}/ | 
[**propertymappings_saml_update**](PropertymappingsApi.md#propertymappings_saml_update) | **PUT** /propertymappings/saml/{pm_uuid}/ | 
[**propertymappings_saml_used_by_list**](PropertymappingsApi.md#propertymappings_saml_used_by_list) | **GET** /propertymappings/saml/{pm_uuid}/used_by/ | 
[**propertymappings_scim_create**](PropertymappingsApi.md#propertymappings_scim_create) | **POST** /propertymappings/scim/ | 
[**propertymappings_scim_destroy**](PropertymappingsApi.md#propertymappings_scim_destroy) | **DELETE** /propertymappings/scim/{pm_uuid}/ | 
[**propertymappings_scim_list**](PropertymappingsApi.md#propertymappings_scim_list) | **GET** /propertymappings/scim/ | 
[**propertymappings_scim_partial_update**](PropertymappingsApi.md#propertymappings_scim_partial_update) | **PATCH** /propertymappings/scim/{pm_uuid}/ | 
[**propertymappings_scim_retrieve**](PropertymappingsApi.md#propertymappings_scim_retrieve) | **GET** /propertymappings/scim/{pm_uuid}/ | 
[**propertymappings_scim_update**](PropertymappingsApi.md#propertymappings_scim_update) | **PUT** /propertymappings/scim/{pm_uuid}/ | 
[**propertymappings_scim_used_by_list**](PropertymappingsApi.md#propertymappings_scim_used_by_list) | **GET** /propertymappings/scim/{pm_uuid}/used_by/ | 
[**propertymappings_scope_create**](PropertymappingsApi.md#propertymappings_scope_create) | **POST** /propertymappings/scope/ | 
[**propertymappings_scope_destroy**](PropertymappingsApi.md#propertymappings_scope_destroy) | **DELETE** /propertymappings/scope/{pm_uuid}/ | 
[**propertymappings_scope_list**](PropertymappingsApi.md#propertymappings_scope_list) | **GET** /propertymappings/scope/ | 
[**propertymappings_scope_partial_update**](PropertymappingsApi.md#propertymappings_scope_partial_update) | **PATCH** /propertymappings/scope/{pm_uuid}/ | 
[**propertymappings_scope_retrieve**](PropertymappingsApi.md#propertymappings_scope_retrieve) | **GET** /propertymappings/scope/{pm_uuid}/ | 
[**propertymappings_scope_update**](PropertymappingsApi.md#propertymappings_scope_update) | **PUT** /propertymappings/scope/{pm_uuid}/ | 
[**propertymappings_scope_used_by_list**](PropertymappingsApi.md#propertymappings_scope_used_by_list) | **GET** /propertymappings/scope/{pm_uuid}/used_by/ | 


# **propertymappings_all_destroy**
> propertymappings_all_destroy(pm_uuid)



PropertyMapping Viewset

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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Property Mapping.

    try:
        api_instance.propertymappings_all_destroy(pm_uuid)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_all_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Property Mapping. | 

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

# **propertymappings_all_list**
> PaginatedPropertyMappingList propertymappings_all_list(managed__isnull=managed__isnull, ordering=ordering, page=page, page_size=page_size, search=search)



PropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_property_mapping_list import PaginatedPropertyMappingList
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    managed__isnull = True # bool |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.propertymappings_all_list(managed__isnull=managed__isnull, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of PropertymappingsApi->propertymappings_all_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_all_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed__isnull** | **bool**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedPropertyMappingList**](PaginatedPropertyMappingList.md)

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

# **propertymappings_all_retrieve**
> PropertyMapping propertymappings_all_retrieve(pm_uuid)



PropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.property_mapping import PropertyMapping
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Property Mapping.

    try:
        api_response = api_instance.propertymappings_all_retrieve(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_all_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_all_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Property Mapping. | 

### Return type

[**PropertyMapping**](PropertyMapping.md)

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

# **propertymappings_all_test_create**
> PropertyMappingTestResult propertymappings_all_test_create(pm_uuid, format_result=format_result, property_mapping_test_request=property_mapping_test_request)



Test Property Mapping

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.property_mapping_test_request import PropertyMappingTestRequest
from authentik_openapi.models.property_mapping_test_result import PropertyMappingTestResult
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Property Mapping.
    format_result = True # bool |  (optional)
    property_mapping_test_request = authentik_openapi.PropertyMappingTestRequest() # PropertyMappingTestRequest |  (optional)

    try:
        api_response = api_instance.propertymappings_all_test_create(pm_uuid, format_result=format_result, property_mapping_test_request=property_mapping_test_request)
        print("The response of PropertymappingsApi->propertymappings_all_test_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_all_test_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Property Mapping. | 
 **format_result** | **bool**|  | [optional] 
 **property_mapping_test_request** | [**PropertyMappingTestRequest**](PropertyMappingTestRequest.md)|  | [optional] 

### Return type

[**PropertyMappingTestResult**](PropertyMappingTestResult.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid parameters |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **propertymappings_all_types_list**
> List[TypeCreate] propertymappings_all_types_list()



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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)

    try:
        api_response = api_instance.propertymappings_all_types_list()
        print("The response of PropertymappingsApi->propertymappings_all_types_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_all_types_list: %s\n" % e)
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

# **propertymappings_all_used_by_list**
> List[UsedBy] propertymappings_all_used_by_list(pm_uuid)



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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Property Mapping.

    try:
        api_response = api_instance.propertymappings_all_used_by_list(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_all_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_all_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Property Mapping. | 

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

# **propertymappings_ldap_create**
> LDAPPropertyMapping propertymappings_ldap_create(ldap_property_mapping_request)



LDAP PropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.ldap_property_mapping import LDAPPropertyMapping
from authentik_openapi.models.ldap_property_mapping_request import LDAPPropertyMappingRequest
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    ldap_property_mapping_request = authentik_openapi.LDAPPropertyMappingRequest() # LDAPPropertyMappingRequest | 

    try:
        api_response = api_instance.propertymappings_ldap_create(ldap_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_ldap_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_ldap_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldap_property_mapping_request** | [**LDAPPropertyMappingRequest**](LDAPPropertyMappingRequest.md)|  | 

### Return type

[**LDAPPropertyMapping**](LDAPPropertyMapping.md)

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

# **propertymappings_ldap_destroy**
> propertymappings_ldap_destroy(pm_uuid)



LDAP PropertyMapping Viewset

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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this LDAP Property Mapping.

    try:
        api_instance.propertymappings_ldap_destroy(pm_uuid)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_ldap_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this LDAP Property Mapping. | 

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

# **propertymappings_ldap_list**
> PaginatedLDAPPropertyMappingList propertymappings_ldap_list(expression=expression, managed=managed, name=name, object_field=object_field, ordering=ordering, page=page, page_size=page_size, pm_uuid=pm_uuid, search=search)



LDAP PropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_ldap_property_mapping_list import PaginatedLDAPPropertyMappingList
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    expression = 'expression_example' # str |  (optional)
    managed = ['managed_example'] # List[str] |  (optional)
    name = 'name_example' # str |  (optional)
    object_field = 'object_field_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    pm_uuid = 'pm_uuid_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.propertymappings_ldap_list(expression=expression, managed=managed, name=name, object_field=object_field, ordering=ordering, page=page, page_size=page_size, pm_uuid=pm_uuid, search=search)
        print("The response of PropertymappingsApi->propertymappings_ldap_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_ldap_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expression** | **str**|  | [optional] 
 **managed** | [**List[str]**](str.md)|  | [optional] 
 **name** | **str**|  | [optional] 
 **object_field** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **pm_uuid** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedLDAPPropertyMappingList**](PaginatedLDAPPropertyMappingList.md)

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

# **propertymappings_ldap_partial_update**
> LDAPPropertyMapping propertymappings_ldap_partial_update(pm_uuid, patched_ldap_property_mapping_request=patched_ldap_property_mapping_request)



LDAP PropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.ldap_property_mapping import LDAPPropertyMapping
from authentik_openapi.models.patched_ldap_property_mapping_request import PatchedLDAPPropertyMappingRequest
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this LDAP Property Mapping.
    patched_ldap_property_mapping_request = authentik_openapi.PatchedLDAPPropertyMappingRequest() # PatchedLDAPPropertyMappingRequest |  (optional)

    try:
        api_response = api_instance.propertymappings_ldap_partial_update(pm_uuid, patched_ldap_property_mapping_request=patched_ldap_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_ldap_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_ldap_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this LDAP Property Mapping. | 
 **patched_ldap_property_mapping_request** | [**PatchedLDAPPropertyMappingRequest**](PatchedLDAPPropertyMappingRequest.md)|  | [optional] 

### Return type

[**LDAPPropertyMapping**](LDAPPropertyMapping.md)

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

# **propertymappings_ldap_retrieve**
> LDAPPropertyMapping propertymappings_ldap_retrieve(pm_uuid)



LDAP PropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.ldap_property_mapping import LDAPPropertyMapping
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this LDAP Property Mapping.

    try:
        api_response = api_instance.propertymappings_ldap_retrieve(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_ldap_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_ldap_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this LDAP Property Mapping. | 

### Return type

[**LDAPPropertyMapping**](LDAPPropertyMapping.md)

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

# **propertymappings_ldap_update**
> LDAPPropertyMapping propertymappings_ldap_update(pm_uuid, ldap_property_mapping_request)



LDAP PropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.ldap_property_mapping import LDAPPropertyMapping
from authentik_openapi.models.ldap_property_mapping_request import LDAPPropertyMappingRequest
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this LDAP Property Mapping.
    ldap_property_mapping_request = authentik_openapi.LDAPPropertyMappingRequest() # LDAPPropertyMappingRequest | 

    try:
        api_response = api_instance.propertymappings_ldap_update(pm_uuid, ldap_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_ldap_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_ldap_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this LDAP Property Mapping. | 
 **ldap_property_mapping_request** | [**LDAPPropertyMappingRequest**](LDAPPropertyMappingRequest.md)|  | 

### Return type

[**LDAPPropertyMapping**](LDAPPropertyMapping.md)

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

# **propertymappings_ldap_used_by_list**
> List[UsedBy] propertymappings_ldap_used_by_list(pm_uuid)



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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this LDAP Property Mapping.

    try:
        api_response = api_instance.propertymappings_ldap_used_by_list(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_ldap_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_ldap_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this LDAP Property Mapping. | 

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

# **propertymappings_notification_create**
> NotificationWebhookMapping propertymappings_notification_create(notification_webhook_mapping_request)



NotificationWebhookMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.notification_webhook_mapping import NotificationWebhookMapping
from authentik_openapi.models.notification_webhook_mapping_request import NotificationWebhookMappingRequest
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    notification_webhook_mapping_request = authentik_openapi.NotificationWebhookMappingRequest() # NotificationWebhookMappingRequest | 

    try:
        api_response = api_instance.propertymappings_notification_create(notification_webhook_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_notification_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_notification_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_webhook_mapping_request** | [**NotificationWebhookMappingRequest**](NotificationWebhookMappingRequest.md)|  | 

### Return type

[**NotificationWebhookMapping**](NotificationWebhookMapping.md)

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

# **propertymappings_notification_destroy**
> propertymappings_notification_destroy(pm_uuid)



NotificationWebhookMapping Viewset

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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Webhook Mapping.

    try:
        api_instance.propertymappings_notification_destroy(pm_uuid)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_notification_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Webhook Mapping. | 

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

# **propertymappings_notification_list**
> PaginatedNotificationWebhookMappingList propertymappings_notification_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)



NotificationWebhookMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_notification_webhook_mapping_list import PaginatedNotificationWebhookMappingList
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.propertymappings_notification_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of PropertymappingsApi->propertymappings_notification_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_notification_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedNotificationWebhookMappingList**](PaginatedNotificationWebhookMappingList.md)

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

# **propertymappings_notification_partial_update**
> NotificationWebhookMapping propertymappings_notification_partial_update(pm_uuid, patched_notification_webhook_mapping_request=patched_notification_webhook_mapping_request)



NotificationWebhookMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.notification_webhook_mapping import NotificationWebhookMapping
from authentik_openapi.models.patched_notification_webhook_mapping_request import PatchedNotificationWebhookMappingRequest
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Webhook Mapping.
    patched_notification_webhook_mapping_request = authentik_openapi.PatchedNotificationWebhookMappingRequest() # PatchedNotificationWebhookMappingRequest |  (optional)

    try:
        api_response = api_instance.propertymappings_notification_partial_update(pm_uuid, patched_notification_webhook_mapping_request=patched_notification_webhook_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_notification_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_notification_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Webhook Mapping. | 
 **patched_notification_webhook_mapping_request** | [**PatchedNotificationWebhookMappingRequest**](PatchedNotificationWebhookMappingRequest.md)|  | [optional] 

### Return type

[**NotificationWebhookMapping**](NotificationWebhookMapping.md)

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

# **propertymappings_notification_retrieve**
> NotificationWebhookMapping propertymappings_notification_retrieve(pm_uuid)



NotificationWebhookMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.notification_webhook_mapping import NotificationWebhookMapping
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Webhook Mapping.

    try:
        api_response = api_instance.propertymappings_notification_retrieve(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_notification_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_notification_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Webhook Mapping. | 

### Return type

[**NotificationWebhookMapping**](NotificationWebhookMapping.md)

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

# **propertymappings_notification_update**
> NotificationWebhookMapping propertymappings_notification_update(pm_uuid, notification_webhook_mapping_request)



NotificationWebhookMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.notification_webhook_mapping import NotificationWebhookMapping
from authentik_openapi.models.notification_webhook_mapping_request import NotificationWebhookMappingRequest
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Webhook Mapping.
    notification_webhook_mapping_request = authentik_openapi.NotificationWebhookMappingRequest() # NotificationWebhookMappingRequest | 

    try:
        api_response = api_instance.propertymappings_notification_update(pm_uuid, notification_webhook_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_notification_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_notification_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Webhook Mapping. | 
 **notification_webhook_mapping_request** | [**NotificationWebhookMappingRequest**](NotificationWebhookMappingRequest.md)|  | 

### Return type

[**NotificationWebhookMapping**](NotificationWebhookMapping.md)

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

# **propertymappings_notification_used_by_list**
> List[UsedBy] propertymappings_notification_used_by_list(pm_uuid)



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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Webhook Mapping.

    try:
        api_response = api_instance.propertymappings_notification_used_by_list(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_notification_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_notification_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Webhook Mapping. | 

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

# **propertymappings_provider_google_workspace_create**
> GoogleWorkspaceProviderMapping propertymappings_provider_google_workspace_create(google_workspace_provider_mapping_request)



GoogleWorkspaceProviderMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.google_workspace_provider_mapping import GoogleWorkspaceProviderMapping
from authentik_openapi.models.google_workspace_provider_mapping_request import GoogleWorkspaceProviderMappingRequest
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    google_workspace_provider_mapping_request = authentik_openapi.GoogleWorkspaceProviderMappingRequest() # GoogleWorkspaceProviderMappingRequest | 

    try:
        api_response = api_instance.propertymappings_provider_google_workspace_create(google_workspace_provider_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_provider_google_workspace_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_google_workspace_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **google_workspace_provider_mapping_request** | [**GoogleWorkspaceProviderMappingRequest**](GoogleWorkspaceProviderMappingRequest.md)|  | 

### Return type

[**GoogleWorkspaceProviderMapping**](GoogleWorkspaceProviderMapping.md)

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

# **propertymappings_provider_google_workspace_destroy**
> propertymappings_provider_google_workspace_destroy(pm_uuid)



GoogleWorkspaceProviderMapping Viewset

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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Google Workspace Provider Mapping.

    try:
        api_instance.propertymappings_provider_google_workspace_destroy(pm_uuid)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_google_workspace_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Google Workspace Provider Mapping. | 

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

# **propertymappings_provider_google_workspace_list**
> PaginatedGoogleWorkspaceProviderMappingList propertymappings_provider_google_workspace_list(expression=expression, managed=managed, name=name, ordering=ordering, page=page, page_size=page_size, pm_uuid=pm_uuid, search=search)



GoogleWorkspaceProviderMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_google_workspace_provider_mapping_list import PaginatedGoogleWorkspaceProviderMappingList
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    expression = 'expression_example' # str |  (optional)
    managed = ['managed_example'] # List[str] |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    pm_uuid = 'pm_uuid_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.propertymappings_provider_google_workspace_list(expression=expression, managed=managed, name=name, ordering=ordering, page=page, page_size=page_size, pm_uuid=pm_uuid, search=search)
        print("The response of PropertymappingsApi->propertymappings_provider_google_workspace_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_google_workspace_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expression** | **str**|  | [optional] 
 **managed** | [**List[str]**](str.md)|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **pm_uuid** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedGoogleWorkspaceProviderMappingList**](PaginatedGoogleWorkspaceProviderMappingList.md)

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

# **propertymappings_provider_google_workspace_partial_update**
> GoogleWorkspaceProviderMapping propertymappings_provider_google_workspace_partial_update(pm_uuid, patched_google_workspace_provider_mapping_request=patched_google_workspace_provider_mapping_request)



GoogleWorkspaceProviderMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.google_workspace_provider_mapping import GoogleWorkspaceProviderMapping
from authentik_openapi.models.patched_google_workspace_provider_mapping_request import PatchedGoogleWorkspaceProviderMappingRequest
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Google Workspace Provider Mapping.
    patched_google_workspace_provider_mapping_request = authentik_openapi.PatchedGoogleWorkspaceProviderMappingRequest() # PatchedGoogleWorkspaceProviderMappingRequest |  (optional)

    try:
        api_response = api_instance.propertymappings_provider_google_workspace_partial_update(pm_uuid, patched_google_workspace_provider_mapping_request=patched_google_workspace_provider_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_provider_google_workspace_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_google_workspace_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Google Workspace Provider Mapping. | 
 **patched_google_workspace_provider_mapping_request** | [**PatchedGoogleWorkspaceProviderMappingRequest**](PatchedGoogleWorkspaceProviderMappingRequest.md)|  | [optional] 

### Return type

[**GoogleWorkspaceProviderMapping**](GoogleWorkspaceProviderMapping.md)

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

# **propertymappings_provider_google_workspace_retrieve**
> GoogleWorkspaceProviderMapping propertymappings_provider_google_workspace_retrieve(pm_uuid)



GoogleWorkspaceProviderMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.google_workspace_provider_mapping import GoogleWorkspaceProviderMapping
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Google Workspace Provider Mapping.

    try:
        api_response = api_instance.propertymappings_provider_google_workspace_retrieve(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_provider_google_workspace_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_google_workspace_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Google Workspace Provider Mapping. | 

### Return type

[**GoogleWorkspaceProviderMapping**](GoogleWorkspaceProviderMapping.md)

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

# **propertymappings_provider_google_workspace_update**
> GoogleWorkspaceProviderMapping propertymappings_provider_google_workspace_update(pm_uuid, google_workspace_provider_mapping_request)



GoogleWorkspaceProviderMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.google_workspace_provider_mapping import GoogleWorkspaceProviderMapping
from authentik_openapi.models.google_workspace_provider_mapping_request import GoogleWorkspaceProviderMappingRequest
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Google Workspace Provider Mapping.
    google_workspace_provider_mapping_request = authentik_openapi.GoogleWorkspaceProviderMappingRequest() # GoogleWorkspaceProviderMappingRequest | 

    try:
        api_response = api_instance.propertymappings_provider_google_workspace_update(pm_uuid, google_workspace_provider_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_provider_google_workspace_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_google_workspace_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Google Workspace Provider Mapping. | 
 **google_workspace_provider_mapping_request** | [**GoogleWorkspaceProviderMappingRequest**](GoogleWorkspaceProviderMappingRequest.md)|  | 

### Return type

[**GoogleWorkspaceProviderMapping**](GoogleWorkspaceProviderMapping.md)

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

# **propertymappings_provider_google_workspace_used_by_list**
> List[UsedBy] propertymappings_provider_google_workspace_used_by_list(pm_uuid)



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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Google Workspace Provider Mapping.

    try:
        api_response = api_instance.propertymappings_provider_google_workspace_used_by_list(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_provider_google_workspace_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_google_workspace_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Google Workspace Provider Mapping. | 

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

# **propertymappings_provider_microsoft_entra_create**
> MicrosoftEntraProviderMapping propertymappings_provider_microsoft_entra_create(microsoft_entra_provider_mapping_request)



MicrosoftEntraProviderMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.microsoft_entra_provider_mapping import MicrosoftEntraProviderMapping
from authentik_openapi.models.microsoft_entra_provider_mapping_request import MicrosoftEntraProviderMappingRequest
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    microsoft_entra_provider_mapping_request = authentik_openapi.MicrosoftEntraProviderMappingRequest() # MicrosoftEntraProviderMappingRequest | 

    try:
        api_response = api_instance.propertymappings_provider_microsoft_entra_create(microsoft_entra_provider_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_provider_microsoft_entra_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_microsoft_entra_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **microsoft_entra_provider_mapping_request** | [**MicrosoftEntraProviderMappingRequest**](MicrosoftEntraProviderMappingRequest.md)|  | 

### Return type

[**MicrosoftEntraProviderMapping**](MicrosoftEntraProviderMapping.md)

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

# **propertymappings_provider_microsoft_entra_destroy**
> propertymappings_provider_microsoft_entra_destroy(pm_uuid)



MicrosoftEntraProviderMapping Viewset

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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Microsoft Entra Provider Mapping.

    try:
        api_instance.propertymappings_provider_microsoft_entra_destroy(pm_uuid)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_microsoft_entra_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Microsoft Entra Provider Mapping. | 

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

# **propertymappings_provider_microsoft_entra_list**
> PaginatedMicrosoftEntraProviderMappingList propertymappings_provider_microsoft_entra_list(expression=expression, managed=managed, name=name, ordering=ordering, page=page, page_size=page_size, pm_uuid=pm_uuid, search=search)



MicrosoftEntraProviderMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_microsoft_entra_provider_mapping_list import PaginatedMicrosoftEntraProviderMappingList
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    expression = 'expression_example' # str |  (optional)
    managed = ['managed_example'] # List[str] |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    pm_uuid = 'pm_uuid_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.propertymappings_provider_microsoft_entra_list(expression=expression, managed=managed, name=name, ordering=ordering, page=page, page_size=page_size, pm_uuid=pm_uuid, search=search)
        print("The response of PropertymappingsApi->propertymappings_provider_microsoft_entra_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_microsoft_entra_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expression** | **str**|  | [optional] 
 **managed** | [**List[str]**](str.md)|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **pm_uuid** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedMicrosoftEntraProviderMappingList**](PaginatedMicrosoftEntraProviderMappingList.md)

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

# **propertymappings_provider_microsoft_entra_partial_update**
> MicrosoftEntraProviderMapping propertymappings_provider_microsoft_entra_partial_update(pm_uuid, patched_microsoft_entra_provider_mapping_request=patched_microsoft_entra_provider_mapping_request)



MicrosoftEntraProviderMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.microsoft_entra_provider_mapping import MicrosoftEntraProviderMapping
from authentik_openapi.models.patched_microsoft_entra_provider_mapping_request import PatchedMicrosoftEntraProviderMappingRequest
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Microsoft Entra Provider Mapping.
    patched_microsoft_entra_provider_mapping_request = authentik_openapi.PatchedMicrosoftEntraProviderMappingRequest() # PatchedMicrosoftEntraProviderMappingRequest |  (optional)

    try:
        api_response = api_instance.propertymappings_provider_microsoft_entra_partial_update(pm_uuid, patched_microsoft_entra_provider_mapping_request=patched_microsoft_entra_provider_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_provider_microsoft_entra_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_microsoft_entra_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Microsoft Entra Provider Mapping. | 
 **patched_microsoft_entra_provider_mapping_request** | [**PatchedMicrosoftEntraProviderMappingRequest**](PatchedMicrosoftEntraProviderMappingRequest.md)|  | [optional] 

### Return type

[**MicrosoftEntraProviderMapping**](MicrosoftEntraProviderMapping.md)

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

# **propertymappings_provider_microsoft_entra_retrieve**
> MicrosoftEntraProviderMapping propertymappings_provider_microsoft_entra_retrieve(pm_uuid)



MicrosoftEntraProviderMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.microsoft_entra_provider_mapping import MicrosoftEntraProviderMapping
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Microsoft Entra Provider Mapping.

    try:
        api_response = api_instance.propertymappings_provider_microsoft_entra_retrieve(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_provider_microsoft_entra_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_microsoft_entra_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Microsoft Entra Provider Mapping. | 

### Return type

[**MicrosoftEntraProviderMapping**](MicrosoftEntraProviderMapping.md)

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

# **propertymappings_provider_microsoft_entra_update**
> MicrosoftEntraProviderMapping propertymappings_provider_microsoft_entra_update(pm_uuid, microsoft_entra_provider_mapping_request)



MicrosoftEntraProviderMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.microsoft_entra_provider_mapping import MicrosoftEntraProviderMapping
from authentik_openapi.models.microsoft_entra_provider_mapping_request import MicrosoftEntraProviderMappingRequest
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Microsoft Entra Provider Mapping.
    microsoft_entra_provider_mapping_request = authentik_openapi.MicrosoftEntraProviderMappingRequest() # MicrosoftEntraProviderMappingRequest | 

    try:
        api_response = api_instance.propertymappings_provider_microsoft_entra_update(pm_uuid, microsoft_entra_provider_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_provider_microsoft_entra_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_microsoft_entra_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Microsoft Entra Provider Mapping. | 
 **microsoft_entra_provider_mapping_request** | [**MicrosoftEntraProviderMappingRequest**](MicrosoftEntraProviderMappingRequest.md)|  | 

### Return type

[**MicrosoftEntraProviderMapping**](MicrosoftEntraProviderMapping.md)

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

# **propertymappings_provider_microsoft_entra_used_by_list**
> List[UsedBy] propertymappings_provider_microsoft_entra_used_by_list(pm_uuid)



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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Microsoft Entra Provider Mapping.

    try:
        api_response = api_instance.propertymappings_provider_microsoft_entra_used_by_list(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_provider_microsoft_entra_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_provider_microsoft_entra_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Microsoft Entra Provider Mapping. | 

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

# **propertymappings_rac_create**
> RACPropertyMapping propertymappings_rac_create(rac_property_mapping_request)



RACPropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.rac_property_mapping import RACPropertyMapping
from authentik_openapi.models.rac_property_mapping_request import RACPropertyMappingRequest
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    rac_property_mapping_request = authentik_openapi.RACPropertyMappingRequest() # RACPropertyMappingRequest | 

    try:
        api_response = api_instance.propertymappings_rac_create(rac_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_rac_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_rac_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rac_property_mapping_request** | [**RACPropertyMappingRequest**](RACPropertyMappingRequest.md)|  | 

### Return type

[**RACPropertyMapping**](RACPropertyMapping.md)

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

# **propertymappings_rac_destroy**
> propertymappings_rac_destroy(pm_uuid)



RACPropertyMapping Viewset

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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this RAC Property Mapping.

    try:
        api_instance.propertymappings_rac_destroy(pm_uuid)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_rac_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this RAC Property Mapping. | 

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

# **propertymappings_rac_list**
> PaginatedRACPropertyMappingList propertymappings_rac_list(managed=managed, name=name, ordering=ordering, page=page, page_size=page_size, search=search)



RACPropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_rac_property_mapping_list import PaginatedRACPropertyMappingList
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    managed = ['managed_example'] # List[str] |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.propertymappings_rac_list(managed=managed, name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of PropertymappingsApi->propertymappings_rac_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_rac_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed** | [**List[str]**](str.md)|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedRACPropertyMappingList**](PaginatedRACPropertyMappingList.md)

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

# **propertymappings_rac_partial_update**
> RACPropertyMapping propertymappings_rac_partial_update(pm_uuid, patched_rac_property_mapping_request=patched_rac_property_mapping_request)



RACPropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_rac_property_mapping_request import PatchedRACPropertyMappingRequest
from authentik_openapi.models.rac_property_mapping import RACPropertyMapping
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this RAC Property Mapping.
    patched_rac_property_mapping_request = authentik_openapi.PatchedRACPropertyMappingRequest() # PatchedRACPropertyMappingRequest |  (optional)

    try:
        api_response = api_instance.propertymappings_rac_partial_update(pm_uuid, patched_rac_property_mapping_request=patched_rac_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_rac_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_rac_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this RAC Property Mapping. | 
 **patched_rac_property_mapping_request** | [**PatchedRACPropertyMappingRequest**](PatchedRACPropertyMappingRequest.md)|  | [optional] 

### Return type

[**RACPropertyMapping**](RACPropertyMapping.md)

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

# **propertymappings_rac_retrieve**
> RACPropertyMapping propertymappings_rac_retrieve(pm_uuid)



RACPropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.rac_property_mapping import RACPropertyMapping
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this RAC Property Mapping.

    try:
        api_response = api_instance.propertymappings_rac_retrieve(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_rac_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_rac_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this RAC Property Mapping. | 

### Return type

[**RACPropertyMapping**](RACPropertyMapping.md)

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

# **propertymappings_rac_update**
> RACPropertyMapping propertymappings_rac_update(pm_uuid, rac_property_mapping_request)



RACPropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.rac_property_mapping import RACPropertyMapping
from authentik_openapi.models.rac_property_mapping_request import RACPropertyMappingRequest
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this RAC Property Mapping.
    rac_property_mapping_request = authentik_openapi.RACPropertyMappingRequest() # RACPropertyMappingRequest | 

    try:
        api_response = api_instance.propertymappings_rac_update(pm_uuid, rac_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_rac_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_rac_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this RAC Property Mapping. | 
 **rac_property_mapping_request** | [**RACPropertyMappingRequest**](RACPropertyMappingRequest.md)|  | 

### Return type

[**RACPropertyMapping**](RACPropertyMapping.md)

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

# **propertymappings_rac_used_by_list**
> List[UsedBy] propertymappings_rac_used_by_list(pm_uuid)



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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this RAC Property Mapping.

    try:
        api_response = api_instance.propertymappings_rac_used_by_list(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_rac_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_rac_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this RAC Property Mapping. | 

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

# **propertymappings_saml_create**
> SAMLPropertyMapping propertymappings_saml_create(saml_property_mapping_request)



SAMLPropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.saml_property_mapping import SAMLPropertyMapping
from authentik_openapi.models.saml_property_mapping_request import SAMLPropertyMappingRequest
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    saml_property_mapping_request = authentik_openapi.SAMLPropertyMappingRequest() # SAMLPropertyMappingRequest | 

    try:
        api_response = api_instance.propertymappings_saml_create(saml_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_saml_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_saml_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saml_property_mapping_request** | [**SAMLPropertyMappingRequest**](SAMLPropertyMappingRequest.md)|  | 

### Return type

[**SAMLPropertyMapping**](SAMLPropertyMapping.md)

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

# **propertymappings_saml_destroy**
> propertymappings_saml_destroy(pm_uuid)



SAMLPropertyMapping Viewset

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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this SAML Property Mapping.

    try:
        api_instance.propertymappings_saml_destroy(pm_uuid)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_saml_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this SAML Property Mapping. | 

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

# **propertymappings_saml_list**
> PaginatedSAMLPropertyMappingList propertymappings_saml_list(expression=expression, friendly_name=friendly_name, managed=managed, name=name, ordering=ordering, page=page, page_size=page_size, pm_uuid=pm_uuid, saml_name=saml_name, search=search)



SAMLPropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_saml_property_mapping_list import PaginatedSAMLPropertyMappingList
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    expression = 'expression_example' # str |  (optional)
    friendly_name = 'friendly_name_example' # str |  (optional)
    managed = ['managed_example'] # List[str] |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    pm_uuid = 'pm_uuid_example' # str |  (optional)
    saml_name = 'saml_name_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.propertymappings_saml_list(expression=expression, friendly_name=friendly_name, managed=managed, name=name, ordering=ordering, page=page, page_size=page_size, pm_uuid=pm_uuid, saml_name=saml_name, search=search)
        print("The response of PropertymappingsApi->propertymappings_saml_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_saml_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expression** | **str**|  | [optional] 
 **friendly_name** | **str**|  | [optional] 
 **managed** | [**List[str]**](str.md)|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **pm_uuid** | **str**|  | [optional] 
 **saml_name** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedSAMLPropertyMappingList**](PaginatedSAMLPropertyMappingList.md)

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

# **propertymappings_saml_partial_update**
> SAMLPropertyMapping propertymappings_saml_partial_update(pm_uuid, patched_saml_property_mapping_request=patched_saml_property_mapping_request)



SAMLPropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_saml_property_mapping_request import PatchedSAMLPropertyMappingRequest
from authentik_openapi.models.saml_property_mapping import SAMLPropertyMapping
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this SAML Property Mapping.
    patched_saml_property_mapping_request = authentik_openapi.PatchedSAMLPropertyMappingRequest() # PatchedSAMLPropertyMappingRequest |  (optional)

    try:
        api_response = api_instance.propertymappings_saml_partial_update(pm_uuid, patched_saml_property_mapping_request=patched_saml_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_saml_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_saml_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this SAML Property Mapping. | 
 **patched_saml_property_mapping_request** | [**PatchedSAMLPropertyMappingRequest**](PatchedSAMLPropertyMappingRequest.md)|  | [optional] 

### Return type

[**SAMLPropertyMapping**](SAMLPropertyMapping.md)

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

# **propertymappings_saml_retrieve**
> SAMLPropertyMapping propertymappings_saml_retrieve(pm_uuid)



SAMLPropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.saml_property_mapping import SAMLPropertyMapping
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this SAML Property Mapping.

    try:
        api_response = api_instance.propertymappings_saml_retrieve(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_saml_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_saml_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this SAML Property Mapping. | 

### Return type

[**SAMLPropertyMapping**](SAMLPropertyMapping.md)

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

# **propertymappings_saml_update**
> SAMLPropertyMapping propertymappings_saml_update(pm_uuid, saml_property_mapping_request)



SAMLPropertyMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.saml_property_mapping import SAMLPropertyMapping
from authentik_openapi.models.saml_property_mapping_request import SAMLPropertyMappingRequest
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this SAML Property Mapping.
    saml_property_mapping_request = authentik_openapi.SAMLPropertyMappingRequest() # SAMLPropertyMappingRequest | 

    try:
        api_response = api_instance.propertymappings_saml_update(pm_uuid, saml_property_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_saml_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_saml_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this SAML Property Mapping. | 
 **saml_property_mapping_request** | [**SAMLPropertyMappingRequest**](SAMLPropertyMappingRequest.md)|  | 

### Return type

[**SAMLPropertyMapping**](SAMLPropertyMapping.md)

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

# **propertymappings_saml_used_by_list**
> List[UsedBy] propertymappings_saml_used_by_list(pm_uuid)



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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this SAML Property Mapping.

    try:
        api_response = api_instance.propertymappings_saml_used_by_list(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_saml_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_saml_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this SAML Property Mapping. | 

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

# **propertymappings_scim_create**
> SCIMMapping propertymappings_scim_create(scim_mapping_request)



SCIMMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.scim_mapping import SCIMMapping
from authentik_openapi.models.scim_mapping_request import SCIMMappingRequest
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    scim_mapping_request = authentik_openapi.SCIMMappingRequest() # SCIMMappingRequest | 

    try:
        api_response = api_instance.propertymappings_scim_create(scim_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_scim_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_scim_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scim_mapping_request** | [**SCIMMappingRequest**](SCIMMappingRequest.md)|  | 

### Return type

[**SCIMMapping**](SCIMMapping.md)

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

# **propertymappings_scim_destroy**
> propertymappings_scim_destroy(pm_uuid)



SCIMMapping Viewset

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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this SCIM Mapping.

    try:
        api_instance.propertymappings_scim_destroy(pm_uuid)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_scim_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this SCIM Mapping. | 

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

# **propertymappings_scim_list**
> PaginatedSCIMMappingList propertymappings_scim_list(expression=expression, managed=managed, name=name, ordering=ordering, page=page, page_size=page_size, pm_uuid=pm_uuid, search=search)



SCIMMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_scim_mapping_list import PaginatedSCIMMappingList
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    expression = 'expression_example' # str |  (optional)
    managed = ['managed_example'] # List[str] |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    pm_uuid = 'pm_uuid_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.propertymappings_scim_list(expression=expression, managed=managed, name=name, ordering=ordering, page=page, page_size=page_size, pm_uuid=pm_uuid, search=search)
        print("The response of PropertymappingsApi->propertymappings_scim_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_scim_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expression** | **str**|  | [optional] 
 **managed** | [**List[str]**](str.md)|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **pm_uuid** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedSCIMMappingList**](PaginatedSCIMMappingList.md)

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

# **propertymappings_scim_partial_update**
> SCIMMapping propertymappings_scim_partial_update(pm_uuid, patched_scim_mapping_request=patched_scim_mapping_request)



SCIMMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_scim_mapping_request import PatchedSCIMMappingRequest
from authentik_openapi.models.scim_mapping import SCIMMapping
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this SCIM Mapping.
    patched_scim_mapping_request = authentik_openapi.PatchedSCIMMappingRequest() # PatchedSCIMMappingRequest |  (optional)

    try:
        api_response = api_instance.propertymappings_scim_partial_update(pm_uuid, patched_scim_mapping_request=patched_scim_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_scim_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_scim_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this SCIM Mapping. | 
 **patched_scim_mapping_request** | [**PatchedSCIMMappingRequest**](PatchedSCIMMappingRequest.md)|  | [optional] 

### Return type

[**SCIMMapping**](SCIMMapping.md)

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

# **propertymappings_scim_retrieve**
> SCIMMapping propertymappings_scim_retrieve(pm_uuid)



SCIMMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.scim_mapping import SCIMMapping
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this SCIM Mapping.

    try:
        api_response = api_instance.propertymappings_scim_retrieve(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_scim_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_scim_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this SCIM Mapping. | 

### Return type

[**SCIMMapping**](SCIMMapping.md)

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

# **propertymappings_scim_update**
> SCIMMapping propertymappings_scim_update(pm_uuid, scim_mapping_request)



SCIMMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.scim_mapping import SCIMMapping
from authentik_openapi.models.scim_mapping_request import SCIMMappingRequest
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this SCIM Mapping.
    scim_mapping_request = authentik_openapi.SCIMMappingRequest() # SCIMMappingRequest | 

    try:
        api_response = api_instance.propertymappings_scim_update(pm_uuid, scim_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_scim_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_scim_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this SCIM Mapping. | 
 **scim_mapping_request** | [**SCIMMappingRequest**](SCIMMappingRequest.md)|  | 

### Return type

[**SCIMMapping**](SCIMMapping.md)

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

# **propertymappings_scim_used_by_list**
> List[UsedBy] propertymappings_scim_used_by_list(pm_uuid)



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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this SCIM Mapping.

    try:
        api_response = api_instance.propertymappings_scim_used_by_list(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_scim_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_scim_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this SCIM Mapping. | 

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

# **propertymappings_scope_create**
> ScopeMapping propertymappings_scope_create(scope_mapping_request)



ScopeMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.scope_mapping import ScopeMapping
from authentik_openapi.models.scope_mapping_request import ScopeMappingRequest
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    scope_mapping_request = authentik_openapi.ScopeMappingRequest() # ScopeMappingRequest | 

    try:
        api_response = api_instance.propertymappings_scope_create(scope_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_scope_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_scope_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_mapping_request** | [**ScopeMappingRequest**](ScopeMappingRequest.md)|  | 

### Return type

[**ScopeMapping**](ScopeMapping.md)

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

# **propertymappings_scope_destroy**
> propertymappings_scope_destroy(pm_uuid)



ScopeMapping Viewset

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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Scope Mapping.

    try:
        api_instance.propertymappings_scope_destroy(pm_uuid)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_scope_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Scope Mapping. | 

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

# **propertymappings_scope_list**
> PaginatedScopeMappingList propertymappings_scope_list(managed=managed, name=name, ordering=ordering, page=page, page_size=page_size, scope_name=scope_name, search=search)



ScopeMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_scope_mapping_list import PaginatedScopeMappingList
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    managed = ['managed_example'] # List[str] |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    scope_name = 'scope_name_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.propertymappings_scope_list(managed=managed, name=name, ordering=ordering, page=page, page_size=page_size, scope_name=scope_name, search=search)
        print("The response of PropertymappingsApi->propertymappings_scope_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_scope_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed** | [**List[str]**](str.md)|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **scope_name** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedScopeMappingList**](PaginatedScopeMappingList.md)

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

# **propertymappings_scope_partial_update**
> ScopeMapping propertymappings_scope_partial_update(pm_uuid, patched_scope_mapping_request=patched_scope_mapping_request)



ScopeMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_scope_mapping_request import PatchedScopeMappingRequest
from authentik_openapi.models.scope_mapping import ScopeMapping
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Scope Mapping.
    patched_scope_mapping_request = authentik_openapi.PatchedScopeMappingRequest() # PatchedScopeMappingRequest |  (optional)

    try:
        api_response = api_instance.propertymappings_scope_partial_update(pm_uuid, patched_scope_mapping_request=patched_scope_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_scope_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_scope_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Scope Mapping. | 
 **patched_scope_mapping_request** | [**PatchedScopeMappingRequest**](PatchedScopeMappingRequest.md)|  | [optional] 

### Return type

[**ScopeMapping**](ScopeMapping.md)

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

# **propertymappings_scope_retrieve**
> ScopeMapping propertymappings_scope_retrieve(pm_uuid)



ScopeMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.scope_mapping import ScopeMapping
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Scope Mapping.

    try:
        api_response = api_instance.propertymappings_scope_retrieve(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_scope_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_scope_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Scope Mapping. | 

### Return type

[**ScopeMapping**](ScopeMapping.md)

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

# **propertymappings_scope_update**
> ScopeMapping propertymappings_scope_update(pm_uuid, scope_mapping_request)



ScopeMapping Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.scope_mapping import ScopeMapping
from authentik_openapi.models.scope_mapping_request import ScopeMappingRequest
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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Scope Mapping.
    scope_mapping_request = authentik_openapi.ScopeMappingRequest() # ScopeMappingRequest | 

    try:
        api_response = api_instance.propertymappings_scope_update(pm_uuid, scope_mapping_request)
        print("The response of PropertymappingsApi->propertymappings_scope_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_scope_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Scope Mapping. | 
 **scope_mapping_request** | [**ScopeMappingRequest**](ScopeMappingRequest.md)|  | 

### Return type

[**ScopeMapping**](ScopeMapping.md)

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

# **propertymappings_scope_used_by_list**
> List[UsedBy] propertymappings_scope_used_by_list(pm_uuid)



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
    api_instance = authentik_openapi.PropertymappingsApi(api_client)
    pm_uuid = 'pm_uuid_example' # str | A UUID string identifying this Scope Mapping.

    try:
        api_response = api_instance.propertymappings_scope_used_by_list(pm_uuid)
        print("The response of PropertymappingsApi->propertymappings_scope_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropertymappingsApi->propertymappings_scope_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pm_uuid** | **str**| A UUID string identifying this Scope Mapping. | 

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

