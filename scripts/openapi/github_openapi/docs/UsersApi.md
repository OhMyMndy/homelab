# github_openapi.UsersApi

All URIs are relative to *https://api.github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_add_email_for_authenticated_user**](UsersApi.md#users_add_email_for_authenticated_user) | **POST** /user/emails | Add an email address for the authenticated user
[**users_add_social_account_for_authenticated_user**](UsersApi.md#users_add_social_account_for_authenticated_user) | **POST** /user/social_accounts | Add social accounts for the authenticated user
[**users_block**](UsersApi.md#users_block) | **PUT** /user/blocks/{username} | Block a user
[**users_check_blocked**](UsersApi.md#users_check_blocked) | **GET** /user/blocks/{username} | Check if a user is blocked by the authenticated user
[**users_check_following_for_user**](UsersApi.md#users_check_following_for_user) | **GET** /users/{username}/following/{target_user} | Check if a user follows another user
[**users_check_person_is_followed_by_authenticated**](UsersApi.md#users_check_person_is_followed_by_authenticated) | **GET** /user/following/{username} | Check if a person is followed by the authenticated user
[**users_create_gpg_key_for_authenticated_user**](UsersApi.md#users_create_gpg_key_for_authenticated_user) | **POST** /user/gpg_keys | Create a GPG key for the authenticated user
[**users_create_public_ssh_key_for_authenticated_user**](UsersApi.md#users_create_public_ssh_key_for_authenticated_user) | **POST** /user/keys | Create a public SSH key for the authenticated user
[**users_create_ssh_signing_key_for_authenticated_user**](UsersApi.md#users_create_ssh_signing_key_for_authenticated_user) | **POST** /user/ssh_signing_keys | Create a SSH signing key for the authenticated user
[**users_delete_email_for_authenticated_user**](UsersApi.md#users_delete_email_for_authenticated_user) | **DELETE** /user/emails | Delete an email address for the authenticated user
[**users_delete_gpg_key_for_authenticated_user**](UsersApi.md#users_delete_gpg_key_for_authenticated_user) | **DELETE** /user/gpg_keys/{gpg_key_id} | Delete a GPG key for the authenticated user
[**users_delete_public_ssh_key_for_authenticated_user**](UsersApi.md#users_delete_public_ssh_key_for_authenticated_user) | **DELETE** /user/keys/{key_id} | Delete a public SSH key for the authenticated user
[**users_delete_social_account_for_authenticated_user**](UsersApi.md#users_delete_social_account_for_authenticated_user) | **DELETE** /user/social_accounts | Delete social accounts for the authenticated user
[**users_delete_ssh_signing_key_for_authenticated_user**](UsersApi.md#users_delete_ssh_signing_key_for_authenticated_user) | **DELETE** /user/ssh_signing_keys/{ssh_signing_key_id} | Delete an SSH signing key for the authenticated user
[**users_follow**](UsersApi.md#users_follow) | **PUT** /user/following/{username} | Follow a user
[**users_get_authenticated**](UsersApi.md#users_get_authenticated) | **GET** /user | Get the authenticated user
[**users_get_by_id**](UsersApi.md#users_get_by_id) | **GET** /user/{account_id} | Get a user using their ID
[**users_get_by_username**](UsersApi.md#users_get_by_username) | **GET** /users/{username} | Get a user
[**users_get_context_for_user**](UsersApi.md#users_get_context_for_user) | **GET** /users/{username}/hovercard | Get contextual information for a user
[**users_get_gpg_key_for_authenticated_user**](UsersApi.md#users_get_gpg_key_for_authenticated_user) | **GET** /user/gpg_keys/{gpg_key_id} | Get a GPG key for the authenticated user
[**users_get_public_ssh_key_for_authenticated_user**](UsersApi.md#users_get_public_ssh_key_for_authenticated_user) | **GET** /user/keys/{key_id} | Get a public SSH key for the authenticated user
[**users_get_ssh_signing_key_for_authenticated_user**](UsersApi.md#users_get_ssh_signing_key_for_authenticated_user) | **GET** /user/ssh_signing_keys/{ssh_signing_key_id} | Get an SSH signing key for the authenticated user
[**users_list**](UsersApi.md#users_list) | **GET** /users | List users
[**users_list_attestations**](UsersApi.md#users_list_attestations) | **GET** /users/{username}/attestations/{subject_digest} | List attestations
[**users_list_blocked_by_authenticated_user**](UsersApi.md#users_list_blocked_by_authenticated_user) | **GET** /user/blocks | List users blocked by the authenticated user
[**users_list_emails_for_authenticated_user**](UsersApi.md#users_list_emails_for_authenticated_user) | **GET** /user/emails | List email addresses for the authenticated user
[**users_list_followed_by_authenticated_user**](UsersApi.md#users_list_followed_by_authenticated_user) | **GET** /user/following | List the people the authenticated user follows
[**users_list_followers_for_authenticated_user**](UsersApi.md#users_list_followers_for_authenticated_user) | **GET** /user/followers | List followers of the authenticated user
[**users_list_followers_for_user**](UsersApi.md#users_list_followers_for_user) | **GET** /users/{username}/followers | List followers of a user
[**users_list_following_for_user**](UsersApi.md#users_list_following_for_user) | **GET** /users/{username}/following | List the people a user follows
[**users_list_gpg_keys_for_authenticated_user**](UsersApi.md#users_list_gpg_keys_for_authenticated_user) | **GET** /user/gpg_keys | List GPG keys for the authenticated user
[**users_list_gpg_keys_for_user**](UsersApi.md#users_list_gpg_keys_for_user) | **GET** /users/{username}/gpg_keys | List GPG keys for a user
[**users_list_public_emails_for_authenticated_user**](UsersApi.md#users_list_public_emails_for_authenticated_user) | **GET** /user/public_emails | List public email addresses for the authenticated user
[**users_list_public_keys_for_user**](UsersApi.md#users_list_public_keys_for_user) | **GET** /users/{username}/keys | List public keys for a user
[**users_list_public_ssh_keys_for_authenticated_user**](UsersApi.md#users_list_public_ssh_keys_for_authenticated_user) | **GET** /user/keys | List public SSH keys for the authenticated user
[**users_list_social_accounts_for_authenticated_user**](UsersApi.md#users_list_social_accounts_for_authenticated_user) | **GET** /user/social_accounts | List social accounts for the authenticated user
[**users_list_social_accounts_for_user**](UsersApi.md#users_list_social_accounts_for_user) | **GET** /users/{username}/social_accounts | List social accounts for a user
[**users_list_ssh_signing_keys_for_authenticated_user**](UsersApi.md#users_list_ssh_signing_keys_for_authenticated_user) | **GET** /user/ssh_signing_keys | List SSH signing keys for the authenticated user
[**users_list_ssh_signing_keys_for_user**](UsersApi.md#users_list_ssh_signing_keys_for_user) | **GET** /users/{username}/ssh_signing_keys | List SSH signing keys for a user
[**users_set_primary_email_visibility_for_authenticated_user**](UsersApi.md#users_set_primary_email_visibility_for_authenticated_user) | **PATCH** /user/email/visibility | Set primary email visibility for the authenticated user
[**users_unblock**](UsersApi.md#users_unblock) | **DELETE** /user/blocks/{username} | Unblock a user
[**users_unfollow**](UsersApi.md#users_unfollow) | **DELETE** /user/following/{username} | Unfollow a user
[**users_update_authenticated**](UsersApi.md#users_update_authenticated) | **PATCH** /user | Update the authenticated user


# **users_add_email_for_authenticated_user**
> List[Email] users_add_email_for_authenticated_user(users_add_email_for_authenticated_user_request=users_add_email_for_authenticated_user_request)

Add an email address for the authenticated user

OAuth app tokens and personal access tokens (classic) need the `user` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.email import Email
from github_openapi.models.users_add_email_for_authenticated_user_request import UsersAddEmailForAuthenticatedUserRequest
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
    api_instance = github_openapi.UsersApi(api_client)
    users_add_email_for_authenticated_user_request = {"emails":["octocat@github.com","mona@github.com","octocat@octocat.org"]} # UsersAddEmailForAuthenticatedUserRequest |  (optional)

    try:
        # Add an email address for the authenticated user
        api_response = api_instance.users_add_email_for_authenticated_user(users_add_email_for_authenticated_user_request=users_add_email_for_authenticated_user_request)
        print("The response of UsersApi->users_add_email_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_add_email_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_add_email_for_authenticated_user_request** | [**UsersAddEmailForAuthenticatedUserRequest**](UsersAddEmailForAuthenticatedUserRequest.md)|  | [optional] 

### Return type

[**List[Email]**](Email.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**304** | Not modified |  -  |
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_add_social_account_for_authenticated_user**
> List[SocialAccount] users_add_social_account_for_authenticated_user(users_add_social_account_for_authenticated_user_request)

Add social accounts for the authenticated user

Add one or more social accounts to the authenticated user's profile.  OAuth app tokens and personal access tokens (classic) need the `user` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.social_account import SocialAccount
from github_openapi.models.users_add_social_account_for_authenticated_user_request import UsersAddSocialAccountForAuthenticatedUserRequest
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
    api_instance = github_openapi.UsersApi(api_client)
    users_add_social_account_for_authenticated_user_request = {"account_urls":["https://facebook.com/GitHub","https://www.youtube.com/@GitHub"]} # UsersAddSocialAccountForAuthenticatedUserRequest | 

    try:
        # Add social accounts for the authenticated user
        api_response = api_instance.users_add_social_account_for_authenticated_user(users_add_social_account_for_authenticated_user_request)
        print("The response of UsersApi->users_add_social_account_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_add_social_account_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_add_social_account_for_authenticated_user_request** | [**UsersAddSocialAccountForAuthenticatedUserRequest**](UsersAddSocialAccountForAuthenticatedUserRequest.md)|  | 

### Return type

[**List[SocialAccount]**](SocialAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**304** | Not modified |  -  |
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_block**
> users_block(username)

Block a user

Blocks the given user and returns a 204. If the authenticated user cannot block the given user a 422 is returned.

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
    api_instance = github_openapi.UsersApi(api_client)
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Block a user
        api_instance.users_block(username)
    except Exception as e:
        print("Exception when calling UsersApi->users_block: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**401** | Requires authentication |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_check_blocked**
> users_check_blocked(username)

Check if a user is blocked by the authenticated user

Returns a 204 if the given user is blocked by the authenticated user. Returns a 404 if the given user is not blocked by the authenticated user, or if the given user account has been identified as spam by GitHub.

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
    api_instance = github_openapi.UsersApi(api_client)
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Check if a user is blocked by the authenticated user
        api_instance.users_check_blocked(username)
    except Exception as e:
        print("Exception when calling UsersApi->users_check_blocked: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**204** | If the user is blocked |  -  |
**404** | If the user is not blocked |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_check_following_for_user**
> users_check_following_for_user(username, target_user)

Check if a user follows another user



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
    api_instance = github_openapi.UsersApi(api_client)
    username = 'username_example' # str | The handle for the GitHub user account.
    target_user = 'target_user_example' # str | 

    try:
        # Check if a user follows another user
        api_instance.users_check_following_for_user(username, target_user)
    except Exception as e:
        print("Exception when calling UsersApi->users_check_following_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The handle for the GitHub user account. | 
 **target_user** | **str**|  | 

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
**204** | if the user follows the target user |  -  |
**404** | if the user does not follow the target user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_check_person_is_followed_by_authenticated**
> users_check_person_is_followed_by_authenticated(username)

Check if a person is followed by the authenticated user



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
    api_instance = github_openapi.UsersApi(api_client)
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Check if a person is followed by the authenticated user
        api_instance.users_check_person_is_followed_by_authenticated(username)
    except Exception as e:
        print("Exception when calling UsersApi->users_check_person_is_followed_by_authenticated: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**204** | if the person is followed by the authenticated user |  -  |
**404** | if the person is not followed by the authenticated user |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_create_gpg_key_for_authenticated_user**
> GpgKey users_create_gpg_key_for_authenticated_user(users_create_gpg_key_for_authenticated_user_request)

Create a GPG key for the authenticated user

Adds a GPG key to the authenticated user's GitHub account.  OAuth app tokens and personal access tokens (classic) need the `write:gpg_key` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.gpg_key import GpgKey
from github_openapi.models.users_create_gpg_key_for_authenticated_user_request import UsersCreateGpgKeyForAuthenticatedUserRequest
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
    api_instance = github_openapi.UsersApi(api_client)
    users_create_gpg_key_for_authenticated_user_request = {"name":"Octocat's GPG Key","armored_public_key":"-----BEGIN PGP PUBLIC KEY BLOCK-----\nVersion: GnuPG v1\n\nmQINBFnZ2ZIBEADQ2Z7Z7\n-----END PGP PUBLIC KEY BLOCK-----"} # UsersCreateGpgKeyForAuthenticatedUserRequest | 

    try:
        # Create a GPG key for the authenticated user
        api_response = api_instance.users_create_gpg_key_for_authenticated_user(users_create_gpg_key_for_authenticated_user_request)
        print("The response of UsersApi->users_create_gpg_key_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_create_gpg_key_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_create_gpg_key_for_authenticated_user_request** | [**UsersCreateGpgKeyForAuthenticatedUserRequest**](UsersCreateGpgKeyForAuthenticatedUserRequest.md)|  | 

### Return type

[**GpgKey**](GpgKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**304** | Not modified |  -  |
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_create_public_ssh_key_for_authenticated_user**
> Key users_create_public_ssh_key_for_authenticated_user(users_create_public_ssh_key_for_authenticated_user_request)

Create a public SSH key for the authenticated user

Adds a public SSH key to the authenticated user's GitHub account.  OAuth app tokens and personal access tokens (classic) need the `write:gpg_key` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.key import Key
from github_openapi.models.users_create_public_ssh_key_for_authenticated_user_request import UsersCreatePublicSshKeyForAuthenticatedUserRequest
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
    api_instance = github_openapi.UsersApi(api_client)
    users_create_public_ssh_key_for_authenticated_user_request = {"title":"ssh-rsa AAAAB3NzaC1yc2EAAA","key":"2Sg8iYjAxxmI2LvUXpJjkYrMxURPc8r+dB7TJyvv1234"} # UsersCreatePublicSshKeyForAuthenticatedUserRequest | 

    try:
        # Create a public SSH key for the authenticated user
        api_response = api_instance.users_create_public_ssh_key_for_authenticated_user(users_create_public_ssh_key_for_authenticated_user_request)
        print("The response of UsersApi->users_create_public_ssh_key_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_create_public_ssh_key_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_create_public_ssh_key_for_authenticated_user_request** | [**UsersCreatePublicSshKeyForAuthenticatedUserRequest**](UsersCreatePublicSshKeyForAuthenticatedUserRequest.md)|  | 

### Return type

[**Key**](Key.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**304** | Not modified |  -  |
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_create_ssh_signing_key_for_authenticated_user**
> SshSigningKey users_create_ssh_signing_key_for_authenticated_user(users_create_ssh_signing_key_for_authenticated_user_request)

Create a SSH signing key for the authenticated user

Creates an SSH signing key for the authenticated user's GitHub account.  OAuth app tokens and personal access tokens (classic) need the `write:ssh_signing_key` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.ssh_signing_key import SshSigningKey
from github_openapi.models.users_create_ssh_signing_key_for_authenticated_user_request import UsersCreateSshSigningKeyForAuthenticatedUserRequest
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
    api_instance = github_openapi.UsersApi(api_client)
    users_create_ssh_signing_key_for_authenticated_user_request = {"key":"2Sg8iYjAxxmI2LvUXpJjkYrMxURPc8r+dB7TJyvv1234","title":"ssh-rsa AAAAB3NzaC1yc2EAAA"} # UsersCreateSshSigningKeyForAuthenticatedUserRequest | 

    try:
        # Create a SSH signing key for the authenticated user
        api_response = api_instance.users_create_ssh_signing_key_for_authenticated_user(users_create_ssh_signing_key_for_authenticated_user_request)
        print("The response of UsersApi->users_create_ssh_signing_key_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_create_ssh_signing_key_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_create_ssh_signing_key_for_authenticated_user_request** | [**UsersCreateSshSigningKeyForAuthenticatedUserRequest**](UsersCreateSshSigningKeyForAuthenticatedUserRequest.md)|  | 

### Return type

[**SshSigningKey**](SshSigningKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**304** | Not modified |  -  |
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_delete_email_for_authenticated_user**
> users_delete_email_for_authenticated_user(users_delete_email_for_authenticated_user_request=users_delete_email_for_authenticated_user_request)

Delete an email address for the authenticated user

OAuth app tokens and personal access tokens (classic) need the `user` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.users_delete_email_for_authenticated_user_request import UsersDeleteEmailForAuthenticatedUserRequest
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
    api_instance = github_openapi.UsersApi(api_client)
    users_delete_email_for_authenticated_user_request = {"emails":["octocat@github.com","mona@github.com"]} # UsersDeleteEmailForAuthenticatedUserRequest |  (optional)

    try:
        # Delete an email address for the authenticated user
        api_instance.users_delete_email_for_authenticated_user(users_delete_email_for_authenticated_user_request=users_delete_email_for_authenticated_user_request)
    except Exception as e:
        print("Exception when calling UsersApi->users_delete_email_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_delete_email_for_authenticated_user_request** | [**UsersDeleteEmailForAuthenticatedUserRequest**](UsersDeleteEmailForAuthenticatedUserRequest.md)|  | [optional] 

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
**304** | Not modified |  -  |
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_delete_gpg_key_for_authenticated_user**
> users_delete_gpg_key_for_authenticated_user(gpg_key_id)

Delete a GPG key for the authenticated user

Removes a GPG key from the authenticated user's GitHub account.  OAuth app tokens and personal access tokens (classic) need the `admin:gpg_key` scope to use this endpoint.

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
    api_instance = github_openapi.UsersApi(api_client)
    gpg_key_id = 56 # int | The unique identifier of the GPG key.

    try:
        # Delete a GPG key for the authenticated user
        api_instance.users_delete_gpg_key_for_authenticated_user(gpg_key_id)
    except Exception as e:
        print("Exception when calling UsersApi->users_delete_gpg_key_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gpg_key_id** | **int**| The unique identifier of the GPG key. | 

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
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_delete_public_ssh_key_for_authenticated_user**
> users_delete_public_ssh_key_for_authenticated_user(key_id)

Delete a public SSH key for the authenticated user

Removes a public SSH key from the authenticated user's GitHub account.  OAuth app tokens and personal access tokens (classic) need the `admin:public_key` scope to use this endpoint.

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
    api_instance = github_openapi.UsersApi(api_client)
    key_id = 56 # int | The unique identifier of the key.

    try:
        # Delete a public SSH key for the authenticated user
        api_instance.users_delete_public_ssh_key_for_authenticated_user(key_id)
    except Exception as e:
        print("Exception when calling UsersApi->users_delete_public_ssh_key_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **int**| The unique identifier of the key. | 

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
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_delete_social_account_for_authenticated_user**
> users_delete_social_account_for_authenticated_user(users_delete_social_account_for_authenticated_user_request)

Delete social accounts for the authenticated user

Deletes one or more social accounts from the authenticated user's profile.  OAuth app tokens and personal access tokens (classic) need the `user` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.users_delete_social_account_for_authenticated_user_request import UsersDeleteSocialAccountForAuthenticatedUserRequest
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
    api_instance = github_openapi.UsersApi(api_client)
    users_delete_social_account_for_authenticated_user_request = {"account_urls":["https://facebook.com/GitHub","https://www.youtube.com/@GitHub"]} # UsersDeleteSocialAccountForAuthenticatedUserRequest | 

    try:
        # Delete social accounts for the authenticated user
        api_instance.users_delete_social_account_for_authenticated_user(users_delete_social_account_for_authenticated_user_request)
    except Exception as e:
        print("Exception when calling UsersApi->users_delete_social_account_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_delete_social_account_for_authenticated_user_request** | [**UsersDeleteSocialAccountForAuthenticatedUserRequest**](UsersDeleteSocialAccountForAuthenticatedUserRequest.md)|  | 

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
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**304** | Not modified |  -  |
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_delete_ssh_signing_key_for_authenticated_user**
> users_delete_ssh_signing_key_for_authenticated_user(ssh_signing_key_id)

Delete an SSH signing key for the authenticated user

Deletes an SSH signing key from the authenticated user's GitHub account.  OAuth app tokens and personal access tokens (classic) need the `admin:ssh_signing_key` scope to use this endpoint.

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
    api_instance = github_openapi.UsersApi(api_client)
    ssh_signing_key_id = 56 # int | The unique identifier of the SSH signing key.

    try:
        # Delete an SSH signing key for the authenticated user
        api_instance.users_delete_ssh_signing_key_for_authenticated_user(ssh_signing_key_id)
    except Exception as e:
        print("Exception when calling UsersApi->users_delete_ssh_signing_key_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_signing_key_id** | **int**| The unique identifier of the SSH signing key. | 

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
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_follow**
> users_follow(username)

Follow a user

Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see \"[HTTP verbs](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#http-method).\"  OAuth app tokens and personal access tokens (classic) need the `user:follow` scope to use this endpoint.

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
    api_instance = github_openapi.UsersApi(api_client)
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Follow a user
        api_instance.users_follow(username)
    except Exception as e:
        print("Exception when calling UsersApi->users_follow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**401** | Requires authentication |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_authenticated**
> UsersGetAuthenticated200Response users_get_authenticated()

Get the authenticated user

OAuth app tokens and personal access tokens (classic) need the `user` scope in order for the response to include private profile information.

### Example


```python
import github_openapi
from github_openapi.models.users_get_authenticated200_response import UsersGetAuthenticated200Response
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
    api_instance = github_openapi.UsersApi(api_client)

    try:
        # Get the authenticated user
        api_response = api_instance.users_get_authenticated()
        print("The response of UsersApi->users_get_authenticated:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_get_authenticated: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UsersGetAuthenticated200Response**](UsersGetAuthenticated200Response.md)

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

# **users_get_by_id**
> UsersGetAuthenticated200Response users_get_by_id(account_id)

Get a user using their ID

Provides publicly available information about someone with a GitHub account. This method takes their durable user `ID` instead of their `login`, which can change over time.  The `email` key in the following response is the publicly visible email address from your GitHub [profile page](https://github.com/settings/profile). When setting up your profile, you can select a primary email address to be “public” which provides an email entry for this endpoint. If you do not set a public email address for `email`, then it will have a value of `null`. You only see publicly visible email addresses when authenticated with GitHub. For more information, see [Authentication](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#authentication).  The Emails API enables you to list all of your email addresses, and toggle a primary email to be visible publicly. For more information, see \"[Emails API](https://docs.github.com/rest/users/emails)\".

### Example


```python
import github_openapi
from github_openapi.models.users_get_authenticated200_response import UsersGetAuthenticated200Response
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
    api_instance = github_openapi.UsersApi(api_client)
    account_id = 56 # int | account_id parameter

    try:
        # Get a user using their ID
        api_response = api_instance.users_get_by_id(account_id)
        print("The response of UsersApi->users_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **int**| account_id parameter | 

### Return type

[**UsersGetAuthenticated200Response**](UsersGetAuthenticated200Response.md)

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

# **users_get_by_username**
> UsersGetAuthenticated200Response users_get_by_username(username)

Get a user

Provides publicly available information about someone with a GitHub account.  The `email` key in the following response is the publicly visible email address from your GitHub [profile page](https://github.com/settings/profile). When setting up your profile, you can select a primary email address to be “public” which provides an email entry for this endpoint. If you do not set a public email address for `email`, then it will have a value of `null`. You only see publicly visible email addresses when authenticated with GitHub. For more information, see [Authentication](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#authentication).  The Emails API enables you to list all of your email addresses, and toggle a primary email to be visible publicly. For more information, see \"[Emails API](https://docs.github.com/rest/users/emails)\".

### Example


```python
import github_openapi
from github_openapi.models.users_get_authenticated200_response import UsersGetAuthenticated200Response
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
    api_instance = github_openapi.UsersApi(api_client)
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Get a user
        api_response = api_instance.users_get_by_username(username)
        print("The response of UsersApi->users_get_by_username:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_get_by_username: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The handle for the GitHub user account. | 

### Return type

[**UsersGetAuthenticated200Response**](UsersGetAuthenticated200Response.md)

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

# **users_get_context_for_user**
> Hovercard users_get_context_for_user(username, subject_type=subject_type, subject_id=subject_id)

Get contextual information for a user

Provides hovercard information. You can find out more about someone in relation to their pull requests, issues, repositories, and organizations.    The `subject_type` and `subject_id` parameters provide context for the person's hovercard, which returns more information than without the parameters. For example, if you wanted to find out more about `octocat` who owns the `Spoon-Knife` repository, you would use a `subject_type` value of `repository` and a `subject_id` value of `1300192` (the ID of the `Spoon-Knife` repository).  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.hovercard import Hovercard
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
    api_instance = github_openapi.UsersApi(api_client)
    username = 'username_example' # str | The handle for the GitHub user account.
    subject_type = 'subject_type_example' # str | Identifies which additional information you'd like to receive about the person's hovercard. Can be `organization`, `repository`, `issue`, `pull_request`. **Required** when using `subject_id`. (optional)
    subject_id = 'subject_id_example' # str | Uses the ID for the `subject_type` you specified. **Required** when using `subject_type`. (optional)

    try:
        # Get contextual information for a user
        api_response = api_instance.users_get_context_for_user(username, subject_type=subject_type, subject_id=subject_id)
        print("The response of UsersApi->users_get_context_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_get_context_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The handle for the GitHub user account. | 
 **subject_type** | **str**| Identifies which additional information you&#39;d like to receive about the person&#39;s hovercard. Can be &#x60;organization&#x60;, &#x60;repository&#x60;, &#x60;issue&#x60;, &#x60;pull_request&#x60;. **Required** when using &#x60;subject_id&#x60;. | [optional] 
 **subject_id** | **str**| Uses the ID for the &#x60;subject_type&#x60; you specified. **Required** when using &#x60;subject_type&#x60;. | [optional] 

### Return type

[**Hovercard**](Hovercard.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_gpg_key_for_authenticated_user**
> GpgKey users_get_gpg_key_for_authenticated_user(gpg_key_id)

Get a GPG key for the authenticated user

View extended details for a single GPG key.  OAuth app tokens and personal access tokens (classic) need the `read:gpg_key` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.gpg_key import GpgKey
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
    api_instance = github_openapi.UsersApi(api_client)
    gpg_key_id = 56 # int | The unique identifier of the GPG key.

    try:
        # Get a GPG key for the authenticated user
        api_response = api_instance.users_get_gpg_key_for_authenticated_user(gpg_key_id)
        print("The response of UsersApi->users_get_gpg_key_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_get_gpg_key_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gpg_key_id** | **int**| The unique identifier of the GPG key. | 

### Return type

[**GpgKey**](GpgKey.md)

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
**304** | Not modified |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_public_ssh_key_for_authenticated_user**
> Key users_get_public_ssh_key_for_authenticated_user(key_id)

Get a public SSH key for the authenticated user

View extended details for a single public SSH key.  OAuth app tokens and personal access tokens (classic) need the `read:public_key` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.key import Key
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
    api_instance = github_openapi.UsersApi(api_client)
    key_id = 56 # int | The unique identifier of the key.

    try:
        # Get a public SSH key for the authenticated user
        api_response = api_instance.users_get_public_ssh_key_for_authenticated_user(key_id)
        print("The response of UsersApi->users_get_public_ssh_key_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_get_public_ssh_key_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **int**| The unique identifier of the key. | 

### Return type

[**Key**](Key.md)

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
**304** | Not modified |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_ssh_signing_key_for_authenticated_user**
> SshSigningKey users_get_ssh_signing_key_for_authenticated_user(ssh_signing_key_id)

Get an SSH signing key for the authenticated user

Gets extended details for an SSH signing key.  OAuth app tokens and personal access tokens (classic) need the `read:ssh_signing_key` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.ssh_signing_key import SshSigningKey
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
    api_instance = github_openapi.UsersApi(api_client)
    ssh_signing_key_id = 56 # int | The unique identifier of the SSH signing key.

    try:
        # Get an SSH signing key for the authenticated user
        api_response = api_instance.users_get_ssh_signing_key_for_authenticated_user(ssh_signing_key_id)
        print("The response of UsersApi->users_get_ssh_signing_key_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_get_ssh_signing_key_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_signing_key_id** | **int**| The unique identifier of the SSH signing key. | 

### Return type

[**SshSigningKey**](SshSigningKey.md)

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
**304** | Not modified |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_list**
> List[SimpleUser] users_list(since=since, per_page=per_page)

List users

Lists all users, in the order that they signed up on GitHub. This list includes personal user accounts and organization accounts.  Note: Pagination is powered exclusively by the `since` parameter. Use the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers) to get the URL for the next page of users.

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
    api_instance = github_openapi.UsersApi(api_client)
    since = 56 # int | A user ID. Only return users with an ID greater than this ID. (optional)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)

    try:
        # List users
        api_response = api_instance.users_list(since=since, per_page=per_page)
        print("The response of UsersApi->users_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **int**| A user ID. Only return users with an ID greater than this ID. | [optional] 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]

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
**304** | Not modified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_list_attestations**
> UsersListAttestations200Response users_list_attestations(username, subject_digest, per_page=per_page, before=before, after=after)

List attestations

List a collection of artifact attestations with a given subject digest that are associated with repositories owned by a user.  The collection of attestations returned by this endpoint is filtered according to the authenticated user's permissions; if the authenticated user cannot read a repository, the attestations associated with that repository will not be included in the response. In addition, when using a fine-grained access token the `attestations:read` permission is required.  **Please note:** in order to offer meaningful security benefits, an attestation's signature and timestamps **must** be cryptographically verified, and the identity of the attestation signer **must** be validated. Attestations can be verified using the [GitHub CLI `attestation verify` command](https://cli.github.com/manual/gh_attestation_verify). For more information, see [our guide on how to use artifact attestations to establish a build's provenance](https://docs.github.com/actions/security-guides/using-artifact-attestations-to-establish-provenance-for-builds).

### Example


```python
import github_openapi
from github_openapi.models.users_list_attestations200_response import UsersListAttestations200Response
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
    api_instance = github_openapi.UsersApi(api_client)
    username = 'username_example' # str | The handle for the GitHub user account.
    subject_digest = 'subject_digest_example' # str | Subject Digest
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    before = 'before_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)
    after = 'after_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)

    try:
        # List attestations
        api_response = api_instance.users_list_attestations(username, subject_digest, per_page=per_page, before=before, after=after)
        print("The response of UsersApi->users_list_attestations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_list_attestations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The handle for the GitHub user account. | 
 **subject_digest** | **str**| Subject Digest | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **before** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 
 **after** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 

### Return type

[**UsersListAttestations200Response**](UsersListAttestations200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**201** | Response |  -  |
**204** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_list_blocked_by_authenticated_user**
> List[SimpleUser] users_list_blocked_by_authenticated_user(per_page=per_page, page=page)

List users blocked by the authenticated user

List the users you've blocked on your personal account.

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
    api_instance = github_openapi.UsersApi(api_client)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List users blocked by the authenticated user
        api_response = api_instance.users_list_blocked_by_authenticated_user(per_page=per_page, page=page)
        print("The response of UsersApi->users_list_blocked_by_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_list_blocked_by_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | Response |  -  |
**304** | Not modified |  -  |
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_list_emails_for_authenticated_user**
> List[Email] users_list_emails_for_authenticated_user(per_page=per_page, page=page)

List email addresses for the authenticated user

Lists all of your email addresses, and specifies which one is visible to the public.  OAuth app tokens and personal access tokens (classic) need the `user:email` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.email import Email
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
    api_instance = github_openapi.UsersApi(api_client)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List email addresses for the authenticated user
        api_response = api_instance.users_list_emails_for_authenticated_user(per_page=per_page, page=page)
        print("The response of UsersApi->users_list_emails_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_list_emails_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Email]**](Email.md)

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
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_list_followed_by_authenticated_user**
> List[SimpleUser] users_list_followed_by_authenticated_user(per_page=per_page, page=page)

List the people the authenticated user follows

Lists the people who the authenticated user follows.

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
    api_instance = github_openapi.UsersApi(api_client)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List the people the authenticated user follows
        api_response = api_instance.users_list_followed_by_authenticated_user(per_page=per_page, page=page)
        print("The response of UsersApi->users_list_followed_by_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_list_followed_by_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**304** | Not modified |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_list_followers_for_authenticated_user**
> List[SimpleUser] users_list_followers_for_authenticated_user(per_page=per_page, page=page)

List followers of the authenticated user

Lists the people following the authenticated user.

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
    api_instance = github_openapi.UsersApi(api_client)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List followers of the authenticated user
        api_response = api_instance.users_list_followers_for_authenticated_user(per_page=per_page, page=page)
        print("The response of UsersApi->users_list_followers_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_list_followers_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**304** | Not modified |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_list_followers_for_user**
> List[SimpleUser] users_list_followers_for_user(username, per_page=per_page, page=page)

List followers of a user

Lists the people following the specified user.

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
    api_instance = github_openapi.UsersApi(api_client)
    username = 'username_example' # str | The handle for the GitHub user account.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List followers of a user
        api_response = api_instance.users_list_followers_for_user(username, per_page=per_page, page=page)
        print("The response of UsersApi->users_list_followers_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_list_followers_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The handle for the GitHub user account. | 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_list_following_for_user**
> List[SimpleUser] users_list_following_for_user(username, per_page=per_page, page=page)

List the people a user follows

Lists the people who the specified user follows.

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
    api_instance = github_openapi.UsersApi(api_client)
    username = 'username_example' # str | The handle for the GitHub user account.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List the people a user follows
        api_response = api_instance.users_list_following_for_user(username, per_page=per_page, page=page)
        print("The response of UsersApi->users_list_following_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_list_following_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The handle for the GitHub user account. | 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_list_gpg_keys_for_authenticated_user**
> List[GpgKey] users_list_gpg_keys_for_authenticated_user(per_page=per_page, page=page)

List GPG keys for the authenticated user

Lists the current user's GPG keys.  OAuth app tokens and personal access tokens (classic) need the `read:gpg_key` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.gpg_key import GpgKey
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
    api_instance = github_openapi.UsersApi(api_client)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List GPG keys for the authenticated user
        api_response = api_instance.users_list_gpg_keys_for_authenticated_user(per_page=per_page, page=page)
        print("The response of UsersApi->users_list_gpg_keys_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_list_gpg_keys_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[GpgKey]**](GpgKey.md)

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
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_list_gpg_keys_for_user**
> List[GpgKey] users_list_gpg_keys_for_user(username, per_page=per_page, page=page)

List GPG keys for a user

Lists the GPG keys for a user. This information is accessible by anyone.

### Example


```python
import github_openapi
from github_openapi.models.gpg_key import GpgKey
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
    api_instance = github_openapi.UsersApi(api_client)
    username = 'username_example' # str | The handle for the GitHub user account.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List GPG keys for a user
        api_response = api_instance.users_list_gpg_keys_for_user(username, per_page=per_page, page=page)
        print("The response of UsersApi->users_list_gpg_keys_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_list_gpg_keys_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The handle for the GitHub user account. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[GpgKey]**](GpgKey.md)

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

# **users_list_public_emails_for_authenticated_user**
> List[Email] users_list_public_emails_for_authenticated_user(per_page=per_page, page=page)

List public email addresses for the authenticated user

Lists your publicly visible email address, which you can set with the [Set primary email visibility for the authenticated user](https://docs.github.com/rest/users/emails#set-primary-email-visibility-for-the-authenticated-user) endpoint.  OAuth app tokens and personal access tokens (classic) need the `user:email` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.email import Email
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
    api_instance = github_openapi.UsersApi(api_client)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List public email addresses for the authenticated user
        api_response = api_instance.users_list_public_emails_for_authenticated_user(per_page=per_page, page=page)
        print("The response of UsersApi->users_list_public_emails_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_list_public_emails_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Email]**](Email.md)

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
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_list_public_keys_for_user**
> List[KeySimple] users_list_public_keys_for_user(username, per_page=per_page, page=page)

List public keys for a user

Lists the _verified_ public SSH keys for a user. This is accessible by anyone.

### Example


```python
import github_openapi
from github_openapi.models.key_simple import KeySimple
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
    api_instance = github_openapi.UsersApi(api_client)
    username = 'username_example' # str | The handle for the GitHub user account.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List public keys for a user
        api_response = api_instance.users_list_public_keys_for_user(username, per_page=per_page, page=page)
        print("The response of UsersApi->users_list_public_keys_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_list_public_keys_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The handle for the GitHub user account. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[KeySimple]**](KeySimple.md)

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

# **users_list_public_ssh_keys_for_authenticated_user**
> List[Key] users_list_public_ssh_keys_for_authenticated_user(per_page=per_page, page=page)

List public SSH keys for the authenticated user

Lists the public SSH keys for the authenticated user's GitHub account.  OAuth app tokens and personal access tokens (classic) need the `read:public_key` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.key import Key
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
    api_instance = github_openapi.UsersApi(api_client)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List public SSH keys for the authenticated user
        api_response = api_instance.users_list_public_ssh_keys_for_authenticated_user(per_page=per_page, page=page)
        print("The response of UsersApi->users_list_public_ssh_keys_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_list_public_ssh_keys_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Key]**](Key.md)

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
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_list_social_accounts_for_authenticated_user**
> List[SocialAccount] users_list_social_accounts_for_authenticated_user(per_page=per_page, page=page)

List social accounts for the authenticated user

Lists all of your social accounts.

### Example


```python
import github_openapi
from github_openapi.models.social_account import SocialAccount
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
    api_instance = github_openapi.UsersApi(api_client)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List social accounts for the authenticated user
        api_response = api_instance.users_list_social_accounts_for_authenticated_user(per_page=per_page, page=page)
        print("The response of UsersApi->users_list_social_accounts_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_list_social_accounts_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[SocialAccount]**](SocialAccount.md)

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
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_list_social_accounts_for_user**
> List[SocialAccount] users_list_social_accounts_for_user(username, per_page=per_page, page=page)

List social accounts for a user

Lists social media accounts for a user. This endpoint is accessible by anyone.

### Example


```python
import github_openapi
from github_openapi.models.social_account import SocialAccount
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
    api_instance = github_openapi.UsersApi(api_client)
    username = 'username_example' # str | The handle for the GitHub user account.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List social accounts for a user
        api_response = api_instance.users_list_social_accounts_for_user(username, per_page=per_page, page=page)
        print("The response of UsersApi->users_list_social_accounts_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_list_social_accounts_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The handle for the GitHub user account. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[SocialAccount]**](SocialAccount.md)

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

# **users_list_ssh_signing_keys_for_authenticated_user**
> List[SshSigningKey] users_list_ssh_signing_keys_for_authenticated_user(per_page=per_page, page=page)

List SSH signing keys for the authenticated user

Lists the SSH signing keys for the authenticated user's GitHub account.  OAuth app tokens and personal access tokens (classic) need the `read:ssh_signing_key` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.ssh_signing_key import SshSigningKey
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
    api_instance = github_openapi.UsersApi(api_client)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List SSH signing keys for the authenticated user
        api_response = api_instance.users_list_ssh_signing_keys_for_authenticated_user(per_page=per_page, page=page)
        print("The response of UsersApi->users_list_ssh_signing_keys_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_list_ssh_signing_keys_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[SshSigningKey]**](SshSigningKey.md)

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
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_list_ssh_signing_keys_for_user**
> List[SshSigningKey] users_list_ssh_signing_keys_for_user(username, per_page=per_page, page=page)

List SSH signing keys for a user

Lists the SSH signing keys for a user. This operation is accessible by anyone.

### Example


```python
import github_openapi
from github_openapi.models.ssh_signing_key import SshSigningKey
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
    api_instance = github_openapi.UsersApi(api_client)
    username = 'username_example' # str | The handle for the GitHub user account.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List SSH signing keys for a user
        api_response = api_instance.users_list_ssh_signing_keys_for_user(username, per_page=per_page, page=page)
        print("The response of UsersApi->users_list_ssh_signing_keys_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_list_ssh_signing_keys_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The handle for the GitHub user account. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[SshSigningKey]**](SshSigningKey.md)

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

# **users_set_primary_email_visibility_for_authenticated_user**
> List[Email] users_set_primary_email_visibility_for_authenticated_user(users_set_primary_email_visibility_for_authenticated_user_request)

Set primary email visibility for the authenticated user

Sets the visibility for your primary email addresses.

### Example


```python
import github_openapi
from github_openapi.models.email import Email
from github_openapi.models.users_set_primary_email_visibility_for_authenticated_user_request import UsersSetPrimaryEmailVisibilityForAuthenticatedUserRequest
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
    api_instance = github_openapi.UsersApi(api_client)
    users_set_primary_email_visibility_for_authenticated_user_request = {"visibility":"private"} # UsersSetPrimaryEmailVisibilityForAuthenticatedUserRequest | 

    try:
        # Set primary email visibility for the authenticated user
        api_response = api_instance.users_set_primary_email_visibility_for_authenticated_user(users_set_primary_email_visibility_for_authenticated_user_request)
        print("The response of UsersApi->users_set_primary_email_visibility_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_set_primary_email_visibility_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_set_primary_email_visibility_for_authenticated_user_request** | [**UsersSetPrimaryEmailVisibilityForAuthenticatedUserRequest**](UsersSetPrimaryEmailVisibilityForAuthenticatedUserRequest.md)|  | 

### Return type

[**List[Email]**](Email.md)

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
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_unblock**
> users_unblock(username)

Unblock a user

Unblocks the given user and returns a 204.

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
    api_instance = github_openapi.UsersApi(api_client)
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Unblock a user
        api_instance.users_unblock(username)
    except Exception as e:
        print("Exception when calling UsersApi->users_unblock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_unfollow**
> users_unfollow(username)

Unfollow a user

OAuth app tokens and personal access tokens (classic) need the `user:follow` scope to use this endpoint.

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
    api_instance = github_openapi.UsersApi(api_client)
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Unfollow a user
        api_instance.users_unfollow(username)
    except Exception as e:
        print("Exception when calling UsersApi->users_unfollow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_update_authenticated**
> PrivateUser users_update_authenticated(users_update_authenticated_request=users_update_authenticated_request)

Update the authenticated user

**Note:** If your email is set to private and you send an `email` parameter as part of this request to update your profile, your privacy settings are still enforced: the email address will not be displayed on your public profile or via the API.

### Example


```python
import github_openapi
from github_openapi.models.private_user import PrivateUser
from github_openapi.models.users_update_authenticated_request import UsersUpdateAuthenticatedRequest
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
    api_instance = github_openapi.UsersApi(api_client)
    users_update_authenticated_request = {"blog":"https://github.com/blog","name":"monalisa octocat"} # UsersUpdateAuthenticatedRequest |  (optional)

    try:
        # Update the authenticated user
        api_response = api_instance.users_update_authenticated(users_update_authenticated_request=users_update_authenticated_request)
        print("The response of UsersApi->users_update_authenticated:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_update_authenticated: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_update_authenticated_request** | [**UsersUpdateAuthenticatedRequest**](UsersUpdateAuthenticatedRequest.md)|  | [optional] 

### Return type

[**PrivateUser**](PrivateUser.md)

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
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

