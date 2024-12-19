# authentik_openapi.ManagedApi

All URIs are relative to *https://auth.home.ohmymndy.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**managed_blueprints_apply_create**](ManagedApi.md#managed_blueprints_apply_create) | **POST** /managed/blueprints/{instance_uuid}/apply/ | 
[**managed_blueprints_available_list**](ManagedApi.md#managed_blueprints_available_list) | **GET** /managed/blueprints/available/ | 
[**managed_blueprints_create**](ManagedApi.md#managed_blueprints_create) | **POST** /managed/blueprints/ | 
[**managed_blueprints_destroy**](ManagedApi.md#managed_blueprints_destroy) | **DELETE** /managed/blueprints/{instance_uuid}/ | 
[**managed_blueprints_list**](ManagedApi.md#managed_blueprints_list) | **GET** /managed/blueprints/ | 
[**managed_blueprints_partial_update**](ManagedApi.md#managed_blueprints_partial_update) | **PATCH** /managed/blueprints/{instance_uuid}/ | 
[**managed_blueprints_retrieve**](ManagedApi.md#managed_blueprints_retrieve) | **GET** /managed/blueprints/{instance_uuid}/ | 
[**managed_blueprints_update**](ManagedApi.md#managed_blueprints_update) | **PUT** /managed/blueprints/{instance_uuid}/ | 
[**managed_blueprints_used_by_list**](ManagedApi.md#managed_blueprints_used_by_list) | **GET** /managed/blueprints/{instance_uuid}/used_by/ | 


# **managed_blueprints_apply_create**
> BlueprintInstance managed_blueprints_apply_create(instance_uuid)



Apply a blueprint

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.blueprint_instance import BlueprintInstance
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ManagedApi(api_client)
    instance_uuid = 'instance_uuid_example' # str | A UUID string identifying this Blueprint Instance.

    try:
        api_response = api_instance.managed_blueprints_apply_create(instance_uuid)
        print("The response of ManagedApi->managed_blueprints_apply_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->managed_blueprints_apply_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_uuid** | **str**| A UUID string identifying this Blueprint Instance. | 

### Return type

[**BlueprintInstance**](BlueprintInstance.md)

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

# **managed_blueprints_available_list**
> List[BlueprintFile] managed_blueprints_available_list()



Get blueprints

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.blueprint_file import BlueprintFile
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ManagedApi(api_client)

    try:
        api_response = api_instance.managed_blueprints_available_list()
        print("The response of ManagedApi->managed_blueprints_available_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->managed_blueprints_available_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[BlueprintFile]**](BlueprintFile.md)

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

# **managed_blueprints_create**
> BlueprintInstance managed_blueprints_create(blueprint_instance_request)



Blueprint instances

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.blueprint_instance import BlueprintInstance
from authentik_openapi.models.blueprint_instance_request import BlueprintInstanceRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ManagedApi(api_client)
    blueprint_instance_request = authentik_openapi.BlueprintInstanceRequest() # BlueprintInstanceRequest | 

    try:
        api_response = api_instance.managed_blueprints_create(blueprint_instance_request)
        print("The response of ManagedApi->managed_blueprints_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->managed_blueprints_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blueprint_instance_request** | [**BlueprintInstanceRequest**](BlueprintInstanceRequest.md)|  | 

### Return type

[**BlueprintInstance**](BlueprintInstance.md)

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

# **managed_blueprints_destroy**
> managed_blueprints_destroy(instance_uuid)



Blueprint instances

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
    api_instance = authentik_openapi.ManagedApi(api_client)
    instance_uuid = 'instance_uuid_example' # str | A UUID string identifying this Blueprint Instance.

    try:
        api_instance.managed_blueprints_destroy(instance_uuid)
    except Exception as e:
        print("Exception when calling ManagedApi->managed_blueprints_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_uuid** | **str**| A UUID string identifying this Blueprint Instance. | 

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

# **managed_blueprints_list**
> PaginatedBlueprintInstanceList managed_blueprints_list(name=name, ordering=ordering, page=page, page_size=page_size, path=path, search=search)



Blueprint instances

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_blueprint_instance_list import PaginatedBlueprintInstanceList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ManagedApi(api_client)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    path = 'path_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.managed_blueprints_list(name=name, ordering=ordering, page=page, page_size=page_size, path=path, search=search)
        print("The response of ManagedApi->managed_blueprints_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->managed_blueprints_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **path** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedBlueprintInstanceList**](PaginatedBlueprintInstanceList.md)

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

# **managed_blueprints_partial_update**
> BlueprintInstance managed_blueprints_partial_update(instance_uuid, patched_blueprint_instance_request=patched_blueprint_instance_request)



Blueprint instances

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.blueprint_instance import BlueprintInstance
from authentik_openapi.models.patched_blueprint_instance_request import PatchedBlueprintInstanceRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ManagedApi(api_client)
    instance_uuid = 'instance_uuid_example' # str | A UUID string identifying this Blueprint Instance.
    patched_blueprint_instance_request = authentik_openapi.PatchedBlueprintInstanceRequest() # PatchedBlueprintInstanceRequest |  (optional)

    try:
        api_response = api_instance.managed_blueprints_partial_update(instance_uuid, patched_blueprint_instance_request=patched_blueprint_instance_request)
        print("The response of ManagedApi->managed_blueprints_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->managed_blueprints_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_uuid** | **str**| A UUID string identifying this Blueprint Instance. | 
 **patched_blueprint_instance_request** | [**PatchedBlueprintInstanceRequest**](PatchedBlueprintInstanceRequest.md)|  | [optional] 

### Return type

[**BlueprintInstance**](BlueprintInstance.md)

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

# **managed_blueprints_retrieve**
> BlueprintInstance managed_blueprints_retrieve(instance_uuid)



Blueprint instances

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.blueprint_instance import BlueprintInstance
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ManagedApi(api_client)
    instance_uuid = 'instance_uuid_example' # str | A UUID string identifying this Blueprint Instance.

    try:
        api_response = api_instance.managed_blueprints_retrieve(instance_uuid)
        print("The response of ManagedApi->managed_blueprints_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->managed_blueprints_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_uuid** | **str**| A UUID string identifying this Blueprint Instance. | 

### Return type

[**BlueprintInstance**](BlueprintInstance.md)

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

# **managed_blueprints_update**
> BlueprintInstance managed_blueprints_update(instance_uuid, blueprint_instance_request)



Blueprint instances

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.blueprint_instance import BlueprintInstance
from authentik_openapi.models.blueprint_instance_request import BlueprintInstanceRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.ManagedApi(api_client)
    instance_uuid = 'instance_uuid_example' # str | A UUID string identifying this Blueprint Instance.
    blueprint_instance_request = authentik_openapi.BlueprintInstanceRequest() # BlueprintInstanceRequest | 

    try:
        api_response = api_instance.managed_blueprints_update(instance_uuid, blueprint_instance_request)
        print("The response of ManagedApi->managed_blueprints_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->managed_blueprints_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_uuid** | **str**| A UUID string identifying this Blueprint Instance. | 
 **blueprint_instance_request** | [**BlueprintInstanceRequest**](BlueprintInstanceRequest.md)|  | 

### Return type

[**BlueprintInstance**](BlueprintInstance.md)

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

# **managed_blueprints_used_by_list**
> List[UsedBy] managed_blueprints_used_by_list(instance_uuid)



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
    api_instance = authentik_openapi.ManagedApi(api_client)
    instance_uuid = 'instance_uuid_example' # str | A UUID string identifying this Blueprint Instance.

    try:
        api_response = api_instance.managed_blueprints_used_by_list(instance_uuid)
        print("The response of ManagedApi->managed_blueprints_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedApi->managed_blueprints_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_uuid** | **str**| A UUID string identifying this Blueprint Instance. | 

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

