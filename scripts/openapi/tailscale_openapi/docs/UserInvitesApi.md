# tailscale_openapi.UserInvitesApi

All URIs are relative to *https://api.tailscale.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_invites**](UserInvitesApi.md#create_user_invites) | **POST** /tailnet/{tailnet}/user-invites | Create user invites
[**delete_user_invite**](UserInvitesApi.md#delete_user_invite) | **DELETE** /user-invites/{userInviteId} | Delete a user invite
[**get_user_invite**](UserInvitesApi.md#get_user_invite) | **GET** /user-invites/{userInviteId} | Get a user invite
[**list_user_invites**](UserInvitesApi.md#list_user_invites) | **GET** /tailnet/{tailnet}/user-invites | List user invites
[**resend_user_invite**](UserInvitesApi.md#resend_user_invite) | **POST** /user-invites/{userInviteId}/resend | Resend a user invite


# **create_user_invites**
> List[UserInvite] create_user_invites(tailnet, create_user_invites_request_inner=create_user_invites_request_inner)

Create user invites

Create, and optionally email out, new user invites to join the tailnet.

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.create_user_invites_request_inner import CreateUserInvitesRequestInner
from tailscale_openapi.models.user_invite import UserInvite
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
    api_instance = tailscale_openapi.UserInvitesApi(api_client)
    tailnet = 'example.com' # str | The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (`-`) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/-/...\"   ```  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \"tailnet name\" found in the DNS tab).    For example, if your organization name is `alice@example.com`, your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\"   ```    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name). 
    create_user_invites_request_inner = [tailscale_openapi.CreateUserInvitesRequestInner()] # List[CreateUserInvitesRequestInner] |  (optional)

    try:
        # Create user invites
        api_response = api_instance.create_user_invites(tailnet, create_user_invites_request_inner=create_user_invites_request_inner)
        print("The response of UserInvitesApi->create_user_invites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserInvitesApi->create_user_invites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tailnet** | **str**| The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (&#x60;-&#x60;) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/-/...\&quot;   &#x60;&#x60;&#x60;  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \&quot;tailnet name\&quot; found in the DNS tab).    For example, if your organization name is &#x60;alice@example.com&#x60;, your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\&quot;   &#x60;&#x60;&#x60;    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name).  | 
 **create_user_invites_request_inner** | [**List[CreateUserInvitesRequestInner]**](CreateUserInvitesRequestInner.md)|  | [optional] 

### Return type

[**List[UserInvite]**](UserInvite.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**404** | Tailnet not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_invite**
> delete_user_invite(user_invite_id)

Delete a user invite

Deletes a specific user invite. 

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
    api_instance = tailscale_openapi.UserInvitesApi(api_client)
    user_invite_id = 'user_invite_id_example' # str | ID of the user invite.

    try:
        # Delete a user invite
        api_instance.delete_user_invite(user_invite_id)
    except Exception as e:
        print("Exception when calling UserInvitesApi->delete_user_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_invite_id** | **str**| ID of the user invite. | 

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
**404** | User invite not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_invite**
> UserInvite get_user_invite(user_invite_id)

Get a user invite

Retrieve a specific user invite. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.user_invite import UserInvite
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
    api_instance = tailscale_openapi.UserInvitesApi(api_client)
    user_invite_id = 'user_invite_id_example' # str | ID of the user invite.

    try:
        # Get a user invite
        api_response = api_instance.get_user_invite(user_invite_id)
        print("The response of UserInvitesApi->get_user_invite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserInvitesApi->get_user_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_invite_id** | **str**| ID of the user invite. | 

### Return type

[**UserInvite**](UserInvite.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**404** | User invite not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_invites**
> List[UserInvite] list_user_invites(tailnet)

List user invites

List all open (not yet accepted) user invites to the tailnet.

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.user_invite import UserInvite
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
    api_instance = tailscale_openapi.UserInvitesApi(api_client)
    tailnet = 'example.com' # str | The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (`-`) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/-/...\"   ```  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \"tailnet name\" found in the DNS tab).    For example, if your organization name is `alice@example.com`, your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\"   ```    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name). 

    try:
        # List user invites
        api_response = api_instance.list_user_invites(tailnet)
        print("The response of UserInvitesApi->list_user_invites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserInvitesApi->list_user_invites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tailnet** | **str**| The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (&#x60;-&#x60;) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/-/...\&quot;   &#x60;&#x60;&#x60;  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \&quot;tailnet name\&quot; found in the DNS tab).    For example, if your organization name is &#x60;alice@example.com&#x60;, your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\&quot;   &#x60;&#x60;&#x60;    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name).  | 

### Return type

[**List[UserInvite]**](UserInvite.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**404** | Tailnet not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_user_invite**
> resend_user_invite(user_invite_id)

Resend a user invite

Resend a user invite by email. You can only use this if the specified invite was originally created with an email specified. Refer to [creating user invites for a tailnet](#tag/userinvites/post/tailnet/{tailnet}/user-invites).  Note: Invite resends are rate limited to one per minute. 

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
    api_instance = tailscale_openapi.UserInvitesApi(api_client)
    user_invite_id = 'user_invite_id_example' # str | ID of the user invite.

    try:
        # Resend a user invite
        api_instance.resend_user_invite(user_invite_id)
    except Exception as e:
        print("Exception when calling UserInvitesApi->resend_user_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_invite_id** | **str**| ID of the user invite. | 

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
**404** | User invite not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

