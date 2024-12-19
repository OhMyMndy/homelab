# authentik_openapi.AuthenticatorsApi

All URIs are relative to *https://auth.home.ohmymndy.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticators_admin_all_list**](AuthenticatorsApi.md#authenticators_admin_all_list) | **GET** /authenticators/admin/all/ | 
[**authenticators_admin_duo_create**](AuthenticatorsApi.md#authenticators_admin_duo_create) | **POST** /authenticators/admin/duo/ | 
[**authenticators_admin_duo_destroy**](AuthenticatorsApi.md#authenticators_admin_duo_destroy) | **DELETE** /authenticators/admin/duo/{id}/ | 
[**authenticators_admin_duo_list**](AuthenticatorsApi.md#authenticators_admin_duo_list) | **GET** /authenticators/admin/duo/ | 
[**authenticators_admin_duo_partial_update**](AuthenticatorsApi.md#authenticators_admin_duo_partial_update) | **PATCH** /authenticators/admin/duo/{id}/ | 
[**authenticators_admin_duo_retrieve**](AuthenticatorsApi.md#authenticators_admin_duo_retrieve) | **GET** /authenticators/admin/duo/{id}/ | 
[**authenticators_admin_duo_update**](AuthenticatorsApi.md#authenticators_admin_duo_update) | **PUT** /authenticators/admin/duo/{id}/ | 
[**authenticators_admin_sms_create**](AuthenticatorsApi.md#authenticators_admin_sms_create) | **POST** /authenticators/admin/sms/ | 
[**authenticators_admin_sms_destroy**](AuthenticatorsApi.md#authenticators_admin_sms_destroy) | **DELETE** /authenticators/admin/sms/{id}/ | 
[**authenticators_admin_sms_list**](AuthenticatorsApi.md#authenticators_admin_sms_list) | **GET** /authenticators/admin/sms/ | 
[**authenticators_admin_sms_partial_update**](AuthenticatorsApi.md#authenticators_admin_sms_partial_update) | **PATCH** /authenticators/admin/sms/{id}/ | 
[**authenticators_admin_sms_retrieve**](AuthenticatorsApi.md#authenticators_admin_sms_retrieve) | **GET** /authenticators/admin/sms/{id}/ | 
[**authenticators_admin_sms_update**](AuthenticatorsApi.md#authenticators_admin_sms_update) | **PUT** /authenticators/admin/sms/{id}/ | 
[**authenticators_admin_static_create**](AuthenticatorsApi.md#authenticators_admin_static_create) | **POST** /authenticators/admin/static/ | 
[**authenticators_admin_static_destroy**](AuthenticatorsApi.md#authenticators_admin_static_destroy) | **DELETE** /authenticators/admin/static/{id}/ | 
[**authenticators_admin_static_list**](AuthenticatorsApi.md#authenticators_admin_static_list) | **GET** /authenticators/admin/static/ | 
[**authenticators_admin_static_partial_update**](AuthenticatorsApi.md#authenticators_admin_static_partial_update) | **PATCH** /authenticators/admin/static/{id}/ | 
[**authenticators_admin_static_retrieve**](AuthenticatorsApi.md#authenticators_admin_static_retrieve) | **GET** /authenticators/admin/static/{id}/ | 
[**authenticators_admin_static_update**](AuthenticatorsApi.md#authenticators_admin_static_update) | **PUT** /authenticators/admin/static/{id}/ | 
[**authenticators_admin_totp_create**](AuthenticatorsApi.md#authenticators_admin_totp_create) | **POST** /authenticators/admin/totp/ | 
[**authenticators_admin_totp_destroy**](AuthenticatorsApi.md#authenticators_admin_totp_destroy) | **DELETE** /authenticators/admin/totp/{id}/ | 
[**authenticators_admin_totp_list**](AuthenticatorsApi.md#authenticators_admin_totp_list) | **GET** /authenticators/admin/totp/ | 
[**authenticators_admin_totp_partial_update**](AuthenticatorsApi.md#authenticators_admin_totp_partial_update) | **PATCH** /authenticators/admin/totp/{id}/ | 
[**authenticators_admin_totp_retrieve**](AuthenticatorsApi.md#authenticators_admin_totp_retrieve) | **GET** /authenticators/admin/totp/{id}/ | 
[**authenticators_admin_totp_update**](AuthenticatorsApi.md#authenticators_admin_totp_update) | **PUT** /authenticators/admin/totp/{id}/ | 
[**authenticators_admin_webauthn_create**](AuthenticatorsApi.md#authenticators_admin_webauthn_create) | **POST** /authenticators/admin/webauthn/ | 
[**authenticators_admin_webauthn_destroy**](AuthenticatorsApi.md#authenticators_admin_webauthn_destroy) | **DELETE** /authenticators/admin/webauthn/{id}/ | 
[**authenticators_admin_webauthn_list**](AuthenticatorsApi.md#authenticators_admin_webauthn_list) | **GET** /authenticators/admin/webauthn/ | 
[**authenticators_admin_webauthn_partial_update**](AuthenticatorsApi.md#authenticators_admin_webauthn_partial_update) | **PATCH** /authenticators/admin/webauthn/{id}/ | 
[**authenticators_admin_webauthn_retrieve**](AuthenticatorsApi.md#authenticators_admin_webauthn_retrieve) | **GET** /authenticators/admin/webauthn/{id}/ | 
[**authenticators_admin_webauthn_update**](AuthenticatorsApi.md#authenticators_admin_webauthn_update) | **PUT** /authenticators/admin/webauthn/{id}/ | 
[**authenticators_all_list**](AuthenticatorsApi.md#authenticators_all_list) | **GET** /authenticators/all/ | 
[**authenticators_duo_destroy**](AuthenticatorsApi.md#authenticators_duo_destroy) | **DELETE** /authenticators/duo/{id}/ | 
[**authenticators_duo_list**](AuthenticatorsApi.md#authenticators_duo_list) | **GET** /authenticators/duo/ | 
[**authenticators_duo_partial_update**](AuthenticatorsApi.md#authenticators_duo_partial_update) | **PATCH** /authenticators/duo/{id}/ | 
[**authenticators_duo_retrieve**](AuthenticatorsApi.md#authenticators_duo_retrieve) | **GET** /authenticators/duo/{id}/ | 
[**authenticators_duo_update**](AuthenticatorsApi.md#authenticators_duo_update) | **PUT** /authenticators/duo/{id}/ | 
[**authenticators_duo_used_by_list**](AuthenticatorsApi.md#authenticators_duo_used_by_list) | **GET** /authenticators/duo/{id}/used_by/ | 
[**authenticators_sms_destroy**](AuthenticatorsApi.md#authenticators_sms_destroy) | **DELETE** /authenticators/sms/{id}/ | 
[**authenticators_sms_list**](AuthenticatorsApi.md#authenticators_sms_list) | **GET** /authenticators/sms/ | 
[**authenticators_sms_partial_update**](AuthenticatorsApi.md#authenticators_sms_partial_update) | **PATCH** /authenticators/sms/{id}/ | 
[**authenticators_sms_retrieve**](AuthenticatorsApi.md#authenticators_sms_retrieve) | **GET** /authenticators/sms/{id}/ | 
[**authenticators_sms_update**](AuthenticatorsApi.md#authenticators_sms_update) | **PUT** /authenticators/sms/{id}/ | 
[**authenticators_sms_used_by_list**](AuthenticatorsApi.md#authenticators_sms_used_by_list) | **GET** /authenticators/sms/{id}/used_by/ | 
[**authenticators_static_destroy**](AuthenticatorsApi.md#authenticators_static_destroy) | **DELETE** /authenticators/static/{id}/ | 
[**authenticators_static_list**](AuthenticatorsApi.md#authenticators_static_list) | **GET** /authenticators/static/ | 
[**authenticators_static_partial_update**](AuthenticatorsApi.md#authenticators_static_partial_update) | **PATCH** /authenticators/static/{id}/ | 
[**authenticators_static_retrieve**](AuthenticatorsApi.md#authenticators_static_retrieve) | **GET** /authenticators/static/{id}/ | 
[**authenticators_static_update**](AuthenticatorsApi.md#authenticators_static_update) | **PUT** /authenticators/static/{id}/ | 
[**authenticators_static_used_by_list**](AuthenticatorsApi.md#authenticators_static_used_by_list) | **GET** /authenticators/static/{id}/used_by/ | 
[**authenticators_totp_destroy**](AuthenticatorsApi.md#authenticators_totp_destroy) | **DELETE** /authenticators/totp/{id}/ | 
[**authenticators_totp_list**](AuthenticatorsApi.md#authenticators_totp_list) | **GET** /authenticators/totp/ | 
[**authenticators_totp_partial_update**](AuthenticatorsApi.md#authenticators_totp_partial_update) | **PATCH** /authenticators/totp/{id}/ | 
[**authenticators_totp_retrieve**](AuthenticatorsApi.md#authenticators_totp_retrieve) | **GET** /authenticators/totp/{id}/ | 
[**authenticators_totp_update**](AuthenticatorsApi.md#authenticators_totp_update) | **PUT** /authenticators/totp/{id}/ | 
[**authenticators_totp_used_by_list**](AuthenticatorsApi.md#authenticators_totp_used_by_list) | **GET** /authenticators/totp/{id}/used_by/ | 
[**authenticators_webauthn_destroy**](AuthenticatorsApi.md#authenticators_webauthn_destroy) | **DELETE** /authenticators/webauthn/{id}/ | 
[**authenticators_webauthn_list**](AuthenticatorsApi.md#authenticators_webauthn_list) | **GET** /authenticators/webauthn/ | 
[**authenticators_webauthn_partial_update**](AuthenticatorsApi.md#authenticators_webauthn_partial_update) | **PATCH** /authenticators/webauthn/{id}/ | 
[**authenticators_webauthn_retrieve**](AuthenticatorsApi.md#authenticators_webauthn_retrieve) | **GET** /authenticators/webauthn/{id}/ | 
[**authenticators_webauthn_update**](AuthenticatorsApi.md#authenticators_webauthn_update) | **PUT** /authenticators/webauthn/{id}/ | 
[**authenticators_webauthn_used_by_list**](AuthenticatorsApi.md#authenticators_webauthn_used_by_list) | **GET** /authenticators/webauthn/{id}/used_by/ | 


# **authenticators_admin_all_list**
> List[Device] authenticators_admin_all_list(user=user)



Get all devices for current user

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.device import Device
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    user = 56 # int |  (optional)

    try:
        api_response = api_instance.authenticators_admin_all_list(user=user)
        print("The response of AuthenticatorsApi->authenticators_admin_all_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_admin_all_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **int**|  | [optional] 

### Return type

[**List[Device]**](Device.md)

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

# **authenticators_admin_duo_create**
> DuoDevice authenticators_admin_duo_create(duo_device_request)



Viewset for Duo authenticator devices (for admins)

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.duo_device import DuoDevice
from authentik_openapi.models.duo_device_request import DuoDeviceRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    duo_device_request = authentik_openapi.DuoDeviceRequest() # DuoDeviceRequest | 

    try:
        api_response = api_instance.authenticators_admin_duo_create(duo_device_request)
        print("The response of AuthenticatorsApi->authenticators_admin_duo_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_admin_duo_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **duo_device_request** | [**DuoDeviceRequest**](DuoDeviceRequest.md)|  | 

### Return type

[**DuoDevice**](DuoDevice.md)

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

# **authenticators_admin_duo_destroy**
> authenticators_admin_duo_destroy(id)



Viewset for Duo authenticator devices (for admins)

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
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this Duo Device.

    try:
        api_instance.authenticators_admin_duo_destroy(id)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_admin_duo_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Duo Device. | 

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

# **authenticators_admin_duo_list**
> PaginatedDuoDeviceList authenticators_admin_duo_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)



Viewset for Duo authenticator devices (for admins)

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_duo_device_list import PaginatedDuoDeviceList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.authenticators_admin_duo_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of AuthenticatorsApi->authenticators_admin_duo_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_admin_duo_list: %s\n" % e)
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

[**PaginatedDuoDeviceList**](PaginatedDuoDeviceList.md)

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

# **authenticators_admin_duo_partial_update**
> DuoDevice authenticators_admin_duo_partial_update(id, patched_duo_device_request=patched_duo_device_request)



Viewset for Duo authenticator devices (for admins)

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.duo_device import DuoDevice
from authentik_openapi.models.patched_duo_device_request import PatchedDuoDeviceRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this Duo Device.
    patched_duo_device_request = authentik_openapi.PatchedDuoDeviceRequest() # PatchedDuoDeviceRequest |  (optional)

    try:
        api_response = api_instance.authenticators_admin_duo_partial_update(id, patched_duo_device_request=patched_duo_device_request)
        print("The response of AuthenticatorsApi->authenticators_admin_duo_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_admin_duo_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Duo Device. | 
 **patched_duo_device_request** | [**PatchedDuoDeviceRequest**](PatchedDuoDeviceRequest.md)|  | [optional] 

### Return type

[**DuoDevice**](DuoDevice.md)

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

# **authenticators_admin_duo_retrieve**
> DuoDevice authenticators_admin_duo_retrieve(id)



Viewset for Duo authenticator devices (for admins)

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.duo_device import DuoDevice
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this Duo Device.

    try:
        api_response = api_instance.authenticators_admin_duo_retrieve(id)
        print("The response of AuthenticatorsApi->authenticators_admin_duo_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_admin_duo_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Duo Device. | 

### Return type

[**DuoDevice**](DuoDevice.md)

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

# **authenticators_admin_duo_update**
> DuoDevice authenticators_admin_duo_update(id, duo_device_request)



Viewset for Duo authenticator devices (for admins)

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.duo_device import DuoDevice
from authentik_openapi.models.duo_device_request import DuoDeviceRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this Duo Device.
    duo_device_request = authentik_openapi.DuoDeviceRequest() # DuoDeviceRequest | 

    try:
        api_response = api_instance.authenticators_admin_duo_update(id, duo_device_request)
        print("The response of AuthenticatorsApi->authenticators_admin_duo_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_admin_duo_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Duo Device. | 
 **duo_device_request** | [**DuoDeviceRequest**](DuoDeviceRequest.md)|  | 

### Return type

[**DuoDevice**](DuoDevice.md)

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

# **authenticators_admin_sms_create**
> SMSDevice authenticators_admin_sms_create(sms_device_request)



Viewset for sms authenticator devices (for admins)

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.sms_device import SMSDevice
from authentik_openapi.models.sms_device_request import SMSDeviceRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    sms_device_request = authentik_openapi.SMSDeviceRequest() # SMSDeviceRequest | 

    try:
        api_response = api_instance.authenticators_admin_sms_create(sms_device_request)
        print("The response of AuthenticatorsApi->authenticators_admin_sms_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_admin_sms_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sms_device_request** | [**SMSDeviceRequest**](SMSDeviceRequest.md)|  | 

### Return type

[**SMSDevice**](SMSDevice.md)

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

# **authenticators_admin_sms_destroy**
> authenticators_admin_sms_destroy(id)



Viewset for sms authenticator devices (for admins)

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
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this SMS Device.

    try:
        api_instance.authenticators_admin_sms_destroy(id)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_admin_sms_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SMS Device. | 

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

# **authenticators_admin_sms_list**
> PaginatedSMSDeviceList authenticators_admin_sms_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)



Viewset for sms authenticator devices (for admins)

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_sms_device_list import PaginatedSMSDeviceList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.authenticators_admin_sms_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of AuthenticatorsApi->authenticators_admin_sms_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_admin_sms_list: %s\n" % e)
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

[**PaginatedSMSDeviceList**](PaginatedSMSDeviceList.md)

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

# **authenticators_admin_sms_partial_update**
> SMSDevice authenticators_admin_sms_partial_update(id, patched_sms_device_request=patched_sms_device_request)



Viewset for sms authenticator devices (for admins)

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_sms_device_request import PatchedSMSDeviceRequest
from authentik_openapi.models.sms_device import SMSDevice
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this SMS Device.
    patched_sms_device_request = authentik_openapi.PatchedSMSDeviceRequest() # PatchedSMSDeviceRequest |  (optional)

    try:
        api_response = api_instance.authenticators_admin_sms_partial_update(id, patched_sms_device_request=patched_sms_device_request)
        print("The response of AuthenticatorsApi->authenticators_admin_sms_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_admin_sms_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SMS Device. | 
 **patched_sms_device_request** | [**PatchedSMSDeviceRequest**](PatchedSMSDeviceRequest.md)|  | [optional] 

### Return type

[**SMSDevice**](SMSDevice.md)

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

# **authenticators_admin_sms_retrieve**
> SMSDevice authenticators_admin_sms_retrieve(id)



Viewset for sms authenticator devices (for admins)

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.sms_device import SMSDevice
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this SMS Device.

    try:
        api_response = api_instance.authenticators_admin_sms_retrieve(id)
        print("The response of AuthenticatorsApi->authenticators_admin_sms_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_admin_sms_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SMS Device. | 

### Return type

[**SMSDevice**](SMSDevice.md)

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

# **authenticators_admin_sms_update**
> SMSDevice authenticators_admin_sms_update(id, sms_device_request)



Viewset for sms authenticator devices (for admins)

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.sms_device import SMSDevice
from authentik_openapi.models.sms_device_request import SMSDeviceRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this SMS Device.
    sms_device_request = authentik_openapi.SMSDeviceRequest() # SMSDeviceRequest | 

    try:
        api_response = api_instance.authenticators_admin_sms_update(id, sms_device_request)
        print("The response of AuthenticatorsApi->authenticators_admin_sms_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_admin_sms_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SMS Device. | 
 **sms_device_request** | [**SMSDeviceRequest**](SMSDeviceRequest.md)|  | 

### Return type

[**SMSDevice**](SMSDevice.md)

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

# **authenticators_admin_static_create**
> StaticDevice authenticators_admin_static_create(static_device_request)



Viewset for static authenticator devices (for admins)

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.static_device import StaticDevice
from authentik_openapi.models.static_device_request import StaticDeviceRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    static_device_request = authentik_openapi.StaticDeviceRequest() # StaticDeviceRequest | 

    try:
        api_response = api_instance.authenticators_admin_static_create(static_device_request)
        print("The response of AuthenticatorsApi->authenticators_admin_static_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_admin_static_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **static_device_request** | [**StaticDeviceRequest**](StaticDeviceRequest.md)|  | 

### Return type

[**StaticDevice**](StaticDevice.md)

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

# **authenticators_admin_static_destroy**
> authenticators_admin_static_destroy(id)



Viewset for static authenticator devices (for admins)

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
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this Static Device.

    try:
        api_instance.authenticators_admin_static_destroy(id)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_admin_static_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Static Device. | 

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

# **authenticators_admin_static_list**
> PaginatedStaticDeviceList authenticators_admin_static_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)



Viewset for static authenticator devices (for admins)

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_static_device_list import PaginatedStaticDeviceList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.authenticators_admin_static_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of AuthenticatorsApi->authenticators_admin_static_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_admin_static_list: %s\n" % e)
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

[**PaginatedStaticDeviceList**](PaginatedStaticDeviceList.md)

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

# **authenticators_admin_static_partial_update**
> StaticDevice authenticators_admin_static_partial_update(id, patched_static_device_request=patched_static_device_request)



Viewset for static authenticator devices (for admins)

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_static_device_request import PatchedStaticDeviceRequest
from authentik_openapi.models.static_device import StaticDevice
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this Static Device.
    patched_static_device_request = authentik_openapi.PatchedStaticDeviceRequest() # PatchedStaticDeviceRequest |  (optional)

    try:
        api_response = api_instance.authenticators_admin_static_partial_update(id, patched_static_device_request=patched_static_device_request)
        print("The response of AuthenticatorsApi->authenticators_admin_static_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_admin_static_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Static Device. | 
 **patched_static_device_request** | [**PatchedStaticDeviceRequest**](PatchedStaticDeviceRequest.md)|  | [optional] 

### Return type

[**StaticDevice**](StaticDevice.md)

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

# **authenticators_admin_static_retrieve**
> StaticDevice authenticators_admin_static_retrieve(id)



Viewset for static authenticator devices (for admins)

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.static_device import StaticDevice
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this Static Device.

    try:
        api_response = api_instance.authenticators_admin_static_retrieve(id)
        print("The response of AuthenticatorsApi->authenticators_admin_static_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_admin_static_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Static Device. | 

### Return type

[**StaticDevice**](StaticDevice.md)

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

# **authenticators_admin_static_update**
> StaticDevice authenticators_admin_static_update(id, static_device_request)



Viewset for static authenticator devices (for admins)

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.static_device import StaticDevice
from authentik_openapi.models.static_device_request import StaticDeviceRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this Static Device.
    static_device_request = authentik_openapi.StaticDeviceRequest() # StaticDeviceRequest | 

    try:
        api_response = api_instance.authenticators_admin_static_update(id, static_device_request)
        print("The response of AuthenticatorsApi->authenticators_admin_static_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_admin_static_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Static Device. | 
 **static_device_request** | [**StaticDeviceRequest**](StaticDeviceRequest.md)|  | 

### Return type

[**StaticDevice**](StaticDevice.md)

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

# **authenticators_admin_totp_create**
> TOTPDevice authenticators_admin_totp_create(totp_device_request)



Viewset for totp authenticator devices (for admins)

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.totp_device import TOTPDevice
from authentik_openapi.models.totp_device_request import TOTPDeviceRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    totp_device_request = authentik_openapi.TOTPDeviceRequest() # TOTPDeviceRequest | 

    try:
        api_response = api_instance.authenticators_admin_totp_create(totp_device_request)
        print("The response of AuthenticatorsApi->authenticators_admin_totp_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_admin_totp_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **totp_device_request** | [**TOTPDeviceRequest**](TOTPDeviceRequest.md)|  | 

### Return type

[**TOTPDevice**](TOTPDevice.md)

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

# **authenticators_admin_totp_destroy**
> authenticators_admin_totp_destroy(id)



Viewset for totp authenticator devices (for admins)

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
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this TOTP Device.

    try:
        api_instance.authenticators_admin_totp_destroy(id)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_admin_totp_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this TOTP Device. | 

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

# **authenticators_admin_totp_list**
> PaginatedTOTPDeviceList authenticators_admin_totp_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)



Viewset for totp authenticator devices (for admins)

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_totp_device_list import PaginatedTOTPDeviceList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.authenticators_admin_totp_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of AuthenticatorsApi->authenticators_admin_totp_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_admin_totp_list: %s\n" % e)
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

[**PaginatedTOTPDeviceList**](PaginatedTOTPDeviceList.md)

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

# **authenticators_admin_totp_partial_update**
> TOTPDevice authenticators_admin_totp_partial_update(id, patched_totp_device_request=patched_totp_device_request)



Viewset for totp authenticator devices (for admins)

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_totp_device_request import PatchedTOTPDeviceRequest
from authentik_openapi.models.totp_device import TOTPDevice
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this TOTP Device.
    patched_totp_device_request = authentik_openapi.PatchedTOTPDeviceRequest() # PatchedTOTPDeviceRequest |  (optional)

    try:
        api_response = api_instance.authenticators_admin_totp_partial_update(id, patched_totp_device_request=patched_totp_device_request)
        print("The response of AuthenticatorsApi->authenticators_admin_totp_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_admin_totp_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this TOTP Device. | 
 **patched_totp_device_request** | [**PatchedTOTPDeviceRequest**](PatchedTOTPDeviceRequest.md)|  | [optional] 

### Return type

[**TOTPDevice**](TOTPDevice.md)

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

# **authenticators_admin_totp_retrieve**
> TOTPDevice authenticators_admin_totp_retrieve(id)



Viewset for totp authenticator devices (for admins)

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.totp_device import TOTPDevice
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this TOTP Device.

    try:
        api_response = api_instance.authenticators_admin_totp_retrieve(id)
        print("The response of AuthenticatorsApi->authenticators_admin_totp_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_admin_totp_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this TOTP Device. | 

### Return type

[**TOTPDevice**](TOTPDevice.md)

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

# **authenticators_admin_totp_update**
> TOTPDevice authenticators_admin_totp_update(id, totp_device_request)



Viewset for totp authenticator devices (for admins)

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.totp_device import TOTPDevice
from authentik_openapi.models.totp_device_request import TOTPDeviceRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this TOTP Device.
    totp_device_request = authentik_openapi.TOTPDeviceRequest() # TOTPDeviceRequest | 

    try:
        api_response = api_instance.authenticators_admin_totp_update(id, totp_device_request)
        print("The response of AuthenticatorsApi->authenticators_admin_totp_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_admin_totp_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this TOTP Device. | 
 **totp_device_request** | [**TOTPDeviceRequest**](TOTPDeviceRequest.md)|  | 

### Return type

[**TOTPDevice**](TOTPDevice.md)

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

# **authenticators_admin_webauthn_create**
> WebAuthnDevice authenticators_admin_webauthn_create(web_authn_device_request)



Viewset for WebAuthn authenticator devices (for admins)

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.web_authn_device import WebAuthnDevice
from authentik_openapi.models.web_authn_device_request import WebAuthnDeviceRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    web_authn_device_request = authentik_openapi.WebAuthnDeviceRequest() # WebAuthnDeviceRequest | 

    try:
        api_response = api_instance.authenticators_admin_webauthn_create(web_authn_device_request)
        print("The response of AuthenticatorsApi->authenticators_admin_webauthn_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_admin_webauthn_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_authn_device_request** | [**WebAuthnDeviceRequest**](WebAuthnDeviceRequest.md)|  | 

### Return type

[**WebAuthnDevice**](WebAuthnDevice.md)

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

# **authenticators_admin_webauthn_destroy**
> authenticators_admin_webauthn_destroy(id)



Viewset for WebAuthn authenticator devices (for admins)

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
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this WebAuthn Device.

    try:
        api_instance.authenticators_admin_webauthn_destroy(id)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_admin_webauthn_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this WebAuthn Device. | 

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

# **authenticators_admin_webauthn_list**
> PaginatedWebAuthnDeviceList authenticators_admin_webauthn_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)



Viewset for WebAuthn authenticator devices (for admins)

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_web_authn_device_list import PaginatedWebAuthnDeviceList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.authenticators_admin_webauthn_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of AuthenticatorsApi->authenticators_admin_webauthn_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_admin_webauthn_list: %s\n" % e)
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

[**PaginatedWebAuthnDeviceList**](PaginatedWebAuthnDeviceList.md)

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

# **authenticators_admin_webauthn_partial_update**
> WebAuthnDevice authenticators_admin_webauthn_partial_update(id, patched_web_authn_device_request=patched_web_authn_device_request)



Viewset for WebAuthn authenticator devices (for admins)

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_web_authn_device_request import PatchedWebAuthnDeviceRequest
from authentik_openapi.models.web_authn_device import WebAuthnDevice
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this WebAuthn Device.
    patched_web_authn_device_request = authentik_openapi.PatchedWebAuthnDeviceRequest() # PatchedWebAuthnDeviceRequest |  (optional)

    try:
        api_response = api_instance.authenticators_admin_webauthn_partial_update(id, patched_web_authn_device_request=patched_web_authn_device_request)
        print("The response of AuthenticatorsApi->authenticators_admin_webauthn_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_admin_webauthn_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this WebAuthn Device. | 
 **patched_web_authn_device_request** | [**PatchedWebAuthnDeviceRequest**](PatchedWebAuthnDeviceRequest.md)|  | [optional] 

### Return type

[**WebAuthnDevice**](WebAuthnDevice.md)

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

# **authenticators_admin_webauthn_retrieve**
> WebAuthnDevice authenticators_admin_webauthn_retrieve(id)



Viewset for WebAuthn authenticator devices (for admins)

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.web_authn_device import WebAuthnDevice
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this WebAuthn Device.

    try:
        api_response = api_instance.authenticators_admin_webauthn_retrieve(id)
        print("The response of AuthenticatorsApi->authenticators_admin_webauthn_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_admin_webauthn_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this WebAuthn Device. | 

### Return type

[**WebAuthnDevice**](WebAuthnDevice.md)

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

# **authenticators_admin_webauthn_update**
> WebAuthnDevice authenticators_admin_webauthn_update(id, web_authn_device_request)



Viewset for WebAuthn authenticator devices (for admins)

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.web_authn_device import WebAuthnDevice
from authentik_openapi.models.web_authn_device_request import WebAuthnDeviceRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this WebAuthn Device.
    web_authn_device_request = authentik_openapi.WebAuthnDeviceRequest() # WebAuthnDeviceRequest | 

    try:
        api_response = api_instance.authenticators_admin_webauthn_update(id, web_authn_device_request)
        print("The response of AuthenticatorsApi->authenticators_admin_webauthn_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_admin_webauthn_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this WebAuthn Device. | 
 **web_authn_device_request** | [**WebAuthnDeviceRequest**](WebAuthnDeviceRequest.md)|  | 

### Return type

[**WebAuthnDevice**](WebAuthnDevice.md)

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

# **authenticators_all_list**
> List[Device] authenticators_all_list()



Get all devices for current user

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.device import Device
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)

    try:
        api_response = api_instance.authenticators_all_list()
        print("The response of AuthenticatorsApi->authenticators_all_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_all_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Device]**](Device.md)

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

# **authenticators_duo_destroy**
> authenticators_duo_destroy(id)



Viewset for Duo authenticator devices

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
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this Duo Device.

    try:
        api_instance.authenticators_duo_destroy(id)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_duo_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Duo Device. | 

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

# **authenticators_duo_list**
> PaginatedDuoDeviceList authenticators_duo_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)



Viewset for Duo authenticator devices

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_duo_device_list import PaginatedDuoDeviceList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.authenticators_duo_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of AuthenticatorsApi->authenticators_duo_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_duo_list: %s\n" % e)
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

[**PaginatedDuoDeviceList**](PaginatedDuoDeviceList.md)

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

# **authenticators_duo_partial_update**
> DuoDevice authenticators_duo_partial_update(id, patched_duo_device_request=patched_duo_device_request)



Viewset for Duo authenticator devices

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.duo_device import DuoDevice
from authentik_openapi.models.patched_duo_device_request import PatchedDuoDeviceRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this Duo Device.
    patched_duo_device_request = authentik_openapi.PatchedDuoDeviceRequest() # PatchedDuoDeviceRequest |  (optional)

    try:
        api_response = api_instance.authenticators_duo_partial_update(id, patched_duo_device_request=patched_duo_device_request)
        print("The response of AuthenticatorsApi->authenticators_duo_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_duo_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Duo Device. | 
 **patched_duo_device_request** | [**PatchedDuoDeviceRequest**](PatchedDuoDeviceRequest.md)|  | [optional] 

### Return type

[**DuoDevice**](DuoDevice.md)

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

# **authenticators_duo_retrieve**
> DuoDevice authenticators_duo_retrieve(id)



Viewset for Duo authenticator devices

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.duo_device import DuoDevice
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this Duo Device.

    try:
        api_response = api_instance.authenticators_duo_retrieve(id)
        print("The response of AuthenticatorsApi->authenticators_duo_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_duo_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Duo Device. | 

### Return type

[**DuoDevice**](DuoDevice.md)

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

# **authenticators_duo_update**
> DuoDevice authenticators_duo_update(id, duo_device_request)



Viewset for Duo authenticator devices

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.duo_device import DuoDevice
from authentik_openapi.models.duo_device_request import DuoDeviceRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this Duo Device.
    duo_device_request = authentik_openapi.DuoDeviceRequest() # DuoDeviceRequest | 

    try:
        api_response = api_instance.authenticators_duo_update(id, duo_device_request)
        print("The response of AuthenticatorsApi->authenticators_duo_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_duo_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Duo Device. | 
 **duo_device_request** | [**DuoDeviceRequest**](DuoDeviceRequest.md)|  | 

### Return type

[**DuoDevice**](DuoDevice.md)

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

# **authenticators_duo_used_by_list**
> List[UsedBy] authenticators_duo_used_by_list(id)



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
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this Duo Device.

    try:
        api_response = api_instance.authenticators_duo_used_by_list(id)
        print("The response of AuthenticatorsApi->authenticators_duo_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_duo_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Duo Device. | 

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

# **authenticators_sms_destroy**
> authenticators_sms_destroy(id)



Viewset for sms authenticator devices

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
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this SMS Device.

    try:
        api_instance.authenticators_sms_destroy(id)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_sms_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SMS Device. | 

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

# **authenticators_sms_list**
> PaginatedSMSDeviceList authenticators_sms_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)



Viewset for sms authenticator devices

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_sms_device_list import PaginatedSMSDeviceList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.authenticators_sms_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of AuthenticatorsApi->authenticators_sms_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_sms_list: %s\n" % e)
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

[**PaginatedSMSDeviceList**](PaginatedSMSDeviceList.md)

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

# **authenticators_sms_partial_update**
> SMSDevice authenticators_sms_partial_update(id, patched_sms_device_request=patched_sms_device_request)



Viewset for sms authenticator devices

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_sms_device_request import PatchedSMSDeviceRequest
from authentik_openapi.models.sms_device import SMSDevice
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this SMS Device.
    patched_sms_device_request = authentik_openapi.PatchedSMSDeviceRequest() # PatchedSMSDeviceRequest |  (optional)

    try:
        api_response = api_instance.authenticators_sms_partial_update(id, patched_sms_device_request=patched_sms_device_request)
        print("The response of AuthenticatorsApi->authenticators_sms_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_sms_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SMS Device. | 
 **patched_sms_device_request** | [**PatchedSMSDeviceRequest**](PatchedSMSDeviceRequest.md)|  | [optional] 

### Return type

[**SMSDevice**](SMSDevice.md)

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

# **authenticators_sms_retrieve**
> SMSDevice authenticators_sms_retrieve(id)



Viewset for sms authenticator devices

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.sms_device import SMSDevice
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this SMS Device.

    try:
        api_response = api_instance.authenticators_sms_retrieve(id)
        print("The response of AuthenticatorsApi->authenticators_sms_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_sms_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SMS Device. | 

### Return type

[**SMSDevice**](SMSDevice.md)

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

# **authenticators_sms_update**
> SMSDevice authenticators_sms_update(id, sms_device_request)



Viewset for sms authenticator devices

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.sms_device import SMSDevice
from authentik_openapi.models.sms_device_request import SMSDeviceRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this SMS Device.
    sms_device_request = authentik_openapi.SMSDeviceRequest() # SMSDeviceRequest | 

    try:
        api_response = api_instance.authenticators_sms_update(id, sms_device_request)
        print("The response of AuthenticatorsApi->authenticators_sms_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_sms_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SMS Device. | 
 **sms_device_request** | [**SMSDeviceRequest**](SMSDeviceRequest.md)|  | 

### Return type

[**SMSDevice**](SMSDevice.md)

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

# **authenticators_sms_used_by_list**
> List[UsedBy] authenticators_sms_used_by_list(id)



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
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this SMS Device.

    try:
        api_response = api_instance.authenticators_sms_used_by_list(id)
        print("The response of AuthenticatorsApi->authenticators_sms_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_sms_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this SMS Device. | 

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

# **authenticators_static_destroy**
> authenticators_static_destroy(id)



Viewset for static authenticator devices

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
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this Static Device.

    try:
        api_instance.authenticators_static_destroy(id)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_static_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Static Device. | 

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

# **authenticators_static_list**
> PaginatedStaticDeviceList authenticators_static_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)



Viewset for static authenticator devices

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_static_device_list import PaginatedStaticDeviceList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.authenticators_static_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of AuthenticatorsApi->authenticators_static_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_static_list: %s\n" % e)
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

[**PaginatedStaticDeviceList**](PaginatedStaticDeviceList.md)

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

# **authenticators_static_partial_update**
> StaticDevice authenticators_static_partial_update(id, patched_static_device_request=patched_static_device_request)



Viewset for static authenticator devices

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_static_device_request import PatchedStaticDeviceRequest
from authentik_openapi.models.static_device import StaticDevice
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this Static Device.
    patched_static_device_request = authentik_openapi.PatchedStaticDeviceRequest() # PatchedStaticDeviceRequest |  (optional)

    try:
        api_response = api_instance.authenticators_static_partial_update(id, patched_static_device_request=patched_static_device_request)
        print("The response of AuthenticatorsApi->authenticators_static_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_static_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Static Device. | 
 **patched_static_device_request** | [**PatchedStaticDeviceRequest**](PatchedStaticDeviceRequest.md)|  | [optional] 

### Return type

[**StaticDevice**](StaticDevice.md)

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

# **authenticators_static_retrieve**
> StaticDevice authenticators_static_retrieve(id)



Viewset for static authenticator devices

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.static_device import StaticDevice
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this Static Device.

    try:
        api_response = api_instance.authenticators_static_retrieve(id)
        print("The response of AuthenticatorsApi->authenticators_static_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_static_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Static Device. | 

### Return type

[**StaticDevice**](StaticDevice.md)

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

# **authenticators_static_update**
> StaticDevice authenticators_static_update(id, static_device_request)



Viewset for static authenticator devices

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.static_device import StaticDevice
from authentik_openapi.models.static_device_request import StaticDeviceRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this Static Device.
    static_device_request = authentik_openapi.StaticDeviceRequest() # StaticDeviceRequest | 

    try:
        api_response = api_instance.authenticators_static_update(id, static_device_request)
        print("The response of AuthenticatorsApi->authenticators_static_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_static_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Static Device. | 
 **static_device_request** | [**StaticDeviceRequest**](StaticDeviceRequest.md)|  | 

### Return type

[**StaticDevice**](StaticDevice.md)

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

# **authenticators_static_used_by_list**
> List[UsedBy] authenticators_static_used_by_list(id)



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
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this Static Device.

    try:
        api_response = api_instance.authenticators_static_used_by_list(id)
        print("The response of AuthenticatorsApi->authenticators_static_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_static_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this Static Device. | 

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

# **authenticators_totp_destroy**
> authenticators_totp_destroy(id)



Viewset for totp authenticator devices

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
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this TOTP Device.

    try:
        api_instance.authenticators_totp_destroy(id)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_totp_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this TOTP Device. | 

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

# **authenticators_totp_list**
> PaginatedTOTPDeviceList authenticators_totp_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)



Viewset for totp authenticator devices

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_totp_device_list import PaginatedTOTPDeviceList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.authenticators_totp_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of AuthenticatorsApi->authenticators_totp_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_totp_list: %s\n" % e)
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

[**PaginatedTOTPDeviceList**](PaginatedTOTPDeviceList.md)

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

# **authenticators_totp_partial_update**
> TOTPDevice authenticators_totp_partial_update(id, patched_totp_device_request=patched_totp_device_request)



Viewset for totp authenticator devices

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_totp_device_request import PatchedTOTPDeviceRequest
from authentik_openapi.models.totp_device import TOTPDevice
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this TOTP Device.
    patched_totp_device_request = authentik_openapi.PatchedTOTPDeviceRequest() # PatchedTOTPDeviceRequest |  (optional)

    try:
        api_response = api_instance.authenticators_totp_partial_update(id, patched_totp_device_request=patched_totp_device_request)
        print("The response of AuthenticatorsApi->authenticators_totp_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_totp_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this TOTP Device. | 
 **patched_totp_device_request** | [**PatchedTOTPDeviceRequest**](PatchedTOTPDeviceRequest.md)|  | [optional] 

### Return type

[**TOTPDevice**](TOTPDevice.md)

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

# **authenticators_totp_retrieve**
> TOTPDevice authenticators_totp_retrieve(id)



Viewset for totp authenticator devices

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.totp_device import TOTPDevice
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this TOTP Device.

    try:
        api_response = api_instance.authenticators_totp_retrieve(id)
        print("The response of AuthenticatorsApi->authenticators_totp_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_totp_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this TOTP Device. | 

### Return type

[**TOTPDevice**](TOTPDevice.md)

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

# **authenticators_totp_update**
> TOTPDevice authenticators_totp_update(id, totp_device_request)



Viewset for totp authenticator devices

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.totp_device import TOTPDevice
from authentik_openapi.models.totp_device_request import TOTPDeviceRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this TOTP Device.
    totp_device_request = authentik_openapi.TOTPDeviceRequest() # TOTPDeviceRequest | 

    try:
        api_response = api_instance.authenticators_totp_update(id, totp_device_request)
        print("The response of AuthenticatorsApi->authenticators_totp_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_totp_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this TOTP Device. | 
 **totp_device_request** | [**TOTPDeviceRequest**](TOTPDeviceRequest.md)|  | 

### Return type

[**TOTPDevice**](TOTPDevice.md)

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

# **authenticators_totp_used_by_list**
> List[UsedBy] authenticators_totp_used_by_list(id)



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
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this TOTP Device.

    try:
        api_response = api_instance.authenticators_totp_used_by_list(id)
        print("The response of AuthenticatorsApi->authenticators_totp_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_totp_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this TOTP Device. | 

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

# **authenticators_webauthn_destroy**
> authenticators_webauthn_destroy(id)



Viewset for WebAuthn authenticator devices

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
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this WebAuthn Device.

    try:
        api_instance.authenticators_webauthn_destroy(id)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_webauthn_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this WebAuthn Device. | 

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

# **authenticators_webauthn_list**
> PaginatedWebAuthnDeviceList authenticators_webauthn_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)



Viewset for WebAuthn authenticator devices

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_web_authn_device_list import PaginatedWebAuthnDeviceList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.authenticators_webauthn_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of AuthenticatorsApi->authenticators_webauthn_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_webauthn_list: %s\n" % e)
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

[**PaginatedWebAuthnDeviceList**](PaginatedWebAuthnDeviceList.md)

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

# **authenticators_webauthn_partial_update**
> WebAuthnDevice authenticators_webauthn_partial_update(id, patched_web_authn_device_request=patched_web_authn_device_request)



Viewset for WebAuthn authenticator devices

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.patched_web_authn_device_request import PatchedWebAuthnDeviceRequest
from authentik_openapi.models.web_authn_device import WebAuthnDevice
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this WebAuthn Device.
    patched_web_authn_device_request = authentik_openapi.PatchedWebAuthnDeviceRequest() # PatchedWebAuthnDeviceRequest |  (optional)

    try:
        api_response = api_instance.authenticators_webauthn_partial_update(id, patched_web_authn_device_request=patched_web_authn_device_request)
        print("The response of AuthenticatorsApi->authenticators_webauthn_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_webauthn_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this WebAuthn Device. | 
 **patched_web_authn_device_request** | [**PatchedWebAuthnDeviceRequest**](PatchedWebAuthnDeviceRequest.md)|  | [optional] 

### Return type

[**WebAuthnDevice**](WebAuthnDevice.md)

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

# **authenticators_webauthn_retrieve**
> WebAuthnDevice authenticators_webauthn_retrieve(id)



Viewset for WebAuthn authenticator devices

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.web_authn_device import WebAuthnDevice
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this WebAuthn Device.

    try:
        api_response = api_instance.authenticators_webauthn_retrieve(id)
        print("The response of AuthenticatorsApi->authenticators_webauthn_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_webauthn_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this WebAuthn Device. | 

### Return type

[**WebAuthnDevice**](WebAuthnDevice.md)

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

# **authenticators_webauthn_update**
> WebAuthnDevice authenticators_webauthn_update(id, web_authn_device_request)



Viewset for WebAuthn authenticator devices

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.web_authn_device import WebAuthnDevice
from authentik_openapi.models.web_authn_device_request import WebAuthnDeviceRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this WebAuthn Device.
    web_authn_device_request = authentik_openapi.WebAuthnDeviceRequest() # WebAuthnDeviceRequest | 

    try:
        api_response = api_instance.authenticators_webauthn_update(id, web_authn_device_request)
        print("The response of AuthenticatorsApi->authenticators_webauthn_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_webauthn_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this WebAuthn Device. | 
 **web_authn_device_request** | [**WebAuthnDeviceRequest**](WebAuthnDeviceRequest.md)|  | 

### Return type

[**WebAuthnDevice**](WebAuthnDevice.md)

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

# **authenticators_webauthn_used_by_list**
> List[UsedBy] authenticators_webauthn_used_by_list(id)



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
    api_instance = authentik_openapi.AuthenticatorsApi(api_client)
    id = 56 # int | A unique integer value identifying this WebAuthn Device.

    try:
        api_response = api_instance.authenticators_webauthn_used_by_list(id)
        print("The response of AuthenticatorsApi->authenticators_webauthn_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticatorsApi->authenticators_webauthn_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this WebAuthn Device. | 

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

