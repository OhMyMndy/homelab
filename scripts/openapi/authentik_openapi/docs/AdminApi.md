# authentik_openapi.AdminApi

All URIs are relative to *https://auth.home.ohmymndy.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_apps_list**](AdminApi.md#admin_apps_list) | **GET** /admin/apps/ | 
[**admin_metrics_retrieve**](AdminApi.md#admin_metrics_retrieve) | **GET** /admin/metrics/ | 
[**admin_models_list**](AdminApi.md#admin_models_list) | **GET** /admin/models/ | 
[**admin_settings_partial_update**](AdminApi.md#admin_settings_partial_update) | **PATCH** /admin/settings/ | 
[**admin_settings_retrieve**](AdminApi.md#admin_settings_retrieve) | **GET** /admin/settings/ | 
[**admin_settings_update**](AdminApi.md#admin_settings_update) | **PUT** /admin/settings/ | 
[**admin_system_create**](AdminApi.md#admin_system_create) | **POST** /admin/system/ | 
[**admin_system_retrieve**](AdminApi.md#admin_system_retrieve) | **GET** /admin/system/ | 
[**admin_version_retrieve**](AdminApi.md#admin_version_retrieve) | **GET** /admin/version/ | 
[**admin_workers_retrieve**](AdminApi.md#admin_workers_retrieve) | **GET** /admin/workers/ | 


# **admin_apps_list**
> List[App] admin_apps_list()



Read-only view list all installed apps

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.app import App
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AdminApi(api_client)

    try:
        api_response = api_instance.admin_apps_list()
        print("The response of AdminApi->admin_apps_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_apps_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[App]**](App.md)

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

# **admin_metrics_retrieve**
> LoginMetrics admin_metrics_retrieve()



Login Metrics per 1h

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.login_metrics import LoginMetrics
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AdminApi(api_client)

    try:
        api_response = api_instance.admin_metrics_retrieve()
        print("The response of AdminApi->admin_metrics_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_metrics_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LoginMetrics**](LoginMetrics.md)

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

# **admin_models_list**
> List[App] admin_models_list()



Read-only view list all installed models

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.app import App
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AdminApi(api_client)

    try:
        api_response = api_instance.admin_models_list()
        print("The response of AdminApi->admin_models_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_models_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[App]**](App.md)

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

# **admin_settings_partial_update**
> Settings admin_settings_partial_update(patched_settings_request=patched_settings_request)



Settings view

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_settings_request import PatchedSettingsRequest
from authentik_openapi.models.settings import Settings
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AdminApi(api_client)
    patched_settings_request = authentik_openapi.PatchedSettingsRequest() # PatchedSettingsRequest |  (optional)

    try:
        api_response = api_instance.admin_settings_partial_update(patched_settings_request=patched_settings_request)
        print("The response of AdminApi->admin_settings_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_settings_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patched_settings_request** | [**PatchedSettingsRequest**](PatchedSettingsRequest.md)|  | [optional] 

### Return type

[**Settings**](Settings.md)

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

# **admin_settings_retrieve**
> Settings admin_settings_retrieve()



Settings view

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.settings import Settings
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AdminApi(api_client)

    try:
        api_response = api_instance.admin_settings_retrieve()
        print("The response of AdminApi->admin_settings_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_settings_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Settings**](Settings.md)

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

# **admin_settings_update**
> Settings admin_settings_update(settings_request=settings_request)



Settings view

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.settings import Settings
from authentik_openapi.models.settings_request import SettingsRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AdminApi(api_client)
    settings_request = authentik_openapi.SettingsRequest() # SettingsRequest |  (optional)

    try:
        api_response = api_instance.admin_settings_update(settings_request=settings_request)
        print("The response of AdminApi->admin_settings_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_settings_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_request** | [**SettingsRequest**](SettingsRequest.md)|  | [optional] 

### Return type

[**Settings**](Settings.md)

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

# **admin_system_create**
> SystemInfo admin_system_create()



Get system information.

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.system_info import SystemInfo
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AdminApi(api_client)

    try:
        api_response = api_instance.admin_system_create()
        print("The response of AdminApi->admin_system_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_system_create: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SystemInfo**](SystemInfo.md)

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

# **admin_system_retrieve**
> SystemInfo admin_system_retrieve()



Get system information.

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.system_info import SystemInfo
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AdminApi(api_client)

    try:
        api_response = api_instance.admin_system_retrieve()
        print("The response of AdminApi->admin_system_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_system_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SystemInfo**](SystemInfo.md)

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

# **admin_version_retrieve**
> Version admin_version_retrieve()



Get running and latest version.

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.version import Version
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AdminApi(api_client)

    try:
        api_response = api_instance.admin_version_retrieve()
        print("The response of AdminApi->admin_version_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_version_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Version**](Version.md)

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

# **admin_workers_retrieve**
> Workers admin_workers_retrieve()



Get currently connected worker count.

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.workers import Workers
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AdminApi(api_client)

    try:
        api_response = api_instance.admin_workers_retrieve()
        print("The response of AdminApi->admin_workers_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_workers_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Workers**](Workers.md)

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

