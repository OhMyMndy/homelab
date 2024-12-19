# authentik_openapi.Oauth2Api

All URIs are relative to *https://auth.home.ohmymndy.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth2_access_tokens_destroy**](Oauth2Api.md#oauth2_access_tokens_destroy) | **DELETE** /oauth2/access_tokens/{id}/ | 
[**oauth2_access_tokens_list**](Oauth2Api.md#oauth2_access_tokens_list) | **GET** /oauth2/access_tokens/ | 
[**oauth2_access_tokens_retrieve**](Oauth2Api.md#oauth2_access_tokens_retrieve) | **GET** /oauth2/access_tokens/{id}/ | 
[**oauth2_access_tokens_used_by_list**](Oauth2Api.md#oauth2_access_tokens_used_by_list) | **GET** /oauth2/access_tokens/{id}/used_by/ | 
[**oauth2_authorization_codes_destroy**](Oauth2Api.md#oauth2_authorization_codes_destroy) | **DELETE** /oauth2/authorization_codes/{id}/ | 
[**oauth2_authorization_codes_list**](Oauth2Api.md#oauth2_authorization_codes_list) | **GET** /oauth2/authorization_codes/ | 
[**oauth2_authorization_codes_retrieve**](Oauth2Api.md#oauth2_authorization_codes_retrieve) | **GET** /oauth2/authorization_codes/{id}/ | 
[**oauth2_authorization_codes_used_by_list**](Oauth2Api.md#oauth2_authorization_codes_used_by_list) | **GET** /oauth2/authorization_codes/{id}/used_by/ | 
[**oauth2_refresh_tokens_destroy**](Oauth2Api.md#oauth2_refresh_tokens_destroy) | **DELETE** /oauth2/refresh_tokens/{id}/ | 
[**oauth2_refresh_tokens_list**](Oauth2Api.md#oauth2_refresh_tokens_list) | **GET** /oauth2/refresh_tokens/ | 
[**oauth2_refresh_tokens_retrieve**](Oauth2Api.md#oauth2_refresh_tokens_retrieve) | **GET** /oauth2/refresh_tokens/{id}/ | 
[**oauth2_refresh_tokens_used_by_list**](Oauth2Api.md#oauth2_refresh_tokens_used_by_list) | **GET** /oauth2/refresh_tokens/{id}/used_by/ | 


# **oauth2_access_tokens_destroy**
> oauth2_access_tokens_destroy(id)



AccessToken Viewset

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
    api_instance = authentik_openapi.Oauth2Api(api_client)
    id = 56 # int | A unique integer value identifying this OAuth2 Access Token.

    try:
        api_instance.oauth2_access_tokens_destroy(id)
    except Exception as e:
        print("Exception when calling Oauth2Api->oauth2_access_tokens_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this OAuth2 Access Token. | 

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

# **oauth2_access_tokens_list**
> PaginatedTokenModelList oauth2_access_tokens_list(ordering=ordering, page=page, page_size=page_size, provider=provider, search=search, user=user)



AccessToken Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_token_model_list import PaginatedTokenModelList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.Oauth2Api(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    provider = 56 # int |  (optional)
    search = 'search_example' # str | A search term. (optional)
    user = 56 # int |  (optional)

    try:
        api_response = api_instance.oauth2_access_tokens_list(ordering=ordering, page=page, page_size=page_size, provider=provider, search=search, user=user)
        print("The response of Oauth2Api->oauth2_access_tokens_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Oauth2Api->oauth2_access_tokens_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **provider** | **int**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **user** | **int**|  | [optional] 

### Return type

[**PaginatedTokenModelList**](PaginatedTokenModelList.md)

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

# **oauth2_access_tokens_retrieve**
> TokenModel oauth2_access_tokens_retrieve(id)



AccessToken Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.token_model import TokenModel
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.Oauth2Api(api_client)
    id = 56 # int | A unique integer value identifying this OAuth2 Access Token.

    try:
        api_response = api_instance.oauth2_access_tokens_retrieve(id)
        print("The response of Oauth2Api->oauth2_access_tokens_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Oauth2Api->oauth2_access_tokens_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this OAuth2 Access Token. | 

### Return type

[**TokenModel**](TokenModel.md)

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

# **oauth2_access_tokens_used_by_list**
> List[UsedBy] oauth2_access_tokens_used_by_list(id)



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
    api_instance = authentik_openapi.Oauth2Api(api_client)
    id = 56 # int | A unique integer value identifying this OAuth2 Access Token.

    try:
        api_response = api_instance.oauth2_access_tokens_used_by_list(id)
        print("The response of Oauth2Api->oauth2_access_tokens_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Oauth2Api->oauth2_access_tokens_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this OAuth2 Access Token. | 

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

# **oauth2_authorization_codes_destroy**
> oauth2_authorization_codes_destroy(id)



AuthorizationCode Viewset

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
    api_instance = authentik_openapi.Oauth2Api(api_client)
    id = 56 # int | A unique integer value identifying this Authorization Code.

    try:
        api_instance.oauth2_authorization_codes_destroy(id)
    except Exception as e:
        print("Exception when calling Oauth2Api->oauth2_authorization_codes_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Authorization Code. | 

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

# **oauth2_authorization_codes_list**
> PaginatedExpiringBaseGrantModelList oauth2_authorization_codes_list(ordering=ordering, page=page, page_size=page_size, provider=provider, search=search, user=user)



AuthorizationCode Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_expiring_base_grant_model_list import PaginatedExpiringBaseGrantModelList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.Oauth2Api(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    provider = 56 # int |  (optional)
    search = 'search_example' # str | A search term. (optional)
    user = 56 # int |  (optional)

    try:
        api_response = api_instance.oauth2_authorization_codes_list(ordering=ordering, page=page, page_size=page_size, provider=provider, search=search, user=user)
        print("The response of Oauth2Api->oauth2_authorization_codes_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Oauth2Api->oauth2_authorization_codes_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **provider** | **int**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **user** | **int**|  | [optional] 

### Return type

[**PaginatedExpiringBaseGrantModelList**](PaginatedExpiringBaseGrantModelList.md)

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

# **oauth2_authorization_codes_retrieve**
> ExpiringBaseGrantModel oauth2_authorization_codes_retrieve(id)



AuthorizationCode Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.expiring_base_grant_model import ExpiringBaseGrantModel
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.Oauth2Api(api_client)
    id = 56 # int | A unique integer value identifying this Authorization Code.

    try:
        api_response = api_instance.oauth2_authorization_codes_retrieve(id)
        print("The response of Oauth2Api->oauth2_authorization_codes_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Oauth2Api->oauth2_authorization_codes_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Authorization Code. | 

### Return type

[**ExpiringBaseGrantModel**](ExpiringBaseGrantModel.md)

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

# **oauth2_authorization_codes_used_by_list**
> List[UsedBy] oauth2_authorization_codes_used_by_list(id)



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
    api_instance = authentik_openapi.Oauth2Api(api_client)
    id = 56 # int | A unique integer value identifying this Authorization Code.

    try:
        api_response = api_instance.oauth2_authorization_codes_used_by_list(id)
        print("The response of Oauth2Api->oauth2_authorization_codes_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Oauth2Api->oauth2_authorization_codes_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Authorization Code. | 

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

# **oauth2_refresh_tokens_destroy**
> oauth2_refresh_tokens_destroy(id)



RefreshToken Viewset

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
    api_instance = authentik_openapi.Oauth2Api(api_client)
    id = 56 # int | A unique integer value identifying this OAuth2 Refresh Token.

    try:
        api_instance.oauth2_refresh_tokens_destroy(id)
    except Exception as e:
        print("Exception when calling Oauth2Api->oauth2_refresh_tokens_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this OAuth2 Refresh Token. | 

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

# **oauth2_refresh_tokens_list**
> PaginatedTokenModelList oauth2_refresh_tokens_list(ordering=ordering, page=page, page_size=page_size, provider=provider, search=search, user=user)



RefreshToken Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_token_model_list import PaginatedTokenModelList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.Oauth2Api(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    provider = 56 # int |  (optional)
    search = 'search_example' # str | A search term. (optional)
    user = 56 # int |  (optional)

    try:
        api_response = api_instance.oauth2_refresh_tokens_list(ordering=ordering, page=page, page_size=page_size, provider=provider, search=search, user=user)
        print("The response of Oauth2Api->oauth2_refresh_tokens_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Oauth2Api->oauth2_refresh_tokens_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **provider** | **int**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **user** | **int**|  | [optional] 

### Return type

[**PaginatedTokenModelList**](PaginatedTokenModelList.md)

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

# **oauth2_refresh_tokens_retrieve**
> TokenModel oauth2_refresh_tokens_retrieve(id)



RefreshToken Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.token_model import TokenModel
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.Oauth2Api(api_client)
    id = 56 # int | A unique integer value identifying this OAuth2 Refresh Token.

    try:
        api_response = api_instance.oauth2_refresh_tokens_retrieve(id)
        print("The response of Oauth2Api->oauth2_refresh_tokens_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Oauth2Api->oauth2_refresh_tokens_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this OAuth2 Refresh Token. | 

### Return type

[**TokenModel**](TokenModel.md)

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

# **oauth2_refresh_tokens_used_by_list**
> List[UsedBy] oauth2_refresh_tokens_used_by_list(id)



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
    api_instance = authentik_openapi.Oauth2Api(api_client)
    id = 56 # int | A unique integer value identifying this OAuth2 Refresh Token.

    try:
        api_response = api_instance.oauth2_refresh_tokens_used_by_list(id)
        print("The response of Oauth2Api->oauth2_refresh_tokens_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Oauth2Api->oauth2_refresh_tokens_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this OAuth2 Refresh Token. | 

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

