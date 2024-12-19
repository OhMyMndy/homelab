# github_openapi.DependencyGraphApi

All URIs are relative to *https://api.github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dependency_graph_create_repository_snapshot**](DependencyGraphApi.md#dependency_graph_create_repository_snapshot) | **POST** /repos/{owner}/{repo}/dependency-graph/snapshots | Create a snapshot of dependencies for a repository
[**dependency_graph_diff_range**](DependencyGraphApi.md#dependency_graph_diff_range) | **GET** /repos/{owner}/{repo}/dependency-graph/compare/{basehead} | Get a diff of the dependencies between commits
[**dependency_graph_export_sbom**](DependencyGraphApi.md#dependency_graph_export_sbom) | **GET** /repos/{owner}/{repo}/dependency-graph/sbom | Export a software bill of materials (SBOM) for a repository.


# **dependency_graph_create_repository_snapshot**
> DependencyGraphCreateRepositorySnapshot201Response dependency_graph_create_repository_snapshot(owner, repo, snapshot)

Create a snapshot of dependencies for a repository

Create a new snapshot of a repository's dependencies.  The authenticated user must have access to the repository.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.dependency_graph_create_repository_snapshot201_response import DependencyGraphCreateRepositorySnapshot201Response
from github_openapi.models.snapshot import Snapshot
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
    api_instance = github_openapi.DependencyGraphApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    snapshot = github_openapi.Snapshot() # Snapshot | 

    try:
        # Create a snapshot of dependencies for a repository
        api_response = api_instance.dependency_graph_create_repository_snapshot(owner, repo, snapshot)
        print("The response of DependencyGraphApi->dependency_graph_create_repository_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DependencyGraphApi->dependency_graph_create_repository_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **snapshot** | [**Snapshot**](Snapshot.md)|  | 

### Return type

[**DependencyGraphCreateRepositorySnapshot201Response**](DependencyGraphCreateRepositorySnapshot201Response.md)

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

# **dependency_graph_diff_range**
> List[DependencyGraphDiffInner] dependency_graph_diff_range(owner, repo, basehead, name=name)

Get a diff of the dependencies between commits

Gets the diff of the dependency changes between two commits of a repository, based on the changes to the dependency manifests made in those commits.

### Example


```python
import github_openapi
from github_openapi.models.dependency_graph_diff_inner import DependencyGraphDiffInner
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
    api_instance = github_openapi.DependencyGraphApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    basehead = 'basehead_example' # str | The base and head Git revisions to compare. The Git revisions will be resolved to commit SHAs. Named revisions will be resolved to their corresponding HEAD commits, and an appropriate merge base will be determined. This parameter expects the format `{base}...{head}`.
    name = 'name_example' # str | The full path, relative to the repository root, of the dependency manifest file. (optional)

    try:
        # Get a diff of the dependencies between commits
        api_response = api_instance.dependency_graph_diff_range(owner, repo, basehead, name=name)
        print("The response of DependencyGraphApi->dependency_graph_diff_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DependencyGraphApi->dependency_graph_diff_range: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **basehead** | **str**| The base and head Git revisions to compare. The Git revisions will be resolved to commit SHAs. Named revisions will be resolved to their corresponding HEAD commits, and an appropriate merge base will be determined. This parameter expects the format &#x60;{base}...{head}&#x60;. | 
 **name** | **str**| The full path, relative to the repository root, of the dependency manifest file. | [optional] 

### Return type

[**List[DependencyGraphDiffInner]**](DependencyGraphDiffInner.md)

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
**403** | Response if GitHub Advanced Security is not enabled for this repository |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dependency_graph_export_sbom**
> DependencyGraphSpdxSbom dependency_graph_export_sbom(owner, repo)

Export a software bill of materials (SBOM) for a repository.

Exports the software bill of materials (SBOM) for a repository in SPDX JSON format.

### Example


```python
import github_openapi
from github_openapi.models.dependency_graph_spdx_sbom import DependencyGraphSpdxSbom
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
    api_instance = github_openapi.DependencyGraphApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Export a software bill of materials (SBOM) for a repository.
        api_response = api_instance.dependency_graph_export_sbom(owner, repo)
        print("The response of DependencyGraphApi->dependency_graph_export_sbom:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DependencyGraphApi->dependency_graph_export_sbom: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**DependencyGraphSpdxSbom**](DependencyGraphSpdxSbom.md)

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

