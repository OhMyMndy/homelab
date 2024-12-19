# github_openapi.CodespacesApi

All URIs are relative to *https://api.github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**codespaces_add_repository_for_secret_for_authenticated_user**](CodespacesApi.md#codespaces_add_repository_for_secret_for_authenticated_user) | **PUT** /user/codespaces/secrets/{secret_name}/repositories/{repository_id} | Add a selected repository to a user secret
[**codespaces_add_selected_repo_to_org_secret**](CodespacesApi.md#codespaces_add_selected_repo_to_org_secret) | **PUT** /orgs/{org}/codespaces/secrets/{secret_name}/repositories/{repository_id} | Add selected repository to an organization secret
[**codespaces_check_permissions_for_devcontainer**](CodespacesApi.md#codespaces_check_permissions_for_devcontainer) | **GET** /repos/{owner}/{repo}/codespaces/permissions_check | Check if permissions defined by a devcontainer have been accepted by the authenticated user
[**codespaces_codespace_machines_for_authenticated_user**](CodespacesApi.md#codespaces_codespace_machines_for_authenticated_user) | **GET** /user/codespaces/{codespace_name}/machines | List machine types for a codespace
[**codespaces_create_for_authenticated_user**](CodespacesApi.md#codespaces_create_for_authenticated_user) | **POST** /user/codespaces | Create a codespace for the authenticated user
[**codespaces_create_or_update_org_secret**](CodespacesApi.md#codespaces_create_or_update_org_secret) | **PUT** /orgs/{org}/codespaces/secrets/{secret_name} | Create or update an organization secret
[**codespaces_create_or_update_repo_secret**](CodespacesApi.md#codespaces_create_or_update_repo_secret) | **PUT** /repos/{owner}/{repo}/codespaces/secrets/{secret_name} | Create or update a repository secret
[**codespaces_create_or_update_secret_for_authenticated_user**](CodespacesApi.md#codespaces_create_or_update_secret_for_authenticated_user) | **PUT** /user/codespaces/secrets/{secret_name} | Create or update a secret for the authenticated user
[**codespaces_create_with_pr_for_authenticated_user**](CodespacesApi.md#codespaces_create_with_pr_for_authenticated_user) | **POST** /repos/{owner}/{repo}/pulls/{pull_number}/codespaces | Create a codespace from a pull request
[**codespaces_create_with_repo_for_authenticated_user**](CodespacesApi.md#codespaces_create_with_repo_for_authenticated_user) | **POST** /repos/{owner}/{repo}/codespaces | Create a codespace in a repository
[**codespaces_delete_codespaces_access_users**](CodespacesApi.md#codespaces_delete_codespaces_access_users) | **DELETE** /orgs/{org}/codespaces/access/selected_users | Remove users from Codespaces access for an organization
[**codespaces_delete_for_authenticated_user**](CodespacesApi.md#codespaces_delete_for_authenticated_user) | **DELETE** /user/codespaces/{codespace_name} | Delete a codespace for the authenticated user
[**codespaces_delete_from_organization**](CodespacesApi.md#codespaces_delete_from_organization) | **DELETE** /orgs/{org}/members/{username}/codespaces/{codespace_name} | Delete a codespace from the organization
[**codespaces_delete_org_secret**](CodespacesApi.md#codespaces_delete_org_secret) | **DELETE** /orgs/{org}/codespaces/secrets/{secret_name} | Delete an organization secret
[**codespaces_delete_repo_secret**](CodespacesApi.md#codespaces_delete_repo_secret) | **DELETE** /repos/{owner}/{repo}/codespaces/secrets/{secret_name} | Delete a repository secret
[**codespaces_delete_secret_for_authenticated_user**](CodespacesApi.md#codespaces_delete_secret_for_authenticated_user) | **DELETE** /user/codespaces/secrets/{secret_name} | Delete a secret for the authenticated user
[**codespaces_export_for_authenticated_user**](CodespacesApi.md#codespaces_export_for_authenticated_user) | **POST** /user/codespaces/{codespace_name}/exports | Export a codespace for the authenticated user
[**codespaces_get_codespaces_for_user_in_org**](CodespacesApi.md#codespaces_get_codespaces_for_user_in_org) | **GET** /orgs/{org}/members/{username}/codespaces | List codespaces for a user in organization
[**codespaces_get_export_details_for_authenticated_user**](CodespacesApi.md#codespaces_get_export_details_for_authenticated_user) | **GET** /user/codespaces/{codespace_name}/exports/{export_id} | Get details about a codespace export
[**codespaces_get_for_authenticated_user**](CodespacesApi.md#codespaces_get_for_authenticated_user) | **GET** /user/codespaces/{codespace_name} | Get a codespace for the authenticated user
[**codespaces_get_org_public_key**](CodespacesApi.md#codespaces_get_org_public_key) | **GET** /orgs/{org}/codespaces/secrets/public-key | Get an organization public key
[**codespaces_get_org_secret**](CodespacesApi.md#codespaces_get_org_secret) | **GET** /orgs/{org}/codespaces/secrets/{secret_name} | Get an organization secret
[**codespaces_get_public_key_for_authenticated_user**](CodespacesApi.md#codespaces_get_public_key_for_authenticated_user) | **GET** /user/codespaces/secrets/public-key | Get public key for the authenticated user
[**codespaces_get_repo_public_key**](CodespacesApi.md#codespaces_get_repo_public_key) | **GET** /repos/{owner}/{repo}/codespaces/secrets/public-key | Get a repository public key
[**codespaces_get_repo_secret**](CodespacesApi.md#codespaces_get_repo_secret) | **GET** /repos/{owner}/{repo}/codespaces/secrets/{secret_name} | Get a repository secret
[**codespaces_get_secret_for_authenticated_user**](CodespacesApi.md#codespaces_get_secret_for_authenticated_user) | **GET** /user/codespaces/secrets/{secret_name} | Get a secret for the authenticated user
[**codespaces_list_devcontainers_in_repository_for_authenticated_user**](CodespacesApi.md#codespaces_list_devcontainers_in_repository_for_authenticated_user) | **GET** /repos/{owner}/{repo}/codespaces/devcontainers | List devcontainer configurations in a repository for the authenticated user
[**codespaces_list_for_authenticated_user**](CodespacesApi.md#codespaces_list_for_authenticated_user) | **GET** /user/codespaces | List codespaces for the authenticated user
[**codespaces_list_in_organization**](CodespacesApi.md#codespaces_list_in_organization) | **GET** /orgs/{org}/codespaces | List codespaces for the organization
[**codespaces_list_in_repository_for_authenticated_user**](CodespacesApi.md#codespaces_list_in_repository_for_authenticated_user) | **GET** /repos/{owner}/{repo}/codespaces | List codespaces in a repository for the authenticated user
[**codespaces_list_org_secrets**](CodespacesApi.md#codespaces_list_org_secrets) | **GET** /orgs/{org}/codespaces/secrets | List organization secrets
[**codespaces_list_repo_secrets**](CodespacesApi.md#codespaces_list_repo_secrets) | **GET** /repos/{owner}/{repo}/codespaces/secrets | List repository secrets
[**codespaces_list_repositories_for_secret_for_authenticated_user**](CodespacesApi.md#codespaces_list_repositories_for_secret_for_authenticated_user) | **GET** /user/codespaces/secrets/{secret_name}/repositories | List selected repositories for a user secret
[**codespaces_list_secrets_for_authenticated_user**](CodespacesApi.md#codespaces_list_secrets_for_authenticated_user) | **GET** /user/codespaces/secrets | List secrets for the authenticated user
[**codespaces_list_selected_repos_for_org_secret**](CodespacesApi.md#codespaces_list_selected_repos_for_org_secret) | **GET** /orgs/{org}/codespaces/secrets/{secret_name}/repositories | List selected repositories for an organization secret
[**codespaces_pre_flight_with_repo_for_authenticated_user**](CodespacesApi.md#codespaces_pre_flight_with_repo_for_authenticated_user) | **GET** /repos/{owner}/{repo}/codespaces/new | Get default attributes for a codespace
[**codespaces_publish_for_authenticated_user**](CodespacesApi.md#codespaces_publish_for_authenticated_user) | **POST** /user/codespaces/{codespace_name}/publish | Create a repository from an unpublished codespace
[**codespaces_remove_repository_for_secret_for_authenticated_user**](CodespacesApi.md#codespaces_remove_repository_for_secret_for_authenticated_user) | **DELETE** /user/codespaces/secrets/{secret_name}/repositories/{repository_id} | Remove a selected repository from a user secret
[**codespaces_remove_selected_repo_from_org_secret**](CodespacesApi.md#codespaces_remove_selected_repo_from_org_secret) | **DELETE** /orgs/{org}/codespaces/secrets/{secret_name}/repositories/{repository_id} | Remove selected repository from an organization secret
[**codespaces_repo_machines_for_authenticated_user**](CodespacesApi.md#codespaces_repo_machines_for_authenticated_user) | **GET** /repos/{owner}/{repo}/codespaces/machines | List available machine types for a repository
[**codespaces_set_codespaces_access**](CodespacesApi.md#codespaces_set_codespaces_access) | **PUT** /orgs/{org}/codespaces/access | Manage access control for organization codespaces
[**codespaces_set_codespaces_access_users**](CodespacesApi.md#codespaces_set_codespaces_access_users) | **POST** /orgs/{org}/codespaces/access/selected_users | Add users to Codespaces access for an organization
[**codespaces_set_repositories_for_secret_for_authenticated_user**](CodespacesApi.md#codespaces_set_repositories_for_secret_for_authenticated_user) | **PUT** /user/codespaces/secrets/{secret_name}/repositories | Set selected repositories for a user secret
[**codespaces_set_selected_repos_for_org_secret**](CodespacesApi.md#codespaces_set_selected_repos_for_org_secret) | **PUT** /orgs/{org}/codespaces/secrets/{secret_name}/repositories | Set selected repositories for an organization secret
[**codespaces_start_for_authenticated_user**](CodespacesApi.md#codespaces_start_for_authenticated_user) | **POST** /user/codespaces/{codespace_name}/start | Start a codespace for the authenticated user
[**codespaces_stop_for_authenticated_user**](CodespacesApi.md#codespaces_stop_for_authenticated_user) | **POST** /user/codespaces/{codespace_name}/stop | Stop a codespace for the authenticated user
[**codespaces_stop_in_organization**](CodespacesApi.md#codespaces_stop_in_organization) | **POST** /orgs/{org}/members/{username}/codespaces/{codespace_name}/stop | Stop a codespace for an organization user
[**codespaces_update_for_authenticated_user**](CodespacesApi.md#codespaces_update_for_authenticated_user) | **PATCH** /user/codespaces/{codespace_name} | Update a codespace for the authenticated user


# **codespaces_add_repository_for_secret_for_authenticated_user**
> codespaces_add_repository_for_secret_for_authenticated_user(secret_name, repository_id)

Add a selected repository to a user secret

Adds a repository to the selected repositories for a user's development environment secret.  The authenticated user must have Codespaces access to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `codespace` or `codespace:secrets` scope to use this endpoint.

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
    api_instance = github_openapi.CodespacesApi(api_client)
    secret_name = 'secret_name_example' # str | The name of the secret.
    repository_id = 56 # int | 

    try:
        # Add a selected repository to a user secret
        api_instance.codespaces_add_repository_for_secret_for_authenticated_user(secret_name, repository_id)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_add_repository_for_secret_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_name** | **str**| The name of the secret. | 
 **repository_id** | **int**|  | 

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
**204** | No Content when repository was added to the selected list |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_add_selected_repo_to_org_secret**
> codespaces_add_selected_repo_to_org_secret(org, secret_name, repository_id)

Add selected repository to an organization secret

Adds a repository to an organization development environment secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://docs.github.com/rest/codespaces/organization-secrets#create-or-update-an-organization-secret). OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

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
    api_instance = github_openapi.CodespacesApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    secret_name = 'secret_name_example' # str | The name of the secret.
    repository_id = 56 # int | 

    try:
        # Add selected repository to an organization secret
        api_instance.codespaces_add_selected_repo_to_org_secret(org, secret_name, repository_id)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_add_selected_repo_to_org_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **secret_name** | **str**| The name of the secret. | 
 **repository_id** | **int**|  | 

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
**204** | No Content when repository was added to the selected list |  -  |
**404** | Resource not found |  -  |
**409** | Conflict when visibility type is not set to selected |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_check_permissions_for_devcontainer**
> CodespacesPermissionsCheckForDevcontainer codespaces_check_permissions_for_devcontainer(owner, repo, ref, devcontainer_path)

Check if permissions defined by a devcontainer have been accepted by the authenticated user

Checks whether the permissions defined by a given devcontainer configuration have been accepted by the authenticated user.  OAuth app tokens and personal access tokens (classic) need the `codespace` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespaces_permissions_check_for_devcontainer import CodespacesPermissionsCheckForDevcontainer
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
    api_instance = github_openapi.CodespacesApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    ref = 'master' # str | The git reference that points to the location of the devcontainer configuration to use for the permission check. The value of `ref` will typically be a branch name (`heads/BRANCH_NAME`). For more information, see \"[Git References](https://git-scm.com/book/en/v2/Git-Internals-Git-References)\" in the Git documentation.
    devcontainer_path = '.devcontainer/example/devcontainer.json' # str | Path to the devcontainer.json configuration to use for the permission check.

    try:
        # Check if permissions defined by a devcontainer have been accepted by the authenticated user
        api_response = api_instance.codespaces_check_permissions_for_devcontainer(owner, repo, ref, devcontainer_path)
        print("The response of CodespacesApi->codespaces_check_permissions_for_devcontainer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_check_permissions_for_devcontainer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **ref** | **str**| The git reference that points to the location of the devcontainer configuration to use for the permission check. The value of &#x60;ref&#x60; will typically be a branch name (&#x60;heads/BRANCH_NAME&#x60;). For more information, see \&quot;[Git References](https://git-scm.com/book/en/v2/Git-Internals-Git-References)\&quot; in the Git documentation. | 
 **devcontainer_path** | **str**| Path to the devcontainer.json configuration to use for the permission check. | 

### Return type

[**CodespacesPermissionsCheckForDevcontainer**](CodespacesPermissionsCheckForDevcontainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response when the permission check is successful |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_codespace_machines_for_authenticated_user**
> CodespacesRepoMachinesForAuthenticatedUser200Response codespaces_codespace_machines_for_authenticated_user(codespace_name)

List machine types for a codespace

List the machine types a codespace can transition to use.  OAuth app tokens and personal access tokens (classic) need the `codespace` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespaces_repo_machines_for_authenticated_user200_response import CodespacesRepoMachinesForAuthenticatedUser200Response
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
    api_instance = github_openapi.CodespacesApi(api_client)
    codespace_name = 'codespace_name_example' # str | The name of the codespace.

    try:
        # List machine types for a codespace
        api_response = api_instance.codespaces_codespace_machines_for_authenticated_user(codespace_name)
        print("The response of CodespacesApi->codespaces_codespace_machines_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_codespace_machines_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **codespace_name** | **str**| The name of the codespace. | 

### Return type

[**CodespacesRepoMachinesForAuthenticatedUser200Response**](CodespacesRepoMachinesForAuthenticatedUser200Response.md)

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
**500** | Internal Error |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_create_for_authenticated_user**
> Codespace codespaces_create_for_authenticated_user(codespaces_create_for_authenticated_user_request)

Create a codespace for the authenticated user

Creates a new codespace, owned by the authenticated user.  This endpoint requires either a `repository_id` OR a `pull_request` but not both.  OAuth app tokens and personal access tokens (classic) need the `codespace` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespace import Codespace
from github_openapi.models.codespaces_create_for_authenticated_user_request import CodespacesCreateForAuthenticatedUserRequest
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
    api_instance = github_openapi.CodespacesApi(api_client)
    codespaces_create_for_authenticated_user_request = {"repository_id":1,"ref":"main","geo":"UsWest"} # CodespacesCreateForAuthenticatedUserRequest | 

    try:
        # Create a codespace for the authenticated user
        api_response = api_instance.codespaces_create_for_authenticated_user(codespaces_create_for_authenticated_user_request)
        print("The response of CodespacesApi->codespaces_create_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_create_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **codespaces_create_for_authenticated_user_request** | [**CodespacesCreateForAuthenticatedUserRequest**](CodespacesCreateForAuthenticatedUserRequest.md)|  | 

### Return type

[**Codespace**](Codespace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response when the codespace was successfully created |  -  |
**202** | Response when the codespace creation partially failed but is being retried in the background |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_create_or_update_org_secret**
> object codespaces_create_or_update_org_secret(org, secret_name, codespaces_create_or_update_org_secret_request)

Create or update an organization secret

Creates or updates an organization development environment secret with an encrypted value. Encrypt your secret using [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). For more information, see \"[Encrypting secrets for the REST API](https://docs.github.com/rest/guides/encrypting-secrets-for-the-rest-api).\"  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespaces_create_or_update_org_secret_request import CodespacesCreateOrUpdateOrgSecretRequest
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
    api_instance = github_openapi.CodespacesApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    secret_name = 'secret_name_example' # str | The name of the secret.
    codespaces_create_or_update_org_secret_request = {"encrypted_value":"c2VjcmV0","key_id":"012345678912345678","visibility":"selected","selected_repository_ids":[1296269,1296280]} # CodespacesCreateOrUpdateOrgSecretRequest | 

    try:
        # Create or update an organization secret
        api_response = api_instance.codespaces_create_or_update_org_secret(org, secret_name, codespaces_create_or_update_org_secret_request)
        print("The response of CodespacesApi->codespaces_create_or_update_org_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_create_or_update_org_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **secret_name** | **str**| The name of the secret. | 
 **codespaces_create_or_update_org_secret_request** | [**CodespacesCreateOrUpdateOrgSecretRequest**](CodespacesCreateOrUpdateOrgSecretRequest.md)|  | 

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
**201** | Response when creating a secret |  -  |
**204** | Response when updating a secret |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_create_or_update_repo_secret**
> object codespaces_create_or_update_repo_secret(owner, repo, secret_name, codespaces_create_or_update_repo_secret_request)

Create or update a repository secret

Creates or updates a repository development environment secret with an encrypted value. Encrypt your secret using [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). For more information, see \"[Encrypting secrets for the REST API](https://docs.github.com/rest/guides/encrypting-secrets-for-the-rest-api).\"  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespaces_create_or_update_repo_secret_request import CodespacesCreateOrUpdateRepoSecretRequest
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
    api_instance = github_openapi.CodespacesApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    secret_name = 'secret_name_example' # str | The name of the secret.
    codespaces_create_or_update_repo_secret_request = {"encrypted_value":"c2VjcmV0","key_id":"012345678912345678"} # CodespacesCreateOrUpdateRepoSecretRequest | 

    try:
        # Create or update a repository secret
        api_response = api_instance.codespaces_create_or_update_repo_secret(owner, repo, secret_name, codespaces_create_or_update_repo_secret_request)
        print("The response of CodespacesApi->codespaces_create_or_update_repo_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_create_or_update_repo_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **secret_name** | **str**| The name of the secret. | 
 **codespaces_create_or_update_repo_secret_request** | [**CodespacesCreateOrUpdateRepoSecretRequest**](CodespacesCreateOrUpdateRepoSecretRequest.md)|  | 

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
**201** | Response when creating a secret |  -  |
**204** | Response when updating a secret |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_create_or_update_secret_for_authenticated_user**
> object codespaces_create_or_update_secret_for_authenticated_user(secret_name, codespaces_create_or_update_secret_for_authenticated_user_request)

Create or update a secret for the authenticated user

Creates or updates a development environment secret for a user's codespace with an encrypted value. Encrypt your secret using [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). For more information, see \"[Encrypting secrets for the REST API](https://docs.github.com/rest/guides/encrypting-secrets-for-the-rest-api).\"  The authenticated user must have Codespaces access to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `codespace` or `codespace:secrets` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespaces_create_or_update_secret_for_authenticated_user_request import CodespacesCreateOrUpdateSecretForAuthenticatedUserRequest
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
    api_instance = github_openapi.CodespacesApi(api_client)
    secret_name = 'secret_name_example' # str | The name of the secret.
    codespaces_create_or_update_secret_for_authenticated_user_request = {"encrypted_value":"c2VjcmV0","key_id":"012345678912345678","selected_repository_ids":["1234567","2345678"]} # CodespacesCreateOrUpdateSecretForAuthenticatedUserRequest | 

    try:
        # Create or update a secret for the authenticated user
        api_response = api_instance.codespaces_create_or_update_secret_for_authenticated_user(secret_name, codespaces_create_or_update_secret_for_authenticated_user_request)
        print("The response of CodespacesApi->codespaces_create_or_update_secret_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_create_or_update_secret_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_name** | **str**| The name of the secret. | 
 **codespaces_create_or_update_secret_for_authenticated_user_request** | [**CodespacesCreateOrUpdateSecretForAuthenticatedUserRequest**](CodespacesCreateOrUpdateSecretForAuthenticatedUserRequest.md)|  | 

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
**201** | Response after successfully creating a secret |  -  |
**204** | Response after successfully updating a secret |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_create_with_pr_for_authenticated_user**
> Codespace codespaces_create_with_pr_for_authenticated_user(owner, repo, pull_number, codespaces_create_with_pr_for_authenticated_user_request)

Create a codespace from a pull request

Creates a codespace owned by the authenticated user for the specified pull request.  OAuth app tokens and personal access tokens (classic) need the `codespace` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespace import Codespace
from github_openapi.models.codespaces_create_with_pr_for_authenticated_user_request import CodespacesCreateWithPrForAuthenticatedUserRequest
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
    api_instance = github_openapi.CodespacesApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    pull_number = 56 # int | The number that identifies the pull request.
    codespaces_create_with_pr_for_authenticated_user_request = {"repository_id":1,"ref":"main"} # CodespacesCreateWithPrForAuthenticatedUserRequest | 

    try:
        # Create a codespace from a pull request
        api_response = api_instance.codespaces_create_with_pr_for_authenticated_user(owner, repo, pull_number, codespaces_create_with_pr_for_authenticated_user_request)
        print("The response of CodespacesApi->codespaces_create_with_pr_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_create_with_pr_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **pull_number** | **int**| The number that identifies the pull request. | 
 **codespaces_create_with_pr_for_authenticated_user_request** | [**CodespacesCreateWithPrForAuthenticatedUserRequest**](CodespacesCreateWithPrForAuthenticatedUserRequest.md)|  | 

### Return type

[**Codespace**](Codespace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response when the codespace was successfully created |  -  |
**202** | Response when the codespace creation partially failed but is being retried in the background |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_create_with_repo_for_authenticated_user**
> Codespace codespaces_create_with_repo_for_authenticated_user(owner, repo, codespaces_create_with_repo_for_authenticated_user_request)

Create a codespace in a repository

Creates a codespace owned by the authenticated user in the specified repository.  OAuth app tokens and personal access tokens (classic) need the `codespace` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespace import Codespace
from github_openapi.models.codespaces_create_with_repo_for_authenticated_user_request import CodespacesCreateWithRepoForAuthenticatedUserRequest
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
    api_instance = github_openapi.CodespacesApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    codespaces_create_with_repo_for_authenticated_user_request = {"ref":"main","machine":"standardLinux32gb"} # CodespacesCreateWithRepoForAuthenticatedUserRequest | 

    try:
        # Create a codespace in a repository
        api_response = api_instance.codespaces_create_with_repo_for_authenticated_user(owner, repo, codespaces_create_with_repo_for_authenticated_user_request)
        print("The response of CodespacesApi->codespaces_create_with_repo_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_create_with_repo_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **codespaces_create_with_repo_for_authenticated_user_request** | [**CodespacesCreateWithRepoForAuthenticatedUserRequest**](CodespacesCreateWithRepoForAuthenticatedUserRequest.md)|  | 

### Return type

[**Codespace**](Codespace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response when the codespace was successfully created |  -  |
**202** | Response when the codespace creation partially failed but is being retried in the background |  -  |
**400** | Bad Request |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_delete_codespaces_access_users**
> codespaces_delete_codespaces_access_users(org, codespaces_delete_codespaces_access_users_request)

Remove users from Codespaces access for an organization

Codespaces for the specified users will no longer be billed to the organization.  To use this endpoint, the access settings for the organization must be set to `selected_members`. For information on how to change this setting, see \"[Manage access control for organization codespaces](https://docs.github.com/rest/codespaces/organizations#manage-access-control-for-organization-codespaces).\"  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespaces_delete_codespaces_access_users_request import CodespacesDeleteCodespacesAccessUsersRequest
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
    api_instance = github_openapi.CodespacesApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    codespaces_delete_codespaces_access_users_request = {"selected_usernames":["johnDoe","atomIO"]} # CodespacesDeleteCodespacesAccessUsersRequest | 

    try:
        # Remove users from Codespaces access for an organization
        api_instance.codespaces_delete_codespaces_access_users(org, codespaces_delete_codespaces_access_users_request)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_delete_codespaces_access_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **codespaces_delete_codespaces_access_users_request** | [**CodespacesDeleteCodespacesAccessUsersRequest**](CodespacesDeleteCodespacesAccessUsersRequest.md)|  | 

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
**204** | Response when successfully modifying permissions. |  -  |
**304** | Not modified |  -  |
**400** | Users are neither members nor collaborators of this organization. |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_delete_for_authenticated_user**
> object codespaces_delete_for_authenticated_user(codespace_name)

Delete a codespace for the authenticated user

Deletes a user's codespace.  OAuth app tokens and personal access tokens (classic) need the `codespace` scope to use this endpoint.

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
    api_instance = github_openapi.CodespacesApi(api_client)
    codespace_name = 'codespace_name_example' # str | The name of the codespace.

    try:
        # Delete a codespace for the authenticated user
        api_response = api_instance.codespaces_delete_for_authenticated_user(codespace_name)
        print("The response of CodespacesApi->codespaces_delete_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_delete_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **codespace_name** | **str**| The name of the codespace. | 

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
**202** | Accepted |  -  |
**304** | Not modified |  -  |
**500** | Internal Error |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_delete_from_organization**
> object codespaces_delete_from_organization(org, username, codespace_name)

Delete a codespace from the organization

Deletes a user's codespace.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

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
    api_instance = github_openapi.CodespacesApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    username = 'username_example' # str | The handle for the GitHub user account.
    codespace_name = 'codespace_name_example' # str | The name of the codespace.

    try:
        # Delete a codespace from the organization
        api_response = api_instance.codespaces_delete_from_organization(org, username, codespace_name)
        print("The response of CodespacesApi->codespaces_delete_from_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_delete_from_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **username** | **str**| The handle for the GitHub user account. | 
 **codespace_name** | **str**| The name of the codespace. | 

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
**202** | Accepted |  -  |
**304** | Not modified |  -  |
**500** | Internal Error |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_delete_org_secret**
> codespaces_delete_org_secret(org, secret_name)

Delete an organization secret

Deletes an organization development environment secret using the secret name.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

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
    api_instance = github_openapi.CodespacesApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    secret_name = 'secret_name_example' # str | The name of the secret.

    try:
        # Delete an organization secret
        api_instance.codespaces_delete_org_secret(org, secret_name)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_delete_org_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **secret_name** | **str**| The name of the secret. | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_delete_repo_secret**
> codespaces_delete_repo_secret(owner, repo, secret_name)

Delete a repository secret

Deletes a development environment secret in a repository using the secret name.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

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
    api_instance = github_openapi.CodespacesApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    secret_name = 'secret_name_example' # str | The name of the secret.

    try:
        # Delete a repository secret
        api_instance.codespaces_delete_repo_secret(owner, repo, secret_name)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_delete_repo_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **secret_name** | **str**| The name of the secret. | 

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

# **codespaces_delete_secret_for_authenticated_user**
> codespaces_delete_secret_for_authenticated_user(secret_name)

Delete a secret for the authenticated user

Deletes a development environment secret from a user's codespaces using the secret name. Deleting the secret will remove access from all codespaces that were allowed to access the secret.  The authenticated user must have Codespaces access to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `codespace` or `codespace:secrets` scope to use this endpoint.

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
    api_instance = github_openapi.CodespacesApi(api_client)
    secret_name = 'secret_name_example' # str | The name of the secret.

    try:
        # Delete a secret for the authenticated user
        api_instance.codespaces_delete_secret_for_authenticated_user(secret_name)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_delete_secret_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_name** | **str**| The name of the secret. | 

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

# **codespaces_export_for_authenticated_user**
> CodespaceExportDetails codespaces_export_for_authenticated_user(codespace_name)

Export a codespace for the authenticated user

Triggers an export of the specified codespace and returns a URL and ID where the status of the export can be monitored.  If changes cannot be pushed to the codespace's repository, they will be pushed to a new or previously-existing fork instead.  OAuth app tokens and personal access tokens (classic) need the `codespace` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespace_export_details import CodespaceExportDetails
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
    api_instance = github_openapi.CodespacesApi(api_client)
    codespace_name = 'codespace_name_example' # str | The name of the codespace.

    try:
        # Export a codespace for the authenticated user
        api_response = api_instance.codespaces_export_for_authenticated_user(codespace_name)
        print("The response of CodespacesApi->codespaces_export_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_export_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **codespace_name** | **str**| The name of the codespace. | 

### Return type

[**CodespaceExportDetails**](CodespaceExportDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Response |  -  |
**500** | Internal Error |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_get_codespaces_for_user_in_org**
> CodespacesListInOrganization200Response codespaces_get_codespaces_for_user_in_org(org, username, per_page=per_page, page=page)

List codespaces for a user in organization

Lists the codespaces that a member of an organization has for repositories in that organization.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespaces_list_in_organization200_response import CodespacesListInOrganization200Response
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
    api_instance = github_openapi.CodespacesApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    username = 'username_example' # str | The handle for the GitHub user account.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List codespaces for a user in organization
        api_response = api_instance.codespaces_get_codespaces_for_user_in_org(org, username, per_page=per_page, page=page)
        print("The response of CodespacesApi->codespaces_get_codespaces_for_user_in_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_get_codespaces_for_user_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **username** | **str**| The handle for the GitHub user account. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**CodespacesListInOrganization200Response**](CodespacesListInOrganization200Response.md)

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
**500** | Internal Error |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_get_export_details_for_authenticated_user**
> CodespaceExportDetails codespaces_get_export_details_for_authenticated_user(codespace_name, export_id)

Get details about a codespace export

Gets information about an export of a codespace.  OAuth app tokens and personal access tokens (classic) need the `codespace` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespace_export_details import CodespaceExportDetails
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
    api_instance = github_openapi.CodespacesApi(api_client)
    codespace_name = 'codespace_name_example' # str | The name of the codespace.
    export_id = 'export_id_example' # str | The ID of the export operation, or `latest`. Currently only `latest` is currently supported.

    try:
        # Get details about a codespace export
        api_response = api_instance.codespaces_get_export_details_for_authenticated_user(codespace_name, export_id)
        print("The response of CodespacesApi->codespaces_get_export_details_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_get_export_details_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **codespace_name** | **str**| The name of the codespace. | 
 **export_id** | **str**| The ID of the export operation, or &#x60;latest&#x60;. Currently only &#x60;latest&#x60; is currently supported. | 

### Return type

[**CodespaceExportDetails**](CodespaceExportDetails.md)

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

# **codespaces_get_for_authenticated_user**
> Codespace codespaces_get_for_authenticated_user(codespace_name)

Get a codespace for the authenticated user

Gets information about a user's codespace.  OAuth app tokens and personal access tokens (classic) need the `codespace` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespace import Codespace
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
    api_instance = github_openapi.CodespacesApi(api_client)
    codespace_name = 'codespace_name_example' # str | The name of the codespace.

    try:
        # Get a codespace for the authenticated user
        api_response = api_instance.codespaces_get_for_authenticated_user(codespace_name)
        print("The response of CodespacesApi->codespaces_get_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_get_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **codespace_name** | **str**| The name of the codespace. | 

### Return type

[**Codespace**](Codespace.md)

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
**500** | Internal Error |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_get_org_public_key**
> CodespacesPublicKey codespaces_get_org_public_key(org)

Get an organization public key

Gets a public key for an organization, which is required in order to encrypt secrets. You need to encrypt the value of a secret before you can create or update secrets. OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespaces_public_key import CodespacesPublicKey
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
    api_instance = github_openapi.CodespacesApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.

    try:
        # Get an organization public key
        api_response = api_instance.codespaces_get_org_public_key(org)
        print("The response of CodespacesApi->codespaces_get_org_public_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_get_org_public_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 

### Return type

[**CodespacesPublicKey**](CodespacesPublicKey.md)

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

# **codespaces_get_org_secret**
> CodespacesOrgSecret codespaces_get_org_secret(org, secret_name)

Get an organization secret

Gets an organization development environment secret without revealing its encrypted value.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespaces_org_secret import CodespacesOrgSecret
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
    api_instance = github_openapi.CodespacesApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    secret_name = 'secret_name_example' # str | The name of the secret.

    try:
        # Get an organization secret
        api_response = api_instance.codespaces_get_org_secret(org, secret_name)
        print("The response of CodespacesApi->codespaces_get_org_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_get_org_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **secret_name** | **str**| The name of the secret. | 

### Return type

[**CodespacesOrgSecret**](CodespacesOrgSecret.md)

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

# **codespaces_get_public_key_for_authenticated_user**
> CodespacesUserPublicKey codespaces_get_public_key_for_authenticated_user()

Get public key for the authenticated user

Gets your public key, which you need to encrypt secrets. You need to encrypt a secret before you can create or update secrets.  The authenticated user must have Codespaces access to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `codespace` or `codespace:secrets` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespaces_user_public_key import CodespacesUserPublicKey
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
    api_instance = github_openapi.CodespacesApi(api_client)

    try:
        # Get public key for the authenticated user
        api_response = api_instance.codespaces_get_public_key_for_authenticated_user()
        print("The response of CodespacesApi->codespaces_get_public_key_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_get_public_key_for_authenticated_user: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CodespacesUserPublicKey**](CodespacesUserPublicKey.md)

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

# **codespaces_get_repo_public_key**
> CodespacesPublicKey codespaces_get_repo_public_key(owner, repo)

Get a repository public key

Gets your public key, which you need to encrypt secrets. You need to encrypt a secret before you can create or update secrets.  If the repository is private, OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespaces_public_key import CodespacesPublicKey
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
    api_instance = github_openapi.CodespacesApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Get a repository public key
        api_response = api_instance.codespaces_get_repo_public_key(owner, repo)
        print("The response of CodespacesApi->codespaces_get_repo_public_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_get_repo_public_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**CodespacesPublicKey**](CodespacesPublicKey.md)

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

# **codespaces_get_repo_secret**
> RepoCodespacesSecret codespaces_get_repo_secret(owner, repo, secret_name)

Get a repository secret

Gets a single repository development environment secret without revealing its encrypted value.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.repo_codespaces_secret import RepoCodespacesSecret
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
    api_instance = github_openapi.CodespacesApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    secret_name = 'secret_name_example' # str | The name of the secret.

    try:
        # Get a repository secret
        api_response = api_instance.codespaces_get_repo_secret(owner, repo, secret_name)
        print("The response of CodespacesApi->codespaces_get_repo_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_get_repo_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **secret_name** | **str**| The name of the secret. | 

### Return type

[**RepoCodespacesSecret**](RepoCodespacesSecret.md)

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

# **codespaces_get_secret_for_authenticated_user**
> CodespacesSecret codespaces_get_secret_for_authenticated_user(secret_name)

Get a secret for the authenticated user

Gets a development environment secret available to a user's codespaces without revealing its encrypted value.  The authenticated user must have Codespaces access to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `codespace` or `codespace:secrets` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespaces_secret import CodespacesSecret
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
    api_instance = github_openapi.CodespacesApi(api_client)
    secret_name = 'secret_name_example' # str | The name of the secret.

    try:
        # Get a secret for the authenticated user
        api_response = api_instance.codespaces_get_secret_for_authenticated_user(secret_name)
        print("The response of CodespacesApi->codespaces_get_secret_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_get_secret_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_name** | **str**| The name of the secret. | 

### Return type

[**CodespacesSecret**](CodespacesSecret.md)

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

# **codespaces_list_devcontainers_in_repository_for_authenticated_user**
> CodespacesListDevcontainersInRepositoryForAuthenticatedUser200Response codespaces_list_devcontainers_in_repository_for_authenticated_user(owner, repo, per_page=per_page, page=page)

List devcontainer configurations in a repository for the authenticated user

Lists the devcontainer.json files associated with a specified repository and the authenticated user. These files specify launchpoint configurations for codespaces created within the repository.  OAuth app tokens and personal access tokens (classic) need the `codespace` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespaces_list_devcontainers_in_repository_for_authenticated_user200_response import CodespacesListDevcontainersInRepositoryForAuthenticatedUser200Response
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
    api_instance = github_openapi.CodespacesApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List devcontainer configurations in a repository for the authenticated user
        api_response = api_instance.codespaces_list_devcontainers_in_repository_for_authenticated_user(owner, repo, per_page=per_page, page=page)
        print("The response of CodespacesApi->codespaces_list_devcontainers_in_repository_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_list_devcontainers_in_repository_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**CodespacesListDevcontainersInRepositoryForAuthenticatedUser200Response**](CodespacesListDevcontainersInRepositoryForAuthenticatedUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**500** | Internal Error |  -  |
**400** | Bad Request |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_list_for_authenticated_user**
> CodespacesListInOrganization200Response codespaces_list_for_authenticated_user(per_page=per_page, page=page, repository_id=repository_id)

List codespaces for the authenticated user

Lists the authenticated user's codespaces.  OAuth app tokens and personal access tokens (classic) need the `codespace` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespaces_list_in_organization200_response import CodespacesListInOrganization200Response
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
    api_instance = github_openapi.CodespacesApi(api_client)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    repository_id = 56 # int | ID of the Repository to filter on (optional)

    try:
        # List codespaces for the authenticated user
        api_response = api_instance.codespaces_list_for_authenticated_user(per_page=per_page, page=page, repository_id=repository_id)
        print("The response of CodespacesApi->codespaces_list_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_list_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **repository_id** | **int**| ID of the Repository to filter on | [optional] 

### Return type

[**CodespacesListInOrganization200Response**](CodespacesListInOrganization200Response.md)

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
**500** | Internal Error |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_list_in_organization**
> CodespacesListInOrganization200Response codespaces_list_in_organization(org, per_page=per_page, page=page)

List codespaces for the organization

Lists the codespaces associated to a specified organization.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespaces_list_in_organization200_response import CodespacesListInOrganization200Response
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
    api_instance = github_openapi.CodespacesApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List codespaces for the organization
        api_response = api_instance.codespaces_list_in_organization(org, per_page=per_page, page=page)
        print("The response of CodespacesApi->codespaces_list_in_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_list_in_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**CodespacesListInOrganization200Response**](CodespacesListInOrganization200Response.md)

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
**500** | Internal Error |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_list_in_repository_for_authenticated_user**
> CodespacesListInOrganization200Response codespaces_list_in_repository_for_authenticated_user(owner, repo, per_page=per_page, page=page)

List codespaces in a repository for the authenticated user

Lists the codespaces associated to a specified repository and the authenticated user.  OAuth app tokens and personal access tokens (classic) need the `codespace` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespaces_list_in_organization200_response import CodespacesListInOrganization200Response
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
    api_instance = github_openapi.CodespacesApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List codespaces in a repository for the authenticated user
        api_response = api_instance.codespaces_list_in_repository_for_authenticated_user(owner, repo, per_page=per_page, page=page)
        print("The response of CodespacesApi->codespaces_list_in_repository_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_list_in_repository_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**CodespacesListInOrganization200Response**](CodespacesListInOrganization200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**500** | Internal Error |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_list_org_secrets**
> CodespacesListOrgSecrets200Response codespaces_list_org_secrets(org, per_page=per_page, page=page)

List organization secrets

Lists all Codespaces development environment secrets available at the organization-level without revealing their encrypted values.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespaces_list_org_secrets200_response import CodespacesListOrgSecrets200Response
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
    api_instance = github_openapi.CodespacesApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List organization secrets
        api_response = api_instance.codespaces_list_org_secrets(org, per_page=per_page, page=page)
        print("The response of CodespacesApi->codespaces_list_org_secrets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_list_org_secrets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**CodespacesListOrgSecrets200Response**](CodespacesListOrgSecrets200Response.md)

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

# **codespaces_list_repo_secrets**
> CodespacesListRepoSecrets200Response codespaces_list_repo_secrets(owner, repo, per_page=per_page, page=page)

List repository secrets

Lists all development environment secrets available in a repository without revealing their encrypted values.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespaces_list_repo_secrets200_response import CodespacesListRepoSecrets200Response
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
    api_instance = github_openapi.CodespacesApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List repository secrets
        api_response = api_instance.codespaces_list_repo_secrets(owner, repo, per_page=per_page, page=page)
        print("The response of CodespacesApi->codespaces_list_repo_secrets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_list_repo_secrets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**CodespacesListRepoSecrets200Response**](CodespacesListRepoSecrets200Response.md)

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

# **codespaces_list_repositories_for_secret_for_authenticated_user**
> ActionsListSelectedReposForOrgSecret200Response codespaces_list_repositories_for_secret_for_authenticated_user(secret_name)

List selected repositories for a user secret

List the repositories that have been granted the ability to use a user's development environment secret.  The authenticated user must have Codespaces access to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `codespace` or `codespace:secrets` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_selected_repos_for_org_secret200_response import ActionsListSelectedReposForOrgSecret200Response
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
    api_instance = github_openapi.CodespacesApi(api_client)
    secret_name = 'secret_name_example' # str | The name of the secret.

    try:
        # List selected repositories for a user secret
        api_response = api_instance.codespaces_list_repositories_for_secret_for_authenticated_user(secret_name)
        print("The response of CodespacesApi->codespaces_list_repositories_for_secret_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_list_repositories_for_secret_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_name** | **str**| The name of the secret. | 

### Return type

[**ActionsListSelectedReposForOrgSecret200Response**](ActionsListSelectedReposForOrgSecret200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_list_secrets_for_authenticated_user**
> CodespacesListSecretsForAuthenticatedUser200Response codespaces_list_secrets_for_authenticated_user(per_page=per_page, page=page)

List secrets for the authenticated user

Lists all development environment secrets available for a user's codespaces without revealing their encrypted values.  The authenticated user must have Codespaces access to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `codespace` or `codespace:secrets` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespaces_list_secrets_for_authenticated_user200_response import CodespacesListSecretsForAuthenticatedUser200Response
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
    api_instance = github_openapi.CodespacesApi(api_client)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List secrets for the authenticated user
        api_response = api_instance.codespaces_list_secrets_for_authenticated_user(per_page=per_page, page=page)
        print("The response of CodespacesApi->codespaces_list_secrets_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_list_secrets_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**CodespacesListSecretsForAuthenticatedUser200Response**](CodespacesListSecretsForAuthenticatedUser200Response.md)

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

# **codespaces_list_selected_repos_for_org_secret**
> ActionsListSelectedReposForOrgSecret200Response codespaces_list_selected_repos_for_org_secret(org, secret_name, page=page, per_page=per_page)

List selected repositories for an organization secret

Lists all repositories that have been selected when the `visibility` for repository access to a secret is set to `selected`.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_list_selected_repos_for_org_secret200_response import ActionsListSelectedReposForOrgSecret200Response
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
    api_instance = github_openapi.CodespacesApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    secret_name = 'secret_name_example' # str | The name of the secret.
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)

    try:
        # List selected repositories for an organization secret
        api_response = api_instance.codespaces_list_selected_repos_for_org_secret(org, secret_name, page=page, per_page=per_page)
        print("The response of CodespacesApi->codespaces_list_selected_repos_for_org_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_list_selected_repos_for_org_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **secret_name** | **str**| The name of the secret. | 
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]

### Return type

[**ActionsListSelectedReposForOrgSecret200Response**](ActionsListSelectedReposForOrgSecret200Response.md)

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

# **codespaces_pre_flight_with_repo_for_authenticated_user**
> CodespacesPreFlightWithRepoForAuthenticatedUser200Response codespaces_pre_flight_with_repo_for_authenticated_user(owner, repo, ref=ref, client_ip=client_ip)

Get default attributes for a codespace

Gets the default attributes for codespaces created by the user with the repository.  OAuth app tokens and personal access tokens (classic) need the `codespace` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespaces_pre_flight_with_repo_for_authenticated_user200_response import CodespacesPreFlightWithRepoForAuthenticatedUser200Response
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
    api_instance = github_openapi.CodespacesApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    ref = 'main' # str | The branch or commit to check for a default devcontainer path. If not specified, the default branch will be checked. (optional)
    client_ip = '1.2.3.4' # str | An alternative IP for default location auto-detection, such as when proxying a request. (optional)

    try:
        # Get default attributes for a codespace
        api_response = api_instance.codespaces_pre_flight_with_repo_for_authenticated_user(owner, repo, ref=ref, client_ip=client_ip)
        print("The response of CodespacesApi->codespaces_pre_flight_with_repo_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_pre_flight_with_repo_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **ref** | **str**| The branch or commit to check for a default devcontainer path. If not specified, the default branch will be checked. | [optional] 
 **client_ip** | **str**| An alternative IP for default location auto-detection, such as when proxying a request. | [optional] 

### Return type

[**CodespacesPreFlightWithRepoForAuthenticatedUser200Response**](CodespacesPreFlightWithRepoForAuthenticatedUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response when a user is able to create codespaces from the repository. |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_publish_for_authenticated_user**
> CodespaceWithFullRepository codespaces_publish_for_authenticated_user(codespace_name, codespaces_publish_for_authenticated_user_request)

Create a repository from an unpublished codespace

Publishes an unpublished codespace, creating a new repository and assigning it to the codespace.  The codespace's token is granted write permissions to the repository, allowing the user to push their changes.  This will fail for a codespace that is already published, meaning it has an associated repository.  OAuth app tokens and personal access tokens (classic) need the `codespace` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespace_with_full_repository import CodespaceWithFullRepository
from github_openapi.models.codespaces_publish_for_authenticated_user_request import CodespacesPublishForAuthenticatedUserRequest
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
    api_instance = github_openapi.CodespacesApi(api_client)
    codespace_name = 'codespace_name_example' # str | The name of the codespace.
    codespaces_publish_for_authenticated_user_request = {"repository":"monalisa-octocat-hello-world-g4wpq6h95q","private":false} # CodespacesPublishForAuthenticatedUserRequest | 

    try:
        # Create a repository from an unpublished codespace
        api_response = api_instance.codespaces_publish_for_authenticated_user(codespace_name, codespaces_publish_for_authenticated_user_request)
        print("The response of CodespacesApi->codespaces_publish_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_publish_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **codespace_name** | **str**| The name of the codespace. | 
 **codespaces_publish_for_authenticated_user_request** | [**CodespacesPublishForAuthenticatedUserRequest**](CodespacesPublishForAuthenticatedUserRequest.md)|  | 

### Return type

[**CodespaceWithFullRepository**](CodespaceWithFullRepository.md)

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
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_remove_repository_for_secret_for_authenticated_user**
> codespaces_remove_repository_for_secret_for_authenticated_user(secret_name, repository_id)

Remove a selected repository from a user secret

Removes a repository from the selected repositories for a user's development environment secret.  The authenticated user must have Codespaces access to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `codespace` or `codespace:secrets` scope to use this endpoint.

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
    api_instance = github_openapi.CodespacesApi(api_client)
    secret_name = 'secret_name_example' # str | The name of the secret.
    repository_id = 56 # int | 

    try:
        # Remove a selected repository from a user secret
        api_instance.codespaces_remove_repository_for_secret_for_authenticated_user(secret_name, repository_id)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_remove_repository_for_secret_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_name** | **str**| The name of the secret. | 
 **repository_id** | **int**|  | 

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
**204** | No Content when repository was removed from the selected list |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_remove_selected_repo_from_org_secret**
> codespaces_remove_selected_repo_from_org_secret(org, secret_name, repository_id)

Remove selected repository from an organization secret

Removes a repository from an organization development environment secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://docs.github.com/rest/codespaces/organization-secrets#create-or-update-an-organization-secret).  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

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
    api_instance = github_openapi.CodespacesApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    secret_name = 'secret_name_example' # str | The name of the secret.
    repository_id = 56 # int | 

    try:
        # Remove selected repository from an organization secret
        api_instance.codespaces_remove_selected_repo_from_org_secret(org, secret_name, repository_id)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_remove_selected_repo_from_org_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **secret_name** | **str**| The name of the secret. | 
 **repository_id** | **int**|  | 

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
**204** | Response when repository was removed from the selected list |  -  |
**404** | Resource not found |  -  |
**409** | Conflict when visibility type not set to selected |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_repo_machines_for_authenticated_user**
> CodespacesRepoMachinesForAuthenticatedUser200Response codespaces_repo_machines_for_authenticated_user(owner, repo, location=location, client_ip=client_ip, ref=ref)

List available machine types for a repository

List the machine types available for a given repository based on its configuration.  OAuth app tokens and personal access tokens (classic) need the `codespace` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespaces_repo_machines_for_authenticated_user200_response import CodespacesRepoMachinesForAuthenticatedUser200Response
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
    api_instance = github_openapi.CodespacesApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    location = 'WestUs2' # str | The location to check for available machines. Assigned by IP if not provided. (optional)
    client_ip = 'client_ip_example' # str | IP for location auto-detection when proxying a request (optional)
    ref = 'main' # str | The branch or commit to check for prebuild availability and devcontainer restrictions. (optional)

    try:
        # List available machine types for a repository
        api_response = api_instance.codespaces_repo_machines_for_authenticated_user(owner, repo, location=location, client_ip=client_ip, ref=ref)
        print("The response of CodespacesApi->codespaces_repo_machines_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_repo_machines_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **location** | **str**| The location to check for available machines. Assigned by IP if not provided. | [optional] 
 **client_ip** | **str**| IP for location auto-detection when proxying a request | [optional] 
 **ref** | **str**| The branch or commit to check for prebuild availability and devcontainer restrictions. | [optional] 

### Return type

[**CodespacesRepoMachinesForAuthenticatedUser200Response**](CodespacesRepoMachinesForAuthenticatedUser200Response.md)

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
**500** | Internal Error |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_set_codespaces_access**
> codespaces_set_codespaces_access(org, codespaces_set_codespaces_access_request)

Manage access control for organization codespaces

Sets which users can access codespaces in an organization. This is synonymous with granting or revoking codespaces access permissions for users according to the visibility. OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespaces_set_codespaces_access_request import CodespacesSetCodespacesAccessRequest
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
    api_instance = github_openapi.CodespacesApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    codespaces_set_codespaces_access_request = {"visibility":"selected_members","selected_usernames":["johnDoe","atomIO"]} # CodespacesSetCodespacesAccessRequest | 

    try:
        # Manage access control for organization codespaces
        api_instance.codespaces_set_codespaces_access(org, codespaces_set_codespaces_access_request)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_set_codespaces_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **codespaces_set_codespaces_access_request** | [**CodespacesSetCodespacesAccessRequest**](CodespacesSetCodespacesAccessRequest.md)|  | 

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
**204** | Response when successfully modifying permissions. |  -  |
**304** | Not modified |  -  |
**400** | Users are neither members nor collaborators of this organization. |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_set_codespaces_access_users**
> codespaces_set_codespaces_access_users(org, codespaces_set_codespaces_access_users_request)

Add users to Codespaces access for an organization

Codespaces for the specified users will be billed to the organization.  To use this endpoint, the access settings for the organization must be set to `selected_members`. For information on how to change this setting, see \"[Manage access control for organization codespaces](https://docs.github.com/rest/codespaces/organizations#manage-access-control-for-organization-codespaces).\"  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespaces_set_codespaces_access_users_request import CodespacesSetCodespacesAccessUsersRequest
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
    api_instance = github_openapi.CodespacesApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    codespaces_set_codespaces_access_users_request = {"selected_usernames":["johnDoe","atomIO"]} # CodespacesSetCodespacesAccessUsersRequest | 

    try:
        # Add users to Codespaces access for an organization
        api_instance.codespaces_set_codespaces_access_users(org, codespaces_set_codespaces_access_users_request)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_set_codespaces_access_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **codespaces_set_codespaces_access_users_request** | [**CodespacesSetCodespacesAccessUsersRequest**](CodespacesSetCodespacesAccessUsersRequest.md)|  | 

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
**204** | Response when successfully modifying permissions. |  -  |
**304** | Not modified |  -  |
**400** | Users are neither members nor collaborators of this organization. |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_set_repositories_for_secret_for_authenticated_user**
> codespaces_set_repositories_for_secret_for_authenticated_user(secret_name, codespaces_set_repositories_for_secret_for_authenticated_user_request)

Set selected repositories for a user secret

Select the repositories that will use a user's development environment secret.  The authenticated user must have Codespaces access to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `codespace` or `codespace:secrets` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespaces_set_repositories_for_secret_for_authenticated_user_request import CodespacesSetRepositoriesForSecretForAuthenticatedUserRequest
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
    api_instance = github_openapi.CodespacesApi(api_client)
    secret_name = 'secret_name_example' # str | The name of the secret.
    codespaces_set_repositories_for_secret_for_authenticated_user_request = {"selected_repository_ids":["1296269","1296280"]} # CodespacesSetRepositoriesForSecretForAuthenticatedUserRequest | 

    try:
        # Set selected repositories for a user secret
        api_instance.codespaces_set_repositories_for_secret_for_authenticated_user(secret_name, codespaces_set_repositories_for_secret_for_authenticated_user_request)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_set_repositories_for_secret_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_name** | **str**| The name of the secret. | 
 **codespaces_set_repositories_for_secret_for_authenticated_user_request** | [**CodespacesSetRepositoriesForSecretForAuthenticatedUserRequest**](CodespacesSetRepositoriesForSecretForAuthenticatedUserRequest.md)|  | 

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
**204** | No Content when repositories were added to the selected list |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**500** | Internal Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_set_selected_repos_for_org_secret**
> codespaces_set_selected_repos_for_org_secret(org, secret_name, codespaces_set_selected_repos_for_org_secret_request)

Set selected repositories for an organization secret

Replaces all repositories for an organization development environment secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://docs.github.com/rest/codespaces/organization-secrets#create-or-update-an-organization-secret).  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespaces_set_selected_repos_for_org_secret_request import CodespacesSetSelectedReposForOrgSecretRequest
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
    api_instance = github_openapi.CodespacesApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    secret_name = 'secret_name_example' # str | The name of the secret.
    codespaces_set_selected_repos_for_org_secret_request = {"selected_repository_ids":[64780797]} # CodespacesSetSelectedReposForOrgSecretRequest | 

    try:
        # Set selected repositories for an organization secret
        api_instance.codespaces_set_selected_repos_for_org_secret(org, secret_name, codespaces_set_selected_repos_for_org_secret_request)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_set_selected_repos_for_org_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **secret_name** | **str**| The name of the secret. | 
 **codespaces_set_selected_repos_for_org_secret_request** | [**CodespacesSetSelectedReposForOrgSecretRequest**](CodespacesSetSelectedReposForOrgSecretRequest.md)|  | 

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
**409** | Conflict when visibility type not set to selected |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_start_for_authenticated_user**
> Codespace codespaces_start_for_authenticated_user(codespace_name)

Start a codespace for the authenticated user

Starts a user's codespace.  OAuth app tokens and personal access tokens (classic) need the `codespace` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespace import Codespace
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
    api_instance = github_openapi.CodespacesApi(api_client)
    codespace_name = 'codespace_name_example' # str | The name of the codespace.

    try:
        # Start a codespace for the authenticated user
        api_response = api_instance.codespaces_start_for_authenticated_user(codespace_name)
        print("The response of CodespacesApi->codespaces_start_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_start_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **codespace_name** | **str**| The name of the codespace. | 

### Return type

[**Codespace**](Codespace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**304** | Not modified |  -  |
**500** | Internal Error |  -  |
**400** | Bad Request |  -  |
**401** | Requires authentication |  -  |
**402** | Payment required |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_stop_for_authenticated_user**
> Codespace codespaces_stop_for_authenticated_user(codespace_name)

Stop a codespace for the authenticated user

Stops a user's codespace.  OAuth app tokens and personal access tokens (classic) need the `codespace` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespace import Codespace
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
    api_instance = github_openapi.CodespacesApi(api_client)
    codespace_name = 'codespace_name_example' # str | The name of the codespace.

    try:
        # Stop a codespace for the authenticated user
        api_response = api_instance.codespaces_stop_for_authenticated_user(codespace_name)
        print("The response of CodespacesApi->codespaces_stop_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_stop_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **codespace_name** | **str**| The name of the codespace. | 

### Return type

[**Codespace**](Codespace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**500** | Internal Error |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_stop_in_organization**
> Codespace codespaces_stop_in_organization(org, username, codespace_name)

Stop a codespace for an organization user

Stops a user's codespace.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespace import Codespace
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
    api_instance = github_openapi.CodespacesApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    username = 'username_example' # str | The handle for the GitHub user account.
    codespace_name = 'codespace_name_example' # str | The name of the codespace.

    try:
        # Stop a codespace for an organization user
        api_response = api_instance.codespaces_stop_in_organization(org, username, codespace_name)
        print("The response of CodespacesApi->codespaces_stop_in_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_stop_in_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **username** | **str**| The handle for the GitHub user account. | 
 **codespace_name** | **str**| The name of the codespace. | 

### Return type

[**Codespace**](Codespace.md)

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
**500** | Internal Error |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **codespaces_update_for_authenticated_user**
> Codespace codespaces_update_for_authenticated_user(codespace_name, codespaces_update_for_authenticated_user_request=codespaces_update_for_authenticated_user_request)

Update a codespace for the authenticated user

Updates a codespace owned by the authenticated user. Currently only the codespace's machine type and recent folders can be modified using this endpoint.  If you specify a new machine type it will be applied the next time your codespace is started.  OAuth app tokens and personal access tokens (classic) need the `codespace` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.codespace import Codespace
from github_openapi.models.codespaces_update_for_authenticated_user_request import CodespacesUpdateForAuthenticatedUserRequest
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
    api_instance = github_openapi.CodespacesApi(api_client)
    codespace_name = 'codespace_name_example' # str | The name of the codespace.
    codespaces_update_for_authenticated_user_request = {"machine":"standardLinux"} # CodespacesUpdateForAuthenticatedUserRequest |  (optional)

    try:
        # Update a codespace for the authenticated user
        api_response = api_instance.codespaces_update_for_authenticated_user(codespace_name, codespaces_update_for_authenticated_user_request=codespaces_update_for_authenticated_user_request)
        print("The response of CodespacesApi->codespaces_update_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodespacesApi->codespaces_update_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **codespace_name** | **str**| The name of the codespace. | 
 **codespaces_update_for_authenticated_user_request** | [**CodespacesUpdateForAuthenticatedUserRequest**](CodespacesUpdateForAuthenticatedUserRequest.md)|  | [optional] 

### Return type

[**Codespace**](Codespace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

