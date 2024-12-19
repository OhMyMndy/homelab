# github_openapi.ProjectsApi

All URIs are relative to *https://api.github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_add_collaborator**](ProjectsApi.md#projects_add_collaborator) | **PUT** /projects/{project_id}/collaborators/{username} | Add project collaborator
[**projects_create_card**](ProjectsApi.md#projects_create_card) | **POST** /projects/columns/{column_id}/cards | Create a project card
[**projects_create_column**](ProjectsApi.md#projects_create_column) | **POST** /projects/{project_id}/columns | Create a project column
[**projects_create_for_authenticated_user**](ProjectsApi.md#projects_create_for_authenticated_user) | **POST** /user/projects | Create a user project
[**projects_create_for_org**](ProjectsApi.md#projects_create_for_org) | **POST** /orgs/{org}/projects | Create an organization project
[**projects_create_for_repo**](ProjectsApi.md#projects_create_for_repo) | **POST** /repos/{owner}/{repo}/projects | Create a repository project
[**projects_delete**](ProjectsApi.md#projects_delete) | **DELETE** /projects/{project_id} | Delete a project
[**projects_delete_card**](ProjectsApi.md#projects_delete_card) | **DELETE** /projects/columns/cards/{card_id} | Delete a project card
[**projects_delete_column**](ProjectsApi.md#projects_delete_column) | **DELETE** /projects/columns/{column_id} | Delete a project column
[**projects_get**](ProjectsApi.md#projects_get) | **GET** /projects/{project_id} | Get a project
[**projects_get_card**](ProjectsApi.md#projects_get_card) | **GET** /projects/columns/cards/{card_id} | Get a project card
[**projects_get_column**](ProjectsApi.md#projects_get_column) | **GET** /projects/columns/{column_id} | Get a project column
[**projects_get_permission_for_user**](ProjectsApi.md#projects_get_permission_for_user) | **GET** /projects/{project_id}/collaborators/{username}/permission | Get project permission for a user
[**projects_list_cards**](ProjectsApi.md#projects_list_cards) | **GET** /projects/columns/{column_id}/cards | List project cards
[**projects_list_collaborators**](ProjectsApi.md#projects_list_collaborators) | **GET** /projects/{project_id}/collaborators | List project collaborators
[**projects_list_columns**](ProjectsApi.md#projects_list_columns) | **GET** /projects/{project_id}/columns | List project columns
[**projects_list_for_org**](ProjectsApi.md#projects_list_for_org) | **GET** /orgs/{org}/projects | List organization projects
[**projects_list_for_repo**](ProjectsApi.md#projects_list_for_repo) | **GET** /repos/{owner}/{repo}/projects | List repository projects
[**projects_list_for_user**](ProjectsApi.md#projects_list_for_user) | **GET** /users/{username}/projects | List user projects
[**projects_move_card**](ProjectsApi.md#projects_move_card) | **POST** /projects/columns/cards/{card_id}/moves | Move a project card
[**projects_move_column**](ProjectsApi.md#projects_move_column) | **POST** /projects/columns/{column_id}/moves | Move a project column
[**projects_remove_collaborator**](ProjectsApi.md#projects_remove_collaborator) | **DELETE** /projects/{project_id}/collaborators/{username} | Remove user as a collaborator
[**projects_update**](ProjectsApi.md#projects_update) | **PATCH** /projects/{project_id} | Update a project
[**projects_update_card**](ProjectsApi.md#projects_update_card) | **PATCH** /projects/columns/cards/{card_id} | Update an existing project card
[**projects_update_column**](ProjectsApi.md#projects_update_column) | **PATCH** /projects/columns/{column_id} | Update an existing project column


# **projects_add_collaborator**
> projects_add_collaborator(project_id, username, projects_add_collaborator_request=projects_add_collaborator_request)

Add project collaborator

Adds a collaborator to an organization project and sets their permission level. You must be an organization owner or a project `admin` to add a collaborator.

### Example


```python
import github_openapi
from github_openapi.models.projects_add_collaborator_request import ProjectsAddCollaboratorRequest
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
    api_instance = github_openapi.ProjectsApi(api_client)
    project_id = 56 # int | The unique identifier of the project.
    username = 'username_example' # str | The handle for the GitHub user account.
    projects_add_collaborator_request = {"permission":"write"} # ProjectsAddCollaboratorRequest |  (optional)

    try:
        # Add project collaborator
        api_instance.projects_add_collaborator(project_id, username, projects_add_collaborator_request=projects_add_collaborator_request)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_add_collaborator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The unique identifier of the project. | 
 **username** | **str**| The handle for the GitHub user account. | 
 **projects_add_collaborator_request** | [**ProjectsAddCollaboratorRequest**](ProjectsAddCollaboratorRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_create_card**
> ProjectCard projects_create_card(column_id, projects_create_card_request)

Create a project card



### Example


```python
import github_openapi
from github_openapi.models.project_card import ProjectCard
from github_openapi.models.projects_create_card_request import ProjectsCreateCardRequest
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
    api_instance = github_openapi.ProjectsApi(api_client)
    column_id = 56 # int | The unique identifier of the column.
    projects_create_card_request = {"note":"Add payload for delete Project column"} # ProjectsCreateCardRequest | 

    try:
        # Create a project card
        api_response = api_instance.projects_create_card(column_id, projects_create_card_request)
        print("The response of ProjectsApi->projects_create_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_create_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **column_id** | **int**| The unique identifier of the column. | 
 **projects_create_card_request** | [**ProjectsCreateCardRequest**](ProjectsCreateCardRequest.md)|  | 

### Return type

[**ProjectCard**](ProjectCard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |
**422** | Validation failed |  -  |
**503** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_create_column**
> ProjectColumn projects_create_column(project_id, projects_update_column_request)

Create a project column

Creates a new project column.

### Example


```python
import github_openapi
from github_openapi.models.project_column import ProjectColumn
from github_openapi.models.projects_update_column_request import ProjectsUpdateColumnRequest
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
    api_instance = github_openapi.ProjectsApi(api_client)
    project_id = 56 # int | The unique identifier of the project.
    projects_update_column_request = {"name":"Remaining tasks"} # ProjectsUpdateColumnRequest | 

    try:
        # Create a project column
        api_response = api_instance.projects_create_column(project_id, projects_update_column_request)
        print("The response of ProjectsApi->projects_create_column:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_create_column: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The unique identifier of the project. | 
 **projects_update_column_request** | [**ProjectsUpdateColumnRequest**](ProjectsUpdateColumnRequest.md)|  | 

### Return type

[**ProjectColumn**](ProjectColumn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_create_for_authenticated_user**
> Project projects_create_for_authenticated_user(projects_create_for_authenticated_user_request)

Create a user project

Creates a user project board. Returns a `410 Gone` status if the user does not have existing classic projects. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned.

### Example


```python
import github_openapi
from github_openapi.models.project import Project
from github_openapi.models.projects_create_for_authenticated_user_request import ProjectsCreateForAuthenticatedUserRequest
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
    api_instance = github_openapi.ProjectsApi(api_client)
    projects_create_for_authenticated_user_request = {"name":"My Projects","body":"A board to manage my personal projects."} # ProjectsCreateForAuthenticatedUserRequest | 

    try:
        # Create a user project
        api_response = api_instance.projects_create_for_authenticated_user(projects_create_for_authenticated_user_request)
        print("The response of ProjectsApi->projects_create_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_create_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projects_create_for_authenticated_user_request** | [**ProjectsCreateForAuthenticatedUserRequest**](ProjectsCreateForAuthenticatedUserRequest.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_create_for_org**
> Project projects_create_for_org(org, projects_create_for_org_request)

Create an organization project

Creates an organization project board. Returns a `410 Gone` status if projects are disabled in the organization or if the organization does not have existing classic projects. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned.

### Example


```python
import github_openapi
from github_openapi.models.project import Project
from github_openapi.models.projects_create_for_org_request import ProjectsCreateForOrgRequest
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
    api_instance = github_openapi.ProjectsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    projects_create_for_org_request = {"name":"Organization Roadmap","body":"High-level roadmap for the upcoming year."} # ProjectsCreateForOrgRequest | 

    try:
        # Create an organization project
        api_response = api_instance.projects_create_for_org(org, projects_create_for_org_request)
        print("The response of ProjectsApi->projects_create_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_create_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **projects_create_for_org_request** | [**ProjectsCreateForOrgRequest**](ProjectsCreateForOrgRequest.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**410** | Gone |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_create_for_repo**
> Project projects_create_for_repo(owner, repo, projects_create_for_org_request)

Create a repository project

Creates a repository project board. Returns a `410 Gone` status if projects are disabled in the repository or if the repository does not have existing classic projects. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned.

### Example


```python
import github_openapi
from github_openapi.models.project import Project
from github_openapi.models.projects_create_for_org_request import ProjectsCreateForOrgRequest
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
    api_instance = github_openapi.ProjectsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    projects_create_for_org_request = {"name":"Projects Documentation","body":"Developer documentation project for the developer site."} # ProjectsCreateForOrgRequest | 

    try:
        # Create a repository project
        api_response = api_instance.projects_create_for_repo(owner, repo, projects_create_for_org_request)
        print("The response of ProjectsApi->projects_create_for_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_create_for_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **projects_create_for_org_request** | [**ProjectsCreateForOrgRequest**](ProjectsCreateForOrgRequest.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**410** | Gone |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_delete**
> projects_delete(project_id)

Delete a project

Deletes a project board. Returns a `404 Not Found` status if projects are disabled.

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
    api_instance = github_openapi.ProjectsApi(api_client)
    project_id = 56 # int | The unique identifier of the project.

    try:
        # Delete a project
        api_instance.projects_delete(project_id)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The unique identifier of the project. | 

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
**204** | Delete Success |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |
**410** | Gone |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_delete_card**
> projects_delete_card(card_id)

Delete a project card

Deletes a project card

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
    api_instance = github_openapi.ProjectsApi(api_client)
    card_id = 56 # int | The unique identifier of the card.

    try:
        # Delete a project card
        api_instance.projects_delete_card(card_id)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_delete_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_id** | **int**| The unique identifier of the card. | 

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
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_delete_column**
> projects_delete_column(column_id)

Delete a project column

Deletes a project column.

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
    api_instance = github_openapi.ProjectsApi(api_client)
    column_id = 56 # int | The unique identifier of the column.

    try:
        # Delete a project column
        api_instance.projects_delete_column(column_id)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_delete_column: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **column_id** | **int**| The unique identifier of the column. | 

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
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get**
> Project projects_get(project_id)

Get a project

Gets a project by its `id`. Returns a `404 Not Found` status if projects are disabled. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned.

### Example


```python
import github_openapi
from github_openapi.models.project import Project
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
    api_instance = github_openapi.ProjectsApi(api_client)
    project_id = 56 # int | The unique identifier of the project.

    try:
        # Get a project
        api_response = api_instance.projects_get(project_id)
        print("The response of ProjectsApi->projects_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The unique identifier of the project. | 

### Return type

[**Project**](Project.md)

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
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get_card**
> ProjectCard projects_get_card(card_id)

Get a project card

Gets information about a project card.

### Example


```python
import github_openapi
from github_openapi.models.project_card import ProjectCard
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
    api_instance = github_openapi.ProjectsApi(api_client)
    card_id = 56 # int | The unique identifier of the card.

    try:
        # Get a project card
        api_response = api_instance.projects_get_card(card_id)
        print("The response of ProjectsApi->projects_get_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_get_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_id** | **int**| The unique identifier of the card. | 

### Return type

[**ProjectCard**](ProjectCard.md)

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
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get_column**
> ProjectColumn projects_get_column(column_id)

Get a project column

Gets information about a project column.

### Example


```python
import github_openapi
from github_openapi.models.project_column import ProjectColumn
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
    api_instance = github_openapi.ProjectsApi(api_client)
    column_id = 56 # int | The unique identifier of the column.

    try:
        # Get a project column
        api_response = api_instance.projects_get_column(column_id)
        print("The response of ProjectsApi->projects_get_column:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_get_column: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **column_id** | **int**| The unique identifier of the column. | 

### Return type

[**ProjectColumn**](ProjectColumn.md)

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
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_get_permission_for_user**
> ProjectCollaboratorPermission projects_get_permission_for_user(project_id, username)

Get project permission for a user

Returns the collaborator's permission level for an organization project. Possible values for the `permission` key: `admin`, `write`, `read`, `none`. You must be an organization owner or a project `admin` to review a user's permission level.

### Example


```python
import github_openapi
from github_openapi.models.project_collaborator_permission import ProjectCollaboratorPermission
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
    api_instance = github_openapi.ProjectsApi(api_client)
    project_id = 56 # int | The unique identifier of the project.
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Get project permission for a user
        api_response = api_instance.projects_get_permission_for_user(project_id, username)
        print("The response of ProjectsApi->projects_get_permission_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_get_permission_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The unique identifier of the project. | 
 **username** | **str**| The handle for the GitHub user account. | 

### Return type

[**ProjectCollaboratorPermission**](ProjectCollaboratorPermission.md)

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
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_list_cards**
> List[ProjectCard] projects_list_cards(column_id, archived_state=archived_state, per_page=per_page, page=page)

List project cards

Lists the project cards in a project.

### Example


```python
import github_openapi
from github_openapi.models.project_card import ProjectCard
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
    api_instance = github_openapi.ProjectsApi(api_client)
    column_id = 56 # int | The unique identifier of the column.
    archived_state = not_archived # str | Filters the project cards that are returned by the card's state. (optional) (default to not_archived)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List project cards
        api_response = api_instance.projects_list_cards(column_id, archived_state=archived_state, per_page=per_page, page=page)
        print("The response of ProjectsApi->projects_list_cards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_list_cards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **column_id** | **int**| The unique identifier of the column. | 
 **archived_state** | **str**| Filters the project cards that are returned by the card&#39;s state. | [optional] [default to not_archived]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[ProjectCard]**](ProjectCard.md)

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
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_list_collaborators**
> List[SimpleUser] projects_list_collaborators(project_id, affiliation=affiliation, per_page=per_page, page=page)

List project collaborators

Lists the collaborators for an organization project. For a project, the list of collaborators includes outside collaborators, organization members that are direct collaborators, organization members with access through team memberships, organization members with access through default organization permissions, and organization owners. You must be an organization owner or a project `admin` to list collaborators.

### Example


```python
import github_openapi
from github_openapi.models.simple_user import SimpleUser
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
    api_instance = github_openapi.ProjectsApi(api_client)
    project_id = 56 # int | The unique identifier of the project.
    affiliation = all # str | Filters the collaborators by their affiliation. `outside` means outside collaborators of a project that are not a member of the project's organization. `direct` means collaborators with permissions to a project, regardless of organization membership status. `all` means all collaborators the authenticated user can see. (optional) (default to all)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List project collaborators
        api_response = api_instance.projects_list_collaborators(project_id, affiliation=affiliation, per_page=per_page, page=page)
        print("The response of ProjectsApi->projects_list_collaborators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_list_collaborators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The unique identifier of the project. | 
 **affiliation** | **str**| Filters the collaborators by their affiliation. &#x60;outside&#x60; means outside collaborators of a project that are not a member of the project&#39;s organization. &#x60;direct&#x60; means collaborators with permissions to a project, regardless of organization membership status. &#x60;all&#x60; means all collaborators the authenticated user can see. | [optional] [default to all]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[SimpleUser]**](SimpleUser.md)

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
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_list_columns**
> List[ProjectColumn] projects_list_columns(project_id, per_page=per_page, page=page)

List project columns

Lists the project columns in a project.

### Example


```python
import github_openapi
from github_openapi.models.project_column import ProjectColumn
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
    api_instance = github_openapi.ProjectsApi(api_client)
    project_id = 56 # int | The unique identifier of the project.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List project columns
        api_response = api_instance.projects_list_columns(project_id, per_page=per_page, page=page)
        print("The response of ProjectsApi->projects_list_columns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_list_columns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The unique identifier of the project. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[ProjectColumn]**](ProjectColumn.md)

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
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_list_for_org**
> List[Project] projects_list_for_org(org, state=state, per_page=per_page, page=page)

List organization projects

Lists the projects in an organization. Returns a `404 Not Found` status if projects are disabled in the organization. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned.

### Example


```python
import github_openapi
from github_openapi.models.project import Project
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
    api_instance = github_openapi.ProjectsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    state = open # str | Indicates the state of the projects to return. (optional) (default to open)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List organization projects
        api_response = api_instance.projects_list_for_org(org, state=state, per_page=per_page, page=page)
        print("The response of ProjectsApi->projects_list_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_list_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **state** | **str**| Indicates the state of the projects to return. | [optional] [default to open]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Project]**](Project.md)

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

# **projects_list_for_repo**
> List[Project] projects_list_for_repo(owner, repo, state=state, per_page=per_page, page=page)

List repository projects

Lists the projects in a repository. Returns a `404 Not Found` status if projects are disabled in the repository. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned.

### Example


```python
import github_openapi
from github_openapi.models.project import Project
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
    api_instance = github_openapi.ProjectsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    state = open # str | Indicates the state of the projects to return. (optional) (default to open)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List repository projects
        api_response = api_instance.projects_list_for_repo(owner, repo, state=state, per_page=per_page, page=page)
        print("The response of ProjectsApi->projects_list_for_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_list_for_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **state** | **str**| Indicates the state of the projects to return. | [optional] [default to open]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Project]**](Project.md)

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
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**410** | Gone |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_list_for_user**
> List[Project] projects_list_for_user(username, state=state, per_page=per_page, page=page)

List user projects

Lists projects for a user.

### Example


```python
import github_openapi
from github_openapi.models.project import Project
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
    api_instance = github_openapi.ProjectsApi(api_client)
    username = 'username_example' # str | The handle for the GitHub user account.
    state = open # str | Indicates the state of the projects to return. (optional) (default to open)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List user projects
        api_response = api_instance.projects_list_for_user(username, state=state, per_page=per_page, page=page)
        print("The response of ProjectsApi->projects_list_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_list_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The handle for the GitHub user account. | 
 **state** | **str**| Indicates the state of the projects to return. | [optional] [default to open]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Project]**](Project.md)

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

# **projects_move_card**
> object projects_move_card(card_id, projects_move_card_request)

Move a project card



### Example


```python
import github_openapi
from github_openapi.models.projects_move_card_request import ProjectsMoveCardRequest
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
    api_instance = github_openapi.ProjectsApi(api_client)
    card_id = 56 # int | The unique identifier of the card.
    projects_move_card_request = {"column_id":42,"position":"bottom"} # ProjectsMoveCardRequest | 

    try:
        # Move a project card
        api_response = api_instance.projects_move_card(card_id, projects_move_card_request)
        print("The response of ProjectsApi->projects_move_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_move_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_id** | **int**| The unique identifier of the card. | 
 **projects_move_card_request** | [**ProjectsMoveCardRequest**](ProjectsMoveCardRequest.md)|  | 

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
**201** | Response |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |
**503** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_move_column**
> object projects_move_column(column_id, projects_move_column_request)

Move a project column



### Example


```python
import github_openapi
from github_openapi.models.projects_move_column_request import ProjectsMoveColumnRequest
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
    api_instance = github_openapi.ProjectsApi(api_client)
    column_id = 56 # int | The unique identifier of the column.
    projects_move_column_request = {"position":"last"} # ProjectsMoveColumnRequest | 

    try:
        # Move a project column
        api_response = api_instance.projects_move_column(column_id, projects_move_column_request)
        print("The response of ProjectsApi->projects_move_column:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_move_column: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **column_id** | **int**| The unique identifier of the column. | 
 **projects_move_column_request** | [**ProjectsMoveColumnRequest**](ProjectsMoveColumnRequest.md)|  | 

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
**201** | Response |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_remove_collaborator**
> projects_remove_collaborator(project_id, username)

Remove user as a collaborator

Removes a collaborator from an organization project. You must be an organization owner or a project `admin` to remove a collaborator.

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
    api_instance = github_openapi.ProjectsApi(api_client)
    project_id = 56 # int | The unique identifier of the project.
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Remove user as a collaborator
        api_instance.projects_remove_collaborator(project_id, username)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_remove_collaborator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The unique identifier of the project. | 
 **username** | **str**| The handle for the GitHub user account. | 

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
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_update**
> Project projects_update(project_id, projects_update_request=projects_update_request)

Update a project

Updates a project board's information. Returns a `404 Not Found` status if projects are disabled. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned.

### Example


```python
import github_openapi
from github_openapi.models.project import Project
from github_openapi.models.projects_update_request import ProjectsUpdateRequest
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
    api_instance = github_openapi.ProjectsApi(api_client)
    project_id = 56 # int | The unique identifier of the project.
    projects_update_request = {"name":"Week One Sprint","state":"open","organization_permission":"write"} # ProjectsUpdateRequest |  (optional)

    try:
        # Update a project
        api_response = api_instance.projects_update(project_id, projects_update_request=projects_update_request)
        print("The response of ProjectsApi->projects_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| The unique identifier of the project. | 
 **projects_update_request** | [**ProjectsUpdateRequest**](ProjectsUpdateRequest.md)|  | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Not Found if the authenticated user does not have access to the project |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |
**410** | Gone |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_update_card**
> ProjectCard projects_update_card(card_id, projects_update_card_request=projects_update_card_request)

Update an existing project card



### Example


```python
import github_openapi
from github_openapi.models.project_card import ProjectCard
from github_openapi.models.projects_update_card_request import ProjectsUpdateCardRequest
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
    api_instance = github_openapi.ProjectsApi(api_client)
    card_id = 56 # int | The unique identifier of the card.
    projects_update_card_request = {"note":"Add payload for delete Project column"} # ProjectsUpdateCardRequest |  (optional)

    try:
        # Update an existing project card
        api_response = api_instance.projects_update_card(card_id, projects_update_card_request=projects_update_card_request)
        print("The response of ProjectsApi->projects_update_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_update_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_id** | **int**| The unique identifier of the card. | 
 **projects_update_card_request** | [**ProjectsUpdateCardRequest**](ProjectsUpdateCardRequest.md)|  | [optional] 

### Return type

[**ProjectCard**](ProjectCard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_update_column**
> ProjectColumn projects_update_column(column_id, projects_update_column_request)

Update an existing project column



### Example


```python
import github_openapi
from github_openapi.models.project_column import ProjectColumn
from github_openapi.models.projects_update_column_request import ProjectsUpdateColumnRequest
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
    api_instance = github_openapi.ProjectsApi(api_client)
    column_id = 56 # int | The unique identifier of the column.
    projects_update_column_request = {"name":"To Do"} # ProjectsUpdateColumnRequest | 

    try:
        # Update an existing project column
        api_response = api_instance.projects_update_column(column_id, projects_update_column_request)
        print("The response of ProjectsApi->projects_update_column:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->projects_update_column: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **column_id** | **int**| The unique identifier of the column. | 
 **projects_update_column_request** | [**ProjectsUpdateColumnRequest**](ProjectsUpdateColumnRequest.md)|  | 

### Return type

[**ProjectColumn**](ProjectColumn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

