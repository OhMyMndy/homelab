# github_openapi.GistsApi

All URIs are relative to *https://api.github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gists_check_is_starred**](GistsApi.md#gists_check_is_starred) | **GET** /gists/{gist_id}/star | Check if a gist is starred
[**gists_create**](GistsApi.md#gists_create) | **POST** /gists | Create a gist
[**gists_create_comment**](GistsApi.md#gists_create_comment) | **POST** /gists/{gist_id}/comments | Create a gist comment
[**gists_delete**](GistsApi.md#gists_delete) | **DELETE** /gists/{gist_id} | Delete a gist
[**gists_delete_comment**](GistsApi.md#gists_delete_comment) | **DELETE** /gists/{gist_id}/comments/{comment_id} | Delete a gist comment
[**gists_fork**](GistsApi.md#gists_fork) | **POST** /gists/{gist_id}/forks | Fork a gist
[**gists_get**](GistsApi.md#gists_get) | **GET** /gists/{gist_id} | Get a gist
[**gists_get_comment**](GistsApi.md#gists_get_comment) | **GET** /gists/{gist_id}/comments/{comment_id} | Get a gist comment
[**gists_get_revision**](GistsApi.md#gists_get_revision) | **GET** /gists/{gist_id}/{sha} | Get a gist revision
[**gists_list**](GistsApi.md#gists_list) | **GET** /gists | List gists for the authenticated user
[**gists_list_comments**](GistsApi.md#gists_list_comments) | **GET** /gists/{gist_id}/comments | List gist comments
[**gists_list_commits**](GistsApi.md#gists_list_commits) | **GET** /gists/{gist_id}/commits | List gist commits
[**gists_list_for_user**](GistsApi.md#gists_list_for_user) | **GET** /users/{username}/gists | List gists for a user
[**gists_list_forks**](GistsApi.md#gists_list_forks) | **GET** /gists/{gist_id}/forks | List gist forks
[**gists_list_public**](GistsApi.md#gists_list_public) | **GET** /gists/public | List public gists
[**gists_list_starred**](GistsApi.md#gists_list_starred) | **GET** /gists/starred | List starred gists
[**gists_star**](GistsApi.md#gists_star) | **PUT** /gists/{gist_id}/star | Star a gist
[**gists_unstar**](GistsApi.md#gists_unstar) | **DELETE** /gists/{gist_id}/star | Unstar a gist
[**gists_update**](GistsApi.md#gists_update) | **PATCH** /gists/{gist_id} | Update a gist
[**gists_update_comment**](GistsApi.md#gists_update_comment) | **PATCH** /gists/{gist_id}/comments/{comment_id} | Update a gist comment


# **gists_check_is_starred**
> gists_check_is_starred(gist_id)

Check if a gist is starred



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
    api_instance = github_openapi.GistsApi(api_client)
    gist_id = 'gist_id_example' # str | The unique identifier of the gist.

    try:
        # Check if a gist is starred
        api_instance.gists_check_is_starred(gist_id)
    except Exception as e:
        print("Exception when calling GistsApi->gists_check_is_starred: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gist_id** | **str**| The unique identifier of the gist. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response if gist is starred |  -  |
**404** | Not Found if gist is not starred |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_create**
> GistSimple gists_create(gists_create_request)

Create a gist

Allows you to add a new gist with one or more files.  > [!NOTE] > Don't name your files \"gistfile\" with a numerical suffix. This is the format of the automatic naming scheme that Gist uses internally.

### Example


```python
import github_openapi
from github_openapi.models.gist_simple import GistSimple
from github_openapi.models.gists_create_request import GistsCreateRequest
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
    api_instance = github_openapi.GistsApi(api_client)
    gists_create_request = {"description":"Example of a gist","public":false,"files":{"README.md":{"content":"Hello World"}}} # GistsCreateRequest | 

    try:
        # Create a gist
        api_response = api_instance.gists_create(gists_create_request)
        print("The response of GistsApi->gists_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GistsApi->gists_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gists_create_request** | [**GistsCreateRequest**](GistsCreateRequest.md)|  | 

### Return type

[**GistSimple**](GistSimple.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  * Location -  <br>  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**304** | Not modified |  -  |
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_create_comment**
> GistComment gists_create_comment(gist_id, gists_create_comment_request)

Create a gist comment

Creates a comment on a gist.  This endpoint supports the following custom media types. For more information, see \"[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types).\"  - **`application/vnd.github.raw+json`**: Returns the raw markdown. This is the default if you do not pass any specific media type. - **`application/vnd.github.base64+json`**: Returns the base64-encoded contents. This can be useful if your gist contains any invalid UTF-8 sequences.

### Example


```python
import github_openapi
from github_openapi.models.gist_comment import GistComment
from github_openapi.models.gists_create_comment_request import GistsCreateCommentRequest
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
    api_instance = github_openapi.GistsApi(api_client)
    gist_id = 'gist_id_example' # str | The unique identifier of the gist.
    gists_create_comment_request = {"body":"This is a comment to a gist"} # GistsCreateCommentRequest | 

    try:
        # Create a gist comment
        api_response = api_instance.gists_create_comment(gist_id, gists_create_comment_request)
        print("The response of GistsApi->gists_create_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GistsApi->gists_create_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gist_id** | **str**| The unique identifier of the gist. | 
 **gists_create_comment_request** | [**GistsCreateCommentRequest**](GistsCreateCommentRequest.md)|  | 

### Return type

[**GistComment**](GistComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  * Location -  <br>  |
**304** | Not modified |  -  |
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_delete**
> gists_delete(gist_id)

Delete a gist



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
    api_instance = github_openapi.GistsApi(api_client)
    gist_id = 'gist_id_example' # str | The unique identifier of the gist.

    try:
        # Delete a gist
        api_instance.gists_delete(gist_id)
    except Exception as e:
        print("Exception when calling GistsApi->gists_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gist_id** | **str**| The unique identifier of the gist. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |
**404** | Resource not found |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_delete_comment**
> gists_delete_comment(gist_id, comment_id)

Delete a gist comment



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
    api_instance = github_openapi.GistsApi(api_client)
    gist_id = 'gist_id_example' # str | The unique identifier of the gist.
    comment_id = 56 # int | The unique identifier of the comment.

    try:
        # Delete a gist comment
        api_instance.gists_delete_comment(gist_id, comment_id)
    except Exception as e:
        print("Exception when calling GistsApi->gists_delete_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gist_id** | **str**| The unique identifier of the gist. | 
 **comment_id** | **int**| The unique identifier of the comment. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |
**304** | Not modified |  -  |
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_fork**
> BaseGist gists_fork(gist_id)

Fork a gist



### Example


```python
import github_openapi
from github_openapi.models.base_gist import BaseGist
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
    api_instance = github_openapi.GistsApi(api_client)
    gist_id = 'gist_id_example' # str | The unique identifier of the gist.

    try:
        # Fork a gist
        api_response = api_instance.gists_fork(gist_id)
        print("The response of GistsApi->gists_fork:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GistsApi->gists_fork: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gist_id** | **str**| The unique identifier of the gist. | 

### Return type

[**BaseGist**](BaseGist.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  * Location -  <br>  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_get**
> GistSimple gists_get(gist_id)

Get a gist

Gets a specified gist.  This endpoint supports the following custom media types. For more information, see \"[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types).\"  - **`application/vnd.github.raw+json`**: Returns the raw markdown. This is the default if you do not pass any specific media type. - **`application/vnd.github.base64+json`**: Returns the base64-encoded contents. This can be useful if your gist contains any invalid UTF-8 sequences.

### Example


```python
import github_openapi
from github_openapi.models.gist_simple import GistSimple
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
    api_instance = github_openapi.GistsApi(api_client)
    gist_id = 'gist_id_example' # str | The unique identifier of the gist.

    try:
        # Get a gist
        api_response = api_instance.gists_get(gist_id)
        print("The response of GistsApi->gists_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GistsApi->gists_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gist_id** | **str**| The unique identifier of the gist. | 

### Return type

[**GistSimple**](GistSimple.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**403** | Forbidden Gist |  -  |
**404** | Resource not found |  -  |
**304** | Not modified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_get_comment**
> GistComment gists_get_comment(gist_id, comment_id)

Get a gist comment

Gets a comment on a gist.  This endpoint supports the following custom media types. For more information, see \"[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types).\"  - **`application/vnd.github.raw+json`**: Returns the raw markdown. This is the default if you do not pass any specific media type. - **`application/vnd.github.base64+json`**: Returns the base64-encoded contents. This can be useful if your gist contains any invalid UTF-8 sequences.

### Example


```python
import github_openapi
from github_openapi.models.gist_comment import GistComment
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
    api_instance = github_openapi.GistsApi(api_client)
    gist_id = 'gist_id_example' # str | The unique identifier of the gist.
    comment_id = 56 # int | The unique identifier of the comment.

    try:
        # Get a gist comment
        api_response = api_instance.gists_get_comment(gist_id, comment_id)
        print("The response of GistsApi->gists_get_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GistsApi->gists_get_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gist_id** | **str**| The unique identifier of the gist. | 
 **comment_id** | **int**| The unique identifier of the comment. | 

### Return type

[**GistComment**](GistComment.md)

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
**404** | Resource not found |  -  |
**403** | Forbidden Gist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_get_revision**
> GistSimple gists_get_revision(gist_id, sha)

Get a gist revision

Gets a specified gist revision.  This endpoint supports the following custom media types. For more information, see \"[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types).\"  - **`application/vnd.github.raw+json`**: Returns the raw markdown. This is the default if you do not pass any specific media type. - **`application/vnd.github.base64+json`**: Returns the base64-encoded contents. This can be useful if your gist contains any invalid UTF-8 sequences.

### Example


```python
import github_openapi
from github_openapi.models.gist_simple import GistSimple
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
    api_instance = github_openapi.GistsApi(api_client)
    gist_id = 'gist_id_example' # str | The unique identifier of the gist.
    sha = 'sha_example' # str | 

    try:
        # Get a gist revision
        api_response = api_instance.gists_get_revision(gist_id, sha)
        print("The response of GistsApi->gists_get_revision:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GistsApi->gists_get_revision: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gist_id** | **str**| The unique identifier of the gist. | 
 **sha** | **str**|  | 

### Return type

[**GistSimple**](GistSimple.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_list**
> List[BaseGist] gists_list(since=since, per_page=per_page, page=page)

List gists for the authenticated user

Lists the authenticated user's gists or if called anonymously, this endpoint returns all public gists:

### Example


```python
import github_openapi
from github_openapi.models.base_gist import BaseGist
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
    api_instance = github_openapi.GistsApi(api_client)
    since = '2013-10-20T19:20:30+01:00' # datetime | Only show results that were last updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. (optional)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List gists for the authenticated user
        api_response = api_instance.gists_list(since=since, per_page=per_page, page=page)
        print("The response of GistsApi->gists_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GistsApi->gists_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **datetime**| Only show results that were last updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[BaseGist]**](BaseGist.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_list_comments**
> List[GistComment] gists_list_comments(gist_id, per_page=per_page, page=page)

List gist comments

Lists the comments on a gist.  This endpoint supports the following custom media types. For more information, see \"[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types).\"  - **`application/vnd.github.raw+json`**: Returns the raw markdown. This is the default if you do not pass any specific media type. - **`application/vnd.github.base64+json`**: Returns the base64-encoded contents. This can be useful if your gist contains any invalid UTF-8 sequences.

### Example


```python
import github_openapi
from github_openapi.models.gist_comment import GistComment
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
    api_instance = github_openapi.GistsApi(api_client)
    gist_id = 'gist_id_example' # str | The unique identifier of the gist.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List gist comments
        api_response = api_instance.gists_list_comments(gist_id, per_page=per_page, page=page)
        print("The response of GistsApi->gists_list_comments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GistsApi->gists_list_comments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gist_id** | **str**| The unique identifier of the gist. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[GistComment]**](GistComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |
**304** | Not modified |  -  |
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_list_commits**
> List[GistCommit] gists_list_commits(gist_id, per_page=per_page, page=page)

List gist commits



### Example


```python
import github_openapi
from github_openapi.models.gist_commit import GistCommit
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
    api_instance = github_openapi.GistsApi(api_client)
    gist_id = 'gist_id_example' # str | The unique identifier of the gist.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List gist commits
        api_response = api_instance.gists_list_commits(gist_id, per_page=per_page, page=page)
        print("The response of GistsApi->gists_list_commits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GistsApi->gists_list_commits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gist_id** | **str**| The unique identifier of the gist. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[GistCommit]**](GistCommit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |
**404** | Resource not found |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_list_for_user**
> List[BaseGist] gists_list_for_user(username, since=since, per_page=per_page, page=page)

List gists for a user

Lists public gists for the specified user:

### Example


```python
import github_openapi
from github_openapi.models.base_gist import BaseGist
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
    api_instance = github_openapi.GistsApi(api_client)
    username = 'username_example' # str | The handle for the GitHub user account.
    since = '2013-10-20T19:20:30+01:00' # datetime | Only show results that were last updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. (optional)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List gists for a user
        api_response = api_instance.gists_list_for_user(username, since=since, per_page=per_page, page=page)
        print("The response of GistsApi->gists_list_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GistsApi->gists_list_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The handle for the GitHub user account. | 
 **since** | **datetime**| Only show results that were last updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[BaseGist]**](BaseGist.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_list_forks**
> List[GistSimple] gists_list_forks(gist_id, per_page=per_page, page=page)

List gist forks



### Example


```python
import github_openapi
from github_openapi.models.gist_simple import GistSimple
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
    api_instance = github_openapi.GistsApi(api_client)
    gist_id = 'gist_id_example' # str | The unique identifier of the gist.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List gist forks
        api_response = api_instance.gists_list_forks(gist_id, per_page=per_page, page=page)
        print("The response of GistsApi->gists_list_forks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GistsApi->gists_list_forks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gist_id** | **str**| The unique identifier of the gist. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[GistSimple]**](GistSimple.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |
**404** | Resource not found |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_list_public**
> List[BaseGist] gists_list_public(since=since, per_page=per_page, page=page)

List public gists

List public gists sorted by most recently updated to least recently updated.  Note: With [pagination](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api), you can fetch up to 3000 gists. For example, you can fetch 100 pages with 30 gists per page or 30 pages with 100 gists per page.

### Example


```python
import github_openapi
from github_openapi.models.base_gist import BaseGist
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
    api_instance = github_openapi.GistsApi(api_client)
    since = '2013-10-20T19:20:30+01:00' # datetime | Only show results that were last updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. (optional)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List public gists
        api_response = api_instance.gists_list_public(since=since, per_page=per_page, page=page)
        print("The response of GistsApi->gists_list_public:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GistsApi->gists_list_public: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **datetime**| Only show results that were last updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[BaseGist]**](BaseGist.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_list_starred**
> List[BaseGist] gists_list_starred(since=since, per_page=per_page, page=page)

List starred gists

List the authenticated user's starred gists:

### Example


```python
import github_openapi
from github_openapi.models.base_gist import BaseGist
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
    api_instance = github_openapi.GistsApi(api_client)
    since = '2013-10-20T19:20:30+01:00' # datetime | Only show results that were last updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. (optional)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List starred gists
        api_response = api_instance.gists_list_starred(since=since, per_page=per_page, page=page)
        print("The response of GistsApi->gists_list_starred:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GistsApi->gists_list_starred: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **datetime**| Only show results that were last updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[BaseGist]**](BaseGist.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |
**401** | Requires authentication |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_star**
> gists_star(gist_id)

Star a gist

Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see \"[HTTP method](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#http-method).\"

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
    api_instance = github_openapi.GistsApi(api_client)
    gist_id = 'gist_id_example' # str | The unique identifier of the gist.

    try:
        # Star a gist
        api_instance.gists_star(gist_id)
    except Exception as e:
        print("Exception when calling GistsApi->gists_star: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gist_id** | **str**| The unique identifier of the gist. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |
**404** | Resource not found |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_unstar**
> gists_unstar(gist_id)

Unstar a gist



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
    api_instance = github_openapi.GistsApi(api_client)
    gist_id = 'gist_id_example' # str | The unique identifier of the gist.

    try:
        # Unstar a gist
        api_instance.gists_unstar(gist_id)
    except Exception as e:
        print("Exception when calling GistsApi->gists_unstar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gist_id** | **str**| The unique identifier of the gist. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |
**304** | Not modified |  -  |
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_update**
> GistSimple gists_update(gist_id, gists_update_request)

Update a gist

Allows you to update a gist's description and to update, delete, or rename gist files. Files from the previous version of the gist that aren't explicitly changed during an edit are unchanged.  At least one of `description` or `files` is required.  This endpoint supports the following custom media types. For more information, see \"[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types).\"  - **`application/vnd.github.raw+json`**: Returns the raw markdown. This is the default if you do not pass any specific media type. - **`application/vnd.github.base64+json`**: Returns the base64-encoded contents. This can be useful if your gist contains any invalid UTF-8 sequences.

### Example


```python
import github_openapi
from github_openapi.models.gist_simple import GistSimple
from github_openapi.models.gists_update_request import GistsUpdateRequest
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
    api_instance = github_openapi.GistsApi(api_client)
    gist_id = 'gist_id_example' # str | The unique identifier of the gist.
    gists_update_request = {"description":"An updated gist description","files":{"README.md":{"content":"Hello World from GitHub"}}} # GistsUpdateRequest | 

    try:
        # Update a gist
        api_response = api_instance.gists_update(gist_id, gists_update_request)
        print("The response of GistsApi->gists_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GistsApi->gists_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gist_id** | **str**| The unique identifier of the gist. | 
 **gists_update_request** | [**GistsUpdateRequest**](GistsUpdateRequest.md)|  | 

### Return type

[**GistSimple**](GistSimple.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gists_update_comment**
> GistComment gists_update_comment(gist_id, comment_id, gists_create_comment_request)

Update a gist comment

Updates a comment on a gist.  This endpoint supports the following custom media types. For more information, see \"[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types).\"  - **`application/vnd.github.raw+json`**: Returns the raw markdown. This is the default if you do not pass any specific media type. - **`application/vnd.github.base64+json`**: Returns the base64-encoded contents. This can be useful if your gist contains any invalid UTF-8 sequences.

### Example


```python
import github_openapi
from github_openapi.models.gist_comment import GistComment
from github_openapi.models.gists_create_comment_request import GistsCreateCommentRequest
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
    api_instance = github_openapi.GistsApi(api_client)
    gist_id = 'gist_id_example' # str | The unique identifier of the gist.
    comment_id = 56 # int | The unique identifier of the comment.
    gists_create_comment_request = {"body":"This is an update to a comment in a gist"} # GistsCreateCommentRequest | 

    try:
        # Update a gist comment
        api_response = api_instance.gists_update_comment(gist_id, comment_id, gists_create_comment_request)
        print("The response of GistsApi->gists_update_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GistsApi->gists_update_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gist_id** | **str**| The unique identifier of the gist. | 
 **comment_id** | **int**| The unique identifier of the comment. | 
 **gists_create_comment_request** | [**GistsCreateCommentRequest**](GistsCreateCommentRequest.md)|  | 

### Return type

[**GistComment**](GistComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

