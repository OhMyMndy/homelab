# tailscale_openapi.DevicePostureApi

All URIs are relative to *https://api.tailscale.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_posture_integration**](DevicePostureApi.md#create_posture_integration) | **POST** /tailnet/{tailnet}/posture/integrations | Create a posture integration
[**delete_posture_integration**](DevicePostureApi.md#delete_posture_integration) | **DELETE** /posture/integrations/{id} | Delete a posture integration
[**get_posture_integration**](DevicePostureApi.md#get_posture_integration) | **GET** /posture/integrations/{id} | Get a posture integration
[**get_posture_integrations**](DevicePostureApi.md#get_posture_integrations) | **GET** /tailnet/{tailnet}/posture/integrations | List all posture integrations
[**update_posture_integration**](DevicePostureApi.md#update_posture_integration) | **PATCH** /posture/integrations/{id} | Update a posture integration


# **create_posture_integration**
> PostureIntegration create_posture_integration(tailnet, posture_integration=posture_integration)

Create a posture integration

Create a posture integration, returning the resulting [PostureIntegration](#model/postureintegration).  Must include `provider` and `clientSecret`.  Currently, only one integration for each provider is supported.  OAuth Scope: `feature_settings`. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.posture_integration import PostureIntegration
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
    api_instance = tailscale_openapi.DevicePostureApi(api_client)
    tailnet = 'example.com' # str | The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (`-`) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/-/...\"   ```  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \"tailnet name\" found in the DNS tab).    For example, if your organization name is `alice@example.com`, your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\"   ```    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name). 
    posture_integration = {"provider":"intune","cloudId":"global","clientId":"93013672-b00c-4344-80ca-7ecf74f9dce1","tenantId":"d1ae389b-5207-43a2-afca-2de6b03ac7e3","clientSecret":"as32598d#@%asdf"} # PostureIntegration |  (optional)

    try:
        # Create a posture integration
        api_response = api_instance.create_posture_integration(tailnet, posture_integration=posture_integration)
        print("The response of DevicePostureApi->create_posture_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicePostureApi->create_posture_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tailnet** | **str**| The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (&#x60;-&#x60;) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/-/...\&quot;   &#x60;&#x60;&#x60;  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \&quot;tailnet name\&quot; found in the DNS tab).    For example, if your organization name is &#x60;alice@example.com&#x60;, your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\&quot;   &#x60;&#x60;&#x60;    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name).  | 
 **posture_integration** | [**PostureIntegration**](PostureIntegration.md)|  | [optional] 

### Return type

[**PostureIntegration**](PostureIntegration.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**403** | User does not have sufficient access to create posture integrations. |  -  |
**409** | A posture integration for the same provider already exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_posture_integration**
> delete_posture_integration(id)

Delete a posture integration

Delete a specific posture integration.  OAuth Scope: `feature_settings`. 

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
    api_instance = tailscale_openapi.DevicePostureApi(api_client)
    id = 'p56wQiqrn7mfKTM59' # str | Unique identifier for a posture integration.

    try:
        # Delete a posture integration
        api_instance.delete_posture_integration(id)
    except Exception as e:
        print("Exception when calling DevicePostureApi->delete_posture_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for a posture integration. | 

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
**403** | User does not have sufficient access to delete this posture integration. |  -  |
**404** | Posture integration not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_posture_integration**
> PostureIntegration get_posture_integration(id)

Get a posture integration

Gets the posture integration identified by `{id}`.  OAuth Scope: `feature_settings:read`. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.posture_integration import PostureIntegration
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
    api_instance = tailscale_openapi.DevicePostureApi(api_client)
    id = 'p56wQiqrn7mfKTM59' # str | Unique identifier for a posture integration.

    try:
        # Get a posture integration
        api_response = api_instance.get_posture_integration(id)
        print("The response of DevicePostureApi->get_posture_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicePostureApi->get_posture_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for a posture integration. | 

### Return type

[**PostureIntegration**](PostureIntegration.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**404** | Posture integration not found, or user is not authorized to read it. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_posture_integrations**
> GetPostureIntegrations200Response get_posture_integrations(tailnet)

List all posture integrations

List all of the posture integrations for a tailnet.  OAuth Scope: `feature_settings:read`. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.get_posture_integrations200_response import GetPostureIntegrations200Response
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
    api_instance = tailscale_openapi.DevicePostureApi(api_client)
    tailnet = 'example.com' # str | The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (`-`) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/-/...\"   ```  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \"tailnet name\" found in the DNS tab).    For example, if your organization name is `alice@example.com`, your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\"   ```    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name). 

    try:
        # List all posture integrations
        api_response = api_instance.get_posture_integrations(tailnet)
        print("The response of DevicePostureApi->get_posture_integrations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicePostureApi->get_posture_integrations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tailnet** | **str**| The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (&#x60;-&#x60;) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/-/...\&quot;   &#x60;&#x60;&#x60;  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \&quot;tailnet name\&quot; found in the DNS tab).    For example, if your organization name is &#x60;alice@example.com&#x60;, your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\&quot;   &#x60;&#x60;&#x60;    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name).  | 

### Return type

[**GetPostureIntegrations200Response**](GetPostureIntegrations200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**403** | User does not have sufficient access to list posture integrations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_posture_integration**
> PostureIntegration update_posture_integration(id, posture_integration=posture_integration)

Update a posture integration

Updates the posture integration identified by `{id}`. You may omit the `clientSecret` from your request to retain the previously configured `clientSecret`.  OAuth Scope: `feature_settings`. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.posture_integration import PostureIntegration
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
    api_instance = tailscale_openapi.DevicePostureApi(api_client)
    id = 'p56wQiqrn7mfKTM59' # str | Unique identifier for a posture integration.
    posture_integration = {"cloudId":"global","clientId":"93013672-b00c-4344-80ca-7ecf74f9dce1","tenantId":"d1ae389b-5207-43a2-afca-2de6b03ac7e3","clientSecret":"as32598d#@%asdf"} # PostureIntegration |  (optional)

    try:
        # Update a posture integration
        api_response = api_instance.update_posture_integration(id, posture_integration=posture_integration)
        print("The response of DevicePostureApi->update_posture_integration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicePostureApi->update_posture_integration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for a posture integration. | 
 **posture_integration** | [**PostureIntegration**](PostureIntegration.md)|  | [optional] 

### Return type

[**PostureIntegration**](PostureIntegration.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**403** | User does not have sufficient access to update this posture integration. |  -  |
**404** | Posture integration not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

