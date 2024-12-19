# authentik_openapi.OutpostsApi

All URIs are relative to *https://auth.home.ohmymndy.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**outposts_instances_create**](OutpostsApi.md#outposts_instances_create) | **POST** /outposts/instances/ | 
[**outposts_instances_default_settings_retrieve**](OutpostsApi.md#outposts_instances_default_settings_retrieve) | **GET** /outposts/instances/default_settings/ | 
[**outposts_instances_destroy**](OutpostsApi.md#outposts_instances_destroy) | **DELETE** /outposts/instances/{uuid}/ | 
[**outposts_instances_health_list**](OutpostsApi.md#outposts_instances_health_list) | **GET** /outposts/instances/{uuid}/health/ | 
[**outposts_instances_list**](OutpostsApi.md#outposts_instances_list) | **GET** /outposts/instances/ | 
[**outposts_instances_partial_update**](OutpostsApi.md#outposts_instances_partial_update) | **PATCH** /outposts/instances/{uuid}/ | 
[**outposts_instances_retrieve**](OutpostsApi.md#outposts_instances_retrieve) | **GET** /outposts/instances/{uuid}/ | 
[**outposts_instances_update**](OutpostsApi.md#outposts_instances_update) | **PUT** /outposts/instances/{uuid}/ | 
[**outposts_instances_used_by_list**](OutpostsApi.md#outposts_instances_used_by_list) | **GET** /outposts/instances/{uuid}/used_by/ | 
[**outposts_ldap_list**](OutpostsApi.md#outposts_ldap_list) | **GET** /outposts/ldap/ | 
[**outposts_ldap_retrieve**](OutpostsApi.md#outposts_ldap_retrieve) | **GET** /outposts/ldap/{id}/ | 
[**outposts_proxy_list**](OutpostsApi.md#outposts_proxy_list) | **GET** /outposts/proxy/ | 
[**outposts_proxy_retrieve**](OutpostsApi.md#outposts_proxy_retrieve) | **GET** /outposts/proxy/{id}/ | 
[**outposts_radius_list**](OutpostsApi.md#outposts_radius_list) | **GET** /outposts/radius/ | 
[**outposts_radius_retrieve**](OutpostsApi.md#outposts_radius_retrieve) | **GET** /outposts/radius/{id}/ | 
[**outposts_service_connections_all_destroy**](OutpostsApi.md#outposts_service_connections_all_destroy) | **DELETE** /outposts/service_connections/all/{uuid}/ | 
[**outposts_service_connections_all_list**](OutpostsApi.md#outposts_service_connections_all_list) | **GET** /outposts/service_connections/all/ | 
[**outposts_service_connections_all_retrieve**](OutpostsApi.md#outposts_service_connections_all_retrieve) | **GET** /outposts/service_connections/all/{uuid}/ | 
[**outposts_service_connections_all_state_retrieve**](OutpostsApi.md#outposts_service_connections_all_state_retrieve) | **GET** /outposts/service_connections/all/{uuid}/state/ | 
[**outposts_service_connections_all_types_list**](OutpostsApi.md#outposts_service_connections_all_types_list) | **GET** /outposts/service_connections/all/types/ | 
[**outposts_service_connections_all_used_by_list**](OutpostsApi.md#outposts_service_connections_all_used_by_list) | **GET** /outposts/service_connections/all/{uuid}/used_by/ | 
[**outposts_service_connections_docker_create**](OutpostsApi.md#outposts_service_connections_docker_create) | **POST** /outposts/service_connections/docker/ | 
[**outposts_service_connections_docker_destroy**](OutpostsApi.md#outposts_service_connections_docker_destroy) | **DELETE** /outposts/service_connections/docker/{uuid}/ | 
[**outposts_service_connections_docker_list**](OutpostsApi.md#outposts_service_connections_docker_list) | **GET** /outposts/service_connections/docker/ | 
[**outposts_service_connections_docker_partial_update**](OutpostsApi.md#outposts_service_connections_docker_partial_update) | **PATCH** /outposts/service_connections/docker/{uuid}/ | 
[**outposts_service_connections_docker_retrieve**](OutpostsApi.md#outposts_service_connections_docker_retrieve) | **GET** /outposts/service_connections/docker/{uuid}/ | 
[**outposts_service_connections_docker_update**](OutpostsApi.md#outposts_service_connections_docker_update) | **PUT** /outposts/service_connections/docker/{uuid}/ | 
[**outposts_service_connections_docker_used_by_list**](OutpostsApi.md#outposts_service_connections_docker_used_by_list) | **GET** /outposts/service_connections/docker/{uuid}/used_by/ | 
[**outposts_service_connections_kubernetes_create**](OutpostsApi.md#outposts_service_connections_kubernetes_create) | **POST** /outposts/service_connections/kubernetes/ | 
[**outposts_service_connections_kubernetes_destroy**](OutpostsApi.md#outposts_service_connections_kubernetes_destroy) | **DELETE** /outposts/service_connections/kubernetes/{uuid}/ | 
[**outposts_service_connections_kubernetes_list**](OutpostsApi.md#outposts_service_connections_kubernetes_list) | **GET** /outposts/service_connections/kubernetes/ | 
[**outposts_service_connections_kubernetes_partial_update**](OutpostsApi.md#outposts_service_connections_kubernetes_partial_update) | **PATCH** /outposts/service_connections/kubernetes/{uuid}/ | 
[**outposts_service_connections_kubernetes_retrieve**](OutpostsApi.md#outposts_service_connections_kubernetes_retrieve) | **GET** /outposts/service_connections/kubernetes/{uuid}/ | 
[**outposts_service_connections_kubernetes_update**](OutpostsApi.md#outposts_service_connections_kubernetes_update) | **PUT** /outposts/service_connections/kubernetes/{uuid}/ | 
[**outposts_service_connections_kubernetes_used_by_list**](OutpostsApi.md#outposts_service_connections_kubernetes_used_by_list) | **GET** /outposts/service_connections/kubernetes/{uuid}/used_by/ | 


# **outposts_instances_create**
> Outpost outposts_instances_create(outpost_request)



Outpost Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.outpost import Outpost
from authentik_openapi.models.outpost_request import OutpostRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.OutpostsApi(api_client)
    outpost_request = authentik_openapi.OutpostRequest() # OutpostRequest | 

    try:
        api_response = api_instance.outposts_instances_create(outpost_request)
        print("The response of OutpostsApi->outposts_instances_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_instances_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **outpost_request** | [**OutpostRequest**](OutpostRequest.md)|  | 

### Return type

[**Outpost**](Outpost.md)

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

# **outposts_instances_default_settings_retrieve**
> OutpostDefaultConfig outposts_instances_default_settings_retrieve()



Global default outpost config

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.outpost_default_config import OutpostDefaultConfig
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.OutpostsApi(api_client)

    try:
        api_response = api_instance.outposts_instances_default_settings_retrieve()
        print("The response of OutpostsApi->outposts_instances_default_settings_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_instances_default_settings_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OutpostDefaultConfig**](OutpostDefaultConfig.md)

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

# **outposts_instances_destroy**
> outposts_instances_destroy(uuid)



Outpost Viewset

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
    api_instance = authentik_openapi.OutpostsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Outpost.

    try:
        api_instance.outposts_instances_destroy(uuid)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_instances_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Outpost. | 

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

# **outposts_instances_health_list**
> List[OutpostHealth] outposts_instances_health_list(uuid, managed__icontains=managed__icontains, managed__iexact=managed__iexact, name__icontains=name__icontains, name__iexact=name__iexact, ordering=ordering, providers__isnull=providers__isnull, providers_by_pk=providers_by_pk, search=search, service_connection__name__icontains=service_connection__name__icontains, service_connection__name__iexact=service_connection__name__iexact)



Get outposts current health

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.outpost_health import OutpostHealth
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.OutpostsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Outpost.
    managed__icontains = 'managed__icontains_example' # str |  (optional)
    managed__iexact = 'managed__iexact_example' # str |  (optional)
    name__icontains = 'name__icontains_example' # str |  (optional)
    name__iexact = 'name__iexact_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    providers__isnull = True # bool |  (optional)
    providers_by_pk = [56] # List[int] |  (optional)
    search = 'search_example' # str | A search term. (optional)
    service_connection__name__icontains = 'service_connection__name__icontains_example' # str |  (optional)
    service_connection__name__iexact = 'service_connection__name__iexact_example' # str |  (optional)

    try:
        api_response = api_instance.outposts_instances_health_list(uuid, managed__icontains=managed__icontains, managed__iexact=managed__iexact, name__icontains=name__icontains, name__iexact=name__iexact, ordering=ordering, providers__isnull=providers__isnull, providers_by_pk=providers_by_pk, search=search, service_connection__name__icontains=service_connection__name__icontains, service_connection__name__iexact=service_connection__name__iexact)
        print("The response of OutpostsApi->outposts_instances_health_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_instances_health_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Outpost. | 
 **managed__icontains** | **str**|  | [optional] 
 **managed__iexact** | **str**|  | [optional] 
 **name__icontains** | **str**|  | [optional] 
 **name__iexact** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **providers__isnull** | **bool**|  | [optional] 
 **providers_by_pk** | [**List[int]**](int.md)|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **service_connection__name__icontains** | **str**|  | [optional] 
 **service_connection__name__iexact** | **str**|  | [optional] 

### Return type

[**List[OutpostHealth]**](OutpostHealth.md)

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

# **outposts_instances_list**
> PaginatedOutpostList outposts_instances_list(managed__icontains=managed__icontains, managed__iexact=managed__iexact, name__icontains=name__icontains, name__iexact=name__iexact, ordering=ordering, page=page, page_size=page_size, providers__isnull=providers__isnull, providers_by_pk=providers_by_pk, search=search, service_connection__name__icontains=service_connection__name__icontains, service_connection__name__iexact=service_connection__name__iexact)



Outpost Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_outpost_list import PaginatedOutpostList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.OutpostsApi(api_client)
    managed__icontains = 'managed__icontains_example' # str |  (optional)
    managed__iexact = 'managed__iexact_example' # str |  (optional)
    name__icontains = 'name__icontains_example' # str |  (optional)
    name__iexact = 'name__iexact_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    providers__isnull = True # bool |  (optional)
    providers_by_pk = [56] # List[int] |  (optional)
    search = 'search_example' # str | A search term. (optional)
    service_connection__name__icontains = 'service_connection__name__icontains_example' # str |  (optional)
    service_connection__name__iexact = 'service_connection__name__iexact_example' # str |  (optional)

    try:
        api_response = api_instance.outposts_instances_list(managed__icontains=managed__icontains, managed__iexact=managed__iexact, name__icontains=name__icontains, name__iexact=name__iexact, ordering=ordering, page=page, page_size=page_size, providers__isnull=providers__isnull, providers_by_pk=providers_by_pk, search=search, service_connection__name__icontains=service_connection__name__icontains, service_connection__name__iexact=service_connection__name__iexact)
        print("The response of OutpostsApi->outposts_instances_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_instances_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed__icontains** | **str**|  | [optional] 
 **managed__iexact** | **str**|  | [optional] 
 **name__icontains** | **str**|  | [optional] 
 **name__iexact** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **providers__isnull** | **bool**|  | [optional] 
 **providers_by_pk** | [**List[int]**](int.md)|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **service_connection__name__icontains** | **str**|  | [optional] 
 **service_connection__name__iexact** | **str**|  | [optional] 

### Return type

[**PaginatedOutpostList**](PaginatedOutpostList.md)

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

# **outposts_instances_partial_update**
> Outpost outposts_instances_partial_update(uuid, patched_outpost_request=patched_outpost_request)



Outpost Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.outpost import Outpost
from authentik_openapi.models.patched_outpost_request import PatchedOutpostRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.OutpostsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Outpost.
    patched_outpost_request = authentik_openapi.PatchedOutpostRequest() # PatchedOutpostRequest |  (optional)

    try:
        api_response = api_instance.outposts_instances_partial_update(uuid, patched_outpost_request=patched_outpost_request)
        print("The response of OutpostsApi->outposts_instances_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_instances_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Outpost. | 
 **patched_outpost_request** | [**PatchedOutpostRequest**](PatchedOutpostRequest.md)|  | [optional] 

### Return type

[**Outpost**](Outpost.md)

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

# **outposts_instances_retrieve**
> Outpost outposts_instances_retrieve(uuid)



Outpost Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.outpost import Outpost
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.OutpostsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Outpost.

    try:
        api_response = api_instance.outposts_instances_retrieve(uuid)
        print("The response of OutpostsApi->outposts_instances_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_instances_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Outpost. | 

### Return type

[**Outpost**](Outpost.md)

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

# **outposts_instances_update**
> Outpost outposts_instances_update(uuid, outpost_request)



Outpost Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.outpost import Outpost
from authentik_openapi.models.outpost_request import OutpostRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.OutpostsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Outpost.
    outpost_request = authentik_openapi.OutpostRequest() # OutpostRequest | 

    try:
        api_response = api_instance.outposts_instances_update(uuid, outpost_request)
        print("The response of OutpostsApi->outposts_instances_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_instances_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Outpost. | 
 **outpost_request** | [**OutpostRequest**](OutpostRequest.md)|  | 

### Return type

[**Outpost**](Outpost.md)

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

# **outposts_instances_used_by_list**
> List[UsedBy] outposts_instances_used_by_list(uuid)



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
    api_instance = authentik_openapi.OutpostsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Outpost.

    try:
        api_response = api_instance.outposts_instances_used_by_list(uuid)
        print("The response of OutpostsApi->outposts_instances_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_instances_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Outpost. | 

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

# **outposts_ldap_list**
> PaginatedLDAPOutpostConfigList outposts_ldap_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)



LDAPProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_ldap_outpost_config_list import PaginatedLDAPOutpostConfigList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.OutpostsApi(api_client)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.outposts_ldap_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of OutpostsApi->outposts_ldap_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_ldap_list: %s\n" % e)
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

[**PaginatedLDAPOutpostConfigList**](PaginatedLDAPOutpostConfigList.md)

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

# **outposts_ldap_retrieve**
> LDAPOutpostConfig outposts_ldap_retrieve(id)



LDAPProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.ldap_outpost_config import LDAPOutpostConfig
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.OutpostsApi(api_client)
    id = 56 # int | A unique integer value identifying this LDAP Provider.

    try:
        api_response = api_instance.outposts_ldap_retrieve(id)
        print("The response of OutpostsApi->outposts_ldap_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_ldap_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this LDAP Provider. | 

### Return type

[**LDAPOutpostConfig**](LDAPOutpostConfig.md)

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

# **outposts_proxy_list**
> PaginatedProxyOutpostConfigList outposts_proxy_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)



ProxyProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_proxy_outpost_config_list import PaginatedProxyOutpostConfigList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.OutpostsApi(api_client)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.outposts_proxy_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of OutpostsApi->outposts_proxy_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_proxy_list: %s\n" % e)
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

[**PaginatedProxyOutpostConfigList**](PaginatedProxyOutpostConfigList.md)

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

# **outposts_proxy_retrieve**
> ProxyOutpostConfig outposts_proxy_retrieve(id)



ProxyProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.proxy_outpost_config import ProxyOutpostConfig
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.OutpostsApi(api_client)
    id = 56 # int | A unique integer value identifying this Proxy Provider.

    try:
        api_response = api_instance.outposts_proxy_retrieve(id)
        print("The response of OutpostsApi->outposts_proxy_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_proxy_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Proxy Provider. | 

### Return type

[**ProxyOutpostConfig**](ProxyOutpostConfig.md)

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

# **outposts_radius_list**
> PaginatedRadiusOutpostConfigList outposts_radius_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)



RadiusProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_radius_outpost_config_list import PaginatedRadiusOutpostConfigList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.OutpostsApi(api_client)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.outposts_radius_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of OutpostsApi->outposts_radius_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_radius_list: %s\n" % e)
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

[**PaginatedRadiusOutpostConfigList**](PaginatedRadiusOutpostConfigList.md)

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

# **outposts_radius_retrieve**
> RadiusOutpostConfig outposts_radius_retrieve(id)



RadiusProvider Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.radius_outpost_config import RadiusOutpostConfig
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.OutpostsApi(api_client)
    id = 56 # int | A unique integer value identifying this Radius Provider.

    try:
        api_response = api_instance.outposts_radius_retrieve(id)
        print("The response of OutpostsApi->outposts_radius_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_radius_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Radius Provider. | 

### Return type

[**RadiusOutpostConfig**](RadiusOutpostConfig.md)

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

# **outposts_service_connections_all_destroy**
> outposts_service_connections_all_destroy(uuid)



ServiceConnection Viewset

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
    api_instance = authentik_openapi.OutpostsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Outpost Service-Connection.

    try:
        api_instance.outposts_service_connections_all_destroy(uuid)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_service_connections_all_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Outpost Service-Connection. | 

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

# **outposts_service_connections_all_list**
> PaginatedServiceConnectionList outposts_service_connections_all_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)



ServiceConnection Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_service_connection_list import PaginatedServiceConnectionList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.OutpostsApi(api_client)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.outposts_service_connections_all_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of OutpostsApi->outposts_service_connections_all_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_service_connections_all_list: %s\n" % e)
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

[**PaginatedServiceConnectionList**](PaginatedServiceConnectionList.md)

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

# **outposts_service_connections_all_retrieve**
> ServiceConnection outposts_service_connections_all_retrieve(uuid)



ServiceConnection Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.service_connection import ServiceConnection
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.OutpostsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Outpost Service-Connection.

    try:
        api_response = api_instance.outposts_service_connections_all_retrieve(uuid)
        print("The response of OutpostsApi->outposts_service_connections_all_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_service_connections_all_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Outpost Service-Connection. | 

### Return type

[**ServiceConnection**](ServiceConnection.md)

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

# **outposts_service_connections_all_state_retrieve**
> ServiceConnectionState outposts_service_connections_all_state_retrieve(uuid)



Get the service connection's state

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.service_connection_state import ServiceConnectionState
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.OutpostsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Outpost Service-Connection.

    try:
        api_response = api_instance.outposts_service_connections_all_state_retrieve(uuid)
        print("The response of OutpostsApi->outposts_service_connections_all_state_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_service_connections_all_state_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Outpost Service-Connection. | 

### Return type

[**ServiceConnectionState**](ServiceConnectionState.md)

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

# **outposts_service_connections_all_types_list**
> List[TypeCreate] outposts_service_connections_all_types_list()



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
    api_instance = authentik_openapi.OutpostsApi(api_client)

    try:
        api_response = api_instance.outposts_service_connections_all_types_list()
        print("The response of OutpostsApi->outposts_service_connections_all_types_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_service_connections_all_types_list: %s\n" % e)
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

# **outposts_service_connections_all_used_by_list**
> List[UsedBy] outposts_service_connections_all_used_by_list(uuid)



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
    api_instance = authentik_openapi.OutpostsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Outpost Service-Connection.

    try:
        api_response = api_instance.outposts_service_connections_all_used_by_list(uuid)
        print("The response of OutpostsApi->outposts_service_connections_all_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_service_connections_all_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Outpost Service-Connection. | 

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

# **outposts_service_connections_docker_create**
> DockerServiceConnection outposts_service_connections_docker_create(docker_service_connection_request)



DockerServiceConnection Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.docker_service_connection import DockerServiceConnection
from authentik_openapi.models.docker_service_connection_request import DockerServiceConnectionRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.OutpostsApi(api_client)
    docker_service_connection_request = authentik_openapi.DockerServiceConnectionRequest() # DockerServiceConnectionRequest | 

    try:
        api_response = api_instance.outposts_service_connections_docker_create(docker_service_connection_request)
        print("The response of OutpostsApi->outposts_service_connections_docker_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_service_connections_docker_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **docker_service_connection_request** | [**DockerServiceConnectionRequest**](DockerServiceConnectionRequest.md)|  | 

### Return type

[**DockerServiceConnection**](DockerServiceConnection.md)

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

# **outposts_service_connections_docker_destroy**
> outposts_service_connections_docker_destroy(uuid)



DockerServiceConnection Viewset

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
    api_instance = authentik_openapi.OutpostsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Docker Service-Connection.

    try:
        api_instance.outposts_service_connections_docker_destroy(uuid)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_service_connections_docker_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Docker Service-Connection. | 

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

# **outposts_service_connections_docker_list**
> PaginatedDockerServiceConnectionList outposts_service_connections_docker_list(local=local, name=name, ordering=ordering, page=page, page_size=page_size, search=search, tls_authentication=tls_authentication, tls_verification=tls_verification, url=url)



DockerServiceConnection Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_docker_service_connection_list import PaginatedDockerServiceConnectionList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.OutpostsApi(api_client)
    local = True # bool |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    tls_authentication = 'tls_authentication_example' # str |  (optional)
    tls_verification = 'tls_verification_example' # str |  (optional)
    url = 'url_example' # str |  (optional)

    try:
        api_response = api_instance.outposts_service_connections_docker_list(local=local, name=name, ordering=ordering, page=page, page_size=page_size, search=search, tls_authentication=tls_authentication, tls_verification=tls_verification, url=url)
        print("The response of OutpostsApi->outposts_service_connections_docker_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_service_connections_docker_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **local** | **bool**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **tls_authentication** | **str**|  | [optional] 
 **tls_verification** | **str**|  | [optional] 
 **url** | **str**|  | [optional] 

### Return type

[**PaginatedDockerServiceConnectionList**](PaginatedDockerServiceConnectionList.md)

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

# **outposts_service_connections_docker_partial_update**
> DockerServiceConnection outposts_service_connections_docker_partial_update(uuid, patched_docker_service_connection_request=patched_docker_service_connection_request)



DockerServiceConnection Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.docker_service_connection import DockerServiceConnection
from authentik_openapi.models.patched_docker_service_connection_request import PatchedDockerServiceConnectionRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.OutpostsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Docker Service-Connection.
    patched_docker_service_connection_request = authentik_openapi.PatchedDockerServiceConnectionRequest() # PatchedDockerServiceConnectionRequest |  (optional)

    try:
        api_response = api_instance.outposts_service_connections_docker_partial_update(uuid, patched_docker_service_connection_request=patched_docker_service_connection_request)
        print("The response of OutpostsApi->outposts_service_connections_docker_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_service_connections_docker_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Docker Service-Connection. | 
 **patched_docker_service_connection_request** | [**PatchedDockerServiceConnectionRequest**](PatchedDockerServiceConnectionRequest.md)|  | [optional] 

### Return type

[**DockerServiceConnection**](DockerServiceConnection.md)

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

# **outposts_service_connections_docker_retrieve**
> DockerServiceConnection outposts_service_connections_docker_retrieve(uuid)



DockerServiceConnection Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.docker_service_connection import DockerServiceConnection
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.OutpostsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Docker Service-Connection.

    try:
        api_response = api_instance.outposts_service_connections_docker_retrieve(uuid)
        print("The response of OutpostsApi->outposts_service_connections_docker_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_service_connections_docker_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Docker Service-Connection. | 

### Return type

[**DockerServiceConnection**](DockerServiceConnection.md)

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

# **outposts_service_connections_docker_update**
> DockerServiceConnection outposts_service_connections_docker_update(uuid, docker_service_connection_request)



DockerServiceConnection Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.docker_service_connection import DockerServiceConnection
from authentik_openapi.models.docker_service_connection_request import DockerServiceConnectionRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.OutpostsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Docker Service-Connection.
    docker_service_connection_request = authentik_openapi.DockerServiceConnectionRequest() # DockerServiceConnectionRequest | 

    try:
        api_response = api_instance.outposts_service_connections_docker_update(uuid, docker_service_connection_request)
        print("The response of OutpostsApi->outposts_service_connections_docker_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_service_connections_docker_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Docker Service-Connection. | 
 **docker_service_connection_request** | [**DockerServiceConnectionRequest**](DockerServiceConnectionRequest.md)|  | 

### Return type

[**DockerServiceConnection**](DockerServiceConnection.md)

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

# **outposts_service_connections_docker_used_by_list**
> List[UsedBy] outposts_service_connections_docker_used_by_list(uuid)



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
    api_instance = authentik_openapi.OutpostsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Docker Service-Connection.

    try:
        api_response = api_instance.outposts_service_connections_docker_used_by_list(uuid)
        print("The response of OutpostsApi->outposts_service_connections_docker_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_service_connections_docker_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Docker Service-Connection. | 

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

# **outposts_service_connections_kubernetes_create**
> KubernetesServiceConnection outposts_service_connections_kubernetes_create(kubernetes_service_connection_request)



KubernetesServiceConnection Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.kubernetes_service_connection import KubernetesServiceConnection
from authentik_openapi.models.kubernetes_service_connection_request import KubernetesServiceConnectionRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.OutpostsApi(api_client)
    kubernetes_service_connection_request = authentik_openapi.KubernetesServiceConnectionRequest() # KubernetesServiceConnectionRequest | 

    try:
        api_response = api_instance.outposts_service_connections_kubernetes_create(kubernetes_service_connection_request)
        print("The response of OutpostsApi->outposts_service_connections_kubernetes_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_service_connections_kubernetes_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kubernetes_service_connection_request** | [**KubernetesServiceConnectionRequest**](KubernetesServiceConnectionRequest.md)|  | 

### Return type

[**KubernetesServiceConnection**](KubernetesServiceConnection.md)

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

# **outposts_service_connections_kubernetes_destroy**
> outposts_service_connections_kubernetes_destroy(uuid)



KubernetesServiceConnection Viewset

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
    api_instance = authentik_openapi.OutpostsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Kubernetes Service-Connection.

    try:
        api_instance.outposts_service_connections_kubernetes_destroy(uuid)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_service_connections_kubernetes_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Kubernetes Service-Connection. | 

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

# **outposts_service_connections_kubernetes_list**
> PaginatedKubernetesServiceConnectionList outposts_service_connections_kubernetes_list(local=local, name=name, ordering=ordering, page=page, page_size=page_size, search=search)



KubernetesServiceConnection Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_kubernetes_service_connection_list import PaginatedKubernetesServiceConnectionList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.OutpostsApi(api_client)
    local = True # bool |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.outposts_service_connections_kubernetes_list(local=local, name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of OutpostsApi->outposts_service_connections_kubernetes_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_service_connections_kubernetes_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **local** | **bool**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedKubernetesServiceConnectionList**](PaginatedKubernetesServiceConnectionList.md)

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

# **outposts_service_connections_kubernetes_partial_update**
> KubernetesServiceConnection outposts_service_connections_kubernetes_partial_update(uuid, patched_kubernetes_service_connection_request=patched_kubernetes_service_connection_request)



KubernetesServiceConnection Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.kubernetes_service_connection import KubernetesServiceConnection
from authentik_openapi.models.patched_kubernetes_service_connection_request import PatchedKubernetesServiceConnectionRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.OutpostsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Kubernetes Service-Connection.
    patched_kubernetes_service_connection_request = authentik_openapi.PatchedKubernetesServiceConnectionRequest() # PatchedKubernetesServiceConnectionRequest |  (optional)

    try:
        api_response = api_instance.outposts_service_connections_kubernetes_partial_update(uuid, patched_kubernetes_service_connection_request=patched_kubernetes_service_connection_request)
        print("The response of OutpostsApi->outposts_service_connections_kubernetes_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_service_connections_kubernetes_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Kubernetes Service-Connection. | 
 **patched_kubernetes_service_connection_request** | [**PatchedKubernetesServiceConnectionRequest**](PatchedKubernetesServiceConnectionRequest.md)|  | [optional] 

### Return type

[**KubernetesServiceConnection**](KubernetesServiceConnection.md)

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

# **outposts_service_connections_kubernetes_retrieve**
> KubernetesServiceConnection outposts_service_connections_kubernetes_retrieve(uuid)



KubernetesServiceConnection Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.kubernetes_service_connection import KubernetesServiceConnection
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.OutpostsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Kubernetes Service-Connection.

    try:
        api_response = api_instance.outposts_service_connections_kubernetes_retrieve(uuid)
        print("The response of OutpostsApi->outposts_service_connections_kubernetes_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_service_connections_kubernetes_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Kubernetes Service-Connection. | 

### Return type

[**KubernetesServiceConnection**](KubernetesServiceConnection.md)

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

# **outposts_service_connections_kubernetes_update**
> KubernetesServiceConnection outposts_service_connections_kubernetes_update(uuid, kubernetes_service_connection_request)



KubernetesServiceConnection Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.kubernetes_service_connection import KubernetesServiceConnection
from authentik_openapi.models.kubernetes_service_connection_request import KubernetesServiceConnectionRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.OutpostsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Kubernetes Service-Connection.
    kubernetes_service_connection_request = authentik_openapi.KubernetesServiceConnectionRequest() # KubernetesServiceConnectionRequest | 

    try:
        api_response = api_instance.outposts_service_connections_kubernetes_update(uuid, kubernetes_service_connection_request)
        print("The response of OutpostsApi->outposts_service_connections_kubernetes_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_service_connections_kubernetes_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Kubernetes Service-Connection. | 
 **kubernetes_service_connection_request** | [**KubernetesServiceConnectionRequest**](KubernetesServiceConnectionRequest.md)|  | 

### Return type

[**KubernetesServiceConnection**](KubernetesServiceConnection.md)

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

# **outposts_service_connections_kubernetes_used_by_list**
> List[UsedBy] outposts_service_connections_kubernetes_used_by_list(uuid)



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
    api_instance = authentik_openapi.OutpostsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Kubernetes Service-Connection.

    try:
        api_response = api_instance.outposts_service_connections_kubernetes_used_by_list(uuid)
        print("The response of OutpostsApi->outposts_service_connections_kubernetes_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OutpostsApi->outposts_service_connections_kubernetes_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Kubernetes Service-Connection. | 

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

