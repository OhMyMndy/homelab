# authentik_openapi.EnterpriseApi

All URIs are relative to *https://auth.home.ohmymndy.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enterprise_license_create**](EnterpriseApi.md#enterprise_license_create) | **POST** /enterprise/license/ | 
[**enterprise_license_destroy**](EnterpriseApi.md#enterprise_license_destroy) | **DELETE** /enterprise/license/{license_uuid}/ | 
[**enterprise_license_forecast_retrieve**](EnterpriseApi.md#enterprise_license_forecast_retrieve) | **GET** /enterprise/license/forecast/ | 
[**enterprise_license_get_install_id_retrieve**](EnterpriseApi.md#enterprise_license_get_install_id_retrieve) | **GET** /enterprise/license/get_install_id/ | 
[**enterprise_license_list**](EnterpriseApi.md#enterprise_license_list) | **GET** /enterprise/license/ | 
[**enterprise_license_partial_update**](EnterpriseApi.md#enterprise_license_partial_update) | **PATCH** /enterprise/license/{license_uuid}/ | 
[**enterprise_license_retrieve**](EnterpriseApi.md#enterprise_license_retrieve) | **GET** /enterprise/license/{license_uuid}/ | 
[**enterprise_license_summary_retrieve**](EnterpriseApi.md#enterprise_license_summary_retrieve) | **GET** /enterprise/license/summary/ | 
[**enterprise_license_update**](EnterpriseApi.md#enterprise_license_update) | **PUT** /enterprise/license/{license_uuid}/ | 
[**enterprise_license_used_by_list**](EnterpriseApi.md#enterprise_license_used_by_list) | **GET** /enterprise/license/{license_uuid}/used_by/ | 


# **enterprise_license_create**
> License enterprise_license_create(license_request)



License Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.license import License
from authentik_openapi.models.license_request import LicenseRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EnterpriseApi(api_client)
    license_request = authentik_openapi.LicenseRequest() # LicenseRequest | 

    try:
        api_response = api_instance.enterprise_license_create(license_request)
        print("The response of EnterpriseApi->enterprise_license_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->enterprise_license_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_request** | [**LicenseRequest**](LicenseRequest.md)|  | 

### Return type

[**License**](License.md)

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

# **enterprise_license_destroy**
> enterprise_license_destroy(license_uuid)



License Viewset

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
    api_instance = authentik_openapi.EnterpriseApi(api_client)
    license_uuid = 'license_uuid_example' # str | A UUID string identifying this License.

    try:
        api_instance.enterprise_license_destroy(license_uuid)
    except Exception as e:
        print("Exception when calling EnterpriseApi->enterprise_license_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_uuid** | **str**| A UUID string identifying this License. | 

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

# **enterprise_license_forecast_retrieve**
> LicenseForecast enterprise_license_forecast_retrieve()



Forecast how many users will be required in a year

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.license_forecast import LicenseForecast
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EnterpriseApi(api_client)

    try:
        api_response = api_instance.enterprise_license_forecast_retrieve()
        print("The response of EnterpriseApi->enterprise_license_forecast_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->enterprise_license_forecast_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LicenseForecast**](LicenseForecast.md)

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

# **enterprise_license_get_install_id_retrieve**
> InstallID enterprise_license_get_install_id_retrieve()



Get install_id

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.install_id import InstallID
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EnterpriseApi(api_client)

    try:
        api_response = api_instance.enterprise_license_get_install_id_retrieve()
        print("The response of EnterpriseApi->enterprise_license_get_install_id_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->enterprise_license_get_install_id_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InstallID**](InstallID.md)

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

# **enterprise_license_list**
> PaginatedLicenseList enterprise_license_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)



License Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_license_list import PaginatedLicenseList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EnterpriseApi(api_client)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.enterprise_license_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of EnterpriseApi->enterprise_license_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->enterprise_license_list: %s\n" % e)
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

[**PaginatedLicenseList**](PaginatedLicenseList.md)

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

# **enterprise_license_partial_update**
> License enterprise_license_partial_update(license_uuid, patched_license_request=patched_license_request)



License Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.license import License
from authentik_openapi.models.patched_license_request import PatchedLicenseRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EnterpriseApi(api_client)
    license_uuid = 'license_uuid_example' # str | A UUID string identifying this License.
    patched_license_request = authentik_openapi.PatchedLicenseRequest() # PatchedLicenseRequest |  (optional)

    try:
        api_response = api_instance.enterprise_license_partial_update(license_uuid, patched_license_request=patched_license_request)
        print("The response of EnterpriseApi->enterprise_license_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->enterprise_license_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_uuid** | **str**| A UUID string identifying this License. | 
 **patched_license_request** | [**PatchedLicenseRequest**](PatchedLicenseRequest.md)|  | [optional] 

### Return type

[**License**](License.md)

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

# **enterprise_license_retrieve**
> License enterprise_license_retrieve(license_uuid)



License Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.license import License
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EnterpriseApi(api_client)
    license_uuid = 'license_uuid_example' # str | A UUID string identifying this License.

    try:
        api_response = api_instance.enterprise_license_retrieve(license_uuid)
        print("The response of EnterpriseApi->enterprise_license_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->enterprise_license_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_uuid** | **str**| A UUID string identifying this License. | 

### Return type

[**License**](License.md)

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

# **enterprise_license_summary_retrieve**
> LicenseSummary enterprise_license_summary_retrieve()



Get the total license status

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.license_summary import LicenseSummary
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EnterpriseApi(api_client)

    try:
        api_response = api_instance.enterprise_license_summary_retrieve()
        print("The response of EnterpriseApi->enterprise_license_summary_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->enterprise_license_summary_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LicenseSummary**](LicenseSummary.md)

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

# **enterprise_license_update**
> License enterprise_license_update(license_uuid, license_request)



License Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.license import License
from authentik_openapi.models.license_request import LicenseRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EnterpriseApi(api_client)
    license_uuid = 'license_uuid_example' # str | A UUID string identifying this License.
    license_request = authentik_openapi.LicenseRequest() # LicenseRequest | 

    try:
        api_response = api_instance.enterprise_license_update(license_uuid, license_request)
        print("The response of EnterpriseApi->enterprise_license_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->enterprise_license_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_uuid** | **str**| A UUID string identifying this License. | 
 **license_request** | [**LicenseRequest**](LicenseRequest.md)|  | 

### Return type

[**License**](License.md)

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

# **enterprise_license_used_by_list**
> List[UsedBy] enterprise_license_used_by_list(license_uuid)



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
    api_instance = authentik_openapi.EnterpriseApi(api_client)
    license_uuid = 'license_uuid_example' # str | A UUID string identifying this License.

    try:
        api_response = api_instance.enterprise_license_used_by_list(license_uuid)
        print("The response of EnterpriseApi->enterprise_license_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnterpriseApi->enterprise_license_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_uuid** | **str**| A UUID string identifying this License. | 

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

