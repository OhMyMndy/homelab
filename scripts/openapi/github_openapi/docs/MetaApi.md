# github_openapi.MetaApi

All URIs are relative to *https://api.github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**meta_get**](MetaApi.md#meta_get) | **GET** /meta | Get GitHub meta information
[**meta_get_all_versions**](MetaApi.md#meta_get_all_versions) | **GET** /versions | Get all API versions
[**meta_get_octocat**](MetaApi.md#meta_get_octocat) | **GET** /octocat | Get Octocat
[**meta_get_zen**](MetaApi.md#meta_get_zen) | **GET** /zen | Get the Zen of GitHub
[**meta_root**](MetaApi.md#meta_root) | **GET** / | GitHub API Root


# **meta_get**
> ApiOverview meta_get()

Get GitHub meta information

Returns meta information about GitHub, including a list of GitHub's IP addresses. For more information, see \"[About GitHub's IP addresses](https://docs.github.com/articles/about-github-s-ip-addresses/).\"  The API's response also includes a list of GitHub's domain names.  The values shown in the documentation's response are example values. You must always query the API directly to get the latest values.  > [!NOTE] > This endpoint returns both IPv4 and IPv6 addresses. However, not all features support IPv6. You should refer to the specific documentation for each feature to determine if IPv6 is supported.

### Example


```python
import github_openapi
from github_openapi.models.api_overview import ApiOverview
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.MetaApi(api_client)

    try:
        # Get GitHub meta information
        api_response = api_instance.meta_get()
        print("The response of MetaApi->meta_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaApi->meta_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiOverview**](ApiOverview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**304** | Not modified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meta_get_all_versions**
> List[date] meta_get_all_versions()

Get all API versions

Get all supported GitHub API versions.

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.MetaApi(api_client)

    try:
        # Get all API versions
        api_response = api_instance.meta_get_all_versions()
        print("The response of MetaApi->meta_get_all_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaApi->meta_get_all_versions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[date]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meta_get_octocat**
> str meta_get_octocat(s=s)

Get Octocat

Get the octocat as ASCII art

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.MetaApi(api_client)
    s = 's_example' # str | The words to show in Octocat's speech bubble (optional)

    try:
        # Get Octocat
        api_response = api_instance.meta_get_octocat(s=s)
        print("The response of MetaApi->meta_get_octocat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaApi->meta_get_octocat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s** | **str**| The words to show in Octocat&#39;s speech bubble | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octocat-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meta_get_zen**
> str meta_get_zen()

Get the Zen of GitHub

Get a random sentence from the Zen of GitHub

### Example


```python
import github_openapi
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.MetaApi(api_client)

    try:
        # Get the Zen of GitHub
        api_response = api_instance.meta_get_zen()
        print("The response of MetaApi->meta_get_zen:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaApi->meta_get_zen: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **meta_root**
> Root meta_root()

GitHub API Root

Get Hypermedia links to resources accessible in GitHub's REST API

### Example


```python
import github_openapi
from github_openapi.models.root import Root
from github_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.github.com
# See configuration.py for a list of all supported configuration parameters.
configuration = github_openapi.Configuration(
    host = "https://api.github.com"
)


# Enter a context with an instance of the API client
with github_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = github_openapi.MetaApi(api_client)

    try:
        # GitHub API Root
        api_response = api_instance.meta_root()
        print("The response of MetaApi->meta_root:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaApi->meta_root: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Root**](Root.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

