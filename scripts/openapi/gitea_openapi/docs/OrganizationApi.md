# gitea_openapi.OrganizationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_org_repo**](OrganizationApi.md#create_org_repo) | **POST** /orgs/{org}/repos | Create a repository in an organization
[**create_org_repo_deprecated**](OrganizationApi.md#create_org_repo_deprecated) | **POST** /org/{org}/repos | Create a repository in an organization
[**create_org_variable**](OrganizationApi.md#create_org_variable) | **POST** /orgs/{org}/actions/variables/{variablename} | Create an org-level variable
[**delete_org_secret**](OrganizationApi.md#delete_org_secret) | **DELETE** /orgs/{org}/actions/secrets/{secretname} | Delete a secret in an organization
[**delete_org_variable**](OrganizationApi.md#delete_org_variable) | **DELETE** /orgs/{org}/actions/variables/{variablename} | Delete an org-level variable
[**get_org_variable**](OrganizationApi.md#get_org_variable) | **GET** /orgs/{org}/actions/variables/{variablename} | Get an org-level variable
[**get_org_variables_list**](OrganizationApi.md#get_org_variables_list) | **GET** /orgs/{org}/actions/variables | Get an org-level variables list
[**org_add_team_member**](OrganizationApi.md#org_add_team_member) | **PUT** /teams/{id}/members/{username} | Add a team member
[**org_add_team_repository**](OrganizationApi.md#org_add_team_repository) | **PUT** /teams/{id}/repos/{org}/{repo} | Add a repository to a team
[**org_conceal_member**](OrganizationApi.md#org_conceal_member) | **DELETE** /orgs/{org}/public_members/{username} | Conceal a user&#39;s membership
[**org_create**](OrganizationApi.md#org_create) | **POST** /orgs | Create an organization
[**org_create_hook**](OrganizationApi.md#org_create_hook) | **POST** /orgs/{org}/hooks | Create a hook
[**org_create_label**](OrganizationApi.md#org_create_label) | **POST** /orgs/{org}/labels | Create a label for an organization
[**org_create_team**](OrganizationApi.md#org_create_team) | **POST** /orgs/{org}/teams | Create a team
[**org_delete**](OrganizationApi.md#org_delete) | **DELETE** /orgs/{org} | Delete an organization
[**org_delete_avatar**](OrganizationApi.md#org_delete_avatar) | **DELETE** /orgs/{org}/avatar | Delete Avatar
[**org_delete_hook**](OrganizationApi.md#org_delete_hook) | **DELETE** /orgs/{org}/hooks/{id} | Delete a hook
[**org_delete_label**](OrganizationApi.md#org_delete_label) | **DELETE** /orgs/{org}/labels/{id} | Delete a label
[**org_delete_member**](OrganizationApi.md#org_delete_member) | **DELETE** /orgs/{org}/members/{username} | Remove a member from an organization
[**org_delete_team**](OrganizationApi.md#org_delete_team) | **DELETE** /teams/{id} | Delete a team
[**org_edit**](OrganizationApi.md#org_edit) | **PATCH** /orgs/{org} | Edit an organization
[**org_edit_hook**](OrganizationApi.md#org_edit_hook) | **PATCH** /orgs/{org}/hooks/{id} | Update a hook
[**org_edit_label**](OrganizationApi.md#org_edit_label) | **PATCH** /orgs/{org}/labels/{id} | Update a label
[**org_edit_team**](OrganizationApi.md#org_edit_team) | **PATCH** /teams/{id} | Edit a team
[**org_get**](OrganizationApi.md#org_get) | **GET** /orgs/{org} | Get an organization
[**org_get_all**](OrganizationApi.md#org_get_all) | **GET** /orgs | Get list of organizations
[**org_get_hook**](OrganizationApi.md#org_get_hook) | **GET** /orgs/{org}/hooks/{id} | Get a hook
[**org_get_label**](OrganizationApi.md#org_get_label) | **GET** /orgs/{org}/labels/{id} | Get a single label
[**org_get_runner_registration_token**](OrganizationApi.md#org_get_runner_registration_token) | **GET** /orgs/{org}/actions/runners/registration-token | Get an organization&#39;s actions runner registration token
[**org_get_team**](OrganizationApi.md#org_get_team) | **GET** /teams/{id} | Get a team
[**org_get_user_permissions**](OrganizationApi.md#org_get_user_permissions) | **GET** /users/{username}/orgs/{org}/permissions | Get user permissions in organization
[**org_is_member**](OrganizationApi.md#org_is_member) | **GET** /orgs/{org}/members/{username} | Check if a user is a member of an organization
[**org_is_public_member**](OrganizationApi.md#org_is_public_member) | **GET** /orgs/{org}/public_members/{username} | Check if a user is a public member of an organization
[**org_list_actions_secrets**](OrganizationApi.md#org_list_actions_secrets) | **GET** /orgs/{org}/actions/secrets | List an organization&#39;s actions secrets
[**org_list_activity_feeds**](OrganizationApi.md#org_list_activity_feeds) | **GET** /orgs/{org}/activities/feeds | List an organization&#39;s activity feeds
[**org_list_current_user_orgs**](OrganizationApi.md#org_list_current_user_orgs) | **GET** /user/orgs | List the current user&#39;s organizations
[**org_list_hooks**](OrganizationApi.md#org_list_hooks) | **GET** /orgs/{org}/hooks | List an organization&#39;s webhooks
[**org_list_labels**](OrganizationApi.md#org_list_labels) | **GET** /orgs/{org}/labels | List an organization&#39;s labels
[**org_list_members**](OrganizationApi.md#org_list_members) | **GET** /orgs/{org}/members | List an organization&#39;s members
[**org_list_public_members**](OrganizationApi.md#org_list_public_members) | **GET** /orgs/{org}/public_members | List an organization&#39;s public members
[**org_list_repos**](OrganizationApi.md#org_list_repos) | **GET** /orgs/{org}/repos | List an organization&#39;s repos
[**org_list_team_activity_feeds**](OrganizationApi.md#org_list_team_activity_feeds) | **GET** /teams/{id}/activities/feeds | List a team&#39;s activity feeds
[**org_list_team_member**](OrganizationApi.md#org_list_team_member) | **GET** /teams/{id}/members/{username} | List a particular member of team
[**org_list_team_members**](OrganizationApi.md#org_list_team_members) | **GET** /teams/{id}/members | List a team&#39;s members
[**org_list_team_repo**](OrganizationApi.md#org_list_team_repo) | **GET** /teams/{id}/repos/{org}/{repo} | List a particular repo of team
[**org_list_team_repos**](OrganizationApi.md#org_list_team_repos) | **GET** /teams/{id}/repos | List a team&#39;s repos
[**org_list_teams**](OrganizationApi.md#org_list_teams) | **GET** /orgs/{org}/teams | List an organization&#39;s teams
[**org_list_user_orgs**](OrganizationApi.md#org_list_user_orgs) | **GET** /users/{username}/orgs | List a user&#39;s organizations
[**org_publicize_member**](OrganizationApi.md#org_publicize_member) | **PUT** /orgs/{org}/public_members/{username} | Publicize a user&#39;s membership
[**org_remove_team_member**](OrganizationApi.md#org_remove_team_member) | **DELETE** /teams/{id}/members/{username} | Remove a team member
[**org_remove_team_repository**](OrganizationApi.md#org_remove_team_repository) | **DELETE** /teams/{id}/repos/{org}/{repo} | Remove a repository from a team
[**org_update_avatar**](OrganizationApi.md#org_update_avatar) | **POST** /orgs/{org}/avatar | Update Avatar
[**organization_block_user**](OrganizationApi.md#organization_block_user) | **PUT** /orgs/{org}/blocks/{username} | Block a user
[**organization_check_user_block**](OrganizationApi.md#organization_check_user_block) | **GET** /orgs/{org}/blocks/{username} | Check if a user is blocked by the organization
[**organization_list_blocks**](OrganizationApi.md#organization_list_blocks) | **GET** /orgs/{org}/blocks | List users blocked by the organization
[**organization_unblock_user**](OrganizationApi.md#organization_unblock_user) | **DELETE** /orgs/{org}/blocks/{username} | Unblock a user
[**team_search**](OrganizationApi.md#team_search) | **GET** /orgs/{org}/teams/search | Search for teams within an organization
[**update_org_secret**](OrganizationApi.md#update_org_secret) | **PUT** /orgs/{org}/actions/secrets/{secretname} | Create or Update a secret value in an organization
[**update_org_variable**](OrganizationApi.md#update_org_variable) | **PUT** /orgs/{org}/actions/variables/{variablename} | Update an org-level variable


# **create_org_repo**
> Repository create_org_repo(org, body=body)

Create a repository in an organization

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.create_repo_option import CreateRepoOption
from gitea_openapi.models.repository import Repository
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of organization
    body = gitea_openapi.CreateRepoOption() # CreateRepoOption |  (optional)

    try:
        # Create a repository in an organization
        api_response = api_instance.create_org_repo(org, body=body)
        print("The response of OrganizationApi->create_org_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->create_org_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of organization | 
 **body** | [**CreateRepoOption**](CreateRepoOption.md)|  | [optional] 

### Return type

[**Repository**](Repository.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Repository |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_org_repo_deprecated**
> Repository create_org_repo_deprecated(org, body=body)

Create a repository in an organization

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.create_repo_option import CreateRepoOption
from gitea_openapi.models.repository import Repository
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of organization
    body = gitea_openapi.CreateRepoOption() # CreateRepoOption |  (optional)

    try:
        # Create a repository in an organization
        api_response = api_instance.create_org_repo_deprecated(org, body=body)
        print("The response of OrganizationApi->create_org_repo_deprecated:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->create_org_repo_deprecated: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of organization | 
 **body** | [**CreateRepoOption**](CreateRepoOption.md)|  | [optional] 

### Return type

[**Repository**](Repository.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Repository |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_org_variable**
> create_org_variable(org, variablename, body=body)

Create an org-level variable

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.create_variable_option import CreateVariableOption
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    variablename = 'variablename_example' # str | name of the variable
    body = gitea_openapi.CreateVariableOption() # CreateVariableOption |  (optional)

    try:
        # Create an org-level variable
        api_instance.create_org_variable(org, variablename, body=body)
    except Exception as e:
        print("Exception when calling OrganizationApi->create_org_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **variablename** | **str**| name of the variable | 
 **body** | [**CreateVariableOption**](CreateVariableOption.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | response when creating an org-level variable |  -  |
**204** | response when creating an org-level variable |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_org_secret**
> delete_org_secret(org, secretname)

Delete a secret in an organization

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of organization
    secretname = 'secretname_example' # str | name of the secret

    try:
        # Delete a secret in an organization
        api_instance.delete_org_secret(org, secretname)
    except Exception as e:
        print("Exception when calling OrganizationApi->delete_org_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of organization | 
 **secretname** | **str**| name of the secret | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | delete one secret of the organization |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_org_variable**
> ActionVariable delete_org_variable(org, variablename)

Delete an org-level variable

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.action_variable import ActionVariable
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    variablename = 'variablename_example' # str | name of the variable

    try:
        # Delete an org-level variable
        api_response = api_instance.delete_org_variable(org, variablename)
        print("The response of OrganizationApi->delete_org_variable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->delete_org_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **variablename** | **str**| name of the variable | 

### Return type

[**ActionVariable**](ActionVariable.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ActionVariable |  -  |
**201** | response when deleting a variable |  -  |
**204** | response when deleting a variable |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_org_variable**
> ActionVariable get_org_variable(org, variablename)

Get an org-level variable

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.action_variable import ActionVariable
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    variablename = 'variablename_example' # str | name of the variable

    try:
        # Get an org-level variable
        api_response = api_instance.get_org_variable(org, variablename)
        print("The response of OrganizationApi->get_org_variable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->get_org_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **variablename** | **str**| name of the variable | 

### Return type

[**ActionVariable**](ActionVariable.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ActionVariable |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_org_variables_list**
> List[ActionVariable] get_org_variables_list(org, page=page, limit=limit)

Get an org-level variables list

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.action_variable import ActionVariable
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # Get an org-level variables list
        api_response = api_instance.get_org_variables_list(org, page=page, limit=limit)
        print("The response of OrganizationApi->get_org_variables_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->get_org_variables_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[ActionVariable]**](ActionVariable.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | VariableList |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_add_team_member**
> org_add_team_member(id, username)

Add a team member

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    id = 56 # int | id of the team
    username = 'username_example' # str | username of the user to add

    try:
        # Add a team member
        api_instance.org_add_team_member(id, username)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_add_team_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of the team | 
 **username** | **str**| username of the user to add | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_add_team_repository**
> org_add_team_repository(id, org, repo)

Add a repository to a team

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    id = 56 # int | id of the team
    org = 'org_example' # str | organization that owns the repo to add
    repo = 'repo_example' # str | name of the repo to add

    try:
        # Add a repository to a team
        api_instance.org_add_team_repository(id, org, repo)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_add_team_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of the team | 
 **org** | **str**| organization that owns the repo to add | 
 **repo** | **str**| name of the repo to add | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_conceal_member**
> org_conceal_member(org, username)

Conceal a user's membership

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    username = 'username_example' # str | username of the user

    try:
        # Conceal a user's membership
        api_instance.org_conceal_member(org, username)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_conceal_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **username** | **str**| username of the user | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_create**
> Organization org_create(organization)

Create an organization

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.create_org_option import CreateOrgOption
from gitea_openapi.models.organization import Organization
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    organization = gitea_openapi.CreateOrgOption() # CreateOrgOption | 

    try:
        # Create an organization
        api_response = api_instance.org_create(organization)
        print("The response of OrganizationApi->org_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | [**CreateOrgOption**](CreateOrgOption.md)|  | 

### Return type

[**Organization**](Organization.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Organization |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_create_hook**
> Hook org_create_hook(org, body)

Create a hook

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.create_hook_option import CreateHookOption
from gitea_openapi.models.hook import Hook
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    body = gitea_openapi.CreateHookOption() # CreateHookOption | 

    try:
        # Create a hook
        api_response = api_instance.org_create_hook(org, body)
        print("The response of OrganizationApi->org_create_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_create_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **body** | [**CreateHookOption**](CreateHookOption.md)|  | 

### Return type

[**Hook**](Hook.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Hook |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_create_label**
> Label org_create_label(org, body=body)

Create a label for an organization

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.create_label_option import CreateLabelOption
from gitea_openapi.models.label import Label
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    body = gitea_openapi.CreateLabelOption() # CreateLabelOption |  (optional)

    try:
        # Create a label for an organization
        api_response = api_instance.org_create_label(org, body=body)
        print("The response of OrganizationApi->org_create_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_create_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **body** | [**CreateLabelOption**](CreateLabelOption.md)|  | [optional] 

### Return type

[**Label**](Label.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Label |  -  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_create_team**
> Team org_create_team(org, body=body)

Create a team

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.create_team_option import CreateTeamOption
from gitea_openapi.models.team import Team
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    body = gitea_openapi.CreateTeamOption() # CreateTeamOption |  (optional)

    try:
        # Create a team
        api_response = api_instance.org_create_team(org, body=body)
        print("The response of OrganizationApi->org_create_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_create_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **body** | [**CreateTeamOption**](CreateTeamOption.md)|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Team |  -  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_delete**
> org_delete(org)

Delete an organization

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | organization that is to be deleted

    try:
        # Delete an organization
        api_instance.org_delete(org)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| organization that is to be deleted | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_delete_avatar**
> org_delete_avatar(org)

Delete Avatar

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization

    try:
        # Delete Avatar
        api_instance.org_delete_avatar(org)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_delete_avatar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_delete_hook**
> org_delete_hook(org, id)

Delete a hook

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    id = 56 # int | id of the hook to delete

    try:
        # Delete a hook
        api_instance.org_delete_hook(org, id)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_delete_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **id** | **int**| id of the hook to delete | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_delete_label**
> org_delete_label(org, id)

Delete a label

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    id = 56 # int | id of the label to delete

    try:
        # Delete a label
        api_instance.org_delete_label(org, id)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_delete_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **id** | **int**| id of the label to delete | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_delete_member**
> org_delete_member(org, username)

Remove a member from an organization

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    username = 'username_example' # str | username of the user

    try:
        # Remove a member from an organization
        api_instance.org_delete_member(org, username)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_delete_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **username** | **str**| username of the user | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | member removed |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_delete_team**
> org_delete_team(id)

Delete a team

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    id = 56 # int | id of the team to delete

    try:
        # Delete a team
        api_instance.org_delete_team(id)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_delete_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of the team to delete | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | team deleted |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_edit**
> Organization org_edit(org, body)

Edit an organization

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.edit_org_option import EditOrgOption
from gitea_openapi.models.organization import Organization
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization to edit
    body = gitea_openapi.EditOrgOption() # EditOrgOption | 

    try:
        # Edit an organization
        api_response = api_instance.org_edit(org, body)
        print("The response of OrganizationApi->org_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization to edit | 
 **body** | [**EditOrgOption**](EditOrgOption.md)|  | 

### Return type

[**Organization**](Organization.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Organization |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_edit_hook**
> Hook org_edit_hook(org, id, body=body)

Update a hook

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.edit_hook_option import EditHookOption
from gitea_openapi.models.hook import Hook
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    id = 56 # int | id of the hook to update
    body = gitea_openapi.EditHookOption() # EditHookOption |  (optional)

    try:
        # Update a hook
        api_response = api_instance.org_edit_hook(org, id, body=body)
        print("The response of OrganizationApi->org_edit_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_edit_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **id** | **int**| id of the hook to update | 
 **body** | [**EditHookOption**](EditHookOption.md)|  | [optional] 

### Return type

[**Hook**](Hook.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hook |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_edit_label**
> Label org_edit_label(org, id, body=body)

Update a label

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.edit_label_option import EditLabelOption
from gitea_openapi.models.label import Label
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    id = 56 # int | id of the label to edit
    body = gitea_openapi.EditLabelOption() # EditLabelOption |  (optional)

    try:
        # Update a label
        api_response = api_instance.org_edit_label(org, id, body=body)
        print("The response of OrganizationApi->org_edit_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_edit_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **id** | **int**| id of the label to edit | 
 **body** | [**EditLabelOption**](EditLabelOption.md)|  | [optional] 

### Return type

[**Label**](Label.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Label |  -  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_edit_team**
> Team org_edit_team(id, body=body)

Edit a team

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.edit_team_option import EditTeamOption
from gitea_openapi.models.team import Team
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    id = 56 # int | id of the team to edit
    body = gitea_openapi.EditTeamOption() # EditTeamOption |  (optional)

    try:
        # Edit a team
        api_response = api_instance.org_edit_team(id, body=body)
        print("The response of OrganizationApi->org_edit_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_edit_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of the team to edit | 
 **body** | [**EditTeamOption**](EditTeamOption.md)|  | [optional] 

### Return type

[**Team**](Team.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Team |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_get**
> Organization org_get(org)

Get an organization

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.organization import Organization
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization to get

    try:
        # Get an organization
        api_response = api_instance.org_get(org)
        print("The response of OrganizationApi->org_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization to get | 

### Return type

[**Organization**](Organization.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Organization |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_get_all**
> List[Organization] org_get_all(page=page, limit=limit)

Get list of organizations

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.organization import Organization
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # Get list of organizations
        api_response = api_instance.org_get_all(page=page, limit=limit)
        print("The response of OrganizationApi->org_get_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_get_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[Organization]**](Organization.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OrganizationList |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_get_hook**
> Hook org_get_hook(org, id)

Get a hook

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.hook import Hook
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    id = 56 # int | id of the hook to get

    try:
        # Get a hook
        api_response = api_instance.org_get_hook(org, id)
        print("The response of OrganizationApi->org_get_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_get_hook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **id** | **int**| id of the hook to get | 

### Return type

[**Hook**](Hook.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hook |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_get_label**
> Label org_get_label(org, id)

Get a single label

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.label import Label
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    id = 56 # int | id of the label to get

    try:
        # Get a single label
        api_response = api_instance.org_get_label(org, id)
        print("The response of OrganizationApi->org_get_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_get_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **id** | **int**| id of the label to get | 

### Return type

[**Label**](Label.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Label |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_get_runner_registration_token**
> org_get_runner_registration_token(org)

Get an organization's actions runner registration token

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization

    try:
        # Get an organization's actions runner registration token
        api_instance.org_get_runner_registration_token(org)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_get_runner_registration_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RegistrationToken is response related to registration token |  * token -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_get_team**
> Team org_get_team(id)

Get a team

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.team import Team
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    id = 56 # int | id of the team to get

    try:
        # Get a team
        api_response = api_instance.org_get_team(id)
        print("The response of OrganizationApi->org_get_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_get_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of the team to get | 

### Return type

[**Team**](Team.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Team |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_get_user_permissions**
> OrganizationPermissions org_get_user_permissions(username, org)

Get user permissions in organization

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.organization_permissions import OrganizationPermissions
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    username = 'username_example' # str | username of user
    org = 'org_example' # str | name of the organization

    try:
        # Get user permissions in organization
        api_response = api_instance.org_get_user_permissions(username, org)
        print("The response of OrganizationApi->org_get_user_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_get_user_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username of user | 
 **org** | **str**| name of the organization | 

### Return type

[**OrganizationPermissions**](OrganizationPermissions.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OrganizationPermissions |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_is_member**
> org_is_member(org, username)

Check if a user is a member of an organization

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    username = 'username_example' # str | username of the user

    try:
        # Check if a user is a member of an organization
        api_instance.org_is_member(org, username)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_is_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **username** | **str**| username of the user | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | user is a member |  -  |
**303** | redirection to /orgs/{org}/public_members/{username} |  -  |
**404** | user is not a member |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_is_public_member**
> org_is_public_member(org, username)

Check if a user is a public member of an organization

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    username = 'username_example' # str | username of the user

    try:
        # Check if a user is a public member of an organization
        api_instance.org_is_public_member(org, username)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_is_public_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **username** | **str**| username of the user | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | user is a public member |  -  |
**404** | user is not a public member |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_list_actions_secrets**
> List[Secret] org_list_actions_secrets(org, page=page, limit=limit)

List an organization's actions secrets

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.secret import Secret
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # List an organization's actions secrets
        api_response = api_instance.org_list_actions_secrets(org, page=page, limit=limit)
        print("The response of OrganizationApi->org_list_actions_secrets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_list_actions_secrets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[Secret]**](Secret.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SecretList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_list_activity_feeds**
> List[Activity] org_list_activity_feeds(org, var_date=var_date, page=page, limit=limit)

List an organization's activity feeds

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.activity import Activity
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the org
    var_date = '2013-10-20' # date | the date of the activities to be found (optional)
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # List an organization's activity feeds
        api_response = api_instance.org_list_activity_feeds(org, var_date=var_date, page=page, limit=limit)
        print("The response of OrganizationApi->org_list_activity_feeds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_list_activity_feeds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the org | 
 **var_date** | **date**| the date of the activities to be found | [optional] 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[Activity]**](Activity.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ActivityFeedsList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_list_current_user_orgs**
> List[Organization] org_list_current_user_orgs(page=page, limit=limit)

List the current user's organizations

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.organization import Organization
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # List the current user's organizations
        api_response = api_instance.org_list_current_user_orgs(page=page, limit=limit)
        print("The response of OrganizationApi->org_list_current_user_orgs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_list_current_user_orgs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[Organization]**](Organization.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OrganizationList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_list_hooks**
> List[Hook] org_list_hooks(org, page=page, limit=limit)

List an organization's webhooks

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.hook import Hook
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # List an organization's webhooks
        api_response = api_instance.org_list_hooks(org, page=page, limit=limit)
        print("The response of OrganizationApi->org_list_hooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_list_hooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[Hook]**](Hook.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HookList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_list_labels**
> List[Label] org_list_labels(org, page=page, limit=limit)

List an organization's labels

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.label import Label
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # List an organization's labels
        api_response = api_instance.org_list_labels(org, page=page, limit=limit)
        print("The response of OrganizationApi->org_list_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_list_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[Label]**](Label.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | LabelList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_list_members**
> List[User] org_list_members(org, page=page, limit=limit)

List an organization's members

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.user import User
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # List an organization's members
        api_response = api_instance.org_list_members(org, page=page, limit=limit)
        print("The response of OrganizationApi->org_list_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_list_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[User]**](User.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_list_public_members**
> List[User] org_list_public_members(org, page=page, limit=limit)

List an organization's public members

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.user import User
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # List an organization's public members
        api_response = api_instance.org_list_public_members(org, page=page, limit=limit)
        print("The response of OrganizationApi->org_list_public_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_list_public_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[User]**](User.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_list_repos**
> List[Repository] org_list_repos(org, page=page, limit=limit)

List an organization's repos

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.repository import Repository
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # List an organization's repos
        api_response = api_instance.org_list_repos(org, page=page, limit=limit)
        print("The response of OrganizationApi->org_list_repos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_list_repos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[Repository]**](Repository.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RepositoryList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_list_team_activity_feeds**
> List[Activity] org_list_team_activity_feeds(id, var_date=var_date, page=page, limit=limit)

List a team's activity feeds

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.activity import Activity
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    id = 56 # int | id of the team
    var_date = '2013-10-20' # date | the date of the activities to be found (optional)
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # List a team's activity feeds
        api_response = api_instance.org_list_team_activity_feeds(id, var_date=var_date, page=page, limit=limit)
        print("The response of OrganizationApi->org_list_team_activity_feeds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_list_team_activity_feeds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of the team | 
 **var_date** | **date**| the date of the activities to be found | [optional] 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[Activity]**](Activity.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ActivityFeedsList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_list_team_member**
> User org_list_team_member(id, username)

List a particular member of team

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.user import User
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    id = 56 # int | id of the team
    username = 'username_example' # str | username of the member to list

    try:
        # List a particular member of team
        api_response = api_instance.org_list_team_member(id, username)
        print("The response of OrganizationApi->org_list_team_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_list_team_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of the team | 
 **username** | **str**| username of the member to list | 

### Return type

[**User**](User.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_list_team_members**
> List[User] org_list_team_members(id, page=page, limit=limit)

List a team's members

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.user import User
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    id = 56 # int | id of the team
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # List a team's members
        api_response = api_instance.org_list_team_members(id, page=page, limit=limit)
        print("The response of OrganizationApi->org_list_team_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_list_team_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of the team | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[User]**](User.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_list_team_repo**
> Repository org_list_team_repo(id, org, repo)

List a particular repo of team

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.repository import Repository
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    id = 56 # int | id of the team
    org = 'org_example' # str | organization that owns the repo to list
    repo = 'repo_example' # str | name of the repo to list

    try:
        # List a particular repo of team
        api_response = api_instance.org_list_team_repo(id, org, repo)
        print("The response of OrganizationApi->org_list_team_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_list_team_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of the team | 
 **org** | **str**| organization that owns the repo to list | 
 **repo** | **str**| name of the repo to list | 

### Return type

[**Repository**](Repository.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Repository |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_list_team_repos**
> List[Repository] org_list_team_repos(id, page=page, limit=limit)

List a team's repos

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.repository import Repository
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    id = 56 # int | id of the team
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # List a team's repos
        api_response = api_instance.org_list_team_repos(id, page=page, limit=limit)
        print("The response of OrganizationApi->org_list_team_repos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_list_team_repos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of the team | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[Repository]**](Repository.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RepositoryList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_list_teams**
> List[Team] org_list_teams(org, page=page, limit=limit)

List an organization's teams

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.team import Team
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # List an organization's teams
        api_response = api_instance.org_list_teams(org, page=page, limit=limit)
        print("The response of OrganizationApi->org_list_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_list_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[Team]**](Team.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TeamList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_list_user_orgs**
> List[Organization] org_list_user_orgs(username, page=page, limit=limit)

List a user's organizations

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.organization import Organization
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    username = 'username_example' # str | username of user
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # List a user's organizations
        api_response = api_instance.org_list_user_orgs(username, page=page, limit=limit)
        print("The response of OrganizationApi->org_list_user_orgs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_list_user_orgs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username of user | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[Organization]**](Organization.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OrganizationList |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_publicize_member**
> org_publicize_member(org, username)

Publicize a user's membership

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    username = 'username_example' # str | username of the user

    try:
        # Publicize a user's membership
        api_instance.org_publicize_member(org, username)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_publicize_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **username** | **str**| username of the user | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | membership publicized |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_remove_team_member**
> org_remove_team_member(id, username)

Remove a team member

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    id = 56 # int | id of the team
    username = 'username_example' # str | username of the user to remove

    try:
        # Remove a team member
        api_instance.org_remove_team_member(id, username)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_remove_team_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of the team | 
 **username** | **str**| username of the user to remove | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_remove_team_repository**
> org_remove_team_repository(id, org, repo)

Remove a repository from a team

This does not delete the repository, it only removes the repository from the team.

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    id = 56 # int | id of the team
    org = 'org_example' # str | organization that owns the repo to remove
    repo = 'repo_example' # str | name of the repo to remove

    try:
        # Remove a repository from a team
        api_instance.org_remove_team_repository(id, org, repo)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_remove_team_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| id of the team | 
 **org** | **str**| organization that owns the repo to remove | 
 **repo** | **str**| name of the repo to remove | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**403** | APIForbiddenError is a forbidden error response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **org_update_avatar**
> org_update_avatar(org, body=body)

Update Avatar

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.update_user_avatar_option import UpdateUserAvatarOption
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    body = gitea_openapi.UpdateUserAvatarOption() # UpdateUserAvatarOption |  (optional)

    try:
        # Update Avatar
        api_instance.org_update_avatar(org, body=body)
    except Exception as e:
        print("Exception when calling OrganizationApi->org_update_avatar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **body** | [**UpdateUserAvatarOption**](UpdateUserAvatarOption.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json, text/plain
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_block_user**
> organization_block_user(org, username, note=note)

Block a user

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    username = 'username_example' # str | user to block
    note = 'note_example' # str | optional note for the block (optional)

    try:
        # Block a user
        api_instance.organization_block_user(org, username, note=note)
    except Exception as e:
        print("Exception when calling OrganizationApi->organization_block_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **username** | **str**| user to block | 
 **note** | **str**| optional note for the block | [optional] 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_check_user_block**
> organization_check_user_block(org, username)

Check if a user is blocked by the organization

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    username = 'username_example' # str | user to check

    try:
        # Check if a user is blocked by the organization
        api_instance.organization_check_user_block(org, username)
    except Exception as e:
        print("Exception when calling OrganizationApi->organization_check_user_block: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **username** | **str**| user to check | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_list_blocks**
> List[User] organization_list_blocks(org, page=page, limit=limit)

List users blocked by the organization

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.user import User
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # List users blocked by the organization
        api_response = api_instance.organization_list_blocks(org, page=page, limit=limit)
        print("The response of OrganizationApi->organization_list_blocks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->organization_list_blocks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**List[User]**](User.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UserList |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_unblock_user**
> organization_unblock_user(org, username)

Unblock a user

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    username = 'username_example' # str | user to unblock

    try:
        # Unblock a user
        api_instance.organization_unblock_user(org, username)
    except Exception as e:
        print("Exception when calling OrganizationApi->organization_unblock_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **username** | **str**| user to unblock | 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | APIEmpty is an empty response |  -  |
**404** | APINotFound is a not found empty response |  -  |
**422** | APIValidationError is error format response related to input validation |  * message -  <br>  * url -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **team_search**
> TeamSearch200Response team_search(org, q=q, include_desc=include_desc, page=page, limit=limit)

Search for teams within an organization

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.team_search200_response import TeamSearch200Response
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    q = 'q_example' # str | keywords to search (optional)
    include_desc = True # bool | include search within team description (defaults to true) (optional)
    page = 56 # int | page number of results to return (1-based) (optional)
    limit = 56 # int | page size of results (optional)

    try:
        # Search for teams within an organization
        api_response = api_instance.team_search(org, q=q, include_desc=include_desc, page=page, limit=limit)
        print("The response of OrganizationApi->team_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->team_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **q** | **str**| keywords to search | [optional] 
 **include_desc** | **bool**| include search within team description (defaults to true) | [optional] 
 **page** | **int**| page number of results to return (1-based) | [optional] 
 **limit** | **int**| page size of results | [optional] 

### Return type

[**TeamSearch200Response**](TeamSearch200Response.md)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SearchResults of a successful search |  -  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_org_secret**
> update_org_secret(org, secretname, body=body)

Create or Update a secret value in an organization

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.create_or_update_secret_option import CreateOrUpdateSecretOption
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of organization
    secretname = 'secretname_example' # str | name of the secret
    body = gitea_openapi.CreateOrUpdateSecretOption() # CreateOrUpdateSecretOption |  (optional)

    try:
        # Create or Update a secret value in an organization
        api_instance.update_org_secret(org, secretname, body=body)
    except Exception as e:
        print("Exception when calling OrganizationApi->update_org_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of organization | 
 **secretname** | **str**| name of the secret | 
 **body** | [**CreateOrUpdateSecretOption**](CreateOrUpdateSecretOption.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | response when creating a secret |  -  |
**204** | response when updating a secret |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_org_variable**
> update_org_variable(org, variablename, body=body)

Update an org-level variable

### Example

* Api Key Authentication (TOTPHeader):
* Api Key Authentication (AuthorizationHeaderToken):
* Api Key Authentication (SudoHeader):
* Basic Authentication (BasicAuth):
* Api Key Authentication (AccessToken):
* Api Key Authentication (SudoParam):
* Api Key Authentication (Token):

```python
import gitea_openapi
from gitea_openapi.models.update_variable_option import UpdateVariableOption
from gitea_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gitea_openapi.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: TOTPHeader
configuration.api_key['TOTPHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['TOTPHeader'] = 'Bearer'

# Configure API key authorization: AuthorizationHeaderToken
configuration.api_key['AuthorizationHeaderToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AuthorizationHeaderToken'] = 'Bearer'

# Configure API key authorization: SudoHeader
configuration.api_key['SudoHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoHeader'] = 'Bearer'

# Configure HTTP basic authorization: BasicAuth
configuration = gitea_openapi.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: AccessToken
configuration.api_key['AccessToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['AccessToken'] = 'Bearer'

# Configure API key authorization: SudoParam
configuration.api_key['SudoParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SudoParam'] = 'Bearer'

# Configure API key authorization: Token
configuration.api_key['Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with gitea_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gitea_openapi.OrganizationApi(api_client)
    org = 'org_example' # str | name of the organization
    variablename = 'variablename_example' # str | name of the variable
    body = gitea_openapi.UpdateVariableOption() # UpdateVariableOption |  (optional)

    try:
        # Update an org-level variable
        api_instance.update_org_variable(org, variablename, body=body)
    except Exception as e:
        print("Exception when calling OrganizationApi->update_org_variable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| name of the organization | 
 **variablename** | **str**| name of the variable | 
 **body** | [**UpdateVariableOption**](UpdateVariableOption.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[TOTPHeader](../README.md#TOTPHeader), [AuthorizationHeaderToken](../README.md#AuthorizationHeaderToken), [SudoHeader](../README.md#SudoHeader), [BasicAuth](../README.md#BasicAuth), [AccessToken](../README.md#AccessToken), [SudoParam](../README.md#SudoParam), [Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | response when updating an org-level variable |  -  |
**204** | response when updating an org-level variable |  -  |
**400** | APIError is error format response |  * message -  <br>  * url -  <br>  |
**404** | APINotFound is a not found empty response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

