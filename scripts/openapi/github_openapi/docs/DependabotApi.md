# github_openapi.DependabotApi

All URIs are relative to *https://api.github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dependabot_add_selected_repo_to_org_secret**](DependabotApi.md#dependabot_add_selected_repo_to_org_secret) | **PUT** /orgs/{org}/dependabot/secrets/{secret_name}/repositories/{repository_id} | Add selected repository to an organization secret
[**dependabot_create_or_update_org_secret**](DependabotApi.md#dependabot_create_or_update_org_secret) | **PUT** /orgs/{org}/dependabot/secrets/{secret_name} | Create or update an organization secret
[**dependabot_create_or_update_repo_secret**](DependabotApi.md#dependabot_create_or_update_repo_secret) | **PUT** /repos/{owner}/{repo}/dependabot/secrets/{secret_name} | Create or update a repository secret
[**dependabot_delete_org_secret**](DependabotApi.md#dependabot_delete_org_secret) | **DELETE** /orgs/{org}/dependabot/secrets/{secret_name} | Delete an organization secret
[**dependabot_delete_repo_secret**](DependabotApi.md#dependabot_delete_repo_secret) | **DELETE** /repos/{owner}/{repo}/dependabot/secrets/{secret_name} | Delete a repository secret
[**dependabot_get_alert**](DependabotApi.md#dependabot_get_alert) | **GET** /repos/{owner}/{repo}/dependabot/alerts/{alert_number} | Get a Dependabot alert
[**dependabot_get_org_public_key**](DependabotApi.md#dependabot_get_org_public_key) | **GET** /orgs/{org}/dependabot/secrets/public-key | Get an organization public key
[**dependabot_get_org_secret**](DependabotApi.md#dependabot_get_org_secret) | **GET** /orgs/{org}/dependabot/secrets/{secret_name} | Get an organization secret
[**dependabot_get_repo_public_key**](DependabotApi.md#dependabot_get_repo_public_key) | **GET** /repos/{owner}/{repo}/dependabot/secrets/public-key | Get a repository public key
[**dependabot_get_repo_secret**](DependabotApi.md#dependabot_get_repo_secret) | **GET** /repos/{owner}/{repo}/dependabot/secrets/{secret_name} | Get a repository secret
[**dependabot_list_alerts_for_enterprise**](DependabotApi.md#dependabot_list_alerts_for_enterprise) | **GET** /enterprises/{enterprise}/dependabot/alerts | List Dependabot alerts for an enterprise
[**dependabot_list_alerts_for_org**](DependabotApi.md#dependabot_list_alerts_for_org) | **GET** /orgs/{org}/dependabot/alerts | List Dependabot alerts for an organization
[**dependabot_list_alerts_for_repo**](DependabotApi.md#dependabot_list_alerts_for_repo) | **GET** /repos/{owner}/{repo}/dependabot/alerts | List Dependabot alerts for a repository
[**dependabot_list_org_secrets**](DependabotApi.md#dependabot_list_org_secrets) | **GET** /orgs/{org}/dependabot/secrets | List organization secrets
[**dependabot_list_repo_secrets**](DependabotApi.md#dependabot_list_repo_secrets) | **GET** /repos/{owner}/{repo}/dependabot/secrets | List repository secrets
[**dependabot_list_selected_repos_for_org_secret**](DependabotApi.md#dependabot_list_selected_repos_for_org_secret) | **GET** /orgs/{org}/dependabot/secrets/{secret_name}/repositories | List selected repositories for an organization secret
[**dependabot_remove_selected_repo_from_org_secret**](DependabotApi.md#dependabot_remove_selected_repo_from_org_secret) | **DELETE** /orgs/{org}/dependabot/secrets/{secret_name}/repositories/{repository_id} | Remove selected repository from an organization secret
[**dependabot_set_selected_repos_for_org_secret**](DependabotApi.md#dependabot_set_selected_repos_for_org_secret) | **PUT** /orgs/{org}/dependabot/secrets/{secret_name}/repositories | Set selected repositories for an organization secret
[**dependabot_update_alert**](DependabotApi.md#dependabot_update_alert) | **PATCH** /repos/{owner}/{repo}/dependabot/alerts/{alert_number} | Update a Dependabot alert


# **dependabot_add_selected_repo_to_org_secret**
> dependabot_add_selected_repo_to_org_secret(org, secret_name, repository_id)

Add selected repository to an organization secret

Adds a repository to an organization secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://docs.github.com/rest/dependabot/secrets#create-or-update-an-organization-secret).  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

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
    api_instance = github_openapi.DependabotApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    secret_name = 'secret_name_example' # str | The name of the secret.
    repository_id = 56 # int | 

    try:
        # Add selected repository to an organization secret
        api_instance.dependabot_add_selected_repo_to_org_secret(org, secret_name, repository_id)
    except Exception as e:
        print("Exception when calling DependabotApi->dependabot_add_selected_repo_to_org_secret: %s\n" % e)
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
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content when repository was added to the selected list |  -  |
**409** | Conflict when visibility type is not set to selected |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dependabot_create_or_update_org_secret**
> object dependabot_create_or_update_org_secret(org, secret_name, dependabot_create_or_update_org_secret_request)

Create or update an organization secret

Creates or updates an organization secret with an encrypted value. Encrypt your secret using [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). For more information, see \"[Encrypting secrets for the REST API](https://docs.github.com/rest/guides/encrypting-secrets-for-the-rest-api).\"  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.dependabot_create_or_update_org_secret_request import DependabotCreateOrUpdateOrgSecretRequest
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
    api_instance = github_openapi.DependabotApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    secret_name = 'secret_name_example' # str | The name of the secret.
    dependabot_create_or_update_org_secret_request = {"encrypted_value":"c2VjcmV0","key_id":"012345678912345678","visibility":"selected","selected_repository_ids":["1296269","1296280"]} # DependabotCreateOrUpdateOrgSecretRequest | 

    try:
        # Create or update an organization secret
        api_response = api_instance.dependabot_create_or_update_org_secret(org, secret_name, dependabot_create_or_update_org_secret_request)
        print("The response of DependabotApi->dependabot_create_or_update_org_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DependabotApi->dependabot_create_or_update_org_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **secret_name** | **str**| The name of the secret. | 
 **dependabot_create_or_update_org_secret_request** | [**DependabotCreateOrUpdateOrgSecretRequest**](DependabotCreateOrUpdateOrgSecretRequest.md)|  | 

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

# **dependabot_create_or_update_repo_secret**
> object dependabot_create_or_update_repo_secret(owner, repo, secret_name, dependabot_create_or_update_repo_secret_request)

Create or update a repository secret

Creates or updates a repository secret with an encrypted value. Encrypt your secret using [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). For more information, see \"[Encrypting secrets for the REST API](https://docs.github.com/rest/guides/encrypting-secrets-for-the-rest-api).\"  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.dependabot_create_or_update_repo_secret_request import DependabotCreateOrUpdateRepoSecretRequest
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
    api_instance = github_openapi.DependabotApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    secret_name = 'secret_name_example' # str | The name of the secret.
    dependabot_create_or_update_repo_secret_request = {"encrypted_value":"c2VjcmV0","key_id":"012345678912345678"} # DependabotCreateOrUpdateRepoSecretRequest | 

    try:
        # Create or update a repository secret
        api_response = api_instance.dependabot_create_or_update_repo_secret(owner, repo, secret_name, dependabot_create_or_update_repo_secret_request)
        print("The response of DependabotApi->dependabot_create_or_update_repo_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DependabotApi->dependabot_create_or_update_repo_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **secret_name** | **str**| The name of the secret. | 
 **dependabot_create_or_update_repo_secret_request** | [**DependabotCreateOrUpdateRepoSecretRequest**](DependabotCreateOrUpdateRepoSecretRequest.md)|  | 

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

# **dependabot_delete_org_secret**
> dependabot_delete_org_secret(org, secret_name)

Delete an organization secret

Deletes a secret in an organization using the secret name.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

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
    api_instance = github_openapi.DependabotApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    secret_name = 'secret_name_example' # str | The name of the secret.

    try:
        # Delete an organization secret
        api_instance.dependabot_delete_org_secret(org, secret_name)
    except Exception as e:
        print("Exception when calling DependabotApi->dependabot_delete_org_secret: %s\n" % e)
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
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dependabot_delete_repo_secret**
> dependabot_delete_repo_secret(owner, repo, secret_name)

Delete a repository secret

Deletes a secret in a repository using the secret name.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

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
    api_instance = github_openapi.DependabotApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    secret_name = 'secret_name_example' # str | The name of the secret.

    try:
        # Delete a repository secret
        api_instance.dependabot_delete_repo_secret(owner, repo, secret_name)
    except Exception as e:
        print("Exception when calling DependabotApi->dependabot_delete_repo_secret: %s\n" % e)
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

# **dependabot_get_alert**
> DependabotAlert dependabot_get_alert(owner, repo, alert_number)

Get a Dependabot alert

OAuth app tokens and personal access tokens (classic) need the `security_events` scope to use this endpoint. If this endpoint is only used with public repositories, the token can use the `public_repo` scope instead.

### Example


```python
import github_openapi
from github_openapi.models.dependabot_alert import DependabotAlert
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
    api_instance = github_openapi.DependabotApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    alert_number = 56 # int | The number that identifies a Dependabot alert in its repository. You can find this at the end of the URL for a Dependabot alert within GitHub, or in `number` fields in the response from the `GET /repos/{owner}/{repo}/dependabot/alerts` operation.

    try:
        # Get a Dependabot alert
        api_response = api_instance.dependabot_get_alert(owner, repo, alert_number)
        print("The response of DependabotApi->dependabot_get_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DependabotApi->dependabot_get_alert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **alert_number** | **int**| The number that identifies a Dependabot alert in its repository. You can find this at the end of the URL for a Dependabot alert within GitHub, or in &#x60;number&#x60; fields in the response from the &#x60;GET /repos/{owner}/{repo}/dependabot/alerts&#x60; operation. | 

### Return type

[**DependabotAlert**](DependabotAlert.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dependabot_get_org_public_key**
> DependabotPublicKey dependabot_get_org_public_key(org)

Get an organization public key

Gets your public key, which you need to encrypt secrets. You need to encrypt a secret before you can create or update secrets.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.dependabot_public_key import DependabotPublicKey
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
    api_instance = github_openapi.DependabotApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.

    try:
        # Get an organization public key
        api_response = api_instance.dependabot_get_org_public_key(org)
        print("The response of DependabotApi->dependabot_get_org_public_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DependabotApi->dependabot_get_org_public_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 

### Return type

[**DependabotPublicKey**](DependabotPublicKey.md)

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

# **dependabot_get_org_secret**
> OrganizationDependabotSecret dependabot_get_org_secret(org, secret_name)

Get an organization secret

Gets a single organization secret without revealing its encrypted value.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.organization_dependabot_secret import OrganizationDependabotSecret
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
    api_instance = github_openapi.DependabotApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    secret_name = 'secret_name_example' # str | The name of the secret.

    try:
        # Get an organization secret
        api_response = api_instance.dependabot_get_org_secret(org, secret_name)
        print("The response of DependabotApi->dependabot_get_org_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DependabotApi->dependabot_get_org_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **secret_name** | **str**| The name of the secret. | 

### Return type

[**OrganizationDependabotSecret**](OrganizationDependabotSecret.md)

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

# **dependabot_get_repo_public_key**
> DependabotPublicKey dependabot_get_repo_public_key(owner, repo)

Get a repository public key

Gets your public key, which you need to encrypt secrets. You need to encrypt a secret before you can create or update secrets. Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint if the repository is private.

### Example


```python
import github_openapi
from github_openapi.models.dependabot_public_key import DependabotPublicKey
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
    api_instance = github_openapi.DependabotApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Get a repository public key
        api_response = api_instance.dependabot_get_repo_public_key(owner, repo)
        print("The response of DependabotApi->dependabot_get_repo_public_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DependabotApi->dependabot_get_repo_public_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**DependabotPublicKey**](DependabotPublicKey.md)

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

# **dependabot_get_repo_secret**
> DependabotSecret dependabot_get_repo_secret(owner, repo, secret_name)

Get a repository secret

Gets a single repository secret without revealing its encrypted value.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.dependabot_secret import DependabotSecret
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
    api_instance = github_openapi.DependabotApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    secret_name = 'secret_name_example' # str | The name of the secret.

    try:
        # Get a repository secret
        api_response = api_instance.dependabot_get_repo_secret(owner, repo, secret_name)
        print("The response of DependabotApi->dependabot_get_repo_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DependabotApi->dependabot_get_repo_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **secret_name** | **str**| The name of the secret. | 

### Return type

[**DependabotSecret**](DependabotSecret.md)

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

# **dependabot_list_alerts_for_enterprise**
> List[DependabotAlertWithRepository] dependabot_list_alerts_for_enterprise(enterprise, state=state, severity=severity, ecosystem=ecosystem, package=package, scope=scope, sort=sort, direction=direction, before=before, after=after, first=first, last=last, per_page=per_page)

List Dependabot alerts for an enterprise

Lists Dependabot alerts for repositories that are owned by the specified enterprise.  The authenticated user must be a member of the enterprise to use this endpoint.  Alerts are only returned for organizations in the enterprise for which you are an organization owner or a security manager. For more information about security managers, see \"[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization).\"  OAuth app tokens and personal access tokens (classic) need the `repo` or `security_events` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.dependabot_alert_with_repository import DependabotAlertWithRepository
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
    api_instance = github_openapi.DependabotApi(api_client)
    enterprise = 'enterprise_example' # str | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    state = 'state_example' # str | A comma-separated list of states. If specified, only alerts with these states will be returned.  Can be: `auto_dismissed`, `dismissed`, `fixed`, `open` (optional)
    severity = 'severity_example' # str | A comma-separated list of severities. If specified, only alerts with these severities will be returned.  Can be: `low`, `medium`, `high`, `critical` (optional)
    ecosystem = 'ecosystem_example' # str | A comma-separated list of ecosystems. If specified, only alerts for these ecosystems will be returned.  Can be: `composer`, `go`, `maven`, `npm`, `nuget`, `pip`, `pub`, `rubygems`, `rust` (optional)
    package = 'package_example' # str | A comma-separated list of package names. If specified, only alerts for these packages will be returned. (optional)
    scope = 'scope_example' # str | The scope of the vulnerable dependency. If specified, only alerts with this scope will be returned. (optional)
    sort = created # str | The property by which to sort the results. `created` means when the alert was created. `updated` means when the alert's state last changed. (optional) (default to created)
    direction = desc # str | The direction to sort the results by. (optional) (default to desc)
    before = 'before_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)
    after = 'after_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)
    first = 30 # int | **Deprecated**. The number of results per page (max 100), starting from the first matching result. This parameter must not be used in combination with `last`. Instead, use `per_page` in combination with `after` to fetch the first page of results. (optional) (default to 30)
    last = 56 # int | **Deprecated**. The number of results per page (max 100), starting from the last matching result. This parameter must not be used in combination with `first`. Instead, use `per_page` in combination with `before` to fetch the last page of results. (optional)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)

    try:
        # List Dependabot alerts for an enterprise
        api_response = api_instance.dependabot_list_alerts_for_enterprise(enterprise, state=state, severity=severity, ecosystem=ecosystem, package=package, scope=scope, sort=sort, direction=direction, before=before, after=after, first=first, last=last, per_page=per_page)
        print("The response of DependabotApi->dependabot_list_alerts_for_enterprise:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DependabotApi->dependabot_list_alerts_for_enterprise: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **state** | **str**| A comma-separated list of states. If specified, only alerts with these states will be returned.  Can be: &#x60;auto_dismissed&#x60;, &#x60;dismissed&#x60;, &#x60;fixed&#x60;, &#x60;open&#x60; | [optional] 
 **severity** | **str**| A comma-separated list of severities. If specified, only alerts with these severities will be returned.  Can be: &#x60;low&#x60;, &#x60;medium&#x60;, &#x60;high&#x60;, &#x60;critical&#x60; | [optional] 
 **ecosystem** | **str**| A comma-separated list of ecosystems. If specified, only alerts for these ecosystems will be returned.  Can be: &#x60;composer&#x60;, &#x60;go&#x60;, &#x60;maven&#x60;, &#x60;npm&#x60;, &#x60;nuget&#x60;, &#x60;pip&#x60;, &#x60;pub&#x60;, &#x60;rubygems&#x60;, &#x60;rust&#x60; | [optional] 
 **package** | **str**| A comma-separated list of package names. If specified, only alerts for these packages will be returned. | [optional] 
 **scope** | **str**| The scope of the vulnerable dependency. If specified, only alerts with this scope will be returned. | [optional] 
 **sort** | **str**| The property by which to sort the results. &#x60;created&#x60; means when the alert was created. &#x60;updated&#x60; means when the alert&#39;s state last changed. | [optional] [default to created]
 **direction** | **str**| The direction to sort the results by. | [optional] [default to desc]
 **before** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 
 **after** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 
 **first** | **int**| **Deprecated**. The number of results per page (max 100), starting from the first matching result. This parameter must not be used in combination with &#x60;last&#x60;. Instead, use &#x60;per_page&#x60; in combination with &#x60;after&#x60; to fetch the first page of results. | [optional] [default to 30]
 **last** | **int**| **Deprecated**. The number of results per page (max 100), starting from the last matching result. This parameter must not be used in combination with &#x60;first&#x60;. Instead, use &#x60;per_page&#x60; in combination with &#x60;before&#x60; to fetch the last page of results. | [optional] 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]

### Return type

[**List[DependabotAlertWithRepository]**](DependabotAlertWithRepository.md)

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
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dependabot_list_alerts_for_org**
> List[DependabotAlertWithRepository] dependabot_list_alerts_for_org(org, state=state, severity=severity, ecosystem=ecosystem, package=package, scope=scope, sort=sort, direction=direction, before=before, after=after, first=first, last=last, per_page=per_page)

List Dependabot alerts for an organization

Lists Dependabot alerts for an organization.  The authenticated user must be an owner or security manager for the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `security_events` scope to use this endpoint. If this endpoint is only used with public repositories, the token can use the `public_repo` scope instead.

### Example


```python
import github_openapi
from github_openapi.models.dependabot_alert_with_repository import DependabotAlertWithRepository
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
    api_instance = github_openapi.DependabotApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    state = 'state_example' # str | A comma-separated list of states. If specified, only alerts with these states will be returned.  Can be: `auto_dismissed`, `dismissed`, `fixed`, `open` (optional)
    severity = 'severity_example' # str | A comma-separated list of severities. If specified, only alerts with these severities will be returned.  Can be: `low`, `medium`, `high`, `critical` (optional)
    ecosystem = 'ecosystem_example' # str | A comma-separated list of ecosystems. If specified, only alerts for these ecosystems will be returned.  Can be: `composer`, `go`, `maven`, `npm`, `nuget`, `pip`, `pub`, `rubygems`, `rust` (optional)
    package = 'package_example' # str | A comma-separated list of package names. If specified, only alerts for these packages will be returned. (optional)
    scope = 'scope_example' # str | The scope of the vulnerable dependency. If specified, only alerts with this scope will be returned. (optional)
    sort = created # str | The property by which to sort the results. `created` means when the alert was created. `updated` means when the alert's state last changed. (optional) (default to created)
    direction = desc # str | The direction to sort the results by. (optional) (default to desc)
    before = 'before_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)
    after = 'after_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)
    first = 30 # int | **Deprecated**. The number of results per page (max 100), starting from the first matching result. This parameter must not be used in combination with `last`. Instead, use `per_page` in combination with `after` to fetch the first page of results. (optional) (default to 30)
    last = 56 # int | **Deprecated**. The number of results per page (max 100), starting from the last matching result. This parameter must not be used in combination with `first`. Instead, use `per_page` in combination with `before` to fetch the last page of results. (optional)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)

    try:
        # List Dependabot alerts for an organization
        api_response = api_instance.dependabot_list_alerts_for_org(org, state=state, severity=severity, ecosystem=ecosystem, package=package, scope=scope, sort=sort, direction=direction, before=before, after=after, first=first, last=last, per_page=per_page)
        print("The response of DependabotApi->dependabot_list_alerts_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DependabotApi->dependabot_list_alerts_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **state** | **str**| A comma-separated list of states. If specified, only alerts with these states will be returned.  Can be: &#x60;auto_dismissed&#x60;, &#x60;dismissed&#x60;, &#x60;fixed&#x60;, &#x60;open&#x60; | [optional] 
 **severity** | **str**| A comma-separated list of severities. If specified, only alerts with these severities will be returned.  Can be: &#x60;low&#x60;, &#x60;medium&#x60;, &#x60;high&#x60;, &#x60;critical&#x60; | [optional] 
 **ecosystem** | **str**| A comma-separated list of ecosystems. If specified, only alerts for these ecosystems will be returned.  Can be: &#x60;composer&#x60;, &#x60;go&#x60;, &#x60;maven&#x60;, &#x60;npm&#x60;, &#x60;nuget&#x60;, &#x60;pip&#x60;, &#x60;pub&#x60;, &#x60;rubygems&#x60;, &#x60;rust&#x60; | [optional] 
 **package** | **str**| A comma-separated list of package names. If specified, only alerts for these packages will be returned. | [optional] 
 **scope** | **str**| The scope of the vulnerable dependency. If specified, only alerts with this scope will be returned. | [optional] 
 **sort** | **str**| The property by which to sort the results. &#x60;created&#x60; means when the alert was created. &#x60;updated&#x60; means when the alert&#39;s state last changed. | [optional] [default to created]
 **direction** | **str**| The direction to sort the results by. | [optional] [default to desc]
 **before** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 
 **after** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 
 **first** | **int**| **Deprecated**. The number of results per page (max 100), starting from the first matching result. This parameter must not be used in combination with &#x60;last&#x60;. Instead, use &#x60;per_page&#x60; in combination with &#x60;after&#x60; to fetch the first page of results. | [optional] [default to 30]
 **last** | **int**| **Deprecated**. The number of results per page (max 100), starting from the last matching result. This parameter must not be used in combination with &#x60;first&#x60;. Instead, use &#x60;per_page&#x60; in combination with &#x60;before&#x60; to fetch the last page of results. | [optional] 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]

### Return type

[**List[DependabotAlertWithRepository]**](DependabotAlertWithRepository.md)

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
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dependabot_list_alerts_for_repo**
> List[DependabotAlert] dependabot_list_alerts_for_repo(owner, repo, state=state, severity=severity, ecosystem=ecosystem, package=package, manifest=manifest, scope=scope, sort=sort, direction=direction, page=page, per_page=per_page, before=before, after=after, first=first, last=last)

List Dependabot alerts for a repository

OAuth app tokens and personal access tokens (classic) need the `security_events` scope to use this endpoint. If this endpoint is only used with public repositories, the token can use the `public_repo` scope instead.

### Example


```python
import github_openapi
from github_openapi.models.dependabot_alert import DependabotAlert
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
    api_instance = github_openapi.DependabotApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    state = 'state_example' # str | A comma-separated list of states. If specified, only alerts with these states will be returned.  Can be: `auto_dismissed`, `dismissed`, `fixed`, `open` (optional)
    severity = 'severity_example' # str | A comma-separated list of severities. If specified, only alerts with these severities will be returned.  Can be: `low`, `medium`, `high`, `critical` (optional)
    ecosystem = 'ecosystem_example' # str | A comma-separated list of ecosystems. If specified, only alerts for these ecosystems will be returned.  Can be: `composer`, `go`, `maven`, `npm`, `nuget`, `pip`, `pub`, `rubygems`, `rust` (optional)
    package = 'package_example' # str | A comma-separated list of package names. If specified, only alerts for these packages will be returned. (optional)
    manifest = 'manifest_example' # str | A comma-separated list of full manifest paths. If specified, only alerts for these manifests will be returned. (optional)
    scope = 'scope_example' # str | The scope of the vulnerable dependency. If specified, only alerts with this scope will be returned. (optional)
    sort = created # str | The property by which to sort the results. `created` means when the alert was created. `updated` means when the alert's state last changed. (optional) (default to created)
    direction = desc # str | The direction to sort the results by. (optional) (default to desc)
    page = 1 # int | **Closing down notice**. Page number of the results to fetch. Use cursor-based pagination with `before` or `after` instead. (optional) (default to 1)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    before = 'before_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)
    after = 'after_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)
    first = 30 # int | **Deprecated**. The number of results per page (max 100), starting from the first matching result. This parameter must not be used in combination with `last`. Instead, use `per_page` in combination with `after` to fetch the first page of results. (optional) (default to 30)
    last = 56 # int | **Deprecated**. The number of results per page (max 100), starting from the last matching result. This parameter must not be used in combination with `first`. Instead, use `per_page` in combination with `before` to fetch the last page of results. (optional)

    try:
        # List Dependabot alerts for a repository
        api_response = api_instance.dependabot_list_alerts_for_repo(owner, repo, state=state, severity=severity, ecosystem=ecosystem, package=package, manifest=manifest, scope=scope, sort=sort, direction=direction, page=page, per_page=per_page, before=before, after=after, first=first, last=last)
        print("The response of DependabotApi->dependabot_list_alerts_for_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DependabotApi->dependabot_list_alerts_for_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **state** | **str**| A comma-separated list of states. If specified, only alerts with these states will be returned.  Can be: &#x60;auto_dismissed&#x60;, &#x60;dismissed&#x60;, &#x60;fixed&#x60;, &#x60;open&#x60; | [optional] 
 **severity** | **str**| A comma-separated list of severities. If specified, only alerts with these severities will be returned.  Can be: &#x60;low&#x60;, &#x60;medium&#x60;, &#x60;high&#x60;, &#x60;critical&#x60; | [optional] 
 **ecosystem** | **str**| A comma-separated list of ecosystems. If specified, only alerts for these ecosystems will be returned.  Can be: &#x60;composer&#x60;, &#x60;go&#x60;, &#x60;maven&#x60;, &#x60;npm&#x60;, &#x60;nuget&#x60;, &#x60;pip&#x60;, &#x60;pub&#x60;, &#x60;rubygems&#x60;, &#x60;rust&#x60; | [optional] 
 **package** | **str**| A comma-separated list of package names. If specified, only alerts for these packages will be returned. | [optional] 
 **manifest** | **str**| A comma-separated list of full manifest paths. If specified, only alerts for these manifests will be returned. | [optional] 
 **scope** | **str**| The scope of the vulnerable dependency. If specified, only alerts with this scope will be returned. | [optional] 
 **sort** | **str**| The property by which to sort the results. &#x60;created&#x60; means when the alert was created. &#x60;updated&#x60; means when the alert&#39;s state last changed. | [optional] [default to created]
 **direction** | **str**| The direction to sort the results by. | [optional] [default to desc]
 **page** | **int**| **Closing down notice**. Page number of the results to fetch. Use cursor-based pagination with &#x60;before&#x60; or &#x60;after&#x60; instead. | [optional] [default to 1]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **before** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 
 **after** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 
 **first** | **int**| **Deprecated**. The number of results per page (max 100), starting from the first matching result. This parameter must not be used in combination with &#x60;last&#x60;. Instead, use &#x60;per_page&#x60; in combination with &#x60;after&#x60; to fetch the first page of results. | [optional] [default to 30]
 **last** | **int**| **Deprecated**. The number of results per page (max 100), starting from the last matching result. This parameter must not be used in combination with &#x60;first&#x60;. Instead, use &#x60;per_page&#x60; in combination with &#x60;before&#x60; to fetch the last page of results. | [optional] 

### Return type

[**List[DependabotAlert]**](DependabotAlert.md)

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
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dependabot_list_org_secrets**
> DependabotListOrgSecrets200Response dependabot_list_org_secrets(org, per_page=per_page, page=page)

List organization secrets

Lists all secrets available in an organization without revealing their encrypted values.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.dependabot_list_org_secrets200_response import DependabotListOrgSecrets200Response
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
    api_instance = github_openapi.DependabotApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List organization secrets
        api_response = api_instance.dependabot_list_org_secrets(org, per_page=per_page, page=page)
        print("The response of DependabotApi->dependabot_list_org_secrets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DependabotApi->dependabot_list_org_secrets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**DependabotListOrgSecrets200Response**](DependabotListOrgSecrets200Response.md)

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

# **dependabot_list_repo_secrets**
> DependabotListRepoSecrets200Response dependabot_list_repo_secrets(owner, repo, per_page=per_page, page=page)

List repository secrets

Lists all secrets available in a repository without revealing their encrypted values.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.dependabot_list_repo_secrets200_response import DependabotListRepoSecrets200Response
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
    api_instance = github_openapi.DependabotApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List repository secrets
        api_response = api_instance.dependabot_list_repo_secrets(owner, repo, per_page=per_page, page=page)
        print("The response of DependabotApi->dependabot_list_repo_secrets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DependabotApi->dependabot_list_repo_secrets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**DependabotListRepoSecrets200Response**](DependabotListRepoSecrets200Response.md)

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

# **dependabot_list_selected_repos_for_org_secret**
> ActionsListSelectedReposForOrgSecret200Response dependabot_list_selected_repos_for_org_secret(org, secret_name, page=page, per_page=per_page)

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
    api_instance = github_openapi.DependabotApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    secret_name = 'secret_name_example' # str | The name of the secret.
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)

    try:
        # List selected repositories for an organization secret
        api_response = api_instance.dependabot_list_selected_repos_for_org_secret(org, secret_name, page=page, per_page=per_page)
        print("The response of DependabotApi->dependabot_list_selected_repos_for_org_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DependabotApi->dependabot_list_selected_repos_for_org_secret: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dependabot_remove_selected_repo_from_org_secret**
> dependabot_remove_selected_repo_from_org_secret(org, secret_name, repository_id)

Remove selected repository from an organization secret

Removes a repository from an organization secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://docs.github.com/rest/dependabot/secrets#create-or-update-an-organization-secret).  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

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
    api_instance = github_openapi.DependabotApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    secret_name = 'secret_name_example' # str | The name of the secret.
    repository_id = 56 # int | 

    try:
        # Remove selected repository from an organization secret
        api_instance.dependabot_remove_selected_repo_from_org_secret(org, secret_name, repository_id)
    except Exception as e:
        print("Exception when calling DependabotApi->dependabot_remove_selected_repo_from_org_secret: %s\n" % e)
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
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response when repository was removed from the selected list |  -  |
**409** | Conflict when visibility type not set to selected |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dependabot_set_selected_repos_for_org_secret**
> dependabot_set_selected_repos_for_org_secret(org, secret_name, dependabot_set_selected_repos_for_org_secret_request)

Set selected repositories for an organization secret

Replaces all repositories for an organization secret when the `visibility` for repository access is set to `selected`. The visibility is set when you [Create or update an organization secret](https://docs.github.com/rest/dependabot/secrets#create-or-update-an-organization-secret).  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.dependabot_set_selected_repos_for_org_secret_request import DependabotSetSelectedReposForOrgSecretRequest
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
    api_instance = github_openapi.DependabotApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    secret_name = 'secret_name_example' # str | The name of the secret.
    dependabot_set_selected_repos_for_org_secret_request = {"selected_repository_ids":[64780797]} # DependabotSetSelectedReposForOrgSecretRequest | 

    try:
        # Set selected repositories for an organization secret
        api_instance.dependabot_set_selected_repos_for_org_secret(org, secret_name, dependabot_set_selected_repos_for_org_secret_request)
    except Exception as e:
        print("Exception when calling DependabotApi->dependabot_set_selected_repos_for_org_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **secret_name** | **str**| The name of the secret. | 
 **dependabot_set_selected_repos_for_org_secret_request** | [**DependabotSetSelectedReposForOrgSecretRequest**](DependabotSetSelectedReposForOrgSecretRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dependabot_update_alert**
> DependabotAlert dependabot_update_alert(owner, repo, alert_number, dependabot_update_alert_request)

Update a Dependabot alert

The authenticated user must have access to security alerts for the repository to use this endpoint. For more information, see \"[Granting access to security alerts](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-security-and-analysis-settings-for-your-repository#granting-access-to-security-alerts).\"  OAuth app tokens and personal access tokens (classic) need the `security_events` scope to use this endpoint. If this endpoint is only used with public repositories, the token can use the `public_repo` scope instead.

### Example


```python
import github_openapi
from github_openapi.models.dependabot_alert import DependabotAlert
from github_openapi.models.dependabot_update_alert_request import DependabotUpdateAlertRequest
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
    api_instance = github_openapi.DependabotApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    alert_number = 56 # int | The number that identifies a Dependabot alert in its repository. You can find this at the end of the URL for a Dependabot alert within GitHub, or in `number` fields in the response from the `GET /repos/{owner}/{repo}/dependabot/alerts` operation.
    dependabot_update_alert_request = {"state":"dismissed","dismissed_reason":"tolerable_risk","dismissed_comment":"This alert is accurate but we use a sanitizer."} # DependabotUpdateAlertRequest | 

    try:
        # Update a Dependabot alert
        api_response = api_instance.dependabot_update_alert(owner, repo, alert_number, dependabot_update_alert_request)
        print("The response of DependabotApi->dependabot_update_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DependabotApi->dependabot_update_alert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **alert_number** | **int**| The number that identifies a Dependabot alert in its repository. You can find this at the end of the URL for a Dependabot alert within GitHub, or in &#x60;number&#x60; fields in the response from the &#x60;GET /repos/{owner}/{repo}/dependabot/alerts&#x60; operation. | 
 **dependabot_update_alert_request** | [**DependabotUpdateAlertRequest**](DependabotUpdateAlertRequest.md)|  | 

### Return type

[**DependabotAlert**](DependabotAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Conflict |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

