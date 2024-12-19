# github_openapi.CodeSecurityApi

All URIs are relative to *https://api.github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**code_security_attach_configuration**](CodeSecurityApi.md#code_security_attach_configuration) | **POST** /orgs/{org}/code-security/configurations/{configuration_id}/attach | Attach a configuration to repositories
[**code_security_attach_enterprise_configuration**](CodeSecurityApi.md#code_security_attach_enterprise_configuration) | **POST** /enterprises/{enterprise}/code-security/configurations/{configuration_id}/attach | Attach an enterprise configuration to repositories
[**code_security_create_configuration**](CodeSecurityApi.md#code_security_create_configuration) | **POST** /orgs/{org}/code-security/configurations | Create a code security configuration
[**code_security_create_configuration_for_enterprise**](CodeSecurityApi.md#code_security_create_configuration_for_enterprise) | **POST** /enterprises/{enterprise}/code-security/configurations | Create a code security configuration for an enterprise
[**code_security_delete_configuration**](CodeSecurityApi.md#code_security_delete_configuration) | **DELETE** /orgs/{org}/code-security/configurations/{configuration_id} | Delete a code security configuration
[**code_security_delete_configuration_for_enterprise**](CodeSecurityApi.md#code_security_delete_configuration_for_enterprise) | **DELETE** /enterprises/{enterprise}/code-security/configurations/{configuration_id} | Delete a code security configuration for an enterprise
[**code_security_detach_configuration**](CodeSecurityApi.md#code_security_detach_configuration) | **DELETE** /orgs/{org}/code-security/configurations/detach | Detach configurations from repositories
[**code_security_get_configuration**](CodeSecurityApi.md#code_security_get_configuration) | **GET** /orgs/{org}/code-security/configurations/{configuration_id} | Get a code security configuration
[**code_security_get_configuration_for_repository**](CodeSecurityApi.md#code_security_get_configuration_for_repository) | **GET** /repos/{owner}/{repo}/code-security-configuration | Get the code security configuration associated with a repository
[**code_security_get_configurations_for_enterprise**](CodeSecurityApi.md#code_security_get_configurations_for_enterprise) | **GET** /enterprises/{enterprise}/code-security/configurations | Get code security configurations for an enterprise
[**code_security_get_configurations_for_org**](CodeSecurityApi.md#code_security_get_configurations_for_org) | **GET** /orgs/{org}/code-security/configurations | Get code security configurations for an organization
[**code_security_get_default_configurations**](CodeSecurityApi.md#code_security_get_default_configurations) | **GET** /orgs/{org}/code-security/configurations/defaults | Get default code security configurations
[**code_security_get_default_configurations_for_enterprise**](CodeSecurityApi.md#code_security_get_default_configurations_for_enterprise) | **GET** /enterprises/{enterprise}/code-security/configurations/defaults | Get default code security configurations for an enterprise
[**code_security_get_repositories_for_configuration**](CodeSecurityApi.md#code_security_get_repositories_for_configuration) | **GET** /orgs/{org}/code-security/configurations/{configuration_id}/repositories | Get repositories associated with a code security configuration
[**code_security_get_repositories_for_enterprise_configuration**](CodeSecurityApi.md#code_security_get_repositories_for_enterprise_configuration) | **GET** /enterprises/{enterprise}/code-security/configurations/{configuration_id}/repositories | Get repositories associated with an enterprise code security configuration
[**code_security_get_single_configuration_for_enterprise**](CodeSecurityApi.md#code_security_get_single_configuration_for_enterprise) | **GET** /enterprises/{enterprise}/code-security/configurations/{configuration_id} | Retrieve a code security configuration of an enterprise
[**code_security_set_configuration_as_default**](CodeSecurityApi.md#code_security_set_configuration_as_default) | **PUT** /orgs/{org}/code-security/configurations/{configuration_id}/defaults | Set a code security configuration as a default for an organization
[**code_security_set_configuration_as_default_for_enterprise**](CodeSecurityApi.md#code_security_set_configuration_as_default_for_enterprise) | **PUT** /enterprises/{enterprise}/code-security/configurations/{configuration_id}/defaults | Set a code security configuration as a default for an enterprise
[**code_security_update_configuration**](CodeSecurityApi.md#code_security_update_configuration) | **PATCH** /orgs/{org}/code-security/configurations/{configuration_id} | Update a code security configuration
[**code_security_update_enterprise_configuration**](CodeSecurityApi.md#code_security_update_enterprise_configuration) | **PATCH** /enterprises/{enterprise}/code-security/configurations/{configuration_id} | Update a custom code security configuration for an enterprise


# **code_security_attach_configuration**
> object code_security_attach_configuration(org, configuration_id, code_security_attach_configuration_request)

Attach a configuration to repositories

Attach a code security configuration to a set of repositories. If the repositories specified are already attached to a configuration, they will be re-attached to the provided configuration.  If insufficient GHAS licenses are available to attach the configuration to a repository, only free features will be enabled.  The authenticated user must be an administrator or security manager for the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `write:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.code_security_attach_configuration_request import CodeSecurityAttachConfigurationRequest
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
    api_instance = github_openapi.CodeSecurityApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    configuration_id = 56 # int | The unique identifier of the code security configuration.
    code_security_attach_configuration_request = {"scope":"selected","selected_repository_ids":[32,91]} # CodeSecurityAttachConfigurationRequest | 

    try:
        # Attach a configuration to repositories
        api_response = api_instance.code_security_attach_configuration(org, configuration_id, code_security_attach_configuration_request)
        print("The response of CodeSecurityApi->code_security_attach_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeSecurityApi->code_security_attach_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **configuration_id** | **int**| The unique identifier of the code security configuration. | 
 **code_security_attach_configuration_request** | [**CodeSecurityAttachConfigurationRequest**](CodeSecurityAttachConfigurationRequest.md)|  | 

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
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_security_attach_enterprise_configuration**
> object code_security_attach_enterprise_configuration(enterprise, configuration_id, code_security_attach_enterprise_configuration_request)

Attach an enterprise configuration to repositories

Attaches an enterprise code security configuration to repositories. If the repositories specified are already attached to a configuration, they will be re-attached to the provided configuration.  If insufficient GHAS licenses are available to attach the configuration to a repository, only free features will be enabled.  The authenticated user must be an administrator for the enterprise to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:enterprise` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.code_security_attach_enterprise_configuration_request import CodeSecurityAttachEnterpriseConfigurationRequest
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
    api_instance = github_openapi.CodeSecurityApi(api_client)
    enterprise = 'enterprise_example' # str | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    configuration_id = 56 # int | The unique identifier of the code security configuration.
    code_security_attach_enterprise_configuration_request = {"scope":"all"} # CodeSecurityAttachEnterpriseConfigurationRequest | 

    try:
        # Attach an enterprise configuration to repositories
        api_response = api_instance.code_security_attach_enterprise_configuration(enterprise, configuration_id, code_security_attach_enterprise_configuration_request)
        print("The response of CodeSecurityApi->code_security_attach_enterprise_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeSecurityApi->code_security_attach_enterprise_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **configuration_id** | **int**| The unique identifier of the code security configuration. | 
 **code_security_attach_enterprise_configuration_request** | [**CodeSecurityAttachEnterpriseConfigurationRequest**](CodeSecurityAttachEnterpriseConfigurationRequest.md)|  | 

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
**202** | Accepted |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_security_create_configuration**
> CodeSecurityConfiguration code_security_create_configuration(org, code_security_create_configuration_request)

Create a code security configuration

Creates a code security configuration in an organization.  The authenticated user must be an administrator or security manager for the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `write:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.code_security_configuration import CodeSecurityConfiguration
from github_openapi.models.code_security_create_configuration_request import CodeSecurityCreateConfigurationRequest
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
    api_instance = github_openapi.CodeSecurityApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    code_security_create_configuration_request = {"name":"octo-org recommended settings","description":"This is a code security configuration for octo-org","advanced_security":"enabled","dependabot_alerts":"enabled","dependabot_security_updates":"not_set","secret_scanning":"enabled"} # CodeSecurityCreateConfigurationRequest | 

    try:
        # Create a code security configuration
        api_response = api_instance.code_security_create_configuration(org, code_security_create_configuration_request)
        print("The response of CodeSecurityApi->code_security_create_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeSecurityApi->code_security_create_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **code_security_create_configuration_request** | [**CodeSecurityCreateConfigurationRequest**](CodeSecurityCreateConfigurationRequest.md)|  | 

### Return type

[**CodeSecurityConfiguration**](CodeSecurityConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created code security configuration |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_security_create_configuration_for_enterprise**
> CodeSecurityConfiguration code_security_create_configuration_for_enterprise(enterprise, code_security_create_configuration_for_enterprise_request)

Create a code security configuration for an enterprise

Creates a code security configuration in an enterprise.  The authenticated user must be an administrator of the enterprise in order to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:enterprise` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.code_security_configuration import CodeSecurityConfiguration
from github_openapi.models.code_security_create_configuration_for_enterprise_request import CodeSecurityCreateConfigurationForEnterpriseRequest
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
    api_instance = github_openapi.CodeSecurityApi(api_client)
    enterprise = 'enterprise_example' # str | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    code_security_create_configuration_for_enterprise_request = {"name":"High rish settings","description":"This is a code security configuration for octo-enterprise","advanced_security":"enabled","dependabot_alerts":"enabled","dependabot_security_updates":"not_set","secret_scanning":"enabled"} # CodeSecurityCreateConfigurationForEnterpriseRequest | 

    try:
        # Create a code security configuration for an enterprise
        api_response = api_instance.code_security_create_configuration_for_enterprise(enterprise, code_security_create_configuration_for_enterprise_request)
        print("The response of CodeSecurityApi->code_security_create_configuration_for_enterprise:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeSecurityApi->code_security_create_configuration_for_enterprise: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **code_security_create_configuration_for_enterprise_request** | [**CodeSecurityCreateConfigurationForEnterpriseRequest**](CodeSecurityCreateConfigurationForEnterpriseRequest.md)|  | 

### Return type

[**CodeSecurityConfiguration**](CodeSecurityConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created code security configuration |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_security_delete_configuration**
> code_security_delete_configuration(org, configuration_id)

Delete a code security configuration

Deletes the desired code security configuration from an organization. Repositories attached to the configuration will retain their settings but will no longer be associated with the configuration.  The authenticated user must be an administrator or security manager for the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `write:org` scope to use this endpoint.

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
    api_instance = github_openapi.CodeSecurityApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    configuration_id = 56 # int | The unique identifier of the code security configuration.

    try:
        # Delete a code security configuration
        api_instance.code_security_delete_configuration(org, configuration_id)
    except Exception as e:
        print("Exception when calling CodeSecurityApi->code_security_delete_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **configuration_id** | **int**| The unique identifier of the code security configuration. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | A header with no content is returned. |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_security_delete_configuration_for_enterprise**
> code_security_delete_configuration_for_enterprise(enterprise, configuration_id)

Delete a code security configuration for an enterprise

Deletes a code security configuration from an enterprise. Repositories attached to the configuration will retain their settings but will no longer be associated with the configuration.  The authenticated user must be an administrator for the enterprise to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:enterprise` scope to use this endpoint.

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
    api_instance = github_openapi.CodeSecurityApi(api_client)
    enterprise = 'enterprise_example' # str | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    configuration_id = 56 # int | The unique identifier of the code security configuration.

    try:
        # Delete a code security configuration for an enterprise
        api_instance.code_security_delete_configuration_for_enterprise(enterprise, configuration_id)
    except Exception as e:
        print("Exception when calling CodeSecurityApi->code_security_delete_configuration_for_enterprise: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **configuration_id** | **int**| The unique identifier of the code security configuration. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | A header with no content is returned. |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_security_detach_configuration**
> code_security_detach_configuration(org, code_security_detach_configuration_request)

Detach configurations from repositories

Detach code security configuration(s) from a set of repositories. Repositories will retain their settings but will no longer be associated with the configuration.  The authenticated user must be an administrator or security manager for the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `write:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.code_security_detach_configuration_request import CodeSecurityDetachConfigurationRequest
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
    api_instance = github_openapi.CodeSecurityApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    code_security_detach_configuration_request = {"selected_repository_ids":[32,91]} # CodeSecurityDetachConfigurationRequest | 

    try:
        # Detach configurations from repositories
        api_instance.code_security_detach_configuration(org, code_security_detach_configuration_request)
    except Exception as e:
        print("Exception when calling CodeSecurityApi->code_security_detach_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **code_security_detach_configuration_request** | [**CodeSecurityDetachConfigurationRequest**](CodeSecurityDetachConfigurationRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | A header with no content is returned. |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_security_get_configuration**
> CodeSecurityConfiguration code_security_get_configuration(org, configuration_id)

Get a code security configuration

Gets a code security configuration available in an organization.  The authenticated user must be an administrator or security manager for the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `write:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.code_security_configuration import CodeSecurityConfiguration
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
    api_instance = github_openapi.CodeSecurityApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    configuration_id = 56 # int | The unique identifier of the code security configuration.

    try:
        # Get a code security configuration
        api_response = api_instance.code_security_get_configuration(org, configuration_id)
        print("The response of CodeSecurityApi->code_security_get_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeSecurityApi->code_security_get_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **configuration_id** | **int**| The unique identifier of the code security configuration. | 

### Return type

[**CodeSecurityConfiguration**](CodeSecurityConfiguration.md)

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

# **code_security_get_configuration_for_repository**
> CodeSecurityConfigurationForRepository code_security_get_configuration_for_repository(owner, repo)

Get the code security configuration associated with a repository

Get the code security configuration that manages a repository's code security settings.  The authenticated user must be an administrator or security manager for the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.code_security_configuration_for_repository import CodeSecurityConfigurationForRepository
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
    api_instance = github_openapi.CodeSecurityApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Get the code security configuration associated with a repository
        api_response = api_instance.code_security_get_configuration_for_repository(owner, repo)
        print("The response of CodeSecurityApi->code_security_get_configuration_for_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeSecurityApi->code_security_get_configuration_for_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**CodeSecurityConfigurationForRepository**](CodeSecurityConfigurationForRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**204** | A header with no content is returned. |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_security_get_configurations_for_enterprise**
> List[CodeSecurityConfiguration] code_security_get_configurations_for_enterprise(enterprise, per_page=per_page, before=before, after=after)

Get code security configurations for an enterprise

Lists all code security configurations available in an enterprise.  The authenticated user must be an administrator of the enterprise in order to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `read:enterprise` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.code_security_configuration import CodeSecurityConfiguration
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
    api_instance = github_openapi.CodeSecurityApi(api_client)
    enterprise = 'enterprise_example' # str | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    before = 'before_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)
    after = 'after_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)

    try:
        # Get code security configurations for an enterprise
        api_response = api_instance.code_security_get_configurations_for_enterprise(enterprise, per_page=per_page, before=before, after=after)
        print("The response of CodeSecurityApi->code_security_get_configurations_for_enterprise:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeSecurityApi->code_security_get_configurations_for_enterprise: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **before** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 
 **after** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 

### Return type

[**List[CodeSecurityConfiguration]**](CodeSecurityConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_security_get_configurations_for_org**
> List[CodeSecurityConfiguration] code_security_get_configurations_for_org(org, target_type=target_type, per_page=per_page, before=before, after=after)

Get code security configurations for an organization

Lists all code security configurations available in an organization.  The authenticated user must be an administrator or security manager for the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `write:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.code_security_configuration import CodeSecurityConfiguration
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
    api_instance = github_openapi.CodeSecurityApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    target_type = all # str | The target type of the code security configuration (optional) (default to all)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    before = 'before_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)
    after = 'after_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)

    try:
        # Get code security configurations for an organization
        api_response = api_instance.code_security_get_configurations_for_org(org, target_type=target_type, per_page=per_page, before=before, after=after)
        print("The response of CodeSecurityApi->code_security_get_configurations_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeSecurityApi->code_security_get_configurations_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **target_type** | **str**| The target type of the code security configuration | [optional] [default to all]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **before** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 
 **after** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 

### Return type

[**List[CodeSecurityConfiguration]**](CodeSecurityConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_security_get_default_configurations**
> List[CodeSecurityDefaultConfigurationsInner] code_security_get_default_configurations(org)

Get default code security configurations

Lists the default code security configurations for an organization.  The authenticated user must be an administrator or security manager for the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `write:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.code_security_default_configurations_inner import CodeSecurityDefaultConfigurationsInner
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
    api_instance = github_openapi.CodeSecurityApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.

    try:
        # Get default code security configurations
        api_response = api_instance.code_security_get_default_configurations(org)
        print("The response of CodeSecurityApi->code_security_get_default_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeSecurityApi->code_security_get_default_configurations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 

### Return type

[**List[CodeSecurityDefaultConfigurationsInner]**](CodeSecurityDefaultConfigurationsInner.md)

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

# **code_security_get_default_configurations_for_enterprise**
> List[CodeSecurityDefaultConfigurationsInner] code_security_get_default_configurations_for_enterprise(enterprise)

Get default code security configurations for an enterprise

Lists the default code security configurations for an enterprise.  The authenticated user must be an administrator of the enterprise in order to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `read:enterprise` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.code_security_default_configurations_inner import CodeSecurityDefaultConfigurationsInner
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
    api_instance = github_openapi.CodeSecurityApi(api_client)
    enterprise = 'enterprise_example' # str | The slug version of the enterprise name. You can also substitute this value with the enterprise id.

    try:
        # Get default code security configurations for an enterprise
        api_response = api_instance.code_security_get_default_configurations_for_enterprise(enterprise)
        print("The response of CodeSecurityApi->code_security_get_default_configurations_for_enterprise:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeSecurityApi->code_security_get_default_configurations_for_enterprise: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 

### Return type

[**List[CodeSecurityDefaultConfigurationsInner]**](CodeSecurityDefaultConfigurationsInner.md)

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

# **code_security_get_repositories_for_configuration**
> List[CodeSecurityConfigurationRepositories] code_security_get_repositories_for_configuration(org, configuration_id, per_page=per_page, before=before, after=after, status=status)

Get repositories associated with a code security configuration

Lists the repositories associated with a code security configuration in an organization.  The authenticated user must be an administrator or security manager for the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `write:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.code_security_configuration_repositories import CodeSecurityConfigurationRepositories
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
    api_instance = github_openapi.CodeSecurityApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    configuration_id = 56 # int | The unique identifier of the code security configuration.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    before = 'before_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)
    after = 'after_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)
    status = 'all' # str | A comma-separated list of statuses. If specified, only repositories with these attachment statuses will be returned.  Can be: `all`, `attached`, `attaching`, `detached`, `removed`, `enforced`, `failed`, `updating`, `removed_by_enterprise` (optional) (default to 'all')

    try:
        # Get repositories associated with a code security configuration
        api_response = api_instance.code_security_get_repositories_for_configuration(org, configuration_id, per_page=per_page, before=before, after=after, status=status)
        print("The response of CodeSecurityApi->code_security_get_repositories_for_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeSecurityApi->code_security_get_repositories_for_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **configuration_id** | **int**| The unique identifier of the code security configuration. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **before** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 
 **after** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 
 **status** | **str**| A comma-separated list of statuses. If specified, only repositories with these attachment statuses will be returned.  Can be: &#x60;all&#x60;, &#x60;attached&#x60;, &#x60;attaching&#x60;, &#x60;detached&#x60;, &#x60;removed&#x60;, &#x60;enforced&#x60;, &#x60;failed&#x60;, &#x60;updating&#x60;, &#x60;removed_by_enterprise&#x60; | [optional] [default to &#39;all&#39;]

### Return type

[**List[CodeSecurityConfigurationRepositories]**](CodeSecurityConfigurationRepositories.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_security_get_repositories_for_enterprise_configuration**
> List[CodeSecurityConfigurationRepositories] code_security_get_repositories_for_enterprise_configuration(enterprise, configuration_id, per_page=per_page, before=before, after=after, status=status)

Get repositories associated with an enterprise code security configuration

Lists the repositories associated with an enterprise code security configuration in an organization.  The authenticated user must be an administrator of the enterprise in order to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `read:enterprise` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.code_security_configuration_repositories import CodeSecurityConfigurationRepositories
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
    api_instance = github_openapi.CodeSecurityApi(api_client)
    enterprise = 'enterprise_example' # str | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    configuration_id = 56 # int | The unique identifier of the code security configuration.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    before = 'before_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)
    after = 'after_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)
    status = 'all' # str | A comma-separated list of statuses. If specified, only repositories with these attachment statuses will be returned.  Can be: `all`, `attached`, `attaching`, `removed`, `enforced`, `failed`, `updating`, `removed_by_enterprise` (optional) (default to 'all')

    try:
        # Get repositories associated with an enterprise code security configuration
        api_response = api_instance.code_security_get_repositories_for_enterprise_configuration(enterprise, configuration_id, per_page=per_page, before=before, after=after, status=status)
        print("The response of CodeSecurityApi->code_security_get_repositories_for_enterprise_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeSecurityApi->code_security_get_repositories_for_enterprise_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **configuration_id** | **int**| The unique identifier of the code security configuration. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **before** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 
 **after** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 
 **status** | **str**| A comma-separated list of statuses. If specified, only repositories with these attachment statuses will be returned.  Can be: &#x60;all&#x60;, &#x60;attached&#x60;, &#x60;attaching&#x60;, &#x60;removed&#x60;, &#x60;enforced&#x60;, &#x60;failed&#x60;, &#x60;updating&#x60;, &#x60;removed_by_enterprise&#x60; | [optional] [default to &#39;all&#39;]

### Return type

[**List[CodeSecurityConfigurationRepositories]**](CodeSecurityConfigurationRepositories.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_security_get_single_configuration_for_enterprise**
> CodeSecurityConfiguration code_security_get_single_configuration_for_enterprise(enterprise, configuration_id)

Retrieve a code security configuration of an enterprise

Gets a code security configuration available in an enterprise.  The authenticated user must be an administrator of the enterprise in order to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `read:enterprise` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.code_security_configuration import CodeSecurityConfiguration
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
    api_instance = github_openapi.CodeSecurityApi(api_client)
    enterprise = 'enterprise_example' # str | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    configuration_id = 56 # int | The unique identifier of the code security configuration.

    try:
        # Retrieve a code security configuration of an enterprise
        api_response = api_instance.code_security_get_single_configuration_for_enterprise(enterprise, configuration_id)
        print("The response of CodeSecurityApi->code_security_get_single_configuration_for_enterprise:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeSecurityApi->code_security_get_single_configuration_for_enterprise: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **configuration_id** | **int**| The unique identifier of the code security configuration. | 

### Return type

[**CodeSecurityConfiguration**](CodeSecurityConfiguration.md)

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

# **code_security_set_configuration_as_default**
> CodeSecuritySetConfigurationAsDefaultForEnterprise200Response code_security_set_configuration_as_default(org, configuration_id, code_security_set_configuration_as_default_for_enterprise_request)

Set a code security configuration as a default for an organization

Sets a code security configuration as a default to be applied to new repositories in your organization.  This configuration will be applied to the matching repository type (all, none, public, private and internal) by default when they are created.  The authenticated user must be an administrator or security manager for the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `write:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.code_security_set_configuration_as_default_for_enterprise200_response import CodeSecuritySetConfigurationAsDefaultForEnterprise200Response
from github_openapi.models.code_security_set_configuration_as_default_for_enterprise_request import CodeSecuritySetConfigurationAsDefaultForEnterpriseRequest
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
    api_instance = github_openapi.CodeSecurityApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    configuration_id = 56 # int | The unique identifier of the code security configuration.
    code_security_set_configuration_as_default_for_enterprise_request = {"default_for_new_repos":"all"} # CodeSecuritySetConfigurationAsDefaultForEnterpriseRequest | 

    try:
        # Set a code security configuration as a default for an organization
        api_response = api_instance.code_security_set_configuration_as_default(org, configuration_id, code_security_set_configuration_as_default_for_enterprise_request)
        print("The response of CodeSecurityApi->code_security_set_configuration_as_default:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeSecurityApi->code_security_set_configuration_as_default: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **configuration_id** | **int**| The unique identifier of the code security configuration. | 
 **code_security_set_configuration_as_default_for_enterprise_request** | [**CodeSecuritySetConfigurationAsDefaultForEnterpriseRequest**](CodeSecuritySetConfigurationAsDefaultForEnterpriseRequest.md)|  | 

### Return type

[**CodeSecuritySetConfigurationAsDefaultForEnterprise200Response**](CodeSecuritySetConfigurationAsDefaultForEnterprise200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default successfully changed. |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_security_set_configuration_as_default_for_enterprise**
> CodeSecuritySetConfigurationAsDefaultForEnterprise200Response code_security_set_configuration_as_default_for_enterprise(enterprise, configuration_id, code_security_set_configuration_as_default_for_enterprise_request)

Set a code security configuration as a default for an enterprise

Sets a code security configuration as a default to be applied to new repositories in your enterprise.  This configuration will be applied by default to the matching repository type when created, but only for organizations within the enterprise that do not already have a default code security configuration set.  The authenticated user must be an administrator for the enterprise to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:enterprise` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.code_security_set_configuration_as_default_for_enterprise200_response import CodeSecuritySetConfigurationAsDefaultForEnterprise200Response
from github_openapi.models.code_security_set_configuration_as_default_for_enterprise_request import CodeSecuritySetConfigurationAsDefaultForEnterpriseRequest
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
    api_instance = github_openapi.CodeSecurityApi(api_client)
    enterprise = 'enterprise_example' # str | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    configuration_id = 56 # int | The unique identifier of the code security configuration.
    code_security_set_configuration_as_default_for_enterprise_request = {"default_for_new_repos":"all"} # CodeSecuritySetConfigurationAsDefaultForEnterpriseRequest | 

    try:
        # Set a code security configuration as a default for an enterprise
        api_response = api_instance.code_security_set_configuration_as_default_for_enterprise(enterprise, configuration_id, code_security_set_configuration_as_default_for_enterprise_request)
        print("The response of CodeSecurityApi->code_security_set_configuration_as_default_for_enterprise:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeSecurityApi->code_security_set_configuration_as_default_for_enterprise: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **configuration_id** | **int**| The unique identifier of the code security configuration. | 
 **code_security_set_configuration_as_default_for_enterprise_request** | [**CodeSecuritySetConfigurationAsDefaultForEnterpriseRequest**](CodeSecuritySetConfigurationAsDefaultForEnterpriseRequest.md)|  | 

### Return type

[**CodeSecuritySetConfigurationAsDefaultForEnterprise200Response**](CodeSecuritySetConfigurationAsDefaultForEnterprise200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default successfully changed. |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_security_update_configuration**
> CodeSecurityConfiguration code_security_update_configuration(org, configuration_id, code_security_update_configuration_request)

Update a code security configuration

Updates a code security configuration in an organization.  The authenticated user must be an administrator or security manager for the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `write:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.code_security_configuration import CodeSecurityConfiguration
from github_openapi.models.code_security_update_configuration_request import CodeSecurityUpdateConfigurationRequest
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
    api_instance = github_openapi.CodeSecurityApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    configuration_id = 56 # int | The unique identifier of the code security configuration.
    code_security_update_configuration_request = {"name":"octo-org recommended settings v2","secret_scanning":"disabled","code_scanning_default_setup":"enabled"} # CodeSecurityUpdateConfigurationRequest | 

    try:
        # Update a code security configuration
        api_response = api_instance.code_security_update_configuration(org, configuration_id, code_security_update_configuration_request)
        print("The response of CodeSecurityApi->code_security_update_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeSecurityApi->code_security_update_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **configuration_id** | **int**| The unique identifier of the code security configuration. | 
 **code_security_update_configuration_request** | [**CodeSecurityUpdateConfigurationRequest**](CodeSecurityUpdateConfigurationRequest.md)|  | 

### Return type

[**CodeSecurityConfiguration**](CodeSecurityConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response when a configuration is updated |  -  |
**204** | Response when no new updates are made |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **code_security_update_enterprise_configuration**
> CodeSecurityConfiguration code_security_update_enterprise_configuration(enterprise, configuration_id, code_security_update_enterprise_configuration_request)

Update a custom code security configuration for an enterprise

Updates a code security configuration in an enterprise.  The authenticated user must be an administrator of the enterprise in order to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:enterprise` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.code_security_configuration import CodeSecurityConfiguration
from github_openapi.models.code_security_update_enterprise_configuration_request import CodeSecurityUpdateEnterpriseConfigurationRequest
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
    api_instance = github_openapi.CodeSecurityApi(api_client)
    enterprise = 'enterprise_example' # str | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    configuration_id = 56 # int | The unique identifier of the code security configuration.
    code_security_update_enterprise_configuration_request = {"name":"octo-enterprise recommended settings v2","secret_scanning":"disabled","code_scanning_default_setup":"enabled"} # CodeSecurityUpdateEnterpriseConfigurationRequest | 

    try:
        # Update a custom code security configuration for an enterprise
        api_response = api_instance.code_security_update_enterprise_configuration(enterprise, configuration_id, code_security_update_enterprise_configuration_request)
        print("The response of CodeSecurityApi->code_security_update_enterprise_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeSecurityApi->code_security_update_enterprise_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **configuration_id** | **int**| The unique identifier of the code security configuration. | 
 **code_security_update_enterprise_configuration_request** | [**CodeSecurityUpdateEnterpriseConfigurationRequest**](CodeSecurityUpdateEnterpriseConfigurationRequest.md)|  | 

### Return type

[**CodeSecurityConfiguration**](CodeSecurityConfiguration.md)

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
**404** | Resource not found |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

