# github_openapi.ChecksApi

All URIs are relative to *https://api.github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checks_create**](ChecksApi.md#checks_create) | **POST** /repos/{owner}/{repo}/check-runs | Create a check run
[**checks_create_suite**](ChecksApi.md#checks_create_suite) | **POST** /repos/{owner}/{repo}/check-suites | Create a check suite
[**checks_get**](ChecksApi.md#checks_get) | **GET** /repos/{owner}/{repo}/check-runs/{check_run_id} | Get a check run
[**checks_get_suite**](ChecksApi.md#checks_get_suite) | **GET** /repos/{owner}/{repo}/check-suites/{check_suite_id} | Get a check suite
[**checks_list_annotations**](ChecksApi.md#checks_list_annotations) | **GET** /repos/{owner}/{repo}/check-runs/{check_run_id}/annotations | List check run annotations
[**checks_list_for_ref**](ChecksApi.md#checks_list_for_ref) | **GET** /repos/{owner}/{repo}/commits/{ref}/check-runs | List check runs for a Git reference
[**checks_list_for_suite**](ChecksApi.md#checks_list_for_suite) | **GET** /repos/{owner}/{repo}/check-suites/{check_suite_id}/check-runs | List check runs in a check suite
[**checks_list_suites_for_ref**](ChecksApi.md#checks_list_suites_for_ref) | **GET** /repos/{owner}/{repo}/commits/{ref}/check-suites | List check suites for a Git reference
[**checks_rerequest_run**](ChecksApi.md#checks_rerequest_run) | **POST** /repos/{owner}/{repo}/check-runs/{check_run_id}/rerequest | Rerequest a check run
[**checks_rerequest_suite**](ChecksApi.md#checks_rerequest_suite) | **POST** /repos/{owner}/{repo}/check-suites/{check_suite_id}/rerequest | Rerequest a check suite
[**checks_set_suites_preferences**](ChecksApi.md#checks_set_suites_preferences) | **PATCH** /repos/{owner}/{repo}/check-suites/preferences | Update repository preferences for check suites
[**checks_update**](ChecksApi.md#checks_update) | **PATCH** /repos/{owner}/{repo}/check-runs/{check_run_id} | Update a check run


# **checks_create**
> CheckRun checks_create(owner, repo, checks_create_request)

Create a check run

Creates a new check run for a specific commit in a repository.  To create a check run, you must use a GitHub App. OAuth apps and authenticated users are not able to create a check suite.  In a check suite, GitHub limits the number of check runs with the same name to 1000. Once these check runs exceed 1000, GitHub will start to automatically delete older check runs.  > [!NOTE] > The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array.

### Example


```python
import github_openapi
from github_openapi.models.check_run import CheckRun
from github_openapi.models.checks_create_request import ChecksCreateRequest
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
    api_instance = github_openapi.ChecksApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    checks_create_request = {"name":"mighty_readme","head_sha":"ce587453ced02b1526dfb4cb910479d431683101","status":"in_progress","external_id":"42","started_at":"2018-05-04T01:14:52Z","output":{"title":"Mighty Readme report","summary":"","text":""}} # ChecksCreateRequest | 

    try:
        # Create a check run
        api_response = api_instance.checks_create(owner, repo, checks_create_request)
        print("The response of ChecksApi->checks_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChecksApi->checks_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **checks_create_request** | [**ChecksCreateRequest**](ChecksCreateRequest.md)|  | 

### Return type

[**CheckRun**](CheckRun.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checks_create_suite**
> CheckSuite checks_create_suite(owner, repo, checks_create_suite_request)

Create a check suite

Creates a check suite manually. By default, check suites are automatically created when you create a [check run](https://docs.github.com/rest/checks/runs). You only need to use this endpoint for manually creating check suites when you've disabled automatic creation using \"[Update repository preferences for check suites](https://docs.github.com/rest/checks/suites#update-repository-preferences-for-check-suites)\".  > [!NOTE] > The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array and a `null` value for `head_branch`.  OAuth apps and personal access tokens (classic) cannot use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.check_suite import CheckSuite
from github_openapi.models.checks_create_suite_request import ChecksCreateSuiteRequest
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
    api_instance = github_openapi.ChecksApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    checks_create_suite_request = {"head_sha":"d6fde92930d4715a2b49857d24b940956b26d2d3"} # ChecksCreateSuiteRequest | 

    try:
        # Create a check suite
        api_response = api_instance.checks_create_suite(owner, repo, checks_create_suite_request)
        print("The response of ChecksApi->checks_create_suite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChecksApi->checks_create_suite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **checks_create_suite_request** | [**ChecksCreateSuiteRequest**](ChecksCreateSuiteRequest.md)|  | 

### Return type

[**CheckSuite**](CheckSuite.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response when the suite already exists |  -  |
**201** | Response when the suite was created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checks_get**
> CheckRun checks_get(owner, repo, check_run_id)

Get a check run

Gets a single check run using its `id`.  > [!NOTE] > The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint on a private repository.

### Example


```python
import github_openapi
from github_openapi.models.check_run import CheckRun
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
    api_instance = github_openapi.ChecksApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    check_run_id = 56 # int | The unique identifier of the check run.

    try:
        # Get a check run
        api_response = api_instance.checks_get(owner, repo, check_run_id)
        print("The response of ChecksApi->checks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChecksApi->checks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **check_run_id** | **int**| The unique identifier of the check run. | 

### Return type

[**CheckRun**](CheckRun.md)

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

# **checks_get_suite**
> CheckSuite checks_get_suite(owner, repo, check_suite_id)

Get a check suite

Gets a single check suite using its `id`.  > [!NOTE] > The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array and a `null` value for `head_branch`.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint on a private repository.

### Example


```python
import github_openapi
from github_openapi.models.check_suite import CheckSuite
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
    api_instance = github_openapi.ChecksApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    check_suite_id = 56 # int | The unique identifier of the check suite.

    try:
        # Get a check suite
        api_response = api_instance.checks_get_suite(owner, repo, check_suite_id)
        print("The response of ChecksApi->checks_get_suite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChecksApi->checks_get_suite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **check_suite_id** | **int**| The unique identifier of the check suite. | 

### Return type

[**CheckSuite**](CheckSuite.md)

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

# **checks_list_annotations**
> List[CheckAnnotation] checks_list_annotations(owner, repo, check_run_id, per_page=per_page, page=page)

List check run annotations

Lists annotations for a check run using the annotation `id`.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint on a private repository.

### Example


```python
import github_openapi
from github_openapi.models.check_annotation import CheckAnnotation
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
    api_instance = github_openapi.ChecksApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    check_run_id = 56 # int | The unique identifier of the check run.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List check run annotations
        api_response = api_instance.checks_list_annotations(owner, repo, check_run_id, per_page=per_page, page=page)
        print("The response of ChecksApi->checks_list_annotations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChecksApi->checks_list_annotations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **check_run_id** | **int**| The unique identifier of the check run. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[CheckAnnotation]**](CheckAnnotation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checks_list_for_ref**
> ChecksListForSuite200Response checks_list_for_ref(owner, repo, ref, check_name=check_name, status=status, filter=filter, per_page=per_page, page=page, app_id=app_id)

List check runs for a Git reference

Lists check runs for a commit ref. The `ref` can be a SHA, branch name, or a tag name.  > [!NOTE] > The endpoints to manage checks only look for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array.  If there are more than 1000 check suites on a single git reference, this endpoint will limit check runs to the 1000 most recent check suites. To iterate over all possible check runs, use the [List check suites for a Git reference](https://docs.github.com/rest/reference/checks#list-check-suites-for-a-git-reference) endpoint and provide the `check_suite_id` parameter to the [List check runs in a check suite](https://docs.github.com/rest/reference/checks#list-check-runs-in-a-check-suite) endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint on a private repository.

### Example


```python
import github_openapi
from github_openapi.models.checks_list_for_suite200_response import ChecksListForSuite200Response
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
    api_instance = github_openapi.ChecksApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    ref = 'ref_example' # str | The commit reference. Can be a commit SHA, branch name (`heads/BRANCH_NAME`), or tag name (`tags/TAG_NAME`). For more information, see \"[Git References](https://git-scm.com/book/en/v2/Git-Internals-Git-References)\" in the Git documentation.
    check_name = 'check_name_example' # str | Returns check runs with the specified `name`. (optional)
    status = 'status_example' # str | Returns check runs with the specified `status`. (optional)
    filter = latest # str | Filters check runs by their `completed_at` timestamp. `latest` returns the most recent check runs. (optional) (default to latest)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    app_id = 56 # int |  (optional)

    try:
        # List check runs for a Git reference
        api_response = api_instance.checks_list_for_ref(owner, repo, ref, check_name=check_name, status=status, filter=filter, per_page=per_page, page=page, app_id=app_id)
        print("The response of ChecksApi->checks_list_for_ref:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChecksApi->checks_list_for_ref: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **ref** | **str**| The commit reference. Can be a commit SHA, branch name (&#x60;heads/BRANCH_NAME&#x60;), or tag name (&#x60;tags/TAG_NAME&#x60;). For more information, see \&quot;[Git References](https://git-scm.com/book/en/v2/Git-Internals-Git-References)\&quot; in the Git documentation. | 
 **check_name** | **str**| Returns check runs with the specified &#x60;name&#x60;. | [optional] 
 **status** | **str**| Returns check runs with the specified &#x60;status&#x60;. | [optional] 
 **filter** | **str**| Filters check runs by their &#x60;completed_at&#x60; timestamp. &#x60;latest&#x60; returns the most recent check runs. | [optional] [default to latest]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **app_id** | **int**|  | [optional] 

### Return type

[**ChecksListForSuite200Response**](ChecksListForSuite200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checks_list_for_suite**
> ChecksListForSuite200Response checks_list_for_suite(owner, repo, check_suite_id, check_name=check_name, status=status, filter=filter, per_page=per_page, page=page)

List check runs in a check suite

Lists check runs for a check suite using its `id`.  > [!NOTE] > The endpoints to manage checks only look for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint on a private repository.

### Example


```python
import github_openapi
from github_openapi.models.checks_list_for_suite200_response import ChecksListForSuite200Response
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
    api_instance = github_openapi.ChecksApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    check_suite_id = 56 # int | The unique identifier of the check suite.
    check_name = 'check_name_example' # str | Returns check runs with the specified `name`. (optional)
    status = 'status_example' # str | Returns check runs with the specified `status`. (optional)
    filter = latest # str | Filters check runs by their `completed_at` timestamp. `latest` returns the most recent check runs. (optional) (default to latest)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List check runs in a check suite
        api_response = api_instance.checks_list_for_suite(owner, repo, check_suite_id, check_name=check_name, status=status, filter=filter, per_page=per_page, page=page)
        print("The response of ChecksApi->checks_list_for_suite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChecksApi->checks_list_for_suite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **check_suite_id** | **int**| The unique identifier of the check suite. | 
 **check_name** | **str**| Returns check runs with the specified &#x60;name&#x60;. | [optional] 
 **status** | **str**| Returns check runs with the specified &#x60;status&#x60;. | [optional] 
 **filter** | **str**| Filters check runs by their &#x60;completed_at&#x60; timestamp. &#x60;latest&#x60; returns the most recent check runs. | [optional] [default to latest]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**ChecksListForSuite200Response**](ChecksListForSuite200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checks_list_suites_for_ref**
> ChecksListSuitesForRef200Response checks_list_suites_for_ref(owner, repo, ref, app_id=app_id, check_name=check_name, per_page=per_page, page=page)

List check suites for a Git reference

Lists check suites for a commit `ref`. The `ref` can be a SHA, branch name, or a tag name.  > [!NOTE] > The endpoints to manage checks only look for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array and a `null` value for `head_branch`.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint on a private repository.

### Example


```python
import github_openapi
from github_openapi.models.checks_list_suites_for_ref200_response import ChecksListSuitesForRef200Response
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
    api_instance = github_openapi.ChecksApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    ref = 'ref_example' # str | The commit reference. Can be a commit SHA, branch name (`heads/BRANCH_NAME`), or tag name (`tags/TAG_NAME`). For more information, see \"[Git References](https://git-scm.com/book/en/v2/Git-Internals-Git-References)\" in the Git documentation.
    app_id = 1 # int | Filters check suites by GitHub App `id`. (optional)
    check_name = 'check_name_example' # str | Returns check runs with the specified `name`. (optional)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List check suites for a Git reference
        api_response = api_instance.checks_list_suites_for_ref(owner, repo, ref, app_id=app_id, check_name=check_name, per_page=per_page, page=page)
        print("The response of ChecksApi->checks_list_suites_for_ref:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChecksApi->checks_list_suites_for_ref: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **ref** | **str**| The commit reference. Can be a commit SHA, branch name (&#x60;heads/BRANCH_NAME&#x60;), or tag name (&#x60;tags/TAG_NAME&#x60;). For more information, see \&quot;[Git References](https://git-scm.com/book/en/v2/Git-Internals-Git-References)\&quot; in the Git documentation. | 
 **app_id** | **int**| Filters check suites by GitHub App &#x60;id&#x60;. | [optional] 
 **check_name** | **str**| Returns check runs with the specified &#x60;name&#x60;. | [optional] 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**ChecksListSuitesForRef200Response**](ChecksListSuitesForRef200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checks_rerequest_run**
> object checks_rerequest_run(owner, repo, check_run_id)

Rerequest a check run

Triggers GitHub to rerequest an existing check run, without pushing new code to a repository. This endpoint will trigger the [`check_run` webhook](https://docs.github.com/webhooks/event-payloads/#check_run) event with the action `rerequested`. When a check run is `rerequested`, its `status` is reset to `queued` and the `conclusion` is cleared.  For more information about how to re-run GitHub Actions jobs, see \"[Re-run a job from a workflow run](https://docs.github.com/rest/actions/workflow-runs#re-run-a-job-from-a-workflow-run)\".  OAuth apps and personal access tokens (classic) cannot use this endpoint.

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
    api_instance = github_openapi.ChecksApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    check_run_id = 56 # int | The unique identifier of the check run.

    try:
        # Rerequest a check run
        api_response = api_instance.checks_rerequest_run(owner, repo, check_run_id)
        print("The response of ChecksApi->checks_rerequest_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChecksApi->checks_rerequest_run: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **check_run_id** | **int**| The unique identifier of the check run. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |
**403** | Forbidden if the check run is not rerequestable or doesn&#39;t belong to the authenticated GitHub App |  -  |
**422** | Validation error if the check run is not rerequestable |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checks_rerequest_suite**
> object checks_rerequest_suite(owner, repo, check_suite_id)

Rerequest a check suite

Triggers GitHub to rerequest an existing check suite, without pushing new code to a repository. This endpoint will trigger the [`check_suite` webhook](https://docs.github.com/webhooks/event-payloads/#check_suite) event with the action `rerequested`. When a check suite is `rerequested`, its `status` is reset to `queued` and the `conclusion` is cleared.  OAuth apps and personal access tokens (classic) cannot use this endpoint.

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
    api_instance = github_openapi.ChecksApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    check_suite_id = 56 # int | The unique identifier of the check suite.

    try:
        # Rerequest a check suite
        api_response = api_instance.checks_rerequest_suite(owner, repo, check_suite_id)
        print("The response of ChecksApi->checks_rerequest_suite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChecksApi->checks_rerequest_suite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **check_suite_id** | **int**| The unique identifier of the check suite. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checks_set_suites_preferences**
> CheckSuitePreference checks_set_suites_preferences(owner, repo, checks_set_suites_preferences_request)

Update repository preferences for check suites

Changes the default automatic flow when creating check suites. By default, a check suite is automatically created each time code is pushed to a repository. When you disable the automatic creation of check suites, you can manually [Create a check suite](https://docs.github.com/rest/checks/suites#create-a-check-suite). You must have admin permissions in the repository to set preferences for check suites.

### Example


```python
import github_openapi
from github_openapi.models.check_suite_preference import CheckSuitePreference
from github_openapi.models.checks_set_suites_preferences_request import ChecksSetSuitesPreferencesRequest
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
    api_instance = github_openapi.ChecksApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    checks_set_suites_preferences_request = {"auto_trigger_checks":[{"app_id":4,"setting":false}]} # ChecksSetSuitesPreferencesRequest | 

    try:
        # Update repository preferences for check suites
        api_response = api_instance.checks_set_suites_preferences(owner, repo, checks_set_suites_preferences_request)
        print("The response of ChecksApi->checks_set_suites_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChecksApi->checks_set_suites_preferences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **checks_set_suites_preferences_request** | [**ChecksSetSuitesPreferencesRequest**](ChecksSetSuitesPreferencesRequest.md)|  | 

### Return type

[**CheckSuitePreference**](CheckSuitePreference.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checks_update**
> CheckRun checks_update(owner, repo, check_run_id, checks_update_request)

Update a check run

Updates a check run for a specific commit in a repository.  > [!NOTE] > The endpoints to manage checks only look for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array.  OAuth apps and personal access tokens (classic) cannot use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.check_run import CheckRun
from github_openapi.models.checks_update_request import ChecksUpdateRequest
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
    api_instance = github_openapi.ChecksApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    check_run_id = 56 # int | The unique identifier of the check run.
    checks_update_request = {"name":"mighty_readme","started_at":"2018-05-04T01:14:52Z","status":"completed","conclusion":"success","completed_at":"2018-05-04T01:14:52Z","output":{"title":"Mighty Readme report","summary":"There are 0 failures, 2 warnings, and 1 notices.","text":"You may have some misspelled words on lines 2 and 4. You also may want to add a section in your README about how to install your app.","annotations":[{"path":"README.md","annotation_level":"warning","title":"Spell Checker","message":"Check your spelling for 'banaas'.","raw_details":"Do you mean 'bananas' or 'banana'?","start_line":2,"end_line":2},{"path":"README.md","annotation_level":"warning","title":"Spell Checker","message":"Check your spelling for 'aples'","raw_details":"Do you mean 'apples' or 'Naples'","start_line":4,"end_line":4}],"images":[{"alt":"Super bananas","image_url":"http://example.com/images/42"}]}} # ChecksUpdateRequest | 

    try:
        # Update a check run
        api_response = api_instance.checks_update(owner, repo, check_run_id, checks_update_request)
        print("The response of ChecksApi->checks_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChecksApi->checks_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **check_run_id** | **int**| The unique identifier of the check run. | 
 **checks_update_request** | [**ChecksUpdateRequest**](ChecksUpdateRequest.md)|  | 

### Return type

[**CheckRun**](CheckRun.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

