# authentik_openapi.RacApi

All URIs are relative to *https://auth.home.ohmymndy.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rac_connection_tokens_destroy**](RacApi.md#rac_connection_tokens_destroy) | **DELETE** /rac/connection_tokens/{connection_token_uuid}/ | 
[**rac_connection_tokens_list**](RacApi.md#rac_connection_tokens_list) | **GET** /rac/connection_tokens/ | 
[**rac_connection_tokens_partial_update**](RacApi.md#rac_connection_tokens_partial_update) | **PATCH** /rac/connection_tokens/{connection_token_uuid}/ | 
[**rac_connection_tokens_retrieve**](RacApi.md#rac_connection_tokens_retrieve) | **GET** /rac/connection_tokens/{connection_token_uuid}/ | 
[**rac_connection_tokens_update**](RacApi.md#rac_connection_tokens_update) | **PUT** /rac/connection_tokens/{connection_token_uuid}/ | 
[**rac_connection_tokens_used_by_list**](RacApi.md#rac_connection_tokens_used_by_list) | **GET** /rac/connection_tokens/{connection_token_uuid}/used_by/ | 
[**rac_endpoints_create**](RacApi.md#rac_endpoints_create) | **POST** /rac/endpoints/ | 
[**rac_endpoints_destroy**](RacApi.md#rac_endpoints_destroy) | **DELETE** /rac/endpoints/{pbm_uuid}/ | 
[**rac_endpoints_list**](RacApi.md#rac_endpoints_list) | **GET** /rac/endpoints/ | 
[**rac_endpoints_partial_update**](RacApi.md#rac_endpoints_partial_update) | **PATCH** /rac/endpoints/{pbm_uuid}/ | 
[**rac_endpoints_retrieve**](RacApi.md#rac_endpoints_retrieve) | **GET** /rac/endpoints/{pbm_uuid}/ | 
[**rac_endpoints_update**](RacApi.md#rac_endpoints_update) | **PUT** /rac/endpoints/{pbm_uuid}/ | 
[**rac_endpoints_used_by_list**](RacApi.md#rac_endpoints_used_by_list) | **GET** /rac/endpoints/{pbm_uuid}/used_by/ | 


# **rac_connection_tokens_destroy**
> rac_connection_tokens_destroy(connection_token_uuid)



ConnectionToken Viewset

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
    api_instance = authentik_openapi.RacApi(api_client)
    connection_token_uuid = 'connection_token_uuid_example' # str | A UUID string identifying this RAC Connection token.

    try:
        api_instance.rac_connection_tokens_destroy(connection_token_uuid)
    except Exception as e:
        print("Exception when calling RacApi->rac_connection_tokens_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_token_uuid** | **str**| A UUID string identifying this RAC Connection token. | 

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

# **rac_connection_tokens_list**
> PaginatedConnectionTokenList rac_connection_tokens_list(endpoint=endpoint, ordering=ordering, page=page, page_size=page_size, provider=provider, search=search, session__user=session__user)



ConnectionToken Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_connection_token_list import PaginatedConnectionTokenList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.RacApi(api_client)
    endpoint = 'endpoint_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    provider = 56 # int |  (optional)
    search = 'search_example' # str | A search term. (optional)
    session__user = 56 # int |  (optional)

    try:
        api_response = api_instance.rac_connection_tokens_list(endpoint=endpoint, ordering=ordering, page=page, page_size=page_size, provider=provider, search=search, session__user=session__user)
        print("The response of RacApi->rac_connection_tokens_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacApi->rac_connection_tokens_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **provider** | **int**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **session__user** | **int**|  | [optional] 

### Return type

[**PaginatedConnectionTokenList**](PaginatedConnectionTokenList.md)

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

# **rac_connection_tokens_partial_update**
> ConnectionToken rac_connection_tokens_partial_update(connection_token_uuid, patched_connection_token_request=patched_connection_token_request)



ConnectionToken Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.connection_token import ConnectionToken
from authentik_openapi.models.patched_connection_token_request import PatchedConnectionTokenRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.RacApi(api_client)
    connection_token_uuid = 'connection_token_uuid_example' # str | A UUID string identifying this RAC Connection token.
    patched_connection_token_request = authentik_openapi.PatchedConnectionTokenRequest() # PatchedConnectionTokenRequest |  (optional)

    try:
        api_response = api_instance.rac_connection_tokens_partial_update(connection_token_uuid, patched_connection_token_request=patched_connection_token_request)
        print("The response of RacApi->rac_connection_tokens_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacApi->rac_connection_tokens_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_token_uuid** | **str**| A UUID string identifying this RAC Connection token. | 
 **patched_connection_token_request** | [**PatchedConnectionTokenRequest**](PatchedConnectionTokenRequest.md)|  | [optional] 

### Return type

[**ConnectionToken**](ConnectionToken.md)

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

# **rac_connection_tokens_retrieve**
> ConnectionToken rac_connection_tokens_retrieve(connection_token_uuid)



ConnectionToken Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.connection_token import ConnectionToken
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.RacApi(api_client)
    connection_token_uuid = 'connection_token_uuid_example' # str | A UUID string identifying this RAC Connection token.

    try:
        api_response = api_instance.rac_connection_tokens_retrieve(connection_token_uuid)
        print("The response of RacApi->rac_connection_tokens_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacApi->rac_connection_tokens_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_token_uuid** | **str**| A UUID string identifying this RAC Connection token. | 

### Return type

[**ConnectionToken**](ConnectionToken.md)

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

# **rac_connection_tokens_update**
> ConnectionToken rac_connection_tokens_update(connection_token_uuid, connection_token_request)



ConnectionToken Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.connection_token import ConnectionToken
from authentik_openapi.models.connection_token_request import ConnectionTokenRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.RacApi(api_client)
    connection_token_uuid = 'connection_token_uuid_example' # str | A UUID string identifying this RAC Connection token.
    connection_token_request = authentik_openapi.ConnectionTokenRequest() # ConnectionTokenRequest | 

    try:
        api_response = api_instance.rac_connection_tokens_update(connection_token_uuid, connection_token_request)
        print("The response of RacApi->rac_connection_tokens_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacApi->rac_connection_tokens_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_token_uuid** | **str**| A UUID string identifying this RAC Connection token. | 
 **connection_token_request** | [**ConnectionTokenRequest**](ConnectionTokenRequest.md)|  | 

### Return type

[**ConnectionToken**](ConnectionToken.md)

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

# **rac_connection_tokens_used_by_list**
> List[UsedBy] rac_connection_tokens_used_by_list(connection_token_uuid)



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
    api_instance = authentik_openapi.RacApi(api_client)
    connection_token_uuid = 'connection_token_uuid_example' # str | A UUID string identifying this RAC Connection token.

    try:
        api_response = api_instance.rac_connection_tokens_used_by_list(connection_token_uuid)
        print("The response of RacApi->rac_connection_tokens_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacApi->rac_connection_tokens_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_token_uuid** | **str**| A UUID string identifying this RAC Connection token. | 

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

# **rac_endpoints_create**
> Endpoint rac_endpoints_create(endpoint_request)



Endpoint Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.endpoint import Endpoint
from authentik_openapi.models.endpoint_request import EndpointRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.RacApi(api_client)
    endpoint_request = authentik_openapi.EndpointRequest() # EndpointRequest | 

    try:
        api_response = api_instance.rac_endpoints_create(endpoint_request)
        print("The response of RacApi->rac_endpoints_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacApi->rac_endpoints_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_request** | [**EndpointRequest**](EndpointRequest.md)|  | 

### Return type

[**Endpoint**](Endpoint.md)

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

# **rac_endpoints_destroy**
> rac_endpoints_destroy(pbm_uuid)



Endpoint Viewset

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
    api_instance = authentik_openapi.RacApi(api_client)
    pbm_uuid = 'pbm_uuid_example' # str | A UUID string identifying this RAC Endpoint.

    try:
        api_instance.rac_endpoints_destroy(pbm_uuid)
    except Exception as e:
        print("Exception when calling RacApi->rac_endpoints_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pbm_uuid** | **str**| A UUID string identifying this RAC Endpoint. | 

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

# **rac_endpoints_list**
> PaginatedEndpointList rac_endpoints_list(name=name, ordering=ordering, page=page, page_size=page_size, provider=provider, search=search, superuser_full_list=superuser_full_list)



List accessible endpoints

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_endpoint_list import PaginatedEndpointList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.RacApi(api_client)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    provider = 56 # int |  (optional)
    search = 'search_example' # str |  (optional)
    superuser_full_list = True # bool |  (optional)

    try:
        api_response = api_instance.rac_endpoints_list(name=name, ordering=ordering, page=page, page_size=page_size, provider=provider, search=search, superuser_full_list=superuser_full_list)
        print("The response of RacApi->rac_endpoints_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacApi->rac_endpoints_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **provider** | **int**|  | [optional] 
 **search** | **str**|  | [optional] 
 **superuser_full_list** | **bool**|  | [optional] 

### Return type

[**PaginatedEndpointList**](PaginatedEndpointList.md)

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

# **rac_endpoints_partial_update**
> Endpoint rac_endpoints_partial_update(pbm_uuid, patched_endpoint_request=patched_endpoint_request)



Endpoint Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.endpoint import Endpoint
from authentik_openapi.models.patched_endpoint_request import PatchedEndpointRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.RacApi(api_client)
    pbm_uuid = 'pbm_uuid_example' # str | A UUID string identifying this RAC Endpoint.
    patched_endpoint_request = authentik_openapi.PatchedEndpointRequest() # PatchedEndpointRequest |  (optional)

    try:
        api_response = api_instance.rac_endpoints_partial_update(pbm_uuid, patched_endpoint_request=patched_endpoint_request)
        print("The response of RacApi->rac_endpoints_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacApi->rac_endpoints_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pbm_uuid** | **str**| A UUID string identifying this RAC Endpoint. | 
 **patched_endpoint_request** | [**PatchedEndpointRequest**](PatchedEndpointRequest.md)|  | [optional] 

### Return type

[**Endpoint**](Endpoint.md)

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

# **rac_endpoints_retrieve**
> Endpoint rac_endpoints_retrieve(pbm_uuid)



Endpoint Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.endpoint import Endpoint
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.RacApi(api_client)
    pbm_uuid = 'pbm_uuid_example' # str | A UUID string identifying this RAC Endpoint.

    try:
        api_response = api_instance.rac_endpoints_retrieve(pbm_uuid)
        print("The response of RacApi->rac_endpoints_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacApi->rac_endpoints_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pbm_uuid** | **str**| A UUID string identifying this RAC Endpoint. | 

### Return type

[**Endpoint**](Endpoint.md)

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

# **rac_endpoints_update**
> Endpoint rac_endpoints_update(pbm_uuid, endpoint_request)



Endpoint Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.endpoint import Endpoint
from authentik_openapi.models.endpoint_request import EndpointRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.RacApi(api_client)
    pbm_uuid = 'pbm_uuid_example' # str | A UUID string identifying this RAC Endpoint.
    endpoint_request = authentik_openapi.EndpointRequest() # EndpointRequest | 

    try:
        api_response = api_instance.rac_endpoints_update(pbm_uuid, endpoint_request)
        print("The response of RacApi->rac_endpoints_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacApi->rac_endpoints_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pbm_uuid** | **str**| A UUID string identifying this RAC Endpoint. | 
 **endpoint_request** | [**EndpointRequest**](EndpointRequest.md)|  | 

### Return type

[**Endpoint**](Endpoint.md)

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

# **rac_endpoints_used_by_list**
> List[UsedBy] rac_endpoints_used_by_list(pbm_uuid)



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
    api_instance = authentik_openapi.RacApi(api_client)
    pbm_uuid = 'pbm_uuid_example' # str | A UUID string identifying this RAC Endpoint.

    try:
        api_response = api_instance.rac_endpoints_used_by_list(pbm_uuid)
        print("The response of RacApi->rac_endpoints_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RacApi->rac_endpoints_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pbm_uuid** | **str**| A UUID string identifying this RAC Endpoint. | 

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

