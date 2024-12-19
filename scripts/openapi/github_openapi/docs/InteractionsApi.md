# github_openapi.InteractionsApi

All URIs are relative to *https://api.github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**interactions_get_restrictions_for_authenticated_user**](InteractionsApi.md#interactions_get_restrictions_for_authenticated_user) | **GET** /user/interaction-limits | Get interaction restrictions for your public repositories
[**interactions_get_restrictions_for_org**](InteractionsApi.md#interactions_get_restrictions_for_org) | **GET** /orgs/{org}/interaction-limits | Get interaction restrictions for an organization
[**interactions_get_restrictions_for_repo**](InteractionsApi.md#interactions_get_restrictions_for_repo) | **GET** /repos/{owner}/{repo}/interaction-limits | Get interaction restrictions for a repository
[**interactions_remove_restrictions_for_authenticated_user**](InteractionsApi.md#interactions_remove_restrictions_for_authenticated_user) | **DELETE** /user/interaction-limits | Remove interaction restrictions from your public repositories
[**interactions_remove_restrictions_for_org**](InteractionsApi.md#interactions_remove_restrictions_for_org) | **DELETE** /orgs/{org}/interaction-limits | Remove interaction restrictions for an organization
[**interactions_remove_restrictions_for_repo**](InteractionsApi.md#interactions_remove_restrictions_for_repo) | **DELETE** /repos/{owner}/{repo}/interaction-limits | Remove interaction restrictions for a repository
[**interactions_set_restrictions_for_authenticated_user**](InteractionsApi.md#interactions_set_restrictions_for_authenticated_user) | **PUT** /user/interaction-limits | Set interaction restrictions for your public repositories
[**interactions_set_restrictions_for_org**](InteractionsApi.md#interactions_set_restrictions_for_org) | **PUT** /orgs/{org}/interaction-limits | Set interaction restrictions for an organization
[**interactions_set_restrictions_for_repo**](InteractionsApi.md#interactions_set_restrictions_for_repo) | **PUT** /repos/{owner}/{repo}/interaction-limits | Set interaction restrictions for a repository


# **interactions_get_restrictions_for_authenticated_user**
> InteractionsGetRestrictionsForOrg200Response interactions_get_restrictions_for_authenticated_user()

Get interaction restrictions for your public repositories

Shows which type of GitHub user can interact with your public repositories and when the restriction expires.

### Example


```python
import github_openapi
from github_openapi.models.interactions_get_restrictions_for_org200_response import InteractionsGetRestrictionsForOrg200Response
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
    api_instance = github_openapi.InteractionsApi(api_client)

    try:
        # Get interaction restrictions for your public repositories
        api_response = api_instance.interactions_get_restrictions_for_authenticated_user()
        print("The response of InteractionsApi->interactions_get_restrictions_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionsApi->interactions_get_restrictions_for_authenticated_user: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**InteractionsGetRestrictionsForOrg200Response**](InteractionsGetRestrictionsForOrg200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default response |  -  |
**204** | Response when there are no restrictions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **interactions_get_restrictions_for_org**
> InteractionsGetRestrictionsForOrg200Response interactions_get_restrictions_for_org(org)

Get interaction restrictions for an organization

Shows which type of GitHub user can interact with this organization and when the restriction expires. If there is no restrictions, you will see an empty response.

### Example


```python
import github_openapi
from github_openapi.models.interactions_get_restrictions_for_org200_response import InteractionsGetRestrictionsForOrg200Response
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
    api_instance = github_openapi.InteractionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.

    try:
        # Get interaction restrictions for an organization
        api_response = api_instance.interactions_get_restrictions_for_org(org)
        print("The response of InteractionsApi->interactions_get_restrictions_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionsApi->interactions_get_restrictions_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 

### Return type

[**InteractionsGetRestrictionsForOrg200Response**](InteractionsGetRestrictionsForOrg200Response.md)

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

# **interactions_get_restrictions_for_repo**
> InteractionsGetRestrictionsForOrg200Response interactions_get_restrictions_for_repo(owner, repo)

Get interaction restrictions for a repository

Shows which type of GitHub user can interact with this repository and when the restriction expires. If there are no restrictions, you will see an empty response.

### Example


```python
import github_openapi
from github_openapi.models.interactions_get_restrictions_for_org200_response import InteractionsGetRestrictionsForOrg200Response
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
    api_instance = github_openapi.InteractionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Get interaction restrictions for a repository
        api_response = api_instance.interactions_get_restrictions_for_repo(owner, repo)
        print("The response of InteractionsApi->interactions_get_restrictions_for_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionsApi->interactions_get_restrictions_for_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**InteractionsGetRestrictionsForOrg200Response**](InteractionsGetRestrictionsForOrg200Response.md)

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

# **interactions_remove_restrictions_for_authenticated_user**
> interactions_remove_restrictions_for_authenticated_user()

Remove interaction restrictions from your public repositories

Removes any interaction restrictions from your public repositories.

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
    api_instance = github_openapi.InteractionsApi(api_client)

    try:
        # Remove interaction restrictions from your public repositories
        api_instance.interactions_remove_restrictions_for_authenticated_user()
    except Exception as e:
        print("Exception when calling InteractionsApi->interactions_remove_restrictions_for_authenticated_user: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **interactions_remove_restrictions_for_org**
> interactions_remove_restrictions_for_org(org)

Remove interaction restrictions for an organization

Removes all interaction restrictions from public repositories in the given organization. You must be an organization owner to remove restrictions.

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
    api_instance = github_openapi.InteractionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.

    try:
        # Remove interaction restrictions for an organization
        api_instance.interactions_remove_restrictions_for_org(org)
    except Exception as e:
        print("Exception when calling InteractionsApi->interactions_remove_restrictions_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **interactions_remove_restrictions_for_repo**
> interactions_remove_restrictions_for_repo(owner, repo)

Remove interaction restrictions for a repository

Removes all interaction restrictions from the given repository. You must have owner or admin access to remove restrictions. If the interaction limit is set for the user or organization that owns this repository, you will receive a `409 Conflict` response and will not be able to use this endpoint to change the interaction limit for a single repository.

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
    api_instance = github_openapi.InteractionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Remove interaction restrictions for a repository
        api_instance.interactions_remove_restrictions_for_repo(owner, repo)
    except Exception as e:
        print("Exception when calling InteractionsApi->interactions_remove_restrictions_for_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |
**409** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **interactions_set_restrictions_for_authenticated_user**
> InteractionLimitResponse interactions_set_restrictions_for_authenticated_user(interaction_limit)

Set interaction restrictions for your public repositories

Temporarily restricts which type of GitHub user can interact with your public repositories. Setting the interaction limit at the user level will overwrite any interaction limits that are set for individual repositories owned by the user.

### Example


```python
import github_openapi
from github_openapi.models.interaction_limit import InteractionLimit
from github_openapi.models.interaction_limit_response import InteractionLimitResponse
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
    api_instance = github_openapi.InteractionsApi(api_client)
    interaction_limit = {"limit":"collaborators_only","expiry":"one_month"} # InteractionLimit | 

    try:
        # Set interaction restrictions for your public repositories
        api_response = api_instance.interactions_set_restrictions_for_authenticated_user(interaction_limit)
        print("The response of InteractionsApi->interactions_set_restrictions_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionsApi->interactions_set_restrictions_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_limit** | [**InteractionLimit**](InteractionLimit.md)|  | 

### Return type

[**InteractionLimitResponse**](InteractionLimitResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **interactions_set_restrictions_for_org**
> InteractionLimitResponse interactions_set_restrictions_for_org(org, interaction_limit)

Set interaction restrictions for an organization

Temporarily restricts interactions to a certain type of GitHub user in any public repository in the given organization. You must be an organization owner to set these restrictions. Setting the interaction limit at the organization level will overwrite any interaction limits that are set for individual repositories owned by the organization.

### Example


```python
import github_openapi
from github_openapi.models.interaction_limit import InteractionLimit
from github_openapi.models.interaction_limit_response import InteractionLimitResponse
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
    api_instance = github_openapi.InteractionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    interaction_limit = {"limit":"collaborators_only","expiry":"one_month"} # InteractionLimit | 

    try:
        # Set interaction restrictions for an organization
        api_response = api_instance.interactions_set_restrictions_for_org(org, interaction_limit)
        print("The response of InteractionsApi->interactions_set_restrictions_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionsApi->interactions_set_restrictions_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **interaction_limit** | [**InteractionLimit**](InteractionLimit.md)|  | 

### Return type

[**InteractionLimitResponse**](InteractionLimitResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **interactions_set_restrictions_for_repo**
> InteractionLimitResponse interactions_set_restrictions_for_repo(owner, repo, interaction_limit)

Set interaction restrictions for a repository

Temporarily restricts interactions to a certain type of GitHub user within the given repository. You must have owner or admin access to set these restrictions. If an interaction limit is set for the user or organization that owns this repository, you will receive a `409 Conflict` response and will not be able to use this endpoint to change the interaction limit for a single repository.

### Example


```python
import github_openapi
from github_openapi.models.interaction_limit import InteractionLimit
from github_openapi.models.interaction_limit_response import InteractionLimitResponse
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
    api_instance = github_openapi.InteractionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    interaction_limit = {"limit":"collaborators_only","expiry":"one_day"} # InteractionLimit | 

    try:
        # Set interaction restrictions for a repository
        api_response = api_instance.interactions_set_restrictions_for_repo(owner, repo, interaction_limit)
        print("The response of InteractionsApi->interactions_set_restrictions_for_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionsApi->interactions_set_restrictions_for_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **interaction_limit** | [**InteractionLimit**](InteractionLimit.md)|  | 

### Return type

[**InteractionLimitResponse**](InteractionLimitResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**409** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

