# github_openapi.CodeScanningApi

All URIs are relative to *https://api.github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**code_scanning_commit_autofix**](CodeScanningApi.md#code_scanning_commit_autofix) | **POST** /repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/autofix/commits | Commit an autofix for a code scanning alert
[**code_scanning_create_autofix**](CodeScanningApi.md#code_scanning_create_autofix) | **POST** /repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/autofix | Create an autofix for a code scanning alert
[**code_scanning_create_variant_analysis**](CodeScanningApi.md#code_scanning_create_variant_analysis) | **POST** /repos/{owner}/{repo}/code-scanning/codeql/variant-analyses | Create a CodeQL variant analysis
[**code_scanning_delete_analysis**](CodeScanningApi.md#code_scanning_delete_analysis) | **DELETE** /repos/{owner}/{repo}/code-scanning/analyses/{analysis_id} | Delete a code scanning analysis from a repository
[**code_scanning_delete_codeql_database**](CodeScanningApi.md#code_scanning_delete_codeql_database) | **DELETE** /repos/{owner}/{repo}/code-scanning/codeql/databases/{language} | Delete a CodeQL database
[**code_scanning_get_alert**](CodeScanningApi.md#code_scanning_get_alert) | **GET** /repos/{owner}/{repo}/code-scanning/alerts/{alert_number} | Get a code scanning alert
[**code_scanning_get_analysis**](CodeScanningApi.md#code_scanning_get_analysis) | **GET** /repos/{owner}/{repo}/code-scanning/analyses/{analysis_id} | Get a code scanning analysis for a repository
[**code_scanning_get_autofix**](CodeScanningApi.md#code_scanning_get_autofix) | **GET** /repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/autofix | Get the status of an autofix for a code scanning alert
[**code_scanning_get_codeql_database**](CodeScanningApi.md#code_scanning_get_codeql_database) | **GET** /repos/{owner}/{repo}/code-scanning/codeql/databases/{language} | Get a CodeQL database for a repository
[**code_scanning_get_default_setup**](CodeScanningApi.md#code_scanning_get_default_setup) | **GET** /repos/{owner}/{repo}/code-scanning/default-setup | Get a code scanning default setup configuration
[**code_scanning_get_sarif**](CodeScanningApi.md#code_scanning_get_sarif) | **GET** /repos/{owner}/{repo}/code-scanning/sarifs/{sarif_id} | Get information about a SARIF upload
[**code_scanning_get_variant_analysis**](CodeScanningApi.md#code_scanning_get_variant_analysis) | **GET** /repos/{owner}/{repo}/code-scanning/codeql/variant-analyses/{codeql_variant_analysis_id} | Get the summary of a CodeQL variant analysis
[**code_scanning_get_variant_analysis_repo_task**](CodeScanningApi.md#code_scanning_get_variant_analysis_repo_task) | **GET** /repos/{owner}/{repo}/code-scanning/codeql/variant-analyses/{codeql_variant_analysis_id}/repos/{repo_owner}/{repo_name} | Get the analysis status of a repository in a CodeQL variant analysis
[**code_scanning_list_alert_instances**](CodeScanningApi.md#code_scanning_list_alert_instances) | **GET** /repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/instances | List instances of a code scanning alert
[**code_scanning_list_alerts_for_org**](CodeScanningApi.md#code_scanning_list_alerts_for_org) | **GET** /orgs/{org}/code-scanning/alerts | List code scanning alerts for an organization
[**code_scanning_list_alerts_for_repo**](CodeScanningApi.md#code_scanning_list_alerts_for_repo) | **GET** /repos/{owner}/{repo}/code-scanning/alerts | List code scanning alerts for a repository
[**code_scanning_list_codeql_databases**](CodeScanningApi.md#code_scanning_list_codeql_databases) | **GET** /repos/{owner}/{repo}/code-scanning/codeql/databases | List CodeQL databases for a repository
[**code_scanning_list_recent_analyses**](CodeScanningApi.md#code_scanning_list_recent_analyses) | **GET** /repos/{owner}/{repo}/code-scanning/analyses | List code scanning analyses for a repository
[**code_scanning_update_alert**](CodeScanningApi.md#code_scanning_update_alert) | **PATCH** /repos/{owner}/{repo}/code-scanning/alerts/{alert_number} | Update a code scanning alert
[**code_scanning_update_default_setup**](CodeScanningApi.md#code_scanning_update_default_setup) | **PATCH** /repos/{owner}/{repo}/code-scanning/default-setup | Update a code scanning default setup configuration
[**code_scanning_upload_sarif**](CodeScanningApi.md#code_scanning_upload_sarif) | **POST** /repos/{owner}/{repo}/code-scanning/sarifs | Upload an analysis as SARIF data


# **code_scanning_commit_autofix**
> CodeScanningAutofixCommitsResponse code_scanning_commit_autofix(owner, repo, alert_number, code_scanning_autofix_commits=code_scanning_autofix_commits)

Commit an autofix for a code scanning alert

Commits an autofix for a code scanning alert.  If an autofix is commited as a result of this request, then this endpoint will return a 201 Created response.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with private or public repositories, or the `public_repo` scope to use this endpoint with only public repositories.

### Example


```python
import github_openapi
from github_openapi.models.code_scanning_autofix_commits import CodeScanningAutofixCommits
from github_openapi.models.code_scanning_autofix_commits_response import CodeScanningAutofixCommitsResponse
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
    api_instance = github_openapi.CodeScanningApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    alert_number = 56 # int | The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the `number` field in the response from the `GET /repos/{owner}/{repo}/code-scanning/alerts` operation.
    code_scanning_autofix_commits = github_openapi.CodeScanningAutofixCommits() # CodeScanningAutofixCommits |  (optional)

    try:
        # Commit an autofix for a code scanning alert
        api_response = api_instance.code_scanning_commit_autofix(owner, repo, alert_number, code_scanning_autofix_commits=code_scanning_autofix_commits)
        print("The response of CodeScanningApi->code_scanning_commit_autofix:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScanningApi->code_scanning_commit_autofix: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **alert_number** | **int**| The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the &#x60;number&#x60; field in the response from the &#x60;GET /repos/{owner}/{repo}/code-scanning/alerts&#x60; operation. | 
 **code_scanning_autofix_commits** | [**CodeScanningAutofixCommits**](CodeScanningAutofixCommits.md)|  | [optional] 

### Return type

[**CodeScanningAutofixCommitsResponse**](CodeScanningAutofixCommitsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**403** | Response if the repository is archived or if GitHub Advanced Security is not enabled for this repository |  -  |
**404** | Resource not found |  -  |
**422** | Unprocessable Entity |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_scanning_create_autofix**
> CodeScanningAutofix code_scanning_create_autofix(owner, repo, alert_number)

Create an autofix for a code scanning alert

Creates an autofix for a code scanning alert.  If a new autofix is to be created as a result of this request or is currently being generated, then this endpoint will return a 202 Accepted response.  If an autofix already exists for a given alert, then this endpoint will return a 200 OK response.  OAuth app tokens and personal access tokens (classic) need the `security_events` scope to use this endpoint with private or public repositories, or the `public_repo` scope to use this endpoint with only public repositories.

### Example


```python
import github_openapi
from github_openapi.models.code_scanning_autofix import CodeScanningAutofix
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
    api_instance = github_openapi.CodeScanningApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    alert_number = 56 # int | The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the `number` field in the response from the `GET /repos/{owner}/{repo}/code-scanning/alerts` operation.

    try:
        # Create an autofix for a code scanning alert
        api_response = api_instance.code_scanning_create_autofix(owner, repo, alert_number)
        print("The response of CodeScanningApi->code_scanning_create_autofix:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScanningApi->code_scanning_create_autofix: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **alert_number** | **int**| The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the &#x60;number&#x60; field in the response from the &#x60;GET /repos/{owner}/{repo}/code-scanning/alerts&#x60; operation. | 

### Return type

[**CodeScanningAutofix**](CodeScanningAutofix.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**403** | Response if the repository is archived, if GitHub Advanced Security is not enabled for this repository or if rate limit is exceeded |  -  |
**404** | Resource not found |  -  |
**422** | Unprocessable Entity |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_scanning_create_variant_analysis**
> CodeScanningVariantAnalysis code_scanning_create_variant_analysis(owner, repo, code_scanning_create_variant_analysis_request)

Create a CodeQL variant analysis

Creates a new CodeQL variant analysis, which will run a CodeQL query against one or more repositories.  Get started by learning more about [running CodeQL queries at scale with Multi-Repository Variant Analysis](https://docs.github.com/code-security/codeql-for-vs-code/getting-started-with-codeql-for-vs-code/running-codeql-queries-at-scale-with-multi-repository-variant-analysis).  Use the `owner` and `repo` parameters in the URL to specify the controller repository that will be used for running GitHub Actions workflows and storing the results of the CodeQL variant analysis.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.code_scanning_create_variant_analysis_request import CodeScanningCreateVariantAnalysisRequest
from github_openapi.models.code_scanning_variant_analysis import CodeScanningVariantAnalysis
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
    api_instance = github_openapi.CodeScanningApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    code_scanning_create_variant_analysis_request = {"language":"csharp","query_pack":"aGVsbG8=","repositories":["octocat/Hello-World","octocat/example"]} # CodeScanningCreateVariantAnalysisRequest | 

    try:
        # Create a CodeQL variant analysis
        api_response = api_instance.code_scanning_create_variant_analysis(owner, repo, code_scanning_create_variant_analysis_request)
        print("The response of CodeScanningApi->code_scanning_create_variant_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScanningApi->code_scanning_create_variant_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **code_scanning_create_variant_analysis_request** | [**CodeScanningCreateVariantAnalysisRequest**](CodeScanningCreateVariantAnalysisRequest.md)|  | 

### Return type

[**CodeScanningVariantAnalysis**](CodeScanningVariantAnalysis.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Variant analysis submitted for processing |  -  |
**404** | Resource not found |  -  |
**422** | Unable to process variant analysis submission |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_scanning_delete_analysis**
> CodeScanningAnalysisDeletion code_scanning_delete_analysis(owner, repo, analysis_id, confirm_delete=confirm_delete)

Delete a code scanning analysis from a repository

Deletes a specified code scanning analysis from a repository.  You can delete one analysis at a time. To delete a series of analyses, start with the most recent analysis and work backwards. Conceptually, the process is similar to the undo function in a text editor.  When you list the analyses for a repository, one or more will be identified as deletable in the response:  ``` \"deletable\": true ```  An analysis is deletable when it's the most recent in a set of analyses. Typically, a repository will have multiple sets of analyses for each enabled code scanning tool, where a set is determined by a unique combination of analysis values:  * `ref` * `tool` * `category`  If you attempt to delete an analysis that is not the most recent in a set, you'll get a 400 response with the message:  ``` Analysis specified is not deletable. ```  The response from a successful `DELETE` operation provides you with two alternative URLs for deleting the next analysis in the set: `next_analysis_url` and `confirm_delete_url`. Use the `next_analysis_url` URL if you want to avoid accidentally deleting the final analysis in a set. This is a useful option if you want to preserve at least one analysis for the specified tool in your repository. Use the `confirm_delete_url` URL if you are content to remove all analyses for a tool. When you delete the last analysis in a set, the value of `next_analysis_url` and `confirm_delete_url` in the 200 response is `null`.  As an example of the deletion process, let's imagine that you added a workflow that configured a particular code scanning tool to analyze the code in a repository. This tool has added 15 analyses: 10 on the default branch, and another 5 on a topic branch. You therefore have two separate sets of analyses for this tool. You've now decided that you want to remove all of the analyses for the tool. To do this you must make 15 separate deletion requests. To start, you must find an analysis that's identified as deletable. Each set of analyses always has one that's identified as deletable. Having found the deletable analysis for one of the two sets, delete this analysis and then continue deleting the next analysis in the set until they're all deleted. Then repeat the process for the second set. The procedure therefore consists of a nested loop:  **Outer loop**: * List the analyses for the repository, filtered by tool. * Parse this list to find a deletable analysis. If found:    **Inner loop**:   * Delete the identified analysis.   * Parse the response for the value of `confirm_delete_url` and, if found, use this in the next iteration.  The above process assumes that you want to remove all trace of the tool's analyses from the GitHub user interface, for the specified repository, and it therefore uses the `confirm_delete_url` value. Alternatively, you could use the `next_analysis_url` value, which would leave the last analysis in each set undeleted to avoid removing a tool's analysis entirely.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with private or public repositories, or the `public_repo` scope to use this endpoint with only public repositories.

### Example


```python
import github_openapi
from github_openapi.models.code_scanning_analysis_deletion import CodeScanningAnalysisDeletion
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
    api_instance = github_openapi.CodeScanningApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    analysis_id = 56 # int | The ID of the analysis, as returned from the `GET /repos/{owner}/{repo}/code-scanning/analyses` operation.
    confirm_delete = 'confirm_delete_example' # str | Allow deletion if the specified analysis is the last in a set. If you attempt to delete the final analysis in a set without setting this parameter to `true`, you'll get a 400 response with the message: `Analysis is last of its type and deletion may result in the loss of historical alert data. Please specify confirm_delete.` (optional)

    try:
        # Delete a code scanning analysis from a repository
        api_response = api_instance.code_scanning_delete_analysis(owner, repo, analysis_id, confirm_delete=confirm_delete)
        print("The response of CodeScanningApi->code_scanning_delete_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScanningApi->code_scanning_delete_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **analysis_id** | **int**| The ID of the analysis, as returned from the &#x60;GET /repos/{owner}/{repo}/code-scanning/analyses&#x60; operation. | 
 **confirm_delete** | **str**| Allow deletion if the specified analysis is the last in a set. If you attempt to delete the final analysis in a set without setting this parameter to &#x60;true&#x60;, you&#39;ll get a 400 response with the message: &#x60;Analysis is last of its type and deletion may result in the loss of historical alert data. Please specify confirm_delete.&#x60; | [optional] 

### Return type

[**CodeScanningAnalysisDeletion**](CodeScanningAnalysisDeletion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**400** | Bad Request |  -  |
**403** | Response if the repository is archived or if GitHub Advanced Security is not enabled for this repository |  -  |
**404** | Resource not found |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_scanning_delete_codeql_database**
> code_scanning_delete_codeql_database(owner, repo, language)

Delete a CodeQL database

Deletes a CodeQL database for a language in a repository.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with private or public repositories, or the `public_repo` scope to use this endpoint with only public repositories.

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
    api_instance = github_openapi.CodeScanningApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    language = 'language_example' # str | The language of the CodeQL database.

    try:
        # Delete a CodeQL database
        api_instance.code_scanning_delete_codeql_database(owner, repo, language)
    except Exception as e:
        print("Exception when calling CodeScanningApi->code_scanning_delete_codeql_database: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **language** | **str**| The language of the CodeQL database. | 

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
**403** | Response if the repository is archived or if GitHub Advanced Security is not enabled for this repository |  -  |
**404** | Resource not found |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_scanning_get_alert**
> CodeScanningAlert code_scanning_get_alert(owner, repo, alert_number)

Get a code scanning alert

Gets a single code scanning alert.  OAuth app tokens and personal access tokens (classic) need the `security_events` scope to use this endpoint with private or public repositories, or the `public_repo` scope to use this endpoint with only public repositories.

### Example


```python
import github_openapi
from github_openapi.models.code_scanning_alert import CodeScanningAlert
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
    api_instance = github_openapi.CodeScanningApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    alert_number = 56 # int | The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the `number` field in the response from the `GET /repos/{owner}/{repo}/code-scanning/alerts` operation.

    try:
        # Get a code scanning alert
        api_response = api_instance.code_scanning_get_alert(owner, repo, alert_number)
        print("The response of CodeScanningApi->code_scanning_get_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScanningApi->code_scanning_get_alert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **alert_number** | **int**| The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the &#x60;number&#x60; field in the response from the &#x60;GET /repos/{owner}/{repo}/code-scanning/alerts&#x60; operation. | 

### Return type

[**CodeScanningAlert**](CodeScanningAlert.md)

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
**403** | Response if GitHub Advanced Security is not enabled for this repository |  -  |
**404** | Resource not found |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_scanning_get_analysis**
> CodeScanningAnalysis code_scanning_get_analysis(owner, repo, analysis_id)

Get a code scanning analysis for a repository

Gets a specified code scanning analysis for a repository.  The default JSON response contains fields that describe the analysis. This includes the Git reference and commit SHA to which the analysis relates, the datetime of the analysis, the name of the code scanning tool, and the number of alerts.  The `rules_count` field in the default response give the number of rules that were run in the analysis. For very old analyses this data is not available, and `0` is returned in this field.  This endpoint supports the following custom media types. For more information, see \"[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types).\"  - **`application/sarif+json`**: Instead of returning a summary of the analysis, this endpoint returns a subset of the analysis data that was uploaded. The data is formatted as [SARIF version 2.1.0](https://docs.oasis-open.org/sarif/sarif/v2.1.0/cs01/sarif-v2.1.0-cs01.html). It also returns additional data such as the `github/alertNumber` and `github/alertUrl` properties.  OAuth app tokens and personal access tokens (classic) need the `security_events` scope to use this endpoint with private or public repositories, or the `public_repo` scope to use this endpoint with only public repositories.

### Example


```python
import github_openapi
from github_openapi.models.code_scanning_analysis import CodeScanningAnalysis
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
    api_instance = github_openapi.CodeScanningApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    analysis_id = 56 # int | The ID of the analysis, as returned from the `GET /repos/{owner}/{repo}/code-scanning/analyses` operation.

    try:
        # Get a code scanning analysis for a repository
        api_response = api_instance.code_scanning_get_analysis(owner, repo, analysis_id)
        print("The response of CodeScanningApi->code_scanning_get_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScanningApi->code_scanning_get_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **analysis_id** | **int**| The ID of the analysis, as returned from the &#x60;GET /repos/{owner}/{repo}/code-scanning/analyses&#x60; operation. | 

### Return type

[**CodeScanningAnalysis**](CodeScanningAnalysis.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+sarif

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**403** | Response if GitHub Advanced Security is not enabled for this repository |  -  |
**404** | Resource not found |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_scanning_get_autofix**
> CodeScanningAutofix code_scanning_get_autofix(owner, repo, alert_number)

Get the status of an autofix for a code scanning alert

Gets the status and description of an autofix for a code scanning alert.  OAuth app tokens and personal access tokens (classic) need the `security_events` scope to use this endpoint with private or public repositories, or the `public_repo` scope to use this endpoint with only public repositories.

### Example


```python
import github_openapi
from github_openapi.models.code_scanning_autofix import CodeScanningAutofix
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
    api_instance = github_openapi.CodeScanningApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    alert_number = 56 # int | The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the `number` field in the response from the `GET /repos/{owner}/{repo}/code-scanning/alerts` operation.

    try:
        # Get the status of an autofix for a code scanning alert
        api_response = api_instance.code_scanning_get_autofix(owner, repo, alert_number)
        print("The response of CodeScanningApi->code_scanning_get_autofix:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScanningApi->code_scanning_get_autofix: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **alert_number** | **int**| The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the &#x60;number&#x60; field in the response from the &#x60;GET /repos/{owner}/{repo}/code-scanning/alerts&#x60; operation. | 

### Return type

[**CodeScanningAutofix**](CodeScanningAutofix.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**400** | Bad Request |  -  |
**403** | Response if GitHub Advanced Security is not enabled for this repository |  -  |
**404** | Resource not found |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_scanning_get_codeql_database**
> CodeScanningCodeqlDatabase code_scanning_get_codeql_database(owner, repo, language)

Get a CodeQL database for a repository

Gets a CodeQL database for a language in a repository.  By default this endpoint returns JSON metadata about the CodeQL database. To download the CodeQL database binary content, set the `Accept` header of the request to [`application/zip`](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types), and make sure your HTTP client is configured to follow redirects or use the `Location` header to make a second request to get the redirect URL.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with private or public repositories, or the `public_repo` scope to use this endpoint with only public repositories.

### Example


```python
import github_openapi
from github_openapi.models.code_scanning_codeql_database import CodeScanningCodeqlDatabase
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
    api_instance = github_openapi.CodeScanningApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    language = 'language_example' # str | The language of the CodeQL database.

    try:
        # Get a CodeQL database for a repository
        api_response = api_instance.code_scanning_get_codeql_database(owner, repo, language)
        print("The response of CodeScanningApi->code_scanning_get_codeql_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScanningApi->code_scanning_get_codeql_database: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **language** | **str**| The language of the CodeQL database. | 

### Return type

[**CodeScanningCodeqlDatabase**](CodeScanningCodeqlDatabase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**302** | Found |  -  |
**403** | Response if GitHub Advanced Security is not enabled for this repository |  -  |
**404** | Resource not found |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_scanning_get_default_setup**
> CodeScanningDefaultSetup code_scanning_get_default_setup(owner, repo)

Get a code scanning default setup configuration

Gets a code scanning default setup configuration.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with private or public repositories, or the `public_repo` scope to use this endpoint with only public repositories.

### Example


```python
import github_openapi
from github_openapi.models.code_scanning_default_setup import CodeScanningDefaultSetup
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
    api_instance = github_openapi.CodeScanningApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Get a code scanning default setup configuration
        api_response = api_instance.code_scanning_get_default_setup(owner, repo)
        print("The response of CodeScanningApi->code_scanning_get_default_setup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScanningApi->code_scanning_get_default_setup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**CodeScanningDefaultSetup**](CodeScanningDefaultSetup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**403** | Response if GitHub Advanced Security is not enabled for this repository |  -  |
**404** | Resource not found |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_scanning_get_sarif**
> CodeScanningSarifsStatus code_scanning_get_sarif(owner, repo, sarif_id)

Get information about a SARIF upload

Gets information about a SARIF upload, including the status and the URL of the analysis that was uploaded so that you can retrieve details of the analysis. For more information, see \"[Get a code scanning analysis for a repository](/rest/code-scanning/code-scanning#get-a-code-scanning-analysis-for-a-repository).\" OAuth app tokens and personal access tokens (classic) need the `security_events` scope to use this endpoint with private or public repositories, or the `public_repo` scope to use this endpoint with only public repositories.

### Example


```python
import github_openapi
from github_openapi.models.code_scanning_sarifs_status import CodeScanningSarifsStatus
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
    api_instance = github_openapi.CodeScanningApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    sarif_id = 'sarif_id_example' # str | The SARIF ID obtained after uploading.

    try:
        # Get information about a SARIF upload
        api_response = api_instance.code_scanning_get_sarif(owner, repo, sarif_id)
        print("The response of CodeScanningApi->code_scanning_get_sarif:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScanningApi->code_scanning_get_sarif: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **sarif_id** | **str**| The SARIF ID obtained after uploading. | 

### Return type

[**CodeScanningSarifsStatus**](CodeScanningSarifsStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**403** | Response if GitHub Advanced Security is not enabled for this repository |  -  |
**404** | Not Found if the sarif id does not match any upload |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_scanning_get_variant_analysis**
> CodeScanningVariantAnalysis code_scanning_get_variant_analysis(owner, repo, codeql_variant_analysis_id)

Get the summary of a CodeQL variant analysis

Gets the summary of a CodeQL variant analysis.  OAuth app tokens and personal access tokens (classic) need the `security_events` scope to use this endpoint with private or public repositories, or the `public_repo` scope to use this endpoint with only public repositories.

### Example


```python
import github_openapi
from github_openapi.models.code_scanning_variant_analysis import CodeScanningVariantAnalysis
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
    api_instance = github_openapi.CodeScanningApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    codeql_variant_analysis_id = 56 # int | The unique identifier of the variant analysis.

    try:
        # Get the summary of a CodeQL variant analysis
        api_response = api_instance.code_scanning_get_variant_analysis(owner, repo, codeql_variant_analysis_id)
        print("The response of CodeScanningApi->code_scanning_get_variant_analysis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScanningApi->code_scanning_get_variant_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **codeql_variant_analysis_id** | **int**| The unique identifier of the variant analysis. | 

### Return type

[**CodeScanningVariantAnalysis**](CodeScanningVariantAnalysis.md)

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
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_scanning_get_variant_analysis_repo_task**
> CodeScanningVariantAnalysisRepoTask code_scanning_get_variant_analysis_repo_task(owner, repo, codeql_variant_analysis_id, repo_owner, repo_name)

Get the analysis status of a repository in a CodeQL variant analysis

Gets the analysis status of a repository in a CodeQL variant analysis.  OAuth app tokens and personal access tokens (classic) need the `security_events` scope to use this endpoint with private or public repositories, or the `public_repo` scope to use this endpoint with only public repositories.

### Example


```python
import github_openapi
from github_openapi.models.code_scanning_variant_analysis_repo_task import CodeScanningVariantAnalysisRepoTask
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
    api_instance = github_openapi.CodeScanningApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the controller repository.
    codeql_variant_analysis_id = 56 # int | The ID of the variant analysis.
    repo_owner = 'repo_owner_example' # str | The account owner of the variant analysis repository. The name is not case sensitive.
    repo_name = 'repo_name_example' # str | The name of the variant analysis repository.

    try:
        # Get the analysis status of a repository in a CodeQL variant analysis
        api_response = api_instance.code_scanning_get_variant_analysis_repo_task(owner, repo, codeql_variant_analysis_id, repo_owner, repo_name)
        print("The response of CodeScanningApi->code_scanning_get_variant_analysis_repo_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScanningApi->code_scanning_get_variant_analysis_repo_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the controller repository. | 
 **codeql_variant_analysis_id** | **int**| The ID of the variant analysis. | 
 **repo_owner** | **str**| The account owner of the variant analysis repository. The name is not case sensitive. | 
 **repo_name** | **str**| The name of the variant analysis repository. | 

### Return type

[**CodeScanningVariantAnalysisRepoTask**](CodeScanningVariantAnalysisRepoTask.md)

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
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_scanning_list_alert_instances**
> List[CodeScanningAlertInstance] code_scanning_list_alert_instances(owner, repo, alert_number, page=page, per_page=per_page, ref=ref, pr=pr)

List instances of a code scanning alert

Lists all instances of the specified code scanning alert.  OAuth app tokens and personal access tokens (classic) need the `security_events` scope to use this endpoint with private or public repositories, or the `public_repo` scope to use this endpoint with only public repositories.

### Example


```python
import github_openapi
from github_openapi.models.code_scanning_alert_instance import CodeScanningAlertInstance
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
    api_instance = github_openapi.CodeScanningApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    alert_number = 56 # int | The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the `number` field in the response from the `GET /repos/{owner}/{repo}/code-scanning/alerts` operation.
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    ref = 'ref_example' # str | The Git reference for the results you want to list. The `ref` for a branch can be formatted either as `refs/heads/<branch name>` or simply `<branch name>`. To reference a pull request use `refs/pull/<number>/merge`. (optional)
    pr = 56 # int | The number of the pull request for the results you want to list. (optional)

    try:
        # List instances of a code scanning alert
        api_response = api_instance.code_scanning_list_alert_instances(owner, repo, alert_number, page=page, per_page=per_page, ref=ref, pr=pr)
        print("The response of CodeScanningApi->code_scanning_list_alert_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScanningApi->code_scanning_list_alert_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **alert_number** | **int**| The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the &#x60;number&#x60; field in the response from the &#x60;GET /repos/{owner}/{repo}/code-scanning/alerts&#x60; operation. | 
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **ref** | **str**| The Git reference for the results you want to list. The &#x60;ref&#x60; for a branch can be formatted either as &#x60;refs/heads/&lt;branch name&gt;&#x60; or simply &#x60;&lt;branch name&gt;&#x60;. To reference a pull request use &#x60;refs/pull/&lt;number&gt;/merge&#x60;. | [optional] 
 **pr** | **int**| The number of the pull request for the results you want to list. | [optional] 

### Return type

[**List[CodeScanningAlertInstance]**](CodeScanningAlertInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**403** | Response if GitHub Advanced Security is not enabled for this repository |  -  |
**404** | Resource not found |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_scanning_list_alerts_for_org**
> List[CodeScanningOrganizationAlertItems] code_scanning_list_alerts_for_org(org, tool_name=tool_name, tool_guid=tool_guid, before=before, after=after, page=page, per_page=per_page, direction=direction, state=state, sort=sort, severity=severity)

List code scanning alerts for an organization

Lists code scanning alerts for the default branch for all eligible repositories in an organization. Eligible repositories are repositories that are owned by organizations that you own or for which you are a security manager. For more information, see \"[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization).\"  The authenticated user must be an owner or security manager for the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `security_events` or `repo`s cope to use this endpoint with private or public repositories, or the `public_repo` scope to use this endpoint with only public repositories.

### Example


```python
import github_openapi
from github_openapi.models.code_scanning_alert_severity import CodeScanningAlertSeverity
from github_openapi.models.code_scanning_alert_state_query import CodeScanningAlertStateQuery
from github_openapi.models.code_scanning_organization_alert_items import CodeScanningOrganizationAlertItems
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
    api_instance = github_openapi.CodeScanningApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    tool_name = 'tool_name_example' # str | The name of a code scanning tool. Only results by this tool will be listed. You can specify the tool by using either `tool_name` or `tool_guid`, but not both. (optional)
    tool_guid = 'tool_guid_example' # str | The GUID of a code scanning tool. Only results by this tool will be listed. Note that some code scanning tools may not include a GUID in their analysis data. You can specify the tool by using either `tool_guid` or `tool_name`, but not both. (optional)
    before = 'before_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)
    after = 'after_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    direction = desc # str | The direction to sort the results by. (optional) (default to desc)
    state = github_openapi.CodeScanningAlertStateQuery() # CodeScanningAlertStateQuery | If specified, only code scanning alerts with this state will be returned. (optional)
    sort = created # str | The property by which to sort the results. (optional) (default to created)
    severity = github_openapi.CodeScanningAlertSeverity() # CodeScanningAlertSeverity | If specified, only code scanning alerts with this severity will be returned. (optional)

    try:
        # List code scanning alerts for an organization
        api_response = api_instance.code_scanning_list_alerts_for_org(org, tool_name=tool_name, tool_guid=tool_guid, before=before, after=after, page=page, per_page=per_page, direction=direction, state=state, sort=sort, severity=severity)
        print("The response of CodeScanningApi->code_scanning_list_alerts_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScanningApi->code_scanning_list_alerts_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **tool_name** | **str**| The name of a code scanning tool. Only results by this tool will be listed. You can specify the tool by using either &#x60;tool_name&#x60; or &#x60;tool_guid&#x60;, but not both. | [optional] 
 **tool_guid** | **str**| The GUID of a code scanning tool. Only results by this tool will be listed. Note that some code scanning tools may not include a GUID in their analysis data. You can specify the tool by using either &#x60;tool_guid&#x60; or &#x60;tool_name&#x60;, but not both. | [optional] 
 **before** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 
 **after** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **direction** | **str**| The direction to sort the results by. | [optional] [default to desc]
 **state** | [**CodeScanningAlertStateQuery**](.md)| If specified, only code scanning alerts with this state will be returned. | [optional] 
 **sort** | **str**| The property by which to sort the results. | [optional] [default to created]
 **severity** | [**CodeScanningAlertSeverity**](.md)| If specified, only code scanning alerts with this severity will be returned. | [optional] 

### Return type

[**List[CodeScanningOrganizationAlertItems]**](CodeScanningOrganizationAlertItems.md)

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
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_scanning_list_alerts_for_repo**
> List[CodeScanningAlertItems] code_scanning_list_alerts_for_repo(owner, repo, tool_name=tool_name, tool_guid=tool_guid, page=page, per_page=per_page, ref=ref, pr=pr, direction=direction, before=before, after=after, sort=sort, state=state, severity=severity)

List code scanning alerts for a repository

Lists code scanning alerts.  The response includes a `most_recent_instance` object. This provides details of the most recent instance of this alert for the default branch (or for the specified Git reference if you used `ref` in the request).  OAuth app tokens and personal access tokens (classic) need the `security_events` scope to use this endpoint with private or public repositories, or the `public_repo` scope to use this endpoint with only public repositories.

### Example


```python
import github_openapi
from github_openapi.models.code_scanning_alert_items import CodeScanningAlertItems
from github_openapi.models.code_scanning_alert_severity import CodeScanningAlertSeverity
from github_openapi.models.code_scanning_alert_state_query import CodeScanningAlertStateQuery
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
    api_instance = github_openapi.CodeScanningApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    tool_name = 'tool_name_example' # str | The name of a code scanning tool. Only results by this tool will be listed. You can specify the tool by using either `tool_name` or `tool_guid`, but not both. (optional)
    tool_guid = 'tool_guid_example' # str | The GUID of a code scanning tool. Only results by this tool will be listed. Note that some code scanning tools may not include a GUID in their analysis data. You can specify the tool by using either `tool_guid` or `tool_name`, but not both. (optional)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    ref = 'ref_example' # str | The Git reference for the results you want to list. The `ref` for a branch can be formatted either as `refs/heads/<branch name>` or simply `<branch name>`. To reference a pull request use `refs/pull/<number>/merge`. (optional)
    pr = 56 # int | The number of the pull request for the results you want to list. (optional)
    direction = desc # str | The direction to sort the results by. (optional) (default to desc)
    before = 'before_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)
    after = 'after_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)
    sort = created # str | The property by which to sort the results. (optional) (default to created)
    state = github_openapi.CodeScanningAlertStateQuery() # CodeScanningAlertStateQuery | If specified, only code scanning alerts with this state will be returned. (optional)
    severity = github_openapi.CodeScanningAlertSeverity() # CodeScanningAlertSeverity | If specified, only code scanning alerts with this severity will be returned. (optional)

    try:
        # List code scanning alerts for a repository
        api_response = api_instance.code_scanning_list_alerts_for_repo(owner, repo, tool_name=tool_name, tool_guid=tool_guid, page=page, per_page=per_page, ref=ref, pr=pr, direction=direction, before=before, after=after, sort=sort, state=state, severity=severity)
        print("The response of CodeScanningApi->code_scanning_list_alerts_for_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScanningApi->code_scanning_list_alerts_for_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **tool_name** | **str**| The name of a code scanning tool. Only results by this tool will be listed. You can specify the tool by using either &#x60;tool_name&#x60; or &#x60;tool_guid&#x60;, but not both. | [optional] 
 **tool_guid** | **str**| The GUID of a code scanning tool. Only results by this tool will be listed. Note that some code scanning tools may not include a GUID in their analysis data. You can specify the tool by using either &#x60;tool_guid&#x60; or &#x60;tool_name&#x60;, but not both. | [optional] 
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **ref** | **str**| The Git reference for the results you want to list. The &#x60;ref&#x60; for a branch can be formatted either as &#x60;refs/heads/&lt;branch name&gt;&#x60; or simply &#x60;&lt;branch name&gt;&#x60;. To reference a pull request use &#x60;refs/pull/&lt;number&gt;/merge&#x60;. | [optional] 
 **pr** | **int**| The number of the pull request for the results you want to list. | [optional] 
 **direction** | **str**| The direction to sort the results by. | [optional] [default to desc]
 **before** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 
 **after** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 
 **sort** | **str**| The property by which to sort the results. | [optional] [default to created]
 **state** | [**CodeScanningAlertStateQuery**](.md)| If specified, only code scanning alerts with this state will be returned. | [optional] 
 **severity** | [**CodeScanningAlertSeverity**](.md)| If specified, only code scanning alerts with this severity will be returned. | [optional] 

### Return type

[**List[CodeScanningAlertItems]**](CodeScanningAlertItems.md)

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
**403** | Response if GitHub Advanced Security is not enabled for this repository |  -  |
**404** | Resource not found |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_scanning_list_codeql_databases**
> List[CodeScanningCodeqlDatabase] code_scanning_list_codeql_databases(owner, repo)

List CodeQL databases for a repository

Lists the CodeQL databases that are available in a repository.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with private or public repositories, or the `public_repo` scope to use this endpoint with only public repositories.

### Example


```python
import github_openapi
from github_openapi.models.code_scanning_codeql_database import CodeScanningCodeqlDatabase
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
    api_instance = github_openapi.CodeScanningApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # List CodeQL databases for a repository
        api_response = api_instance.code_scanning_list_codeql_databases(owner, repo)
        print("The response of CodeScanningApi->code_scanning_list_codeql_databases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScanningApi->code_scanning_list_codeql_databases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**List[CodeScanningCodeqlDatabase]**](CodeScanningCodeqlDatabase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**403** | Response if GitHub Advanced Security is not enabled for this repository |  -  |
**404** | Resource not found |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_scanning_list_recent_analyses**
> List[CodeScanningAnalysis] code_scanning_list_recent_analyses(owner, repo, tool_name=tool_name, tool_guid=tool_guid, page=page, per_page=per_page, pr=pr, ref=ref, sarif_id=sarif_id, direction=direction, sort=sort)

List code scanning analyses for a repository

Lists the details of all code scanning analyses for a repository, starting with the most recent. The response is paginated and you can use the `page` and `per_page` parameters to list the analyses you're interested in. By default 30 analyses are listed per page.  The `rules_count` field in the response give the number of rules that were run in the analysis. For very old analyses this data is not available, and `0` is returned in this field.  > [!WARNING] > **Closing down notice:** The `tool_name` field is closing down and will, in future, not be included in the response for this endpoint. The example response reflects this change. The tool name can now be found inside the `tool` field.  OAuth app tokens and personal access tokens (classic) need the `security_events` scope to use this endpoint with private or public repositories, or the `public_repo` scope to use this endpoint with only public repositories.

### Example


```python
import github_openapi
from github_openapi.models.code_scanning_analysis import CodeScanningAnalysis
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
    api_instance = github_openapi.CodeScanningApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    tool_name = 'tool_name_example' # str | The name of a code scanning tool. Only results by this tool will be listed. You can specify the tool by using either `tool_name` or `tool_guid`, but not both. (optional)
    tool_guid = 'tool_guid_example' # str | The GUID of a code scanning tool. Only results by this tool will be listed. Note that some code scanning tools may not include a GUID in their analysis data. You can specify the tool by using either `tool_guid` or `tool_name`, but not both. (optional)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    pr = 56 # int | The number of the pull request for the results you want to list. (optional)
    ref = 'ref_example' # str | The Git reference for the analyses you want to list. The `ref` for a branch can be formatted either as `refs/heads/<branch name>` or simply `<branch name>`. To reference a pull request use `refs/pull/<number>/merge`. (optional)
    sarif_id = 'sarif_id_example' # str | Filter analyses belonging to the same SARIF upload. (optional)
    direction = desc # str | The direction to sort the results by. (optional) (default to desc)
    sort = created # str | The property by which to sort the results. (optional) (default to created)

    try:
        # List code scanning analyses for a repository
        api_response = api_instance.code_scanning_list_recent_analyses(owner, repo, tool_name=tool_name, tool_guid=tool_guid, page=page, per_page=per_page, pr=pr, ref=ref, sarif_id=sarif_id, direction=direction, sort=sort)
        print("The response of CodeScanningApi->code_scanning_list_recent_analyses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScanningApi->code_scanning_list_recent_analyses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **tool_name** | **str**| The name of a code scanning tool. Only results by this tool will be listed. You can specify the tool by using either &#x60;tool_name&#x60; or &#x60;tool_guid&#x60;, but not both. | [optional] 
 **tool_guid** | **str**| The GUID of a code scanning tool. Only results by this tool will be listed. Note that some code scanning tools may not include a GUID in their analysis data. You can specify the tool by using either &#x60;tool_guid&#x60; or &#x60;tool_name&#x60;, but not both. | [optional] 
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **pr** | **int**| The number of the pull request for the results you want to list. | [optional] 
 **ref** | **str**| The Git reference for the analyses you want to list. The &#x60;ref&#x60; for a branch can be formatted either as &#x60;refs/heads/&lt;branch name&gt;&#x60; or simply &#x60;&lt;branch name&gt;&#x60;. To reference a pull request use &#x60;refs/pull/&lt;number&gt;/merge&#x60;. | [optional] 
 **sarif_id** | **str**| Filter analyses belonging to the same SARIF upload. | [optional] 
 **direction** | **str**| The direction to sort the results by. | [optional] [default to desc]
 **sort** | **str**| The property by which to sort the results. | [optional] [default to created]

### Return type

[**List[CodeScanningAnalysis]**](CodeScanningAnalysis.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**403** | Response if GitHub Advanced Security is not enabled for this repository |  -  |
**404** | Resource not found |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_scanning_update_alert**
> CodeScanningAlert code_scanning_update_alert(owner, repo, alert_number, code_scanning_update_alert_request)

Update a code scanning alert

Updates the status of a single code scanning alert. OAuth app tokens and personal access tokens (classic) need the `security_events` scope to use this endpoint with private or public repositories, or the `public_repo` scope to use this endpoint with only public repositories.

### Example


```python
import github_openapi
from github_openapi.models.code_scanning_alert import CodeScanningAlert
from github_openapi.models.code_scanning_update_alert_request import CodeScanningUpdateAlertRequest
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
    api_instance = github_openapi.CodeScanningApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    alert_number = 56 # int | The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the `number` field in the response from the `GET /repos/{owner}/{repo}/code-scanning/alerts` operation.
    code_scanning_update_alert_request = {"state":"dismissed","dismissed_reason":"false positive","dismissed_comment":"This alert is not actually correct, because there's a sanitizer included in the library."} # CodeScanningUpdateAlertRequest | 

    try:
        # Update a code scanning alert
        api_response = api_instance.code_scanning_update_alert(owner, repo, alert_number, code_scanning_update_alert_request)
        print("The response of CodeScanningApi->code_scanning_update_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScanningApi->code_scanning_update_alert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **alert_number** | **int**| The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the &#x60;number&#x60; field in the response from the &#x60;GET /repos/{owner}/{repo}/code-scanning/alerts&#x60; operation. | 
 **code_scanning_update_alert_request** | [**CodeScanningUpdateAlertRequest**](CodeScanningUpdateAlertRequest.md)|  | 

### Return type

[**CodeScanningAlert**](CodeScanningAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**403** | Response if the repository is archived or if GitHub Advanced Security is not enabled for this repository |  -  |
**404** | Resource not found |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_scanning_update_default_setup**
> object code_scanning_update_default_setup(owner, repo, code_scanning_default_setup_update)

Update a code scanning default setup configuration

Updates a code scanning default setup configuration.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with private or public repositories, or the `public_repo` scope to use this endpoint with only public repositories.

### Example


```python
import github_openapi
from github_openapi.models.code_scanning_default_setup_update import CodeScanningDefaultSetupUpdate
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
    api_instance = github_openapi.CodeScanningApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    code_scanning_default_setup_update = github_openapi.CodeScanningDefaultSetupUpdate() # CodeScanningDefaultSetupUpdate | 

    try:
        # Update a code scanning default setup configuration
        api_response = api_instance.code_scanning_update_default_setup(owner, repo, code_scanning_default_setup_update)
        print("The response of CodeScanningApi->code_scanning_update_default_setup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScanningApi->code_scanning_update_default_setup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **code_scanning_default_setup_update** | [**CodeScanningDefaultSetupUpdate**](CodeScanningDefaultSetupUpdate.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**202** | Response |  -  |
**403** | Response if the repository is archived or if GitHub Advanced Security is not enabled for this repository |  -  |
**404** | Resource not found |  -  |
**409** | Response if there is already a validation run in progress with a different default setup configuration |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_scanning_upload_sarif**
> CodeScanningSarifsReceipt code_scanning_upload_sarif(owner, repo, code_scanning_upload_sarif_request)

Upload an analysis as SARIF data

Uploads SARIF data containing the results of a code scanning analysis to make the results available in a repository. For troubleshooting information, see \"[Troubleshooting SARIF uploads](https://docs.github.com/code-security/code-scanning/troubleshooting-sarif).\"  There are two places where you can upload code scanning results.  - If you upload to a pull request, for example `--ref refs/pull/42/merge` or `--ref refs/pull/42/head`, then the results appear as alerts in a pull request check. For more information, see \"[Triaging code scanning alerts in pull requests](/code-security/secure-coding/triaging-code-scanning-alerts-in-pull-requests).\"  - If you upload to a branch, for example `--ref refs/heads/my-branch`, then the results appear in the **Security** tab for your repository. For more information, see \"[Managing code scanning alerts for your repository](/code-security/secure-coding/managing-code-scanning-alerts-for-your-repository#viewing-the-alerts-for-a-repository).\"  You must compress the SARIF-formatted analysis data that you want to upload, using `gzip`, and then encode it as a Base64 format string. For example:  ``` gzip -c analysis-data.sarif | base64 -w0 ```  SARIF upload supports a maximum number of entries per the following data objects, and an analysis will be rejected if any of these objects is above its maximum value. For some objects, there are additional values over which the entries will be ignored while keeping the most important entries whenever applicable. To get the most out of your analysis when it includes data above the supported limits, try to optimize the analysis configuration. For example, for the CodeQL tool, identify and remove the most noisy queries. For more information, see \"[SARIF results exceed one or more limits](https://docs.github.com/code-security/code-scanning/troubleshooting-sarif/results-exceed-limit).\"   | **SARIF data**                   | **Maximum values** | **Additional limits**                                                            | |----------------------------------|:------------------:|----------------------------------------------------------------------------------| | Runs per file                    |         20         |                                                                                  | | Results per run                  |       25,000       | Only the top 5,000 results will be included, prioritized by severity.            | | Rules per run                    |       25,000       |                                                                                  | | Tool extensions per run          |        100         |                                                                                  | | Thread Flow Locations per result |       10,000       | Only the top 1,000 Thread Flow Locations will be included, using prioritization. | | Location per result              |       1,000        | Only 100 locations will be included.                                             | | Tags per rule                    |         20         | Only 10 tags will be included.                                                   |   The `202 Accepted` response includes an `id` value. You can use this ID to check the status of the upload by using it in the `/sarifs/{sarif_id}` endpoint. For more information, see \"[Get information about a SARIF upload](/rest/code-scanning/code-scanning#get-information-about-a-sarif-upload).\"  OAuth app tokens and personal access tokens (classic) need the `security_events` scope to use this endpoint with private or public repositories, or the `public_repo` scope to use this endpoint with only public repositories.  This endpoint is limited to 1,000 requests per hour for each user or app installation calling it.

### Example


```python
import github_openapi
from github_openapi.models.code_scanning_sarifs_receipt import CodeScanningSarifsReceipt
from github_openapi.models.code_scanning_upload_sarif_request import CodeScanningUploadSarifRequest
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
    api_instance = github_openapi.CodeScanningApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    code_scanning_upload_sarif_request = {"commit_sha":"4b6472266afd7b471e86085a6659e8c7f2b119da","ref":"refs/heads/master","sarif":"H4sICMLGdF4AA2V4YW1wbGUuc2FyaWYAvVjdbts2FL7PUxDCijaA/CM7iRNfLkPXYgHSNstumlzQ0pHFVCI1korjFgH2ONtr7Ul2KFmy/mOn6QIkjsjDw0/nfN85NL8dEGL9pNwAImqRObECrWM1H40kXQ2XTAfJIlEgXcE1cD10RTQSVDE10K4aKSqZP1AxuKOIKg1ydJU60jSfSh8Hk6EzHA/vlOCWbfa7B6kYPpj90rlsWCZcmbHP5Bs+4oAWIjQD2SMOeJLh2vIQDnIaQerqXHjw8YIgxohybxAyDsS4cAPKsp03K4RcUs6+Up2D+JXpd8mibKIQN9fM/aMCdbyBujGSSQgVxJtx5qX2d2qUcIweQhEuDQf3GBO6CKHkogx/N3MVCKl/AeVKFuf4y5ubsMGDTj1ep+5I7sgmLIpxtU38hLtmMRGSuCFVyip5eKzs5ydh+LztVL6f2m6oih1BkYiuyQIIJWodxVpERPj4sEiWBNNH8EWT0DMG8EAjzKVHXCrB4FkPu/F64NMk1OeC+2yZSNoBOoR7CC0EzYWGbm+xFDFIzbI011+cLjfZtyJkmMZfumAh02uL3NpV2y+MZ6RAjxibyKrNxxJcVjANSb4eBGwZ1M0KsuyR2poLr5rMl8vaDSeVn6eTWEO2j2xIEcmhwlTKNOi4GMOI8gfuZYkvJ7b4v5Tiumyz7RnHeodFzpS8ASIZCH/AYdWi2z3sG8JtFxJ6fF9yR9CdifBr9Pd6d5V2+zbJKjjCFGGmsHuYFy2ytJq9tUxcLSRSQecppOGKrpUxYfxefMEFK+wOGa4hudQByBVT0L+EKtyACxnRsABhEx1QjVDs1KNI9MbpnhqfE45B6FJvu3hRu5VRU9MhZLmK7fqkKyQSTHNoyMqUFMqXCV3CwAeqEwmVokraK8IuBaGvHjQ0gMYrKjnjyw7uk9uD8tgmsBbFMPnU1bV2ZhkJNkuolUiWys3UPWzs5aaIUz9TBe8zMb+6+nT+6fLy91dlE3xzeDDT4zYszb0bW6NjJd0Rvn2EnLvWLFSdKPpBzInzfRgu8ETyMcH8nIfMnJCeC2PyfTA+UKngcnGH7Hw2hGkVQs5YlIRCtdWZYQ4/73es2JlxkfViOEIhoWJq5Oo6UBBfiKIqFBWhiE3jJGbFwVoxBHTRSuIS67sMeplei24X20shLjG+8gqbKC/bESiNMC+wd5q5id0yeS7CJEqXzmrTWNq3k05l84P6f4/bEmXFJjI0fIt1BGQssUnUDkBYeVhE5TqPnMH3jqogDcP0zKcTgLPTMSzOjhbjuVOmW23l1fYNStulfo6sXlFsGLhbDy5RECPRYGCTgOj2bd4nUQEivEd0H7KKYxqnEhFohuur3a3UPskbH/+Yg0+M5P2MHRJu3ziHh3Z2NCrWt3XF1rWTw8Ne/pfbWYXnDSE0SNZQQt1i18q7te2vOhu7ehWuvVyeu0wbLZi24mhoo6aOOTltzG/lgdVvVoXQq5V+pewkFIzL8fjEcadT55jOjpzFzHuOTtDNrMkJPMVQDd7F09RID72O/UPZ0tmctqZ7kWX6EmSZnDpP8GU67SXM8XE3YSrxbKsx6UReZ4y6n/FVZfJjs9Z7stma75W5yQtkzjk5eSJxk1lv4o7+j8TlhaJ2lsKWZO6lruDPBLib3x5ZN/KGWzZ+pn///evv7OOf4iIBv3oY9L/l1wiJ9p0Tc+F1zZnOE9NxXWEus6IQhr5pMfoqxi8WPsuu0azsns4UC6WzNzHIzbeEx4P/AJ3SefgcFAAA"} # CodeScanningUploadSarifRequest | 

    try:
        # Upload an analysis as SARIF data
        api_response = api_instance.code_scanning_upload_sarif(owner, repo, code_scanning_upload_sarif_request)
        print("The response of CodeScanningApi->code_scanning_upload_sarif:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeScanningApi->code_scanning_upload_sarif: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **code_scanning_upload_sarif_request** | [**CodeScanningUploadSarifRequest**](CodeScanningUploadSarifRequest.md)|  | 

### Return type

[**CodeScanningSarifsReceipt**](CodeScanningSarifsReceipt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Response |  -  |
**400** | Bad Request if the sarif field is invalid |  -  |
**403** | Response if the repository is archived or if GitHub Advanced Security is not enabled for this repository |  -  |
**404** | Resource not found |  -  |
**413** | Payload Too Large if the sarif field is too large |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

