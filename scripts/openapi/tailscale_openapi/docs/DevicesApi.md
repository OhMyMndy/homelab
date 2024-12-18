# tailscale_openapi.DevicesApi

All URIs are relative to *https://api.tailscale.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize_device**](DevicesApi.md#authorize_device) | **POST** /device/{deviceId}/authorized | Authorize device
[**delete_custom_device_posture_attributes**](DevicesApi.md#delete_custom_device_posture_attributes) | **DELETE** /device/{deviceId}/attributes/{attributeKey} | Delete custom device posture attributes
[**delete_device**](DevicesApi.md#delete_device) | **DELETE** /device/{deviceId} | Delete a device
[**expire_device_key**](DevicesApi.md#expire_device_key) | **POST** /device/{deviceId}/expire | Expire a device&#39;s key
[**get_device**](DevicesApi.md#get_device) | **GET** /device/{deviceId} | Get a device
[**get_device_posture_attributes**](DevicesApi.md#get_device_posture_attributes) | **GET** /device/{deviceId}/attributes | Get device posture attributes
[**list_device_routes**](DevicesApi.md#list_device_routes) | **GET** /device/{deviceId}/routes | List device routes
[**list_tailnet_devices**](DevicesApi.md#list_tailnet_devices) | **GET** /tailnet/{tailnet}/devices | List tailnet devices
[**set_custom_device_posture_attributes**](DevicesApi.md#set_custom_device_posture_attributes) | **POST** /device/{deviceId}/attributes/{attributeKey} | Set custom device posture attributes
[**set_device_ip**](DevicesApi.md#set_device_ip) | **POST** /device/{deviceId}/ip | Set device IPv4 address
[**set_device_name**](DevicesApi.md#set_device_name) | **POST** /device/{deviceId}/name | Set device name
[**set_device_routes**](DevicesApi.md#set_device_routes) | **POST** /device/{deviceId}/routes | Set device routes
[**set_device_tags**](DevicesApi.md#set_device_tags) | **POST** /device/{deviceId}/tags | Set device tags
[**update_device_key**](DevicesApi.md#update_device_key) | **POST** /device/{deviceId}/key | Update device key


# **authorize_device**
> authorize_device(device_id, authorize_device_request=authorize_device_request)

Authorize device

This call marks a device as authorized or revokes its authorization for tailnets where device authorization is required, according to the authorized field in the payload.  OAuth Scope: `devices:core`. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.authorize_device_request import AuthorizeDeviceRequest
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
    api_instance = tailscale_openapi.DevicesApi(api_client)
    device_id = 'device_id_example' # str | ID of the device. Using the device's `nodeId` is preferred, but its numeric `id` value can also be used. 
    authorize_device_request = tailscale_openapi.AuthorizeDeviceRequest() # AuthorizeDeviceRequest |  (optional)

    try:
        # Authorize device
        api_instance.authorize_device(device_id, authorize_device_request=authorize_device_request)
    except Exception as e:
        print("Exception when calling DevicesApi->authorize_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| ID of the device. Using the device&#39;s &#x60;nodeId&#x60; is preferred, but its numeric &#x60;id&#x60; value can also be used.  | 
 **authorize_device_request** | [**AuthorizeDeviceRequest**](AuthorizeDeviceRequest.md)|  | [optional] 

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
**404** | Device not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_device_posture_attributes**
> delete_custom_device_posture_attributes(device_id, attribute_key)

Delete custom device posture attributes

Delete a posture attribute from the specified device. This is only applicable to user-managed posture attributes in the custom namespace, which is indicated by prefixing the attribute key with `custom:`.  OAuth Scope: `devices:posture_attributes`. 

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
    api_instance = tailscale_openapi.DevicesApi(api_client)
    device_id = 'device_id_example' # str | ID of the device. Using the device's `nodeId` is preferred, but its numeric `id` value can also be used. 
    attribute_key = 'attribute_key_example' # str | The name of the posture attribute to set. This must be prefixed with `custom`:  Keys have a maximum length of 50 characters including the namespace, and can only contain letters, numbers, underscores, and colon.  Keys are case-sensitive. Keys must be unique, but are checked for uniqueness in a case-insensitive manner. For example, `custom:MyAttribute` and `custom:myattribute` cannot both be set within a single tailnet.  All values for a given key need to be of the same type, which is determined when the first value is written for a given key. For example, `custom:myattribute` cannot have a numeric value (`8`7) for one node and a string value (`\"78\"`) for another node within the same tailnet. 

    try:
        # Delete custom device posture attributes
        api_instance.delete_custom_device_posture_attributes(device_id, attribute_key)
    except Exception as e:
        print("Exception when calling DevicesApi->delete_custom_device_posture_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| ID of the device. Using the device&#39;s &#x60;nodeId&#x60; is preferred, but its numeric &#x60;id&#x60; value can also be used.  | 
 **attribute_key** | **str**| The name of the posture attribute to set. This must be prefixed with &#x60;custom&#x60;:  Keys have a maximum length of 50 characters including the namespace, and can only contain letters, numbers, underscores, and colon.  Keys are case-sensitive. Keys must be unique, but are checked for uniqueness in a case-insensitive manner. For example, &#x60;custom:MyAttribute&#x60; and &#x60;custom:myattribute&#x60; cannot both be set within a single tailnet.  All values for a given key need to be of the same type, which is determined when the first value is written for a given key. For example, &#x60;custom:myattribute&#x60; cannot have a numeric value (&#x60;8&#x60;7) for one node and a string value (&#x60;\&quot;78\&quot;&#x60;) for another node within the same tailnet.  | 

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
**404** | Device not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device**
> delete_device(device_id)

Delete a device

Deletes the device from its tailnet. The device must belong to the requesting user's tailnet. Deleting devices shared with the tailnet is not supported.  OAuth Scope: `devices:core`. 

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
    api_instance = tailscale_openapi.DevicesApi(api_client)
    device_id = 'device_id_example' # str | ID of the device. Using the device's `nodeId` is preferred, but its numeric `id` value can also be used. 

    try:
        # Delete a device
        api_instance.delete_device(device_id)
    except Exception as e:
        print("Exception when calling DevicesApi->delete_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| ID of the device. Using the device&#39;s &#x60;nodeId&#x60; is preferred, but its numeric &#x60;id&#x60; value can also be used.  | 

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
**400** | Invalid device value. |  -  |
**500** |  |  -  |
**501** | Device not owned by tailnet. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **expire_device_key**
> expire_device_key(device_id)

Expire a device's key

Mark a device's node key as expired. This will require the device to re-authenticate in order to connect to the tailnet. The device must belong to the requesting user's tailnet.  OAuth Scope: `devices:core`. 

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
    api_instance = tailscale_openapi.DevicesApi(api_client)
    device_id = 'device_id_example' # str | ID of the device. Using the device's `nodeId` is preferred, but its numeric `id` value can also be used. 

    try:
        # Expire a device's key
        api_instance.expire_device_key(device_id)
    except Exception as e:
        print("Exception when calling DevicesApi->expire_device_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| ID of the device. Using the device&#39;s &#x60;nodeId&#x60; is preferred, but its numeric &#x60;id&#x60; value can also be used.  | 

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
**404** | Device not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device**
> Device get_device(device_id)

Get a device

Retrieve the details for the specified device.  OAuth Scope: `devices:core:read`. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.device import Device
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
    api_instance = tailscale_openapi.DevicesApi(api_client)
    device_id = 'device_id_example' # str | ID of the device. Using the device's `nodeId` is preferred, but its numeric `id` value can also be used. 

    try:
        # Get a device
        api_response = api_instance.get_device(device_id)
        print("The response of DevicesApi->get_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->get_device: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| ID of the device. Using the device&#39;s &#x60;nodeId&#x60; is preferred, but its numeric &#x60;id&#x60; value can also be used.  | 

### Return type

[**Device**](Device.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** | Invalid ID supplied. |  -  |
**404** | Device not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_posture_attributes**
> DevicePostureAttributes get_device_posture_attributes(device_id)

Get device posture attributes

Retrieve all posture attributes for the specified device. This returns a JSON object of all the key-value pairs of posture attributes for the device.  OAuth Scope: `devices:posture_attributes:read`. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.device_posture_attributes import DevicePostureAttributes
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
    api_instance = tailscale_openapi.DevicesApi(api_client)
    device_id = 'device_id_example' # str | ID of the device. Using the device's `nodeId` is preferred, but its numeric `id` value can also be used. 

    try:
        # Get device posture attributes
        api_response = api_instance.get_device_posture_attributes(device_id)
        print("The response of DevicesApi->get_device_posture_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->get_device_posture_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| ID of the device. Using the device&#39;s &#x60;nodeId&#x60; is preferred, but its numeric &#x60;id&#x60; value can also be used.  | 

### Return type

[**DevicePostureAttributes**](DevicePostureAttributes.md)

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

# **list_device_routes**
> DeviceRoutes list_device_routes(device_id)

List device routes

Retrieve the list of subnet routes that a device is advertising, as well as those that are enabled for it.  Routes must be both advertised and enabled for a device to act as a subnet router or exit node. If a device has advertised routes, they are not exposed to traffic until they are enabled. Conversely, if routes are enabled before they are advertised, they are not available for routing until the device in question has advertised them.  Learn more about [subnet routers](/kb/1019/subnets) and [exit nodes](/kb/1103/exit-nodes).  OAuth Scope: `devices:routes:read`. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.device_routes import DeviceRoutes
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
    api_instance = tailscale_openapi.DevicesApi(api_client)
    device_id = 'device_id_example' # str | ID of the device. Using the device's `nodeId` is preferred, but its numeric `id` value can also be used. 

    try:
        # List device routes
        api_response = api_instance.list_device_routes(device_id)
        print("The response of DevicesApi->list_device_routes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->list_device_routes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| ID of the device. Using the device&#39;s &#x60;nodeId&#x60; is preferred, but its numeric &#x60;id&#x60; value can also be used.  | 

### Return type

[**DeviceRoutes**](DeviceRoutes.md)

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

# **list_tailnet_devices**
> ListTailnetDevices200Response list_tailnet_devices(tailnet, fields=fields)

List tailnet devices

Lists the devices in a tailnet.  OAuth Scope: `devices:core:read`. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.list_tailnet_devices200_response import ListTailnetDevices200Response
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
    api_instance = tailscale_openapi.DevicesApi(api_client)
    tailnet = 'example.com' # str | The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (`-`) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/-/...\"   ```  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \"tailnet name\" found in the DNS tab).    For example, if your organization name is `alice@example.com`, your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\"   ```    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name). 
    fields = 'all' # str | Optionally controls whether the response returns **all** fields or only a predefined subset of fields. Currently, there are two supported options:  - **`all`:** return all fields in the response - **`default`:** return all fields **except**:   - `enabledRoutes`   - `advertisedRoutes`   - `clientConnectivity` (which contains the following fields: `mappingVariesByDestIP`, `derp`, `endpoints`, `latency`, and `clientSupports`)  If the `fields` parameter is not supplied, then the default (limited fields) option is used.  (optional)

    try:
        # List tailnet devices
        api_response = api_instance.list_tailnet_devices(tailnet, fields=fields)
        print("The response of DevicesApi->list_tailnet_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->list_tailnet_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tailnet** | **str**| The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (&#x60;-&#x60;) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/-/...\&quot;   &#x60;&#x60;&#x60;  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \&quot;tailnet name\&quot; found in the DNS tab).    For example, if your organization name is &#x60;alice@example.com&#x60;, your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\&quot;   &#x60;&#x60;&#x60;    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name).  | 
 **fields** | **str**| Optionally controls whether the response returns **all** fields or only a predefined subset of fields. Currently, there are two supported options:  - **&#x60;all&#x60;:** return all fields in the response - **&#x60;default&#x60;:** return all fields **except**:   - &#x60;enabledRoutes&#x60;   - &#x60;advertisedRoutes&#x60;   - &#x60;clientConnectivity&#x60; (which contains the following fields: &#x60;mappingVariesByDestIP&#x60;, &#x60;derp&#x60;, &#x60;endpoints&#x60;, &#x60;latency&#x60;, and &#x60;clientSupports&#x60;)  If the &#x60;fields&#x60; parameter is not supplied, then the default (limited fields) option is used.  | [optional] 

### Return type

[**ListTailnetDevices200Response**](ListTailnetDevices200Response.md)

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

# **set_custom_device_posture_attributes**
> DevicePostureAttributes set_custom_device_posture_attributes(device_id, attribute_key, set_custom_device_posture_attributes_request)

Set custom device posture attributes

Create or update a custom posture attribute on the specified device. User-managed attributes must be in the custom namespace, which is indicated by prefixing the attribute key with `custom:`.  Custom device posture attributes are available for the Personal and Enterprise plans.  OAuth Scope: `devices:posture_attributes`. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.device_posture_attributes import DevicePostureAttributes
from tailscale_openapi.models.set_custom_device_posture_attributes_request import SetCustomDevicePostureAttributesRequest
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
    api_instance = tailscale_openapi.DevicesApi(api_client)
    device_id = 'device_id_example' # str | ID of the device. Using the device's `nodeId` is preferred, but its numeric `id` value can also be used. 
    attribute_key = 'attribute_key_example' # str | The name of the posture attribute to set. This must be prefixed with `custom`:  Keys have a maximum length of 50 characters including the namespace, and can only contain letters, numbers, underscores, and colon.  Keys are case-sensitive. Keys must be unique, but are checked for uniqueness in a case-insensitive manner. For example, `custom:MyAttribute` and `custom:myattribute` cannot both be set within a single tailnet.  All values for a given key need to be of the same type, which is determined when the first value is written for a given key. For example, `custom:myattribute` cannot have a numeric value (`8`7) for one node and a string value (`\"78\"`) for another node within the same tailnet. 
    set_custom_device_posture_attributes_request = tailscale_openapi.SetCustomDevicePostureAttributesRequest() # SetCustomDevicePostureAttributesRequest | 

    try:
        # Set custom device posture attributes
        api_response = api_instance.set_custom_device_posture_attributes(device_id, attribute_key, set_custom_device_posture_attributes_request)
        print("The response of DevicesApi->set_custom_device_posture_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->set_custom_device_posture_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| ID of the device. Using the device&#39;s &#x60;nodeId&#x60; is preferred, but its numeric &#x60;id&#x60; value can also be used.  | 
 **attribute_key** | **str**| The name of the posture attribute to set. This must be prefixed with &#x60;custom&#x60;:  Keys have a maximum length of 50 characters including the namespace, and can only contain letters, numbers, underscores, and colon.  Keys are case-sensitive. Keys must be unique, but are checked for uniqueness in a case-insensitive manner. For example, &#x60;custom:MyAttribute&#x60; and &#x60;custom:myattribute&#x60; cannot both be set within a single tailnet.  All values for a given key need to be of the same type, which is determined when the first value is written for a given key. For example, &#x60;custom:myattribute&#x60; cannot have a numeric value (&#x60;8&#x60;7) for one node and a string value (&#x60;\&quot;78\&quot;&#x60;) for another node within the same tailnet.  | 
 **set_custom_device_posture_attributes_request** | [**SetCustomDevicePostureAttributesRequest**](SetCustomDevicePostureAttributesRequest.md)|  | 

### Return type

[**DevicePostureAttributes**](DevicePostureAttributes.md)

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

# **set_device_ip**
> set_device_ip(device_id, set_device_ip_request=set_device_ip_request)

Set device IPv4 address

When a device is added to a tailnet, its Tailscale IPv4 address is set at random either from the CGNAT range, or a subset of the CGNAT range specified by an [ip pool](https://tailscale.com/kb/1304/ip-pool). This endpoint can be used to replace the existing IPv4 address with a specific value.  This action will break any existing connections to this machine. You will need to reconnect to this machine using the new IP address. You may also need to flush your DNS cache.  OAuth Scope: `devices:core`. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.set_device_ip_request import SetDeviceIpRequest
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
    api_instance = tailscale_openapi.DevicesApi(api_client)
    device_id = 'device_id_example' # str | ID of the device. Using the device's `nodeId` is preferred, but its numeric `id` value can also be used. 
    set_device_ip_request = tailscale_openapi.SetDeviceIpRequest() # SetDeviceIpRequest |  (optional)

    try:
        # Set device IPv4 address
        api_instance.set_device_ip(device_id, set_device_ip_request=set_device_ip_request)
    except Exception as e:
        print("Exception when calling DevicesApi->set_device_ip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| ID of the device. Using the device&#39;s &#x60;nodeId&#x60; is preferred, but its numeric &#x60;id&#x60; value can also be used.  | 
 **set_device_ip_request** | [**SetDeviceIpRequest**](SetDeviceIpRequest.md)|  | [optional] 

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
**404** | Device not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_device_name**
> set_device_name(device_id, set_device_name_request=set_device_name_request)

Set device name

When a device is added to a tailnet, its Tailscale [device name](https://tailscale.com/kb/1098/machine-names) (also sometimes referred to as machine name) is generated from its OS hostname. The device name is the canonical name for the device on your tailnet.  Device name changes immediately get propogated through your tailnet, so be aware that any existing [Magic DNS](https://tailscale.com/kb/1081/magicdns) URLs using the old name will no longer work.  OAuth Scope: `devices:core`. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.set_device_name_request import SetDeviceNameRequest
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
    api_instance = tailscale_openapi.DevicesApi(api_client)
    device_id = 'device_id_example' # str | ID of the device. Using the device's `nodeId` is preferred, but its numeric `id` value can also be used. 
    set_device_name_request = tailscale_openapi.SetDeviceNameRequest() # SetDeviceNameRequest |  (optional)

    try:
        # Set device name
        api_instance.set_device_name(device_id, set_device_name_request=set_device_name_request)
    except Exception as e:
        print("Exception when calling DevicesApi->set_device_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| ID of the device. Using the device&#39;s &#x60;nodeId&#x60; is preferred, but its numeric &#x60;id&#x60; value can also be used.  | 
 **set_device_name_request** | [**SetDeviceNameRequest**](SetDeviceNameRequest.md)|  | [optional] 

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
**404** | Device not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_device_routes**
> DeviceRoutes set_device_routes(device_id, set_device_routes_request)

Set device routes

Set a device's enabled subnet routes by replacing the existing list of subnet routes with the supplied parameters. [Advertised routes](/kb/1019/subnets#advertise-subnet-routes) cannot be set through the API, since they must be set directly on the device.  Routes must be both advertised and enabled for a device to act as a subnet router or exit node. If a device has advertised routes, they are not exposed to traffic until they are enabled. Conversely, if routes are enabled before they are advertised, they are not available for routing until the device in question has advertised them.  Learn more about [subnet routers](/kb/1019/subnets) and [exit nodes](/kb/1103/exit-nodes).  OAuth Scope: `devices:routes`. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.device_routes import DeviceRoutes
from tailscale_openapi.models.set_device_routes_request import SetDeviceRoutesRequest
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
    api_instance = tailscale_openapi.DevicesApi(api_client)
    device_id = 'device_id_example' # str | ID of the device. Using the device's `nodeId` is preferred, but its numeric `id` value can also be used. 
    set_device_routes_request = tailscale_openapi.SetDeviceRoutesRequest() # SetDeviceRoutesRequest | 

    try:
        # Set device routes
        api_response = api_instance.set_device_routes(device_id, set_device_routes_request)
        print("The response of DevicesApi->set_device_routes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->set_device_routes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| ID of the device. Using the device&#39;s &#x60;nodeId&#x60; is preferred, but its numeric &#x60;id&#x60; value can also be used.  | 
 **set_device_routes_request** | [**SetDeviceRoutesRequest**](SetDeviceRoutesRequest.md)|  | 

### Return type

[**DeviceRoutes**](DeviceRoutes.md)

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

# **set_device_tags**
> set_device_tags(device_id, set_device_tags_request=set_device_tags_request)

Set device tags

Tags let you assign an identity to a device that is separate from human users, and use that identity as part of an ACL to restrict access. Tags are similar to role accounts, but more flexible.  Tags are created in the tailnet policy file by defining the tag and an owner of the tag. Once a device is tagged, the tag is the owner of that device. A single node can have multiple tags assigned.  Consult the policy file for your tailnet in the [admin console](https://login.tailscale.com/admin/acls) for the list of tags that have been created for your tailnet. Learn more about [tags](https://tailscale.com/kb/1068/).  OAuth Scope: `devices:core`. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.set_device_tags_request import SetDeviceTagsRequest
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
    api_instance = tailscale_openapi.DevicesApi(api_client)
    device_id = 'device_id_example' # str | ID of the device. Using the device's `nodeId` is preferred, but its numeric `id` value can also be used. 
    set_device_tags_request = tailscale_openapi.SetDeviceTagsRequest() # SetDeviceTagsRequest |  (optional)

    try:
        # Set device tags
        api_instance.set_device_tags(device_id, set_device_tags_request=set_device_tags_request)
    except Exception as e:
        print("Exception when calling DevicesApi->set_device_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| ID of the device. Using the device&#39;s &#x60;nodeId&#x60; is preferred, but its numeric &#x60;id&#x60; value can also be used.  | 
 **set_device_tags_request** | [**SetDeviceTagsRequest**](SetDeviceTagsRequest.md)|  | [optional] 

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
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_key**
> update_device_key(device_id, update_device_key_request=update_device_key_request)

Update device key

When a device is added to a tailnet, its key expiry is set according to the tailnet's key expiry setting. If the key is not refreshed and expires, the device can no longer communicate with other devices in the tailnet.  OAuth Scope: `devices:core`. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.update_device_key_request import UpdateDeviceKeyRequest
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
    api_instance = tailscale_openapi.DevicesApi(api_client)
    device_id = 'device_id_example' # str | ID of the device. Using the device's `nodeId` is preferred, but its numeric `id` value can also be used. 
    update_device_key_request = tailscale_openapi.UpdateDeviceKeyRequest() # UpdateDeviceKeyRequest |  (optional)

    try:
        # Update device key
        api_instance.update_device_key(device_id, update_device_key_request=update_device_key_request)
    except Exception as e:
        print("Exception when calling DevicesApi->update_device_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| ID of the device. Using the device&#39;s &#x60;nodeId&#x60; is preferred, but its numeric &#x60;id&#x60; value can also be used.  | 
 **update_device_key_request** | [**UpdateDeviceKeyRequest**](UpdateDeviceKeyRequest.md)|  | [optional] 

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
**404** | Device not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

