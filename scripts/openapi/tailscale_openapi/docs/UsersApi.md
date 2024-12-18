# tailscale_openapi.UsersApi

All URIs are relative to *https://api.tailscale.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_user**](UsersApi.md#approve_user) | **POST** /users/{userId}/approve | Approve a user
[**delete_user**](UsersApi.md#delete_user) | **POST** /users/{userId}/delete | Delete a user
[**get_user**](UsersApi.md#get_user) | **GET** /users/{userId} | Get a user
[**list_users**](UsersApi.md#list_users) | **GET** /tailnet/{tailnet}/users | List users
[**restore_user**](UsersApi.md#restore_user) | **POST** /users/{userId}/restore | Restore a user
[**suspend_user**](UsersApi.md#suspend_user) | **POST** /users/{userId}/suspend | Suspend a user
[**update_user_role**](UsersApi.md#update_user_role) | **POST** /users/{userId}/role | Update user role


# **approve_user**
> approve_user(user_id)

Approve a user

Approve a pending user's access to the tailnet. This is a no-op if user approval has not been enabled for the tailnet, or if the user is already approved.  User approval can be managed using the [tailnet settings endpoints](#tag/tailnetsettings).  Learn more about [user approval](/kb/1239/user-approval) and [enabling user approval for your network](/kb/1239/user-approval#enable-user-approval-for-your-network).  OAuth Scope: `users`.  > ⓘ User-based access tokens cannot approve their own user. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tailscale.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = tailscale_openapi.Configuration(
    host = "https://api.tailscale.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = tailscale_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tailscale_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tailscale_openapi.UsersApi(api_client)
    user_id = 'user_id_example' # str | ID of the user. 

    try:
        # Approve a user
        api_instance.approve_user(user_id)
    except Exception as e:
        print("Exception when calling UsersApi->approve_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of the user.  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** |  |  -  |
**403** |  |  -  |
**404** | User not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(user_id)

Delete a user

> ⓘ This endpoint is available for the [Personal and Enterprise plans](/pricing).  Delete a user from their tailnet. Learn more about [deleting users](/kb/1145/remove-team-members#deleting-users).  OAuth Scope: `users`.  > ⓘ User-based access tokens cannot delete their own user. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tailscale.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = tailscale_openapi.Configuration(
    host = "https://api.tailscale.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = tailscale_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tailscale_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tailscale_openapi.UsersApi(api_client)
    user_id = 'user_id_example' # str | ID of the user. 

    try:
        # Delete a user
        api_instance.delete_user(user_id)
    except Exception as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of the user.  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** |  |  -  |
**403** |  |  -  |
**404** | User not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> User get_user(user_id)

Get a user

Retrieve details about the specified user.  OAuth Scope: `users:read`. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.user import User
from tailscale_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tailscale.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = tailscale_openapi.Configuration(
    host = "https://api.tailscale.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = tailscale_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tailscale_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tailscale_openapi.UsersApi(api_client)
    user_id = 'user_id_example' # str | ID of the user. 

    try:
        # Get a user
        api_response = api_instance.get_user(user_id)
        print("The response of UsersApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of the user.  | 

### Return type

[**User**](User.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** |  |  -  |
**403** |  |  -  |
**404** | User not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> ListUsers200Response list_users(tailnet, type=type, role=role)

List users

List all users of a tailnet.  OAuth Scope: `users:read`. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.list_users200_response import ListUsers200Response
from tailscale_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tailscale.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = tailscale_openapi.Configuration(
    host = "https://api.tailscale.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = tailscale_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tailscale_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tailscale_openapi.UsersApi(api_client)
    tailnet = 'example.com' # str | The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (`-`) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/-/...\"   ```  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \"tailnet name\" found in the DNS tab).    For example, if your organization name is `alice@example.com`, your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\"   ```    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name). 
    type = member # str | Allows for filtering the output by user type.  (optional) (default to member)
    role = all # str | Allows for filtering the output by user role. Learn more about [user roles](kb/1138/user-roles).  (optional) (default to all)

    try:
        # List users
        api_response = api_instance.list_users(tailnet, type=type, role=role)
        print("The response of UsersApi->list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->list_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tailnet** | **str**| The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (&#x60;-&#x60;) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/-/...\&quot;   &#x60;&#x60;&#x60;  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \&quot;tailnet name\&quot; found in the DNS tab).    For example, if your organization name is &#x60;alice@example.com&#x60;, your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\&quot;   &#x60;&#x60;&#x60;    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name).  | 
 **type** | **str**| Allows for filtering the output by user type.  | [optional] [default to member]
 **role** | **str**| Allows for filtering the output by user role. Learn more about [user roles](kb/1138/user-roles).  | [optional] [default to all]

### Return type

[**ListUsers200Response**](ListUsers200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** |  |  -  |
**403** |  |  -  |
**404** | Tailnet not found, or user does not have access to read users. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_user**
> restore_user(user_id)

Restore a user

> ⓘ This endpoint is available for the [Personal and Enterprise plans](/pricing).  Restores a suspended user's access to their tailnet. Learn more about [restoring users](/kb/1145/remove-team-members#restoring-users).  OAuth Scope: `users`.  > ⓘ User-based access tokens cannot restore their own user. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tailscale.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = tailscale_openapi.Configuration(
    host = "https://api.tailscale.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = tailscale_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tailscale_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tailscale_openapi.UsersApi(api_client)
    user_id = 'user_id_example' # str | ID of the user. 

    try:
        # Restore a user
        api_instance.restore_user(user_id)
    except Exception as e:
        print("Exception when calling UsersApi->restore_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of the user.  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** |  |  -  |
**403** |  |  -  |
**404** | User not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_user**
> suspend_user(user_id)

Suspend a user

> ⓘ This endpoint is available for the [Personal and Enterprise plans](/pricing).  Suspends a user from their tailnet. Learn more about [suspending users](/kb/1145/remove-team-members#suspending-users).  OAuth Scope: `users`.  > ⓘ User-based access tokens cannot suspend their own user. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tailscale.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = tailscale_openapi.Configuration(
    host = "https://api.tailscale.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = tailscale_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tailscale_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tailscale_openapi.UsersApi(api_client)
    user_id = 'user_id_example' # str | ID of the user. 

    try:
        # Suspend a user
        api_instance.suspend_user(user_id)
    except Exception as e:
        print("Exception when calling UsersApi->suspend_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of the user.  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** |  |  -  |
**403** |  |  -  |
**404** | User not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_role**
> update_user_role(user_id, update_user_role_request=update_user_role_request)

Update user role

Update the role for the specified user.  Learn more about [user roles](kb/1138/user-roles).  OAuth Scope: `users`.  > ⓘ User-based access tokens cannot update their own user's role. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.update_user_role_request import UpdateUserRoleRequest
from tailscale_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.tailscale.com/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = tailscale_openapi.Configuration(
    host = "https://api.tailscale.com/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = tailscale_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with tailscale_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tailscale_openapi.UsersApi(api_client)
    user_id = 'user_id_example' # str | ID of the user. 
    update_user_role_request = tailscale_openapi.UpdateUserRoleRequest() # UpdateUserRoleRequest |  (optional)

    try:
        # Update user role
        api_instance.update_user_role(user_id, update_user_role_request=update_user_role_request)
    except Exception as e:
        print("Exception when calling UsersApi->update_user_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| ID of the user.  | 
 **update_user_role_request** | [**UpdateUserRoleRequest**](UpdateUserRoleRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** |  |  -  |
**403** |  |  -  |
**404** | User not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

