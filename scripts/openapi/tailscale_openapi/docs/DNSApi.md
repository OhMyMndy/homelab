# tailscale_openapi.DNSApi

All URIs are relative to *https://api.tailscale.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dns_preferences**](DNSApi.md#get_dns_preferences) | **GET** /tailnet/{tailnet}/dns/preferences | Get DNS preferences
[**get_split_dns**](DNSApi.md#get_split_dns) | **GET** /tailnet/{tailnet}/dns/split-dns | Get split DNS
[**list_dns_nameservers**](DNSApi.md#list_dns_nameservers) | **GET** /tailnet/{tailnet}/dns/nameservers | List DNS nameservers
[**list_dns_search_paths**](DNSApi.md#list_dns_search_paths) | **GET** /tailnet/{tailnet}/dns/searchpaths | List DNS search paths
[**set_dns_nameservers**](DNSApi.md#set_dns_nameservers) | **POST** /tailnet/{tailnet}/dns/nameservers | Set DNS nameservers
[**set_dns_preferences**](DNSApi.md#set_dns_preferences) | **POST** /tailnet/{tailnet}/dns/preferences | Set DNS preferences
[**set_dns_search_paths**](DNSApi.md#set_dns_search_paths) | **POST** /tailnet/{tailnet}/dns/searchpaths | Set DNS search paths
[**set_split_dns**](DNSApi.md#set_split_dns) | **PUT** /tailnet/{tailnet}/dns/split-dns | Set split DNS
[**update_split_dns**](DNSApi.md#update_split_dns) | **PATCH** /tailnet/{tailnet}/dns/split-dns | Update split DNS


# **get_dns_preferences**
> DnsPreferences get_dns_preferences(tailnet)

Get DNS preferences

Retrieves the DNS preferences that are currently set for the given tailnet. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.dns_preferences import DnsPreferences
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
    api_instance = tailscale_openapi.DNSApi(api_client)
    tailnet = 'example.com' # str | The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (`-`) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/-/...\"   ```  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \"tailnet name\" found in the DNS tab).    For example, if your organization name is `alice@example.com`, your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\"   ```    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name). 

    try:
        # Get DNS preferences
        api_response = api_instance.get_dns_preferences(tailnet)
        print("The response of DNSApi->get_dns_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->get_dns_preferences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tailnet** | **str**| The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (&#x60;-&#x60;) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/-/...\&quot;   &#x60;&#x60;&#x60;  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \&quot;tailnet name\&quot; found in the DNS tab).    For example, if your organization name is &#x60;alice@example.com&#x60;, your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\&quot;   &#x60;&#x60;&#x60;    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name).  | 

### Return type

[**DnsPreferences**](DnsPreferences.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succesful operation. |  -  |
**404** | Tailnet not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_split_dns**
> Dict[str, Optional[List[str]]] get_split_dns(tailnet)

Get split DNS

Retrieves the split DNS settings, which is a map from domains to lists of nameservers, that is currently set for the given tailnet. 

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
    api_instance = tailscale_openapi.DNSApi(api_client)
    tailnet = 'example.com' # str | The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (`-`) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/-/...\"   ```  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \"tailnet name\" found in the DNS tab).    For example, if your organization name is `alice@example.com`, your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\"   ```    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name). 

    try:
        # Get split DNS
        api_response = api_instance.get_split_dns(tailnet)
        print("The response of DNSApi->get_split_dns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->get_split_dns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tailnet** | **str**| The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (&#x60;-&#x60;) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/-/...\&quot;   &#x60;&#x60;&#x60;  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \&quot;tailnet name\&quot; found in the DNS tab).    For example, if your organization name is &#x60;alice@example.com&#x60;, your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\&quot;   &#x60;&#x60;&#x60;    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name).  | 

### Return type

**Dict[str, Optional[List[str]]]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succesful operation. |  -  |
**404** | Tailnet not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dns_nameservers**
> ListDnsNameservers200Response list_dns_nameservers(tailnet)

List DNS nameservers

Lists the global DNS nameservers for a tailnet. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.list_dns_nameservers200_response import ListDnsNameservers200Response
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
    api_instance = tailscale_openapi.DNSApi(api_client)
    tailnet = 'example.com' # str | The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (`-`) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/-/...\"   ```  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \"tailnet name\" found in the DNS tab).    For example, if your organization name is `alice@example.com`, your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\"   ```    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name). 

    try:
        # List DNS nameservers
        api_response = api_instance.list_dns_nameservers(tailnet)
        print("The response of DNSApi->list_dns_nameservers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->list_dns_nameservers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tailnet** | **str**| The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (&#x60;-&#x60;) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/-/...\&quot;   &#x60;&#x60;&#x60;  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \&quot;tailnet name\&quot; found in the DNS tab).    For example, if your organization name is &#x60;alice@example.com&#x60;, your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\&quot;   &#x60;&#x60;&#x60;    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name).  | 

### Return type

[**ListDnsNameservers200Response**](ListDnsNameservers200Response.md)

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

# **list_dns_search_paths**
> DnsSearchPaths list_dns_search_paths(tailnet)

List DNS search paths

Retrieves the list of search paths, also referred to as *search domains*, that is currently set for the given tailnet. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.dns_search_paths import DnsSearchPaths
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
    api_instance = tailscale_openapi.DNSApi(api_client)
    tailnet = 'example.com' # str | The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (`-`) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/-/...\"   ```  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \"tailnet name\" found in the DNS tab).    For example, if your organization name is `alice@example.com`, your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\"   ```    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name). 

    try:
        # List DNS search paths
        api_response = api_instance.list_dns_search_paths(tailnet)
        print("The response of DNSApi->list_dns_search_paths:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->list_dns_search_paths: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tailnet** | **str**| The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (&#x60;-&#x60;) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/-/...\&quot;   &#x60;&#x60;&#x60;  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \&quot;tailnet name\&quot; found in the DNS tab).    For example, if your organization name is &#x60;alice@example.com&#x60;, your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\&quot;   &#x60;&#x60;&#x60;    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name).  | 

### Return type

[**DnsSearchPaths**](DnsSearchPaths.md)

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

# **set_dns_nameservers**
> SetDnsNameservers200Response set_dns_nameservers(tailnet, list_dns_nameservers200_response=list_dns_nameservers200_response)

Set DNS nameservers

Replaces the list of global DNS nameservers for the given tailnet with the list supplied in the request.  Note that changing the list of DNS nameservers may also affect the status of MagicDNS (if MagicDNS is on; learn about [MagicDNS](https://tailscale.com/kb/1081)). If all nameservers have been removed, MagicDNS will be automatically disabled (until explicitly turned back on by the user). 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.list_dns_nameservers200_response import ListDnsNameservers200Response
from tailscale_openapi.models.set_dns_nameservers200_response import SetDnsNameservers200Response
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
    api_instance = tailscale_openapi.DNSApi(api_client)
    tailnet = 'example.com' # str | The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (`-`) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/-/...\"   ```  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \"tailnet name\" found in the DNS tab).    For example, if your organization name is `alice@example.com`, your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\"   ```    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name). 
    list_dns_nameservers200_response = tailscale_openapi.ListDnsNameservers200Response() # ListDnsNameservers200Response |  (optional)

    try:
        # Set DNS nameservers
        api_response = api_instance.set_dns_nameservers(tailnet, list_dns_nameservers200_response=list_dns_nameservers200_response)
        print("The response of DNSApi->set_dns_nameservers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->set_dns_nameservers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tailnet** | **str**| The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (&#x60;-&#x60;) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/-/...\&quot;   &#x60;&#x60;&#x60;  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \&quot;tailnet name\&quot; found in the DNS tab).    For example, if your organization name is &#x60;alice@example.com&#x60;, your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\&quot;   &#x60;&#x60;&#x60;    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name).  | 
 **list_dns_nameservers200_response** | [**ListDnsNameservers200Response**](ListDnsNameservers200Response.md)|  | [optional] 

### Return type

[**SetDnsNameservers200Response**](SetDnsNameservers200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succesful operation. |  -  |
**404** | Tailnet not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_dns_preferences**
> DnsPreferences set_dns_preferences(tailnet, dns_preferences=dns_preferences)

Set DNS preferences

Set the DNS preferences for a tailnet; specifically, the MagicDNS setting. Note that MagicDNS is dependent on DNS servers. Learn about [MagicDNS](https://tailscale.com/kb/1081).  If there is at least one DNS server, then MagicDNS can be enabled. Otherwise, it returns an error.  Note that removing all nameservers will turn off MagicDNS. To reenable it, nameservers must be added back, and MagicDNS must be explicitly turned on. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.dns_preferences import DnsPreferences
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
    api_instance = tailscale_openapi.DNSApi(api_client)
    tailnet = 'example.com' # str | The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (`-`) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/-/...\"   ```  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \"tailnet name\" found in the DNS tab).    For example, if your organization name is `alice@example.com`, your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\"   ```    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name). 
    dns_preferences = tailscale_openapi.DnsPreferences() # DnsPreferences |  (optional)

    try:
        # Set DNS preferences
        api_response = api_instance.set_dns_preferences(tailnet, dns_preferences=dns_preferences)
        print("The response of DNSApi->set_dns_preferences:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->set_dns_preferences: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tailnet** | **str**| The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (&#x60;-&#x60;) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/-/...\&quot;   &#x60;&#x60;&#x60;  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \&quot;tailnet name\&quot; found in the DNS tab).    For example, if your organization name is &#x60;alice@example.com&#x60;, your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\&quot;   &#x60;&#x60;&#x60;    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name).  | 
 **dns_preferences** | [**DnsPreferences**](DnsPreferences.md)|  | [optional] 

### Return type

[**DnsPreferences**](DnsPreferences.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succesful operation. |  -  |
**404** | Tailnet not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_dns_search_paths**
> DnsSearchPaths set_dns_search_paths(tailnet, dns_search_paths=dns_search_paths)

Set DNS search paths

Replaces the list of search paths for the given tailnet. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.dns_search_paths import DnsSearchPaths
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
    api_instance = tailscale_openapi.DNSApi(api_client)
    tailnet = 'example.com' # str | The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (`-`) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/-/...\"   ```  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \"tailnet name\" found in the DNS tab).    For example, if your organization name is `alice@example.com`, your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\"   ```    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name). 
    dns_search_paths = tailscale_openapi.DnsSearchPaths() # DnsSearchPaths |  (optional)

    try:
        # Set DNS search paths
        api_response = api_instance.set_dns_search_paths(tailnet, dns_search_paths=dns_search_paths)
        print("The response of DNSApi->set_dns_search_paths:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->set_dns_search_paths: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tailnet** | **str**| The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (&#x60;-&#x60;) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/-/...\&quot;   &#x60;&#x60;&#x60;  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \&quot;tailnet name\&quot; found in the DNS tab).    For example, if your organization name is &#x60;alice@example.com&#x60;, your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\&quot;   &#x60;&#x60;&#x60;    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name).  | 
 **dns_search_paths** | [**DnsSearchPaths**](DnsSearchPaths.md)|  | [optional] 

### Return type

[**DnsSearchPaths**](DnsSearchPaths.md)

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

# **set_split_dns**
> Dict[str, Optional[List[str]]] set_split_dns(tailnet, request_body=request_body)

Set split DNS

Replaces the split DNS settings for a given tailnet. Setting the value of a mapping to `null` clears the nameservers for that domain. Sending an empty object clears nameservers for all domains. 

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
    api_instance = tailscale_openapi.DNSApi(api_client)
    tailnet = 'example.com' # str | The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (`-`) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/-/...\"   ```  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \"tailnet name\" found in the DNS tab).    For example, if your organization name is `alice@example.com`, your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\"   ```    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name). 
    request_body = None # Dict[str, Optional[List[str]]] |  (optional)

    try:
        # Set split DNS
        api_response = api_instance.set_split_dns(tailnet, request_body=request_body)
        print("The response of DNSApi->set_split_dns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->set_split_dns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tailnet** | **str**| The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (&#x60;-&#x60;) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/-/...\&quot;   &#x60;&#x60;&#x60;  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \&quot;tailnet name\&quot; found in the DNS tab).    For example, if your organization name is &#x60;alice@example.com&#x60;, your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\&quot;   &#x60;&#x60;&#x60;    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name).  | 
 **request_body** | [**Dict[str, Optional[List[str]]]**](List.md)|  | [optional] 

### Return type

**Dict[str, Optional[List[str]]]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succesful operation. |  -  |
**404** | Tailnet not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_split_dns**
> Dict[str, Optional[List[str]]] update_split_dns(tailnet, request_body=request_body)

Update split DNS

Performs partial updates of the split DNS settings for a given tailnet. Only domains specified in the request map will be modified. Setting the value of a mapping to `null` clears the nameservers for that domain. 

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
    api_instance = tailscale_openapi.DNSApi(api_client)
    tailnet = 'example.com' # str | The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (`-`) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/-/...\"   ```  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \"tailnet name\" found in the DNS tab).    For example, if your organization name is `alice@example.com`, your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\"   ```    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name). 
    request_body = None # Dict[str, Optional[List[str]]] |  (optional)

    try:
        # Update split DNS
        api_response = api_instance.update_split_dns(tailnet, request_body=request_body)
        print("The response of DNSApi->update_split_dns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSApi->update_split_dns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tailnet** | **str**| The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (&#x60;-&#x60;) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/-/...\&quot;   &#x60;&#x60;&#x60;  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \&quot;tailnet name\&quot; found in the DNS tab).    For example, if your organization name is &#x60;alice@example.com&#x60;, your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\&quot;   &#x60;&#x60;&#x60;    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name).  | 
 **request_body** | [**Dict[str, Optional[List[str]]]**](List.md)|  | [optional] 

### Return type

**Dict[str, Optional[List[str]]]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Succesful operation. |  -  |
**404** | Tailnet not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

