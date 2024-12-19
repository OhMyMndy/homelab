# github_openapi.MarkdownApi

All URIs are relative to *https://api.github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**markdown_render**](MarkdownApi.md#markdown_render) | **POST** /markdown | Render a Markdown document
[**markdown_render_raw**](MarkdownApi.md#markdown_render_raw) | **POST** /markdown/raw | Render a Markdown document in raw mode


# **markdown_render**
> str markdown_render(markdown_render_request)

Render a Markdown document



### Example


```python
import github_openapi
from github_openapi.models.markdown_render_request import MarkdownRenderRequest
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
    api_instance = github_openapi.MarkdownApi(api_client)
    markdown_render_request = {"text":"Hello **world**"} # MarkdownRenderRequest | 

    try:
        # Render a Markdown document
        api_response = api_instance.markdown_render(markdown_render_request)
        print("The response of MarkdownApi->markdown_render:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarkdownApi->markdown_render: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **markdown_render_request** | [**MarkdownRenderRequest**](MarkdownRenderRequest.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Content-Type -  <br>  * Content-Length -  <br>  * X-CommonMarker-Version -  <br>  |
**304** | Not modified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **markdown_render_raw**
> str markdown_render_raw(body=body)

Render a Markdown document in raw mode

You must send Markdown as plain text (using a `Content-Type` header of `text/plain` or `text/x-markdown`) to this endpoint, rather than using JSON format. In raw mode, [GitHub Flavored Markdown](https://github.github.com/gfm/) is not supported and Markdown will be rendered in plain format like a README.md file. Markdown content must be 400 KB or less.

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
    api_instance = github_openapi.MarkdownApi(api_client)
    body = {"text":"Hello **world**"} # str |  (optional)

    try:
        # Render a Markdown document in raw mode
        api_response = api_instance.markdown_render_raw(body=body)
        print("The response of MarkdownApi->markdown_render_raw:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MarkdownApi->markdown_render_raw: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain, text/x-markdown
 - **Accept**: text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * X-CommonMarker-Version -  <br>  |
**304** | Not modified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

