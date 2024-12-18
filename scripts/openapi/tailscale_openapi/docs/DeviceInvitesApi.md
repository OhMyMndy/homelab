# tailscale_openapi.DeviceInvitesApi

All URIs are relative to *https://api.tailscale.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_device_invite**](DeviceInvitesApi.md#accept_device_invite) | **POST** /device-invites/-/accept | Accept a device invite
[**create_device_invites**](DeviceInvitesApi.md#create_device_invites) | **POST** /device/{deviceId}/device-invites | Create device invites
[**delete_device_invite**](DeviceInvitesApi.md#delete_device_invite) | **DELETE** /device-invites/{deviceInviteId} | Delete a device invite
[**get_device_invite**](DeviceInvitesApi.md#get_device_invite) | **GET** /device-invites/{deviceInviteId} | Get a device invite
[**list_device_invites**](DeviceInvitesApi.md#list_device_invites) | **GET** /device/{deviceId}/device-invites | List device invites
[**resend_device_invite**](DeviceInvitesApi.md#resend_device_invite) | **POST** /device-invites/{deviceInviteId}/resend | Resend a device invite


# **accept_device_invite**
> AcceptDeviceInvite200Response accept_device_invite(accept_device_invite_request=accept_device_invite_request)

Accept a device invite

Accepts the invitation to share a device into the requesting user's tailnet.  Note that device invites cannot be accepted using an API access token generated from an OAuth client as the shared device is scoped to a user. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.accept_device_invite200_response import AcceptDeviceInvite200Response
from tailscale_openapi.models.accept_device_invite_request import AcceptDeviceInviteRequest
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
    api_instance = tailscale_openapi.DeviceInvitesApi(api_client)
    accept_device_invite_request = {"invite":"https://login.tailscale.com/admin/invite/xxxxxx"} # AcceptDeviceInviteRequest |  (optional)

    try:
        # Accept a device invite
        api_response = api_instance.accept_device_invite(accept_device_invite_request=accept_device_invite_request)
        print("The response of DeviceInvitesApi->accept_device_invite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceInvitesApi->accept_device_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept_device_invite_request** | [**AcceptDeviceInviteRequest**](AcceptDeviceInviteRequest.md)|  | [optional] 

### Return type

[**AcceptDeviceInvite200Response**](AcceptDeviceInvite200Response.md)

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
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_device_invites**
> List[DeviceInvite] create_device_invites(device_id, create_device_invites_request_inner=create_device_invites_request_inner)

Create device invites

Create new share invites for a device.  Note that device invites cannot be created using an API access token generated from an OAuth client as the shared device is scoped to a user. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.create_device_invites_request_inner import CreateDeviceInvitesRequestInner
from tailscale_openapi.models.device_invite import DeviceInvite
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
    api_instance = tailscale_openapi.DeviceInvitesApi(api_client)
    device_id = 'device_id_example' # str | ID of the device. Using the device's `nodeId` is preferred, but its numeric `id` value can also be used. 
    create_device_invites_request_inner = [tailscale_openapi.CreateDeviceInvitesRequestInner()] # List[CreateDeviceInvitesRequestInner] | Device invites to create. (optional)

    try:
        # Create device invites
        api_response = api_instance.create_device_invites(device_id, create_device_invites_request_inner=create_device_invites_request_inner)
        print("The response of DeviceInvitesApi->create_device_invites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceInvitesApi->create_device_invites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| ID of the device. Using the device&#39;s &#x60;nodeId&#x60; is preferred, but its numeric &#x60;id&#x60; value can also be used.  | 
 **create_device_invites_request_inner** | [**List[CreateDeviceInvitesRequestInner]**](CreateDeviceInvitesRequestInner.md)| Device invites to create. | [optional] 

### Return type

[**List[DeviceInvite]**](DeviceInvite.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**404** | Device not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_invite**
> delete_device_invite(device_invite_id)

Delete a device invite

Delete a specific device invite.  OAuth Scope: `device_invites`. 

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
    api_instance = tailscale_openapi.DeviceInvitesApi(api_client)
    device_invite_id = 'device_invite_id_example' # str | ID of the device invite.

    try:
        # Delete a device invite
        api_instance.delete_device_invite(device_invite_id)
    except Exception as e:
        print("Exception when calling DeviceInvitesApi->delete_device_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_invite_id** | **str**| ID of the device invite. | 

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
**404** | Device invite not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_invite**
> DeviceInvite get_device_invite(device_invite_id)

Get a device invite

Retrieve a specific device invite.  OAuth Scope: `device_invites:read`. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.device_invite import DeviceInvite
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
    api_instance = tailscale_openapi.DeviceInvitesApi(api_client)
    device_invite_id = 'device_invite_id_example' # str | ID of the device invite.

    try:
        # Get a device invite
        api_response = api_instance.get_device_invite(device_invite_id)
        print("The response of DeviceInvitesApi->get_device_invite:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceInvitesApi->get_device_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_invite_id** | **str**| ID of the device invite. | 

### Return type

[**DeviceInvite**](DeviceInvite.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**404** | Device invite not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_device_invites**
> List[DeviceInvite] list_device_invites(device_id)

List device invites

List all share invites for a device.  OAuth Scope: `device_invites:read`. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.device_invite import DeviceInvite
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
    api_instance = tailscale_openapi.DeviceInvitesApi(api_client)
    device_id = 'device_id_example' # str | ID of the device. Using the device's `nodeId` is preferred, but its numeric `id` value can also be used. 

    try:
        # List device invites
        api_response = api_instance.list_device_invites(device_id)
        print("The response of DeviceInvitesApi->list_device_invites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceInvitesApi->list_device_invites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| ID of the device. Using the device&#39;s &#x60;nodeId&#x60; is preferred, but its numeric &#x60;id&#x60; value can also be used.  | 

### Return type

[**List[DeviceInvite]**](DeviceInvite.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**404** | Device not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_device_invite**
> resend_device_invite(device_invite_id)

Resend a device invite

Resend a device invite by email. You can only use this if the specified invite was originally created with an email specified. Refer to [creating device invites for a device](#tag/deviceinvites/post/device/{deviceId}/device-invites).  Note: Invite resends are rate limited to one per minute.  Note that device invites cannot be resent using an API access token generated from an OAuth client as the shared device is scoped to a user. 

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
    api_instance = tailscale_openapi.DeviceInvitesApi(api_client)
    device_invite_id = 'device_invite_id_example' # str | ID of the device invite.

    try:
        # Resend a device invite
        api_instance.resend_device_invite(device_invite_id)
    except Exception as e:
        print("Exception when calling DeviceInvitesApi->resend_device_invite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_invite_id** | **str**| ID of the device invite. | 

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
**404** | Device invite not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

