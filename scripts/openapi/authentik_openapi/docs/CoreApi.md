# authentik_openapi.CoreApi

All URIs are relative to *https://auth.home.ohmymndy.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**core_applications_check_access_retrieve**](CoreApi.md#core_applications_check_access_retrieve) | **GET** /core/applications/{slug}/check_access/ | 
[**core_applications_create**](CoreApi.md#core_applications_create) | **POST** /core/applications/ | 
[**core_applications_destroy**](CoreApi.md#core_applications_destroy) | **DELETE** /core/applications/{slug}/ | 
[**core_applications_list**](CoreApi.md#core_applications_list) | **GET** /core/applications/ | 
[**core_applications_metrics_list**](CoreApi.md#core_applications_metrics_list) | **GET** /core/applications/{slug}/metrics/ | 
[**core_applications_partial_update**](CoreApi.md#core_applications_partial_update) | **PATCH** /core/applications/{slug}/ | 
[**core_applications_retrieve**](CoreApi.md#core_applications_retrieve) | **GET** /core/applications/{slug}/ | 
[**core_applications_set_icon_create**](CoreApi.md#core_applications_set_icon_create) | **POST** /core/applications/{slug}/set_icon/ | 
[**core_applications_set_icon_url_create**](CoreApi.md#core_applications_set_icon_url_create) | **POST** /core/applications/{slug}/set_icon_url/ | 
[**core_applications_update**](CoreApi.md#core_applications_update) | **PUT** /core/applications/{slug}/ | 
[**core_applications_used_by_list**](CoreApi.md#core_applications_used_by_list) | **GET** /core/applications/{slug}/used_by/ | 
[**core_authenticated_sessions_destroy**](CoreApi.md#core_authenticated_sessions_destroy) | **DELETE** /core/authenticated_sessions/{uuid}/ | 
[**core_authenticated_sessions_list**](CoreApi.md#core_authenticated_sessions_list) | **GET** /core/authenticated_sessions/ | 
[**core_authenticated_sessions_retrieve**](CoreApi.md#core_authenticated_sessions_retrieve) | **GET** /core/authenticated_sessions/{uuid}/ | 
[**core_authenticated_sessions_used_by_list**](CoreApi.md#core_authenticated_sessions_used_by_list) | **GET** /core/authenticated_sessions/{uuid}/used_by/ | 
[**core_brands_create**](CoreApi.md#core_brands_create) | **POST** /core/brands/ | 
[**core_brands_current_retrieve**](CoreApi.md#core_brands_current_retrieve) | **GET** /core/brands/current/ | 
[**core_brands_destroy**](CoreApi.md#core_brands_destroy) | **DELETE** /core/brands/{brand_uuid}/ | 
[**core_brands_list**](CoreApi.md#core_brands_list) | **GET** /core/brands/ | 
[**core_brands_partial_update**](CoreApi.md#core_brands_partial_update) | **PATCH** /core/brands/{brand_uuid}/ | 
[**core_brands_retrieve**](CoreApi.md#core_brands_retrieve) | **GET** /core/brands/{brand_uuid}/ | 
[**core_brands_update**](CoreApi.md#core_brands_update) | **PUT** /core/brands/{brand_uuid}/ | 
[**core_brands_used_by_list**](CoreApi.md#core_brands_used_by_list) | **GET** /core/brands/{brand_uuid}/used_by/ | 
[**core_groups_add_user_create**](CoreApi.md#core_groups_add_user_create) | **POST** /core/groups/{group_uuid}/add_user/ | 
[**core_groups_create**](CoreApi.md#core_groups_create) | **POST** /core/groups/ | 
[**core_groups_destroy**](CoreApi.md#core_groups_destroy) | **DELETE** /core/groups/{group_uuid}/ | 
[**core_groups_list**](CoreApi.md#core_groups_list) | **GET** /core/groups/ | 
[**core_groups_partial_update**](CoreApi.md#core_groups_partial_update) | **PATCH** /core/groups/{group_uuid}/ | 
[**core_groups_remove_user_create**](CoreApi.md#core_groups_remove_user_create) | **POST** /core/groups/{group_uuid}/remove_user/ | 
[**core_groups_retrieve**](CoreApi.md#core_groups_retrieve) | **GET** /core/groups/{group_uuid}/ | 
[**core_groups_update**](CoreApi.md#core_groups_update) | **PUT** /core/groups/{group_uuid}/ | 
[**core_groups_used_by_list**](CoreApi.md#core_groups_used_by_list) | **GET** /core/groups/{group_uuid}/used_by/ | 
[**core_tokens_create**](CoreApi.md#core_tokens_create) | **POST** /core/tokens/ | 
[**core_tokens_destroy**](CoreApi.md#core_tokens_destroy) | **DELETE** /core/tokens/{identifier}/ | 
[**core_tokens_list**](CoreApi.md#core_tokens_list) | **GET** /core/tokens/ | 
[**core_tokens_partial_update**](CoreApi.md#core_tokens_partial_update) | **PATCH** /core/tokens/{identifier}/ | 
[**core_tokens_retrieve**](CoreApi.md#core_tokens_retrieve) | **GET** /core/tokens/{identifier}/ | 
[**core_tokens_set_key_create**](CoreApi.md#core_tokens_set_key_create) | **POST** /core/tokens/{identifier}/set_key/ | 
[**core_tokens_update**](CoreApi.md#core_tokens_update) | **PUT** /core/tokens/{identifier}/ | 
[**core_tokens_used_by_list**](CoreApi.md#core_tokens_used_by_list) | **GET** /core/tokens/{identifier}/used_by/ | 
[**core_tokens_view_key_retrieve**](CoreApi.md#core_tokens_view_key_retrieve) | **GET** /core/tokens/{identifier}/view_key/ | 
[**core_transactional_applications_update**](CoreApi.md#core_transactional_applications_update) | **PUT** /core/transactional/applications/ | 
[**core_user_consent_destroy**](CoreApi.md#core_user_consent_destroy) | **DELETE** /core/user_consent/{id}/ | 
[**core_user_consent_list**](CoreApi.md#core_user_consent_list) | **GET** /core/user_consent/ | 
[**core_user_consent_retrieve**](CoreApi.md#core_user_consent_retrieve) | **GET** /core/user_consent/{id}/ | 
[**core_user_consent_used_by_list**](CoreApi.md#core_user_consent_used_by_list) | **GET** /core/user_consent/{id}/used_by/ | 
[**core_users_create**](CoreApi.md#core_users_create) | **POST** /core/users/ | 
[**core_users_destroy**](CoreApi.md#core_users_destroy) | **DELETE** /core/users/{id}/ | 
[**core_users_impersonate_create**](CoreApi.md#core_users_impersonate_create) | **POST** /core/users/{id}/impersonate/ | 
[**core_users_impersonate_end_retrieve**](CoreApi.md#core_users_impersonate_end_retrieve) | **GET** /core/users/impersonate_end/ | 
[**core_users_list**](CoreApi.md#core_users_list) | **GET** /core/users/ | 
[**core_users_me_retrieve**](CoreApi.md#core_users_me_retrieve) | **GET** /core/users/me/ | 
[**core_users_metrics_retrieve**](CoreApi.md#core_users_metrics_retrieve) | **GET** /core/users/{id}/metrics/ | 
[**core_users_partial_update**](CoreApi.md#core_users_partial_update) | **PATCH** /core/users/{id}/ | 
[**core_users_paths_retrieve**](CoreApi.md#core_users_paths_retrieve) | **GET** /core/users/paths/ | 
[**core_users_recovery_create**](CoreApi.md#core_users_recovery_create) | **POST** /core/users/{id}/recovery/ | 
[**core_users_recovery_email_create**](CoreApi.md#core_users_recovery_email_create) | **POST** /core/users/{id}/recovery_email/ | 
[**core_users_retrieve**](CoreApi.md#core_users_retrieve) | **GET** /core/users/{id}/ | 
[**core_users_service_account_create**](CoreApi.md#core_users_service_account_create) | **POST** /core/users/service_account/ | 
[**core_users_set_password_create**](CoreApi.md#core_users_set_password_create) | **POST** /core/users/{id}/set_password/ | 
[**core_users_update**](CoreApi.md#core_users_update) | **PUT** /core/users/{id}/ | 
[**core_users_used_by_list**](CoreApi.md#core_users_used_by_list) | **GET** /core/users/{id}/used_by/ | 


# **core_applications_check_access_retrieve**
> PolicyTestResult core_applications_check_access_retrieve(slug, for_user=for_user)



Check access to a single application by slug

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.policy_test_result import PolicyTestResult
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    slug = 'slug_example' # str | 
    for_user = 56 # int |  (optional)

    try:
        api_response = api_instance.core_applications_check_access_retrieve(slug, for_user=for_user)
        print("The response of CoreApi->core_applications_check_access_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_applications_check_access_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **for_user** | **int**|  | [optional] 

### Return type

[**PolicyTestResult**](PolicyTestResult.md)

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

# **core_applications_create**
> Application core_applications_create(application_request)



Application Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.application import Application
from authentik_openapi.models.application_request import ApplicationRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    application_request = authentik_openapi.ApplicationRequest() # ApplicationRequest | 

    try:
        api_response = api_instance.core_applications_create(application_request)
        print("The response of CoreApi->core_applications_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_applications_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_request** | [**ApplicationRequest**](ApplicationRequest.md)|  | 

### Return type

[**Application**](Application.md)

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

# **core_applications_destroy**
> core_applications_destroy(slug)



Application Viewset

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
    api_instance = authentik_openapi.CoreApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_instance.core_applications_destroy(slug)
    except Exception as e:
        print("Exception when calling CoreApi->core_applications_destroy: %s\n" % e)
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

# **core_applications_list**
> PaginatedApplicationList core_applications_list(for_user=for_user, group=group, meta_description=meta_description, meta_launch_url=meta_launch_url, meta_publisher=meta_publisher, name=name, ordering=ordering, page=page, page_size=page_size, search=search, slug=slug, superuser_full_list=superuser_full_list)



Custom list method that checks Policy based access instead of guardian

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_application_list import PaginatedApplicationList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    for_user = 56 # int |  (optional)
    group = 'group_example' # str |  (optional)
    meta_description = 'meta_description_example' # str |  (optional)
    meta_launch_url = 'meta_launch_url_example' # str |  (optional)
    meta_publisher = 'meta_publisher_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    slug = 'slug_example' # str |  (optional)
    superuser_full_list = True # bool |  (optional)

    try:
        api_response = api_instance.core_applications_list(for_user=for_user, group=group, meta_description=meta_description, meta_launch_url=meta_launch_url, meta_publisher=meta_publisher, name=name, ordering=ordering, page=page, page_size=page_size, search=search, slug=slug, superuser_full_list=superuser_full_list)
        print("The response of CoreApi->core_applications_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_applications_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **for_user** | **int**|  | [optional] 
 **group** | **str**|  | [optional] 
 **meta_description** | **str**|  | [optional] 
 **meta_launch_url** | **str**|  | [optional] 
 **meta_publisher** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **slug** | **str**|  | [optional] 
 **superuser_full_list** | **bool**|  | [optional] 

### Return type

[**PaginatedApplicationList**](PaginatedApplicationList.md)

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

# **core_applications_metrics_list**
> List[Coordinate] core_applications_metrics_list(slug)



Metrics for application logins

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.coordinate import Coordinate
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.core_applications_metrics_list(slug)
        print("The response of CoreApi->core_applications_metrics_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_applications_metrics_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**List[Coordinate]**](Coordinate.md)

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

# **core_applications_partial_update**
> Application core_applications_partial_update(slug, patched_application_request=patched_application_request)



Application Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.application import Application
from authentik_openapi.models.patched_application_request import PatchedApplicationRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    slug = 'slug_example' # str | 
    patched_application_request = authentik_openapi.PatchedApplicationRequest() # PatchedApplicationRequest |  (optional)

    try:
        api_response = api_instance.core_applications_partial_update(slug, patched_application_request=patched_application_request)
        print("The response of CoreApi->core_applications_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_applications_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **patched_application_request** | [**PatchedApplicationRequest**](PatchedApplicationRequest.md)|  | [optional] 

### Return type

[**Application**](Application.md)

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

# **core_applications_retrieve**
> Application core_applications_retrieve(slug)



Application Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.application import Application
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.core_applications_retrieve(slug)
        print("The response of CoreApi->core_applications_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_applications_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**Application**](Application.md)

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

# **core_applications_set_icon_create**
> core_applications_set_icon_create(slug, file=file, clear=clear)



Set application icon

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
    api_instance = authentik_openapi.CoreApi(api_client)
    slug = 'slug_example' # str | 
    file = None # bytearray |  (optional)
    clear = False # bool |  (optional) (default to False)

    try:
        api_instance.core_applications_set_icon_create(slug, file=file, clear=clear)
    except Exception as e:
        print("Exception when calling CoreApi->core_applications_set_icon_create: %s\n" % e)
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

# **core_applications_set_icon_url_create**
> core_applications_set_icon_url_create(slug, file_path_request)



Set application icon (as URL)

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
    api_instance = authentik_openapi.CoreApi(api_client)
    slug = 'slug_example' # str | 
    file_path_request = authentik_openapi.FilePathRequest() # FilePathRequest | 

    try:
        api_instance.core_applications_set_icon_url_create(slug, file_path_request)
    except Exception as e:
        print("Exception when calling CoreApi->core_applications_set_icon_url_create: %s\n" % e)
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

# **core_applications_update**
> Application core_applications_update(slug, application_request)



Application Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.application import Application
from authentik_openapi.models.application_request import ApplicationRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    slug = 'slug_example' # str | 
    application_request = authentik_openapi.ApplicationRequest() # ApplicationRequest | 

    try:
        api_response = api_instance.core_applications_update(slug, application_request)
        print("The response of CoreApi->core_applications_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_applications_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **application_request** | [**ApplicationRequest**](ApplicationRequest.md)|  | 

### Return type

[**Application**](Application.md)

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

# **core_applications_used_by_list**
> List[UsedBy] core_applications_used_by_list(slug)



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
    api_instance = authentik_openapi.CoreApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.core_applications_used_by_list(slug)
        print("The response of CoreApi->core_applications_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_applications_used_by_list: %s\n" % e)
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

# **core_authenticated_sessions_destroy**
> core_authenticated_sessions_destroy(uuid)



AuthenticatedSession Viewset

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
    api_instance = authentik_openapi.CoreApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Authenticated Session.

    try:
        api_instance.core_authenticated_sessions_destroy(uuid)
    except Exception as e:
        print("Exception when calling CoreApi->core_authenticated_sessions_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Authenticated Session. | 

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

# **core_authenticated_sessions_list**
> PaginatedAuthenticatedSessionList core_authenticated_sessions_list(last_ip=last_ip, last_user_agent=last_user_agent, ordering=ordering, page=page, page_size=page_size, search=search, user__username=user__username)



AuthenticatedSession Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_authenticated_session_list import PaginatedAuthenticatedSessionList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    last_ip = 'last_ip_example' # str |  (optional)
    last_user_agent = 'last_user_agent_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    user__username = 'user__username_example' # str |  (optional)

    try:
        api_response = api_instance.core_authenticated_sessions_list(last_ip=last_ip, last_user_agent=last_user_agent, ordering=ordering, page=page, page_size=page_size, search=search, user__username=user__username)
        print("The response of CoreApi->core_authenticated_sessions_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_authenticated_sessions_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_ip** | **str**|  | [optional] 
 **last_user_agent** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **user__username** | **str**|  | [optional] 

### Return type

[**PaginatedAuthenticatedSessionList**](PaginatedAuthenticatedSessionList.md)

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

# **core_authenticated_sessions_retrieve**
> AuthenticatedSession core_authenticated_sessions_retrieve(uuid)



AuthenticatedSession Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.authenticated_session import AuthenticatedSession
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Authenticated Session.

    try:
        api_response = api_instance.core_authenticated_sessions_retrieve(uuid)
        print("The response of CoreApi->core_authenticated_sessions_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_authenticated_sessions_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Authenticated Session. | 

### Return type

[**AuthenticatedSession**](AuthenticatedSession.md)

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

# **core_authenticated_sessions_used_by_list**
> List[UsedBy] core_authenticated_sessions_used_by_list(uuid)



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
    api_instance = authentik_openapi.CoreApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Authenticated Session.

    try:
        api_response = api_instance.core_authenticated_sessions_used_by_list(uuid)
        print("The response of CoreApi->core_authenticated_sessions_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_authenticated_sessions_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Authenticated Session. | 

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

# **core_brands_create**
> Brand core_brands_create(brand_request)



Brand Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.brand import Brand
from authentik_openapi.models.brand_request import BrandRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    brand_request = authentik_openapi.BrandRequest() # BrandRequest | 

    try:
        api_response = api_instance.core_brands_create(brand_request)
        print("The response of CoreApi->core_brands_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_brands_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_request** | [**BrandRequest**](BrandRequest.md)|  | 

### Return type

[**Brand**](Brand.md)

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

# **core_brands_current_retrieve**
> CurrentBrand core_brands_current_retrieve()



Get current brand

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.current_brand import CurrentBrand
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)

    try:
        api_response = api_instance.core_brands_current_retrieve()
        print("The response of CoreApi->core_brands_current_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_brands_current_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CurrentBrand**](CurrentBrand.md)

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

# **core_brands_destroy**
> core_brands_destroy(brand_uuid)



Brand Viewset

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
    api_instance = authentik_openapi.CoreApi(api_client)
    brand_uuid = 'brand_uuid_example' # str | A UUID string identifying this Brand.

    try:
        api_instance.core_brands_destroy(brand_uuid)
    except Exception as e:
        print("Exception when calling CoreApi->core_brands_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_uuid** | **str**| A UUID string identifying this Brand. | 

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

# **core_brands_list**
> PaginatedBrandList core_brands_list(brand_uuid=brand_uuid, branding_favicon=branding_favicon, branding_logo=branding_logo, branding_title=branding_title, default=default, domain=domain, flow_authentication=flow_authentication, flow_device_code=flow_device_code, flow_invalidation=flow_invalidation, flow_recovery=flow_recovery, flow_unenrollment=flow_unenrollment, flow_user_settings=flow_user_settings, ordering=ordering, page=page, page_size=page_size, search=search, web_certificate=web_certificate)



Brand Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_brand_list import PaginatedBrandList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    brand_uuid = 'brand_uuid_example' # str |  (optional)
    branding_favicon = 'branding_favicon_example' # str |  (optional)
    branding_logo = 'branding_logo_example' # str |  (optional)
    branding_title = 'branding_title_example' # str |  (optional)
    default = True # bool |  (optional)
    domain = 'domain_example' # str |  (optional)
    flow_authentication = 'flow_authentication_example' # str |  (optional)
    flow_device_code = 'flow_device_code_example' # str |  (optional)
    flow_invalidation = 'flow_invalidation_example' # str |  (optional)
    flow_recovery = 'flow_recovery_example' # str |  (optional)
    flow_unenrollment = 'flow_unenrollment_example' # str |  (optional)
    flow_user_settings = 'flow_user_settings_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    web_certificate = 'web_certificate_example' # str |  (optional)

    try:
        api_response = api_instance.core_brands_list(brand_uuid=brand_uuid, branding_favicon=branding_favicon, branding_logo=branding_logo, branding_title=branding_title, default=default, domain=domain, flow_authentication=flow_authentication, flow_device_code=flow_device_code, flow_invalidation=flow_invalidation, flow_recovery=flow_recovery, flow_unenrollment=flow_unenrollment, flow_user_settings=flow_user_settings, ordering=ordering, page=page, page_size=page_size, search=search, web_certificate=web_certificate)
        print("The response of CoreApi->core_brands_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_brands_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_uuid** | **str**|  | [optional] 
 **branding_favicon** | **str**|  | [optional] 
 **branding_logo** | **str**|  | [optional] 
 **branding_title** | **str**|  | [optional] 
 **default** | **bool**|  | [optional] 
 **domain** | **str**|  | [optional] 
 **flow_authentication** | **str**|  | [optional] 
 **flow_device_code** | **str**|  | [optional] 
 **flow_invalidation** | **str**|  | [optional] 
 **flow_recovery** | **str**|  | [optional] 
 **flow_unenrollment** | **str**|  | [optional] 
 **flow_user_settings** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **web_certificate** | **str**|  | [optional] 

### Return type

[**PaginatedBrandList**](PaginatedBrandList.md)

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

# **core_brands_partial_update**
> Brand core_brands_partial_update(brand_uuid, patched_brand_request=patched_brand_request)



Brand Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.brand import Brand
from authentik_openapi.models.patched_brand_request import PatchedBrandRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    brand_uuid = 'brand_uuid_example' # str | A UUID string identifying this Brand.
    patched_brand_request = authentik_openapi.PatchedBrandRequest() # PatchedBrandRequest |  (optional)

    try:
        api_response = api_instance.core_brands_partial_update(brand_uuid, patched_brand_request=patched_brand_request)
        print("The response of CoreApi->core_brands_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_brands_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_uuid** | **str**| A UUID string identifying this Brand. | 
 **patched_brand_request** | [**PatchedBrandRequest**](PatchedBrandRequest.md)|  | [optional] 

### Return type

[**Brand**](Brand.md)

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

# **core_brands_retrieve**
> Brand core_brands_retrieve(brand_uuid)



Brand Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.brand import Brand
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    brand_uuid = 'brand_uuid_example' # str | A UUID string identifying this Brand.

    try:
        api_response = api_instance.core_brands_retrieve(brand_uuid)
        print("The response of CoreApi->core_brands_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_brands_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_uuid** | **str**| A UUID string identifying this Brand. | 

### Return type

[**Brand**](Brand.md)

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

# **core_brands_update**
> Brand core_brands_update(brand_uuid, brand_request)



Brand Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.brand import Brand
from authentik_openapi.models.brand_request import BrandRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    brand_uuid = 'brand_uuid_example' # str | A UUID string identifying this Brand.
    brand_request = authentik_openapi.BrandRequest() # BrandRequest | 

    try:
        api_response = api_instance.core_brands_update(brand_uuid, brand_request)
        print("The response of CoreApi->core_brands_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_brands_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_uuid** | **str**| A UUID string identifying this Brand. | 
 **brand_request** | [**BrandRequest**](BrandRequest.md)|  | 

### Return type

[**Brand**](Brand.md)

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

# **core_brands_used_by_list**
> List[UsedBy] core_brands_used_by_list(brand_uuid)



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
    api_instance = authentik_openapi.CoreApi(api_client)
    brand_uuid = 'brand_uuid_example' # str | A UUID string identifying this Brand.

    try:
        api_response = api_instance.core_brands_used_by_list(brand_uuid)
        print("The response of CoreApi->core_brands_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_brands_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_uuid** | **str**| A UUID string identifying this Brand. | 

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

# **core_groups_add_user_create**
> core_groups_add_user_create(group_uuid, user_account_request)



Add user to group

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user_account_request import UserAccountRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    group_uuid = 'group_uuid_example' # str | A UUID string identifying this Group.
    user_account_request = authentik_openapi.UserAccountRequest() # UserAccountRequest | 

    try:
        api_instance.core_groups_add_user_create(group_uuid, user_account_request)
    except Exception as e:
        print("Exception when calling CoreApi->core_groups_add_user_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_uuid** | **str**| A UUID string identifying this Group. | 
 **user_account_request** | [**UserAccountRequest**](UserAccountRequest.md)|  | 

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
**204** | User added |  -  |
**404** | User not found |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_groups_create**
> Group core_groups_create(group_request)



Group Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.group import Group
from authentik_openapi.models.group_request import GroupRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    group_request = authentik_openapi.GroupRequest() # GroupRequest | 

    try:
        api_response = api_instance.core_groups_create(group_request)
        print("The response of CoreApi->core_groups_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_groups_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_request** | [**GroupRequest**](GroupRequest.md)|  | 

### Return type

[**Group**](Group.md)

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

# **core_groups_destroy**
> core_groups_destroy(group_uuid)



Group Viewset

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
    api_instance = authentik_openapi.CoreApi(api_client)
    group_uuid = 'group_uuid_example' # str | A UUID string identifying this Group.

    try:
        api_instance.core_groups_destroy(group_uuid)
    except Exception as e:
        print("Exception when calling CoreApi->core_groups_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_uuid** | **str**| A UUID string identifying this Group. | 

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

# **core_groups_list**
> PaginatedGroupList core_groups_list(attributes=attributes, include_users=include_users, is_superuser=is_superuser, members_by_pk=members_by_pk, members_by_username=members_by_username, name=name, ordering=ordering, page=page, page_size=page_size, search=search)



Group Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_group_list import PaginatedGroupList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    attributes = 'attributes_example' # str | Attributes (optional)
    include_users = True # bool |  (optional) (default to True)
    is_superuser = True # bool |  (optional)
    members_by_pk = [56] # List[int] |  (optional)
    members_by_username = ['members_by_username_example'] # List[str] | Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.core_groups_list(attributes=attributes, include_users=include_users, is_superuser=is_superuser, members_by_pk=members_by_pk, members_by_username=members_by_username, name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of CoreApi->core_groups_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_groups_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attributes** | **str**| Attributes | [optional] 
 **include_users** | **bool**|  | [optional] [default to True]
 **is_superuser** | **bool**|  | [optional] 
 **members_by_pk** | [**List[int]**](int.md)|  | [optional] 
 **members_by_username** | [**List[str]**](str.md)| Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedGroupList**](PaginatedGroupList.md)

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

# **core_groups_partial_update**
> Group core_groups_partial_update(group_uuid, patched_group_request=patched_group_request)



Group Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.group import Group
from authentik_openapi.models.patched_group_request import PatchedGroupRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    group_uuid = 'group_uuid_example' # str | A UUID string identifying this Group.
    patched_group_request = authentik_openapi.PatchedGroupRequest() # PatchedGroupRequest |  (optional)

    try:
        api_response = api_instance.core_groups_partial_update(group_uuid, patched_group_request=patched_group_request)
        print("The response of CoreApi->core_groups_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_groups_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_uuid** | **str**| A UUID string identifying this Group. | 
 **patched_group_request** | [**PatchedGroupRequest**](PatchedGroupRequest.md)|  | [optional] 

### Return type

[**Group**](Group.md)

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

# **core_groups_remove_user_create**
> core_groups_remove_user_create(group_uuid, user_account_request)



Add user to group

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user_account_request import UserAccountRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    group_uuid = 'group_uuid_example' # str | A UUID string identifying this Group.
    user_account_request = authentik_openapi.UserAccountRequest() # UserAccountRequest | 

    try:
        api_instance.core_groups_remove_user_create(group_uuid, user_account_request)
    except Exception as e:
        print("Exception when calling CoreApi->core_groups_remove_user_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_uuid** | **str**| A UUID string identifying this Group. | 
 **user_account_request** | [**UserAccountRequest**](UserAccountRequest.md)|  | 

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
**204** | User added |  -  |
**404** | User not found |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_groups_retrieve**
> Group core_groups_retrieve(group_uuid, include_users=include_users)



Group Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.group import Group
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    group_uuid = 'group_uuid_example' # str | A UUID string identifying this Group.
    include_users = True # bool |  (optional) (default to True)

    try:
        api_response = api_instance.core_groups_retrieve(group_uuid, include_users=include_users)
        print("The response of CoreApi->core_groups_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_groups_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_uuid** | **str**| A UUID string identifying this Group. | 
 **include_users** | **bool**|  | [optional] [default to True]

### Return type

[**Group**](Group.md)

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

# **core_groups_update**
> Group core_groups_update(group_uuid, group_request)



Group Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.group import Group
from authentik_openapi.models.group_request import GroupRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    group_uuid = 'group_uuid_example' # str | A UUID string identifying this Group.
    group_request = authentik_openapi.GroupRequest() # GroupRequest | 

    try:
        api_response = api_instance.core_groups_update(group_uuid, group_request)
        print("The response of CoreApi->core_groups_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_groups_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_uuid** | **str**| A UUID string identifying this Group. | 
 **group_request** | [**GroupRequest**](GroupRequest.md)|  | 

### Return type

[**Group**](Group.md)

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

# **core_groups_used_by_list**
> List[UsedBy] core_groups_used_by_list(group_uuid)



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
    api_instance = authentik_openapi.CoreApi(api_client)
    group_uuid = 'group_uuid_example' # str | A UUID string identifying this Group.

    try:
        api_response = api_instance.core_groups_used_by_list(group_uuid)
        print("The response of CoreApi->core_groups_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_groups_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_uuid** | **str**| A UUID string identifying this Group. | 

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

# **core_tokens_create**
> Token core_tokens_create(token_request)



Token Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.token import Token
from authentik_openapi.models.token_request import TokenRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    token_request = authentik_openapi.TokenRequest() # TokenRequest | 

    try:
        api_response = api_instance.core_tokens_create(token_request)
        print("The response of CoreApi->core_tokens_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_tokens_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_request** | [**TokenRequest**](TokenRequest.md)|  | 

### Return type

[**Token**](Token.md)

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

# **core_tokens_destroy**
> core_tokens_destroy(identifier)



Token Viewset

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
    api_instance = authentik_openapi.CoreApi(api_client)
    identifier = 'identifier_example' # str | 

    try:
        api_instance.core_tokens_destroy(identifier)
    except Exception as e:
        print("Exception when calling CoreApi->core_tokens_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 

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

# **core_tokens_list**
> PaginatedTokenList core_tokens_list(description=description, expires=expires, expiring=expiring, identifier=identifier, intent=intent, managed=managed, ordering=ordering, page=page, page_size=page_size, search=search, user__username=user__username)



Token Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_token_list import PaginatedTokenList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    description = 'description_example' # str |  (optional)
    expires = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    expiring = True # bool |  (optional)
    identifier = 'identifier_example' # str |  (optional)
    intent = 'intent_example' # str |  (optional)
    managed = 'managed_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    user__username = 'user__username_example' # str |  (optional)

    try:
        api_response = api_instance.core_tokens_list(description=description, expires=expires, expiring=expiring, identifier=identifier, intent=intent, managed=managed, ordering=ordering, page=page, page_size=page_size, search=search, user__username=user__username)
        print("The response of CoreApi->core_tokens_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_tokens_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description** | **str**|  | [optional] 
 **expires** | **datetime**|  | [optional] 
 **expiring** | **bool**|  | [optional] 
 **identifier** | **str**|  | [optional] 
 **intent** | **str**|  | [optional] 
 **managed** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **user__username** | **str**|  | [optional] 

### Return type

[**PaginatedTokenList**](PaginatedTokenList.md)

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

# **core_tokens_partial_update**
> Token core_tokens_partial_update(identifier, patched_token_request=patched_token_request)



Token Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_token_request import PatchedTokenRequest
from authentik_openapi.models.token import Token
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    identifier = 'identifier_example' # str | 
    patched_token_request = authentik_openapi.PatchedTokenRequest() # PatchedTokenRequest |  (optional)

    try:
        api_response = api_instance.core_tokens_partial_update(identifier, patched_token_request=patched_token_request)
        print("The response of CoreApi->core_tokens_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_tokens_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 
 **patched_token_request** | [**PatchedTokenRequest**](PatchedTokenRequest.md)|  | [optional] 

### Return type

[**Token**](Token.md)

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

# **core_tokens_retrieve**
> Token core_tokens_retrieve(identifier)



Token Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.token import Token
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    identifier = 'identifier_example' # str | 

    try:
        api_response = api_instance.core_tokens_retrieve(identifier)
        print("The response of CoreApi->core_tokens_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_tokens_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 

### Return type

[**Token**](Token.md)

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

# **core_tokens_set_key_create**
> core_tokens_set_key_create(identifier, token_set_key_request)



Set token key. Action is logged as event. `authentik_core.set_token_key` permission is required.

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.token_set_key_request import TokenSetKeyRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    identifier = 'identifier_example' # str | 
    token_set_key_request = authentik_openapi.TokenSetKeyRequest() # TokenSetKeyRequest | 

    try:
        api_instance.core_tokens_set_key_create(identifier, token_set_key_request)
    except Exception as e:
        print("Exception when calling CoreApi->core_tokens_set_key_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 
 **token_set_key_request** | [**TokenSetKeyRequest**](TokenSetKeyRequest.md)|  | 

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
**204** | Successfully changed key |  -  |
**400** | Missing key |  -  |
**404** | Token not found or expired |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_tokens_update**
> Token core_tokens_update(identifier, token_request)



Token Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.token import Token
from authentik_openapi.models.token_request import TokenRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    identifier = 'identifier_example' # str | 
    token_request = authentik_openapi.TokenRequest() # TokenRequest | 

    try:
        api_response = api_instance.core_tokens_update(identifier, token_request)
        print("The response of CoreApi->core_tokens_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_tokens_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 
 **token_request** | [**TokenRequest**](TokenRequest.md)|  | 

### Return type

[**Token**](Token.md)

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

# **core_tokens_used_by_list**
> List[UsedBy] core_tokens_used_by_list(identifier)



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
    api_instance = authentik_openapi.CoreApi(api_client)
    identifier = 'identifier_example' # str | 

    try:
        api_response = api_instance.core_tokens_used_by_list(identifier)
        print("The response of CoreApi->core_tokens_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_tokens_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 

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

# **core_tokens_view_key_retrieve**
> TokenView core_tokens_view_key_retrieve(identifier)



Return token key and log access

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.token_view import TokenView
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    identifier = 'identifier_example' # str | 

    try:
        api_response = api_instance.core_tokens_view_key_retrieve(identifier)
        print("The response of CoreApi->core_tokens_view_key_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_tokens_view_key_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | 

### Return type

[**TokenView**](TokenView.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Token not found or expired |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_transactional_applications_update**
> TransactionApplicationResponse core_transactional_applications_update(transaction_application_request)



Convert data into a blueprint, validate it and apply it

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.transaction_application_request import TransactionApplicationRequest
from authentik_openapi.models.transaction_application_response import TransactionApplicationResponse
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    transaction_application_request = authentik_openapi.TransactionApplicationRequest() # TransactionApplicationRequest | 

    try:
        api_response = api_instance.core_transactional_applications_update(transaction_application_request)
        print("The response of CoreApi->core_transactional_applications_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_transactional_applications_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_application_request** | [**TransactionApplicationRequest**](TransactionApplicationRequest.md)|  | 

### Return type

[**TransactionApplicationResponse**](TransactionApplicationResponse.md)

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

# **core_user_consent_destroy**
> core_user_consent_destroy(id)



UserConsent Viewset

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
    api_instance = authentik_openapi.CoreApi(api_client)
    id = 56 # int | A unique integer value identifying this User Consent.

    try:
        api_instance.core_user_consent_destroy(id)
    except Exception as e:
        print("Exception when calling CoreApi->core_user_consent_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User Consent. | 

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

# **core_user_consent_list**
> PaginatedUserConsentList core_user_consent_list(application=application, ordering=ordering, page=page, page_size=page_size, search=search, user=user)



UserConsent Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_user_consent_list import PaginatedUserConsentList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    application = 'application_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    user = 56 # int |  (optional)

    try:
        api_response = api_instance.core_user_consent_list(application=application, ordering=ordering, page=page, page_size=page_size, search=search, user=user)
        print("The response of CoreApi->core_user_consent_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_user_consent_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **user** | **int**|  | [optional] 

### Return type

[**PaginatedUserConsentList**](PaginatedUserConsentList.md)

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

# **core_user_consent_retrieve**
> UserConsent core_user_consent_retrieve(id)



UserConsent Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user_consent import UserConsent
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    id = 56 # int | A unique integer value identifying this User Consent.

    try:
        api_response = api_instance.core_user_consent_retrieve(id)
        print("The response of CoreApi->core_user_consent_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_user_consent_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User Consent. | 

### Return type

[**UserConsent**](UserConsent.md)

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

# **core_user_consent_used_by_list**
> List[UsedBy] core_user_consent_used_by_list(id)



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
    api_instance = authentik_openapi.CoreApi(api_client)
    id = 56 # int | A unique integer value identifying this User Consent.

    try:
        api_response = api_instance.core_user_consent_used_by_list(id)
        print("The response of CoreApi->core_user_consent_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_user_consent_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User Consent. | 

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

# **core_users_create**
> User core_users_create(user_request)



User Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user import User
from authentik_openapi.models.user_request import UserRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    user_request = authentik_openapi.UserRequest() # UserRequest | 

    try:
        api_response = api_instance.core_users_create(user_request)
        print("The response of CoreApi->core_users_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_users_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_request** | [**UserRequest**](UserRequest.md)|  | 

### Return type

[**User**](User.md)

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

# **core_users_destroy**
> core_users_destroy(id)



User Viewset

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
    api_instance = authentik_openapi.CoreApi(api_client)
    id = 56 # int | A unique integer value identifying this User.

    try:
        api_instance.core_users_destroy(id)
    except Exception as e:
        print("Exception when calling CoreApi->core_users_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. | 

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

# **core_users_impersonate_create**
> core_users_impersonate_create(id)



Impersonate a user

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
    api_instance = authentik_openapi.CoreApi(api_client)
    id = 56 # int | A unique integer value identifying this User.

    try:
        api_instance.core_users_impersonate_create(id)
    except Exception as e:
        print("Exception when calling CoreApi->core_users_impersonate_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. | 

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
**204** | Successfully started impersonation |  -  |
**401** | Access denied |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_users_impersonate_end_retrieve**
> core_users_impersonate_end_retrieve()



End Impersonation a user

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
    api_instance = authentik_openapi.CoreApi(api_client)

    try:
        api_instance.core_users_impersonate_end_retrieve()
    except Exception as e:
        print("Exception when calling CoreApi->core_users_impersonate_end_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**204** | Successfully started impersonation |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_users_list**
> PaginatedUserList core_users_list(attributes=attributes, email=email, groups_by_name=groups_by_name, groups_by_pk=groups_by_pk, include_groups=include_groups, is_active=is_active, is_superuser=is_superuser, name=name, ordering=ordering, page=page, page_size=page_size, path=path, path_startswith=path_startswith, search=search, type=type, username=username, uuid=uuid)



User Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_user_list import PaginatedUserList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    attributes = 'attributes_example' # str | Attributes (optional)
    email = 'email_example' # str |  (optional)
    groups_by_name = ['groups_by_name_example'] # List[str] |  (optional)
    groups_by_pk = ['groups_by_pk_example'] # List[str] |  (optional)
    include_groups = True # bool |  (optional) (default to True)
    is_active = True # bool |  (optional)
    is_superuser = True # bool |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    path = 'path_example' # str |  (optional)
    path_startswith = 'path_startswith_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)
    type = ['type_example'] # List[str] |  (optional)
    username = 'username_example' # str |  (optional)
    uuid = 'uuid_example' # str |  (optional)

    try:
        api_response = api_instance.core_users_list(attributes=attributes, email=email, groups_by_name=groups_by_name, groups_by_pk=groups_by_pk, include_groups=include_groups, is_active=is_active, is_superuser=is_superuser, name=name, ordering=ordering, page=page, page_size=page_size, path=path, path_startswith=path_startswith, search=search, type=type, username=username, uuid=uuid)
        print("The response of CoreApi->core_users_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_users_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attributes** | **str**| Attributes | [optional] 
 **email** | **str**|  | [optional] 
 **groups_by_name** | [**List[str]**](str.md)|  | [optional] 
 **groups_by_pk** | [**List[str]**](str.md)|  | [optional] 
 **include_groups** | **bool**|  | [optional] [default to True]
 **is_active** | **bool**|  | [optional] 
 **is_superuser** | **bool**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **path** | **str**|  | [optional] 
 **path_startswith** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **type** | [**List[str]**](str.md)|  | [optional] 
 **username** | **str**|  | [optional] 
 **uuid** | **str**|  | [optional] 

### Return type

[**PaginatedUserList**](PaginatedUserList.md)

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

# **core_users_me_retrieve**
> SessionUser core_users_me_retrieve()



Get information about current user

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.session_user import SessionUser
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)

    try:
        api_response = api_instance.core_users_me_retrieve()
        print("The response of CoreApi->core_users_me_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_users_me_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SessionUser**](SessionUser.md)

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

# **core_users_metrics_retrieve**
> UserMetrics core_users_metrics_retrieve(id)



User metrics per 1h

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user_metrics import UserMetrics
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    id = 56 # int | A unique integer value identifying this User.

    try:
        api_response = api_instance.core_users_metrics_retrieve(id)
        print("The response of CoreApi->core_users_metrics_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_users_metrics_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. | 

### Return type

[**UserMetrics**](UserMetrics.md)

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

# **core_users_partial_update**
> User core_users_partial_update(id, patched_user_request=patched_user_request)



User Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_user_request import PatchedUserRequest
from authentik_openapi.models.user import User
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    id = 56 # int | A unique integer value identifying this User.
    patched_user_request = authentik_openapi.PatchedUserRequest() # PatchedUserRequest |  (optional)

    try:
        api_response = api_instance.core_users_partial_update(id, patched_user_request=patched_user_request)
        print("The response of CoreApi->core_users_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_users_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. | 
 **patched_user_request** | [**PatchedUserRequest**](PatchedUserRequest.md)|  | [optional] 

### Return type

[**User**](User.md)

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

# **core_users_paths_retrieve**
> UserPath core_users_paths_retrieve(search=search)



Get all user paths

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user_path import UserPath
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    search = 'search_example' # str |  (optional)

    try:
        api_response = api_instance.core_users_paths_retrieve(search=search)
        print("The response of CoreApi->core_users_paths_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_users_paths_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**|  | [optional] 

### Return type

[**UserPath**](UserPath.md)

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

# **core_users_recovery_create**
> Link core_users_recovery_create(id)



Create a temporary link that a user can use to recover their accounts

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.link import Link
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    id = 56 # int | A unique integer value identifying this User.

    try:
        api_response = api_instance.core_users_recovery_create(id)
        print("The response of CoreApi->core_users_recovery_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_users_recovery_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. | 

### Return type

[**Link**](Link.md)

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

# **core_users_recovery_email_create**
> core_users_recovery_email_create(email_stage, id)



Create a temporary link that a user can use to recover their accounts

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
    api_instance = authentik_openapi.CoreApi(api_client)
    email_stage = 'email_stage_example' # str | 
    id = 56 # int | A unique integer value identifying this User.

    try:
        api_instance.core_users_recovery_email_create(email_stage, id)
    except Exception as e:
        print("Exception when calling CoreApi->core_users_recovery_email_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_stage** | **str**|  | 
 **id** | **int**| A unique integer value identifying this User. | 

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
**204** | Successfully sent recover email |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_users_retrieve**
> User core_users_retrieve(id)



User Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user import User
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    id = 56 # int | A unique integer value identifying this User.

    try:
        api_response = api_instance.core_users_retrieve(id)
        print("The response of CoreApi->core_users_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_users_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. | 

### Return type

[**User**](User.md)

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

# **core_users_service_account_create**
> UserServiceAccountResponse core_users_service_account_create(user_service_account_request)



Create a new user account that is marked as a service account

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user_service_account_request import UserServiceAccountRequest
from authentik_openapi.models.user_service_account_response import UserServiceAccountResponse
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    user_service_account_request = authentik_openapi.UserServiceAccountRequest() # UserServiceAccountRequest | 

    try:
        api_response = api_instance.core_users_service_account_create(user_service_account_request)
        print("The response of CoreApi->core_users_service_account_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_users_service_account_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_service_account_request** | [**UserServiceAccountRequest**](UserServiceAccountRequest.md)|  | 

### Return type

[**UserServiceAccountResponse**](UserServiceAccountResponse.md)

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

# **core_users_set_password_create**
> core_users_set_password_create(id, user_password_set_request)



Set password for user

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user_password_set_request import UserPasswordSetRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    id = 56 # int | A unique integer value identifying this User.
    user_password_set_request = authentik_openapi.UserPasswordSetRequest() # UserPasswordSetRequest | 

    try:
        api_instance.core_users_set_password_create(id, user_password_set_request)
    except Exception as e:
        print("Exception when calling CoreApi->core_users_set_password_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. | 
 **user_password_set_request** | [**UserPasswordSetRequest**](UserPasswordSetRequest.md)|  | 

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
**204** | Successfully changed password |  -  |
**400** | Bad request |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **core_users_update**
> User core_users_update(id, user_request)



User Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.user import User
from authentik_openapi.models.user_request import UserRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CoreApi(api_client)
    id = 56 # int | A unique integer value identifying this User.
    user_request = authentik_openapi.UserRequest() # UserRequest | 

    try:
        api_response = api_instance.core_users_update(id, user_request)
        print("The response of CoreApi->core_users_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_users_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. | 
 **user_request** | [**UserRequest**](UserRequest.md)|  | 

### Return type

[**User**](User.md)

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

# **core_users_used_by_list**
> List[UsedBy] core_users_used_by_list(id)



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
    api_instance = authentik_openapi.CoreApi(api_client)
    id = 56 # int | A unique integer value identifying this User.

    try:
        api_response = api_instance.core_users_used_by_list(id)
        print("The response of CoreApi->core_users_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoreApi->core_users_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User. | 

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

