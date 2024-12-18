# tailscale_openapi.LoggingApi

All URIs are relative to *https://api.tailscale.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disable_log_streaming**](LoggingApi.md#disable_log_streaming) | **DELETE** /tailnet/{tailnet}/logging/{logType}/stream | Disable log streaming
[**get_aws_external_id**](LoggingApi.md#get_aws_external_id) | **POST** /tailnet/{tailnet}/aws-external-id | Create or get AWS external id
[**get_log_streaming_configuration**](LoggingApi.md#get_log_streaming_configuration) | **GET** /tailnet/{tailnet}/logging/{logType}/stream | Get log streaming configuration
[**get_log_streaming_status**](LoggingApi.md#get_log_streaming_status) | **GET** /tailnet/{tailnet}/logging/{logType}/stream/status | Get log streaming status
[**list_configuration_audit_logs**](LoggingApi.md#list_configuration_audit_logs) | **GET** /tailnet/{tailnet}/logging/configuration | List configuration audit logs
[**list_network_flow_logs**](LoggingApi.md#list_network_flow_logs) | **GET** /tailnet/{tailnet}/logging/network | List network flow logs
[**set_log_streaming_configuration**](LoggingApi.md#set_log_streaming_configuration) | **PUT** /tailnet/{tailnet}/logging/{logType}/stream | Set log streaming configuration


# **disable_log_streaming**
> disable_log_streaming(tailnet, log_type)

Disable log streaming

Delete the log streaming configuration for the provided log type.  OAuth Scope: `log_streaming`. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.log_type import LogType
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
    api_instance = tailscale_openapi.LoggingApi(api_client)
    tailnet = 'example.com' # str | The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (`-`) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/-/...\"   ```  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \"tailnet name\" found in the DNS tab).    For example, if your organization name is `alice@example.com`, your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\"   ```    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name). 
    log_type = tailscale_openapi.LogType() # LogType | The type of log.

    try:
        # Disable log streaming
        api_instance.disable_log_streaming(tailnet, log_type)
    except Exception as e:
        print("Exception when calling LoggingApi->disable_log_streaming: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tailnet** | **str**| The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (&#x60;-&#x60;) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/-/...\&quot;   &#x60;&#x60;&#x60;  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \&quot;tailnet name\&quot; found in the DNS tab).    For example, if your organization name is &#x60;alice@example.com&#x60;, your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\&quot;   &#x60;&#x60;&#x60;    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name).  | 
 **log_type** | [**LogType**](.md)| The type of log. | 

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
**403** | User does not have sufficient access to update log streaming configuration. |  -  |
**404** | Log streaming has not been configured, this &#x60;logType&#x60; is not supported, or user does not have sufficient access to view log streaming configuration. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aws_external_id**
> AwsExternalId get_aws_external_id(tailnet, get_aws_external_id_request=get_aws_external_id_request)

Create or get AWS external id

Get an AWS external id to use for streaming tailnet logs to S3 using role-based authentication, creating a new one for this tailnet when necessary.  OAuth Scope: `log_streaming`. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.aws_external_id import AwsExternalId
from tailscale_openapi.models.get_aws_external_id_request import GetAwsExternalIdRequest
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
    api_instance = tailscale_openapi.LoggingApi(api_client)
    tailnet = 'example.com' # str | The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (`-`) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/-/...\"   ```  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \"tailnet name\" found in the DNS tab).    For example, if your organization name is `alice@example.com`, your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\"   ```    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name). 
    get_aws_external_id_request = {"reusable":true} # GetAwsExternalIdRequest |  (optional)

    try:
        # Create or get AWS external id
        api_response = api_instance.get_aws_external_id(tailnet, get_aws_external_id_request=get_aws_external_id_request)
        print("The response of LoggingApi->get_aws_external_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoggingApi->get_aws_external_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tailnet** | **str**| The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (&#x60;-&#x60;) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/-/...\&quot;   &#x60;&#x60;&#x60;  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \&quot;tailnet name\&quot; found in the DNS tab).    For example, if your organization name is &#x60;alice@example.com&#x60;, your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\&quot;   &#x60;&#x60;&#x60;    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name).  | 
 **get_aws_external_id_request** | [**GetAwsExternalIdRequest**](GetAwsExternalIdRequest.md)|  | [optional] 

### Return type

[**AwsExternalId**](AwsExternalId.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**403** | User does not have sufficient access to obtain an AWS external id. |  -  |
**404** | Tailnet not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_log_streaming_configuration**
> LogstreamEndpointConfiguration get_log_streaming_configuration(tailnet, log_type)

Get log streaming configuration

Retrieve the log streaming configuration for the provided log type.  OAuth Scope: `log_streaming:read`. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.log_type import LogType
from tailscale_openapi.models.logstream_endpoint_configuration import LogstreamEndpointConfiguration
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
    api_instance = tailscale_openapi.LoggingApi(api_client)
    tailnet = 'example.com' # str | The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (`-`) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/-/...\"   ```  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \"tailnet name\" found in the DNS tab).    For example, if your organization name is `alice@example.com`, your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\"   ```    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name). 
    log_type = tailscale_openapi.LogType() # LogType | The type of log.

    try:
        # Get log streaming configuration
        api_response = api_instance.get_log_streaming_configuration(tailnet, log_type)
        print("The response of LoggingApi->get_log_streaming_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoggingApi->get_log_streaming_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tailnet** | **str**| The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (&#x60;-&#x60;) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/-/...\&quot;   &#x60;&#x60;&#x60;  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \&quot;tailnet name\&quot; found in the DNS tab).    For example, if your organization name is &#x60;alice@example.com&#x60;, your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\&quot;   &#x60;&#x60;&#x60;    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name).  | 
 **log_type** | [**LogType**](.md)| The type of log. | 

### Return type

[**LogstreamEndpointConfiguration**](LogstreamEndpointConfiguration.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**404** | Log streaming has not been configured, this &#x60;logType&#x60; is not supported, or user does not have sufficient access to view log streaming configuration. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_log_streaming_status**
> LogstreamEndpointPublishingStatus get_log_streaming_status(tailnet, log_type)

Get log streaming status

Retrieve the log streaming status for the provided log type.  OAuth Scope: `log_streaming:read`. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.log_type import LogType
from tailscale_openapi.models.logstream_endpoint_publishing_status import LogstreamEndpointPublishingStatus
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
    api_instance = tailscale_openapi.LoggingApi(api_client)
    tailnet = 'example.com' # str | The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (`-`) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/-/...\"   ```  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \"tailnet name\" found in the DNS tab).    For example, if your organization name is `alice@example.com`, your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\"   ```    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name). 
    log_type = tailscale_openapi.LogType() # LogType | The type of log.

    try:
        # Get log streaming status
        api_response = api_instance.get_log_streaming_status(tailnet, log_type)
        print("The response of LoggingApi->get_log_streaming_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoggingApi->get_log_streaming_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tailnet** | **str**| The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (&#x60;-&#x60;) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/-/...\&quot;   &#x60;&#x60;&#x60;  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \&quot;tailnet name\&quot; found in the DNS tab).    For example, if your organization name is &#x60;alice@example.com&#x60;, your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\&quot;   &#x60;&#x60;&#x60;    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name).  | 
 **log_type** | [**LogType**](.md)| The type of log. | 

### Return type

[**LogstreamEndpointPublishingStatus**](LogstreamEndpointPublishingStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**404** | Log streaming has not been configured, this &#x60;logType&#x60; is not supported, or user does not have sufficient access to view log streaming status. |  -  |
**502** | The system was unable to communicate with logging server. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_configuration_audit_logs**
> ListConfigurationAuditLogs200Response list_configuration_audit_logs(tailnet, start, end, actor=actor, target=target, event=event)

List configuration audit logs

List all configuration audit logs for a tailnet.  OAuth Scope: `logs:configuration:read`. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.list_configuration_audit_logs200_response import ListConfigurationAuditLogs200Response
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
    api_instance = tailscale_openapi.LoggingApi(api_client)
    tailnet = 'example.com' # str | The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (`-`) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/-/...\"   ```  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \"tailnet name\" found in the DNS tab).    For example, if your organization name is `alice@example.com`, your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\"   ```    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name). 
    start = '2023-12-19T16:39:57-08:00' # str | The start of the time window for which to retrieve logs, in RFC 3339 format.
    end = '2023-12-22T02:15:23-08:00' # str | The end of the time window for which to retrieve logs, in RFC 3339 format.
    actor = ['[uc4p8fRHvJ11KTM59, ~bob]'] # List[str] | List of filters on actors, either exact actor IDs or a wildcard search on login name or display name indicated as `~search`. (optional)
    target = ['[mytarget1, sometarget2]'] # List[str] | List of target elements for which to filter, attempts to match any part of any of the targets to any of the given strings. (optional)
    event = ['[USER.CREATE, NODE.CREATE]'] # List[str] | List of events for which to filter. (optional)

    try:
        # List configuration audit logs
        api_response = api_instance.list_configuration_audit_logs(tailnet, start, end, actor=actor, target=target, event=event)
        print("The response of LoggingApi->list_configuration_audit_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoggingApi->list_configuration_audit_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tailnet** | **str**| The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (&#x60;-&#x60;) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/-/...\&quot;   &#x60;&#x60;&#x60;  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \&quot;tailnet name\&quot; found in the DNS tab).    For example, if your organization name is &#x60;alice@example.com&#x60;, your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\&quot;   &#x60;&#x60;&#x60;    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name).  | 
 **start** | **str**| The start of the time window for which to retrieve logs, in RFC 3339 format. | 
 **end** | **str**| The end of the time window for which to retrieve logs, in RFC 3339 format. | 
 **actor** | [**List[str]**](str.md)| List of filters on actors, either exact actor IDs or a wildcard search on login name or display name indicated as &#x60;~search&#x60;. | [optional] 
 **target** | [**List[str]**](str.md)| List of target elements for which to filter, attempts to match any part of any of the targets to any of the given strings. | [optional] 
 **event** | [**List[str]**](str.md)| List of events for which to filter. | [optional] 

### Return type

[**ListConfigurationAuditLogs200Response**](ListConfigurationAuditLogs200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** | Request has missing or invalid parameter(s). |  -  |
**403** | User does not have sufficient access to view configuration audit logs. |  -  |
**404** | Logging is not supported on this deployment of Tailscale. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_network_flow_logs**
> ListNetworkFlowLogs200Response list_network_flow_logs(tailnet, start, end)

List network flow logs

List all network flow logs for a tailnet.  OAuth Scope: `logs:network:read`. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.list_network_flow_logs200_response import ListNetworkFlowLogs200Response
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
    api_instance = tailscale_openapi.LoggingApi(api_client)
    tailnet = 'example.com' # str | The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (`-`) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/-/...\"   ```  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \"tailnet name\" found in the DNS tab).    For example, if your organization name is `alice@example.com`, your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\"   ```    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name). 
    start = '2023-12-19T16:39:57-08:00' # str | The start of the time window for which to retrieve logs, in RFC 3339 format.
    end = '2023-12-22T02:15:23-08:00' # str | The end of the time window for which to retrieve logs, in RFC 3339 format.

    try:
        # List network flow logs
        api_response = api_instance.list_network_flow_logs(tailnet, start, end)
        print("The response of LoggingApi->list_network_flow_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoggingApi->list_network_flow_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tailnet** | **str**| The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (&#x60;-&#x60;) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/-/...\&quot;   &#x60;&#x60;&#x60;  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \&quot;tailnet name\&quot; found in the DNS tab).    For example, if your organization name is &#x60;alice@example.com&#x60;, your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\&quot;   &#x60;&#x60;&#x60;    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name).  | 
 **start** | **str**| The start of the time window for which to retrieve logs, in RFC 3339 format. | 
 **end** | **str**| The end of the time window for which to retrieve logs, in RFC 3339 format. | 

### Return type

[**ListNetworkFlowLogs200Response**](ListNetworkFlowLogs200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. The &#x60;logs&#x60; field contains an array of [NetworkFlowLog](#model/networkflowlog) objects. |  -  |
**400** | Request has missing or invalid parameter(s). |  -  |
**403** | User does not have sufficient access to view network flow logs. |  -  |
**404** | Logging is not supported on this deployment of Tailscale. |  -  |
**502** | The system was unable to communicate with logging server. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_log_streaming_configuration**
> set_log_streaming_configuration(tailnet, log_type, logstream_endpoint_configuration=logstream_endpoint_configuration)

Set log streaming configuration

Set the log streaming configuration for the provided log type.  OAuth Scope: `log_streaming`. `device_invites` and `policy_file` are also required if streaming to a [private endpoint](https://tailscale.com/kb/1255/log-streaming#private-endpoints). 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.log_type import LogType
from tailscale_openapi.models.logstream_endpoint_configuration import LogstreamEndpointConfiguration
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
    api_instance = tailscale_openapi.LoggingApi(api_client)
    tailnet = 'example.com' # str | The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (`-`) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/-/...\"   ```  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \"tailnet name\" found in the DNS tab).    For example, if your organization name is `alice@example.com`, your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\"   ```    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name). 
    log_type = tailscale_openapi.LogType() # LogType | The type of log.
    logstream_endpoint_configuration = {"destinationType":"elastic","url":"http://100.71.134.73:80/config-log-datastream","user":"myusername","token":"mytoken"} # LogstreamEndpointConfiguration | The [LogstreamEndpointConfiguration](#model/logstreamendpointconfiguration) to set. `logType` is specified in the request URL rather than the body.  (optional)

    try:
        # Set log streaming configuration
        api_instance.set_log_streaming_configuration(tailnet, log_type, logstream_endpoint_configuration=logstream_endpoint_configuration)
    except Exception as e:
        print("Exception when calling LoggingApi->set_log_streaming_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tailnet** | **str**| The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (&#x60;-&#x60;) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/-/...\&quot;   &#x60;&#x60;&#x60;  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \&quot;tailnet name\&quot; found in the DNS tab).    For example, if your organization name is &#x60;alice@example.com&#x60;, your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\&quot;   &#x60;&#x60;&#x60;    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name).  | 
 **log_type** | [**LogType**](.md)| The type of log. | 
 **logstream_endpoint_configuration** | [**LogstreamEndpointConfiguration**](LogstreamEndpointConfiguration.md)| The [LogstreamEndpointConfiguration](#model/logstreamendpointconfiguration) to set. &#x60;logType&#x60; is specified in the request URL rather than the body.  | [optional] 

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
**400** | Request has missing or invalid parameter(s). |  -  |
**403** | User does not have sufficient access to update log streaming configuration. |  -  |
**404** | Tailnet not found, this &#x60;logType&#x60; is not supported, or user does not have sufficient access to view log streaming configuration. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

