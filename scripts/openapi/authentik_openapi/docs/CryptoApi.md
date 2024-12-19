# authentik_openapi.CryptoApi

All URIs are relative to *https://auth.home.ohmymndy.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crypto_certificatekeypairs_create**](CryptoApi.md#crypto_certificatekeypairs_create) | **POST** /crypto/certificatekeypairs/ | 
[**crypto_certificatekeypairs_destroy**](CryptoApi.md#crypto_certificatekeypairs_destroy) | **DELETE** /crypto/certificatekeypairs/{kp_uuid}/ | 
[**crypto_certificatekeypairs_generate_create**](CryptoApi.md#crypto_certificatekeypairs_generate_create) | **POST** /crypto/certificatekeypairs/generate/ | 
[**crypto_certificatekeypairs_list**](CryptoApi.md#crypto_certificatekeypairs_list) | **GET** /crypto/certificatekeypairs/ | 
[**crypto_certificatekeypairs_partial_update**](CryptoApi.md#crypto_certificatekeypairs_partial_update) | **PATCH** /crypto/certificatekeypairs/{kp_uuid}/ | 
[**crypto_certificatekeypairs_retrieve**](CryptoApi.md#crypto_certificatekeypairs_retrieve) | **GET** /crypto/certificatekeypairs/{kp_uuid}/ | 
[**crypto_certificatekeypairs_update**](CryptoApi.md#crypto_certificatekeypairs_update) | **PUT** /crypto/certificatekeypairs/{kp_uuid}/ | 
[**crypto_certificatekeypairs_used_by_list**](CryptoApi.md#crypto_certificatekeypairs_used_by_list) | **GET** /crypto/certificatekeypairs/{kp_uuid}/used_by/ | 
[**crypto_certificatekeypairs_view_certificate_retrieve**](CryptoApi.md#crypto_certificatekeypairs_view_certificate_retrieve) | **GET** /crypto/certificatekeypairs/{kp_uuid}/view_certificate/ | 
[**crypto_certificatekeypairs_view_private_key_retrieve**](CryptoApi.md#crypto_certificatekeypairs_view_private_key_retrieve) | **GET** /crypto/certificatekeypairs/{kp_uuid}/view_private_key/ | 


# **crypto_certificatekeypairs_create**
> CertificateKeyPair crypto_certificatekeypairs_create(certificate_key_pair_request)



CertificateKeyPair Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.certificate_key_pair import CertificateKeyPair
from authentik_openapi.models.certificate_key_pair_request import CertificateKeyPairRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CryptoApi(api_client)
    certificate_key_pair_request = authentik_openapi.CertificateKeyPairRequest() # CertificateKeyPairRequest | 

    try:
        api_response = api_instance.crypto_certificatekeypairs_create(certificate_key_pair_request)
        print("The response of CryptoApi->crypto_certificatekeypairs_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoApi->crypto_certificatekeypairs_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_key_pair_request** | [**CertificateKeyPairRequest**](CertificateKeyPairRequest.md)|  | 

### Return type

[**CertificateKeyPair**](CertificateKeyPair.md)

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

# **crypto_certificatekeypairs_destroy**
> crypto_certificatekeypairs_destroy(kp_uuid)



CertificateKeyPair Viewset

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
    api_instance = authentik_openapi.CryptoApi(api_client)
    kp_uuid = 'kp_uuid_example' # str | A UUID string identifying this Certificate-Key Pair.

    try:
        api_instance.crypto_certificatekeypairs_destroy(kp_uuid)
    except Exception as e:
        print("Exception when calling CryptoApi->crypto_certificatekeypairs_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kp_uuid** | **str**| A UUID string identifying this Certificate-Key Pair. | 

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

# **crypto_certificatekeypairs_generate_create**
> CertificateKeyPair crypto_certificatekeypairs_generate_create(certificate_generation_request)



Generate a new, self-signed certificate-key pair

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.certificate_generation_request import CertificateGenerationRequest
from authentik_openapi.models.certificate_key_pair import CertificateKeyPair
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CryptoApi(api_client)
    certificate_generation_request = authentik_openapi.CertificateGenerationRequest() # CertificateGenerationRequest | 

    try:
        api_response = api_instance.crypto_certificatekeypairs_generate_create(certificate_generation_request)
        print("The response of CryptoApi->crypto_certificatekeypairs_generate_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoApi->crypto_certificatekeypairs_generate_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_generation_request** | [**CertificateGenerationRequest**](CertificateGenerationRequest.md)|  | 

### Return type

[**CertificateKeyPair**](CertificateKeyPair.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Bad request |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crypto_certificatekeypairs_list**
> PaginatedCertificateKeyPairList crypto_certificatekeypairs_list(has_key=has_key, include_details=include_details, managed=managed, name=name, ordering=ordering, page=page, page_size=page_size, search=search)



CertificateKeyPair Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_certificate_key_pair_list import PaginatedCertificateKeyPairList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CryptoApi(api_client)
    has_key = True # bool | Only return certificate-key pairs with keys (optional)
    include_details = True # bool |  (optional) (default to True)
    managed = 'managed_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.crypto_certificatekeypairs_list(has_key=has_key, include_details=include_details, managed=managed, name=name, ordering=ordering, page=page, page_size=page_size, search=search)
        print("The response of CryptoApi->crypto_certificatekeypairs_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoApi->crypto_certificatekeypairs_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **has_key** | **bool**| Only return certificate-key pairs with keys | [optional] 
 **include_details** | **bool**|  | [optional] [default to True]
 **managed** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedCertificateKeyPairList**](PaginatedCertificateKeyPairList.md)

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

# **crypto_certificatekeypairs_partial_update**
> CertificateKeyPair crypto_certificatekeypairs_partial_update(kp_uuid, patched_certificate_key_pair_request=patched_certificate_key_pair_request)



CertificateKeyPair Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.certificate_key_pair import CertificateKeyPair
from authentik_openapi.models.patched_certificate_key_pair_request import PatchedCertificateKeyPairRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CryptoApi(api_client)
    kp_uuid = 'kp_uuid_example' # str | A UUID string identifying this Certificate-Key Pair.
    patched_certificate_key_pair_request = authentik_openapi.PatchedCertificateKeyPairRequest() # PatchedCertificateKeyPairRequest |  (optional)

    try:
        api_response = api_instance.crypto_certificatekeypairs_partial_update(kp_uuid, patched_certificate_key_pair_request=patched_certificate_key_pair_request)
        print("The response of CryptoApi->crypto_certificatekeypairs_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoApi->crypto_certificatekeypairs_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kp_uuid** | **str**| A UUID string identifying this Certificate-Key Pair. | 
 **patched_certificate_key_pair_request** | [**PatchedCertificateKeyPairRequest**](PatchedCertificateKeyPairRequest.md)|  | [optional] 

### Return type

[**CertificateKeyPair**](CertificateKeyPair.md)

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

# **crypto_certificatekeypairs_retrieve**
> CertificateKeyPair crypto_certificatekeypairs_retrieve(kp_uuid)



CertificateKeyPair Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.certificate_key_pair import CertificateKeyPair
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CryptoApi(api_client)
    kp_uuid = 'kp_uuid_example' # str | A UUID string identifying this Certificate-Key Pair.

    try:
        api_response = api_instance.crypto_certificatekeypairs_retrieve(kp_uuid)
        print("The response of CryptoApi->crypto_certificatekeypairs_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoApi->crypto_certificatekeypairs_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kp_uuid** | **str**| A UUID string identifying this Certificate-Key Pair. | 

### Return type

[**CertificateKeyPair**](CertificateKeyPair.md)

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

# **crypto_certificatekeypairs_update**
> CertificateKeyPair crypto_certificatekeypairs_update(kp_uuid, certificate_key_pair_request)



CertificateKeyPair Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.certificate_key_pair import CertificateKeyPair
from authentik_openapi.models.certificate_key_pair_request import CertificateKeyPairRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CryptoApi(api_client)
    kp_uuid = 'kp_uuid_example' # str | A UUID string identifying this Certificate-Key Pair.
    certificate_key_pair_request = authentik_openapi.CertificateKeyPairRequest() # CertificateKeyPairRequest | 

    try:
        api_response = api_instance.crypto_certificatekeypairs_update(kp_uuid, certificate_key_pair_request)
        print("The response of CryptoApi->crypto_certificatekeypairs_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoApi->crypto_certificatekeypairs_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kp_uuid** | **str**| A UUID string identifying this Certificate-Key Pair. | 
 **certificate_key_pair_request** | [**CertificateKeyPairRequest**](CertificateKeyPairRequest.md)|  | 

### Return type

[**CertificateKeyPair**](CertificateKeyPair.md)

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

# **crypto_certificatekeypairs_used_by_list**
> List[UsedBy] crypto_certificatekeypairs_used_by_list(kp_uuid)



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
    api_instance = authentik_openapi.CryptoApi(api_client)
    kp_uuid = 'kp_uuid_example' # str | A UUID string identifying this Certificate-Key Pair.

    try:
        api_response = api_instance.crypto_certificatekeypairs_used_by_list(kp_uuid)
        print("The response of CryptoApi->crypto_certificatekeypairs_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoApi->crypto_certificatekeypairs_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kp_uuid** | **str**| A UUID string identifying this Certificate-Key Pair. | 

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

# **crypto_certificatekeypairs_view_certificate_retrieve**
> CertificateData crypto_certificatekeypairs_view_certificate_retrieve(kp_uuid, download=download)



Return certificate-key pairs certificate and log access

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.certificate_data import CertificateData
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CryptoApi(api_client)
    kp_uuid = 'kp_uuid_example' # str | A UUID string identifying this Certificate-Key Pair.
    download = True # bool |  (optional)

    try:
        api_response = api_instance.crypto_certificatekeypairs_view_certificate_retrieve(kp_uuid, download=download)
        print("The response of CryptoApi->crypto_certificatekeypairs_view_certificate_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoApi->crypto_certificatekeypairs_view_certificate_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kp_uuid** | **str**| A UUID string identifying this Certificate-Key Pair. | 
 **download** | **bool**|  | [optional] 

### Return type

[**CertificateData**](CertificateData.md)

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

# **crypto_certificatekeypairs_view_private_key_retrieve**
> CertificateData crypto_certificatekeypairs_view_private_key_retrieve(kp_uuid, download=download)



Return certificate-key pairs private key and log access

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.certificate_data import CertificateData
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.CryptoApi(api_client)
    kp_uuid = 'kp_uuid_example' # str | A UUID string identifying this Certificate-Key Pair.
    download = True # bool |  (optional)

    try:
        api_response = api_instance.crypto_certificatekeypairs_view_private_key_retrieve(kp_uuid, download=download)
        print("The response of CryptoApi->crypto_certificatekeypairs_view_private_key_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CryptoApi->crypto_certificatekeypairs_view_private_key_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kp_uuid** | **str**| A UUID string identifying this Certificate-Key Pair. | 
 **download** | **bool**|  | [optional] 

### Return type

[**CertificateData**](CertificateData.md)

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

