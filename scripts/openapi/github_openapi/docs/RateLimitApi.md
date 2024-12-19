# github_openapi.RateLimitApi

All URIs are relative to *https://api.github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rate_limit_get**](RateLimitApi.md#rate_limit_get) | **GET** /rate_limit | Get rate limit status for the authenticated user


# **rate_limit_get**
> RateLimitOverview rate_limit_get()

Get rate limit status for the authenticated user

> [!NOTE] > Accessing this endpoint does not count against your REST API rate limit.  Some categories of endpoints have custom rate limits that are separate from the rate limit governing the other REST API endpoints. For this reason, the API response categorizes your rate limit. Under `resources`, you'll see objects relating to different categories: * The `core` object provides your rate limit status for all non-search-related resources in the REST API. * The `search` object provides your rate limit status for the REST API for searching (excluding code searches). For more information, see \"[Search](https://docs.github.com/rest/search/search).\" * The `code_search` object provides your rate limit status for the REST API for searching code. For more information, see \"[Search code](https://docs.github.com/rest/search/search#search-code).\" * The `graphql` object provides your rate limit status for the GraphQL API. For more information, see \"[Resource limitations](https://docs.github.com/graphql/overview/resource-limitations#rate-limit).\" * The `integration_manifest` object provides your rate limit status for the `POST /app-manifests/{code}/conversions` operation. For more information, see \"[Creating a GitHub App from a manifest](https://docs.github.com/apps/creating-github-apps/setting-up-a-github-app/creating-a-github-app-from-a-manifest#3-you-exchange-the-temporary-code-to-retrieve-the-app-configuration).\" * The `dependency_snapshots` object provides your rate limit status for submitting snapshots to the dependency graph. For more information, see \"[Dependency graph](https://docs.github.com/rest/dependency-graph).\" * The `code_scanning_upload` object provides your rate limit status for uploading SARIF results to code scanning. For more information, see \"[Uploading a SARIF file to GitHub](https://docs.github.com/code-security/code-scanning/integrating-with-code-scanning/uploading-a-sarif-file-to-github).\" * The `actions_runner_registration` object provides your rate limit status for registering self-hosted runners in GitHub Actions. For more information, see \"[Self-hosted runners](https://docs.github.com/rest/actions/self-hosted-runners).\" * The `source_import` object is no longer in use for any API endpoints, and it will be removed in the next API version. For more information about API versions, see \"[API Versions](https://docs.github.com/rest/about-the-rest-api/api-versions).\"  > [!NOTE] > The `rate` object is closing down. If you're writing new API client code or updating existing code, you should use the `core` object instead of the `rate` object. The `core` object contains the same information that is present in the `rate` object.

### Example


```python
import github_openapi
from github_openapi.models.rate_limit_overview import RateLimitOverview
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
    api_instance = github_openapi.RateLimitApi(api_client)

    try:
        # Get rate limit status for the authenticated user
        api_response = api_instance.rate_limit_get()
        print("The response of RateLimitApi->rate_limit_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RateLimitApi->rate_limit_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RateLimitOverview**](RateLimitOverview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**304** | Not modified |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

