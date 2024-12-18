# tailscale_openapi.PolicyFileApi

All URIs are relative to *https://api.tailscale.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_policy_file**](PolicyFileApi.md#get_policy_file) | **GET** /tailnet/{tailnet}/acl | Get policy file
[**preview_rule_matches**](PolicyFileApi.md#preview_rule_matches) | **POST** /tailnet/{tailnet}/acl/preview | Preview rule matches
[**set_policy_file**](PolicyFileApi.md#set_policy_file) | **POST** /tailnet/{tailnet}/acl | Set policy file
[**validate_and_test_policy_file**](PolicyFileApi.md#validate_and_test_policy_file) | **POST** /tailnet/{tailnet}/acl/validate | Validate and test policy file


# **get_policy_file**
> object get_policy_file(tailnet, details=details, accept=accept)

Get policy file

Retrieves the current policy file for the given tailnet;  this includes the ACL along with the rules and tests that have been defined.  This method can return the policy file as JSON or HuJSON, depending on the Accept header. The response also includes an `ETag` header, which can be optionally included when [setting the policy file](#tag/policyfile/post/tailnet/{tailnet}/acl) to avoid missed updates.  Learn more about [policy file ACL syntax](https://tailscale.com/kb/1337/acl-syntax).  OAuth Scope: `policy_file:read`. 

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
    api_instance = tailscale_openapi.PolicyFileApi(api_client)
    tailnet = 'example.com' # str | The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (`-`) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/-/...\"   ```  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \"tailnet name\" found in the DNS tab).    For example, if your organization name is `alice@example.com`, your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\"   ```    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name). 
    details = True # bool | Request a detailed description of the tailnet policy file by providing `details=true` in the URL query string. Supplying any other value for `details`, or not sending the param, is treated as sending `details=false`. If using this, do not supply an `Accept` parameter in the header.  The response will contain a JSON object with the fields: - `acl`: a base64-encoded string representation of the huJSON format. - `warnings`: array of strings for syntactically valid but nonsensical entries. - `errors`: an array of strings for parsing failures.  (optional)
    accept = 'accept_example' # str | Response is encoded as JSON if `application/json` is requested, otherwise HuJSON will be returned. (optional)

    try:
        # Get policy file
        api_response = api_instance.get_policy_file(tailnet, details=details, accept=accept)
        print("The response of PolicyFileApi->get_policy_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyFileApi->get_policy_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tailnet** | **str**| The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (&#x60;-&#x60;) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/-/...\&quot;   &#x60;&#x60;&#x60;  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \&quot;tailnet name\&quot; found in the DNS tab).    For example, if your organization name is &#x60;alice@example.com&#x60;, your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\&quot;   &#x60;&#x60;&#x60;    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name).  | 
 **details** | **bool**| Request a detailed description of the tailnet policy file by providing &#x60;details&#x3D;true&#x60; in the URL query string. Supplying any other value for &#x60;details&#x60;, or not sending the param, is treated as sending &#x60;details&#x3D;false&#x60;. If using this, do not supply an &#x60;Accept&#x60; parameter in the header.  The response will contain a JSON object with the fields: - &#x60;acl&#x60;: a base64-encoded string representation of the huJSON format. - &#x60;warnings&#x60;: array of strings for syntactically valid but nonsensical entries. - &#x60;errors&#x60;: an array of strings for parsing failures.  | [optional] 
 **accept** | **str**| Response is encoded as JSON if &#x60;application/json&#x60; is requested, otherwise HuJSON will be returned. | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/hujson

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** |  |  -  |
**403** |  |  -  |
**404** | Tailnet not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_rule_matches**
> PreviewRuleMatches200Response preview_rule_matches(tailnet, type, preview_for, body=body)

Preview rule matches

When given a user or IP port to match against, returns the tailnet policy rules that apply to that resource, without saving the policy file to the server. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.preview_rule_matches200_response import PreviewRuleMatches200Response
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
    api_instance = tailscale_openapi.PolicyFileApi(api_client)
    tailnet = 'example.com' # str | The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (`-`) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/-/...\"   ```  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \"tailnet name\" found in the DNS tab).    For example, if your organization name is `alice@example.com`, your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\"   ```    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name). 
    type = 'user' # str | Specify for which type of resource (user or IP port) matching rules are to be fetched. Read about [previewing changes in the admin console](https://tailscale.com/kb/1018/#previewing-changes).  OAuth Scope: `policy_file:read`. 
    preview_for = '10.0.0.1:80' # str | - If `type` is `user`, provide the email of a valid user with registered machines. - If `type` is `ipport`, provide an IP address + port: `10.0.0.1:80`.  The supplied policy file is queried with this parameter to determine which rules match. 
    body = None # object |  (optional)

    try:
        # Preview rule matches
        api_response = api_instance.preview_rule_matches(tailnet, type, preview_for, body=body)
        print("The response of PolicyFileApi->preview_rule_matches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyFileApi->preview_rule_matches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tailnet** | **str**| The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (&#x60;-&#x60;) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/-/...\&quot;   &#x60;&#x60;&#x60;  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \&quot;tailnet name\&quot; found in the DNS tab).    For example, if your organization name is &#x60;alice@example.com&#x60;, your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\&quot;   &#x60;&#x60;&#x60;    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name).  | 
 **type** | **str**| Specify for which type of resource (user or IP port) matching rules are to be fetched. Read about [previewing changes in the admin console](https://tailscale.com/kb/1018/#previewing-changes).  OAuth Scope: &#x60;policy_file:read&#x60;.  | 
 **preview_for** | **str**| - If &#x60;type&#x60; is &#x60;user&#x60;, provide the email of a valid user with registered machines. - If &#x60;type&#x60; is &#x60;ipport&#x60;, provide an IP address + port: &#x60;10.0.0.1:80&#x60;.  The supplied policy file is queried with this parameter to determine which rules match.  | 
 **body** | **object**|  | [optional] 

### Return type

[**PreviewRuleMatches200Response**](PreviewRuleMatches200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/hujson
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of rules that apply to the resource. |  -  |
**400** |  |  -  |
**403** |  |  -  |
**404** | Tailnet not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_policy_file**
> object set_policy_file(tailnet, if_match=if_match, accept=accept, body=body)

Set policy file

Sets the ACL for the given tailnet. HuJSON and JSON are both accepted inputs. An `If-Match` header can be set to avoid missed updates.  On success, returns the updated ACL in JSON or HuJSON according to the `Accept` header. Otherwise, errors are returned for incorrectly defined ACLs, ACLs with failing tests on attempted updates, and mismatched `If-Match` header and `ETag`.  Learn more about [policy file ACL syntax](https://tailscale.com/kb/1337/acl-syntax).  OAuth Scope: `policy_file`. 

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
    api_instance = tailscale_openapi.PolicyFileApi(api_client)
    tailnet = 'example.com' # str | The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (`-`) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/-/...\"   ```  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \"tailnet name\" found in the DNS tab).    For example, if your organization name is `alice@example.com`, your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\"   ```    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name). 
    if_match = 'if_match_example' # str | This is a safety mechanism to avoid overwriting other users' updates to the tailnet policy file.  - Set the `If-Match` value to that of the `ETag` header returned in a `GET` request to `/api/v2/tailnet/{tailnet}/acl`.   Tailscale compares the `ETag` value in your request to that of the current tailnet file and only replaces the file if there's a match.   (A mismatch indicates that another update has been made to the file.) For example: `-H \"If-Match: \\\"e0b2816b418\\\"\"`. - Alternately, set the `If-Match` value to `ts-default` to ensure that the policy file is replaced *only if the current policy file is still the untouched default created automatically* for each tailnet.   For example: `-H \"If-Match: \\\"ts-default\\\"\"`.  (optional)
    accept = 'accept_example' # str | Response is encoded as JSON if `application/json` is requested, otherwise HuJSON will be returned. (optional)
    body = None # object |  (optional)

    try:
        # Set policy file
        api_response = api_instance.set_policy_file(tailnet, if_match=if_match, accept=accept, body=body)
        print("The response of PolicyFileApi->set_policy_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyFileApi->set_policy_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tailnet** | **str**| The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (&#x60;-&#x60;) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/-/...\&quot;   &#x60;&#x60;&#x60;  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \&quot;tailnet name\&quot; found in the DNS tab).    For example, if your organization name is &#x60;alice@example.com&#x60;, your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\&quot;   &#x60;&#x60;&#x60;    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name).  | 
 **if_match** | **str**| This is a safety mechanism to avoid overwriting other users&#39; updates to the tailnet policy file.  - Set the &#x60;If-Match&#x60; value to that of the &#x60;ETag&#x60; header returned in a &#x60;GET&#x60; request to &#x60;/api/v2/tailnet/{tailnet}/acl&#x60;.   Tailscale compares the &#x60;ETag&#x60; value in your request to that of the current tailnet file and only replaces the file if there&#39;s a match.   (A mismatch indicates that another update has been made to the file.) For example: &#x60;-H \&quot;If-Match: \\\&quot;e0b2816b418\\\&quot;\&quot;&#x60;. - Alternately, set the &#x60;If-Match&#x60; value to &#x60;ts-default&#x60; to ensure that the policy file is replaced *only if the current policy file is still the untouched default created automatically* for each tailnet.   For example: &#x60;-H \&quot;If-Match: \\\&quot;ts-default\\\&quot;\&quot;&#x60;.  | [optional] 
 **accept** | **str**| Response is encoded as JSON if &#x60;application/json&#x60; is requested, otherwise HuJSON will be returned. | [optional] 
 **body** | **object**|  | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/hujson
 - **Accept**: application/json, application/hujson

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation. |  -  |
**400** | ACL validation or test error. |  -  |
**403** |  |  -  |
**404** | Tailnet not found. |  -  |
**412** | If-Match hash mismatch. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_and_test_policy_file**
> ValidateAndTestPolicyFile200Response validate_and_test_policy_file(tailnet, validate_and_test_policy_file_request=validate_and_test_policy_file_request)

Validate and test policy file

This endpoint works in one of two modes, neither of which modifies your current tailnet policy file:  - Run ACL tests: When the request body contains ACL tests as a JSON array,   Tailscale runs ACL tests against the tailnet's current policy file.   Learn more about [ACL tests](https://tailscale.com/kb/1337/acl-syntax#tests). - Validate a new policy file: When the request body is a JSON object,   Tailscale interprets the body as a hypothetical new tailnet policy file with new ACLs,   including any new rules and tests.   It validates that the policy file is parsable and runs tests to validate the existing rules.  In either case, this method does not modify the tailnet policy file in any way.  OAuth Scope: `policy_file:read`. 

### Example

* Bearer Authentication (bearerAuth):

```python
import tailscale_openapi
from tailscale_openapi.models.validate_and_test_policy_file200_response import ValidateAndTestPolicyFile200Response
from tailscale_openapi.models.validate_and_test_policy_file_request import ValidateAndTestPolicyFileRequest
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
    api_instance = tailscale_openapi.PolicyFileApi(api_client)
    tailnet = 'example.com' # str | The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (`-`) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/-/...\"   ```  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \"tailnet name\" found in the DNS tab).    For example, if your organization name is `alice@example.com`, your API calls would start:    ```sh   curl \"https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\"   ```    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name). 
    validate_and_test_policy_file_request = [{"src":"user1@example.com","accept":["example-host-1:22"],"deny":["example-host-2:100"]}] # ValidateAndTestPolicyFileRequest |  (optional)

    try:
        # Validate and test policy file
        api_response = api_instance.validate_and_test_policy_file(tailnet, validate_and_test_policy_file_request=validate_and_test_policy_file_request)
        print("The response of PolicyFileApi->validate_and_test_policy_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyFileApi->validate_and_test_policy_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tailnet** | **str**| The tailnet organization name.  When specifying a tailnet in the API, you can:  - Provide a dash (&#x60;-&#x60;) to reference the default tailnet of the access token being used to make the API call.   This is the best option for most users.   Your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/-/...\&quot;   &#x60;&#x60;&#x60;  - Provide the **organization** name found on the **[General Settings](https://login.tailscale.com/admin/settings/general)**   page of the Tailscale admin console (not to be confused with the \&quot;tailnet name\&quot; found in the DNS tab).    For example, if your organization name is &#x60;alice@example.com&#x60;, your API calls would start:    &#x60;&#x60;&#x60;sh   curl \&quot;https://api.tailscale.com/api/v2/tailnet/alice@example.com/...\&quot;   &#x60;&#x60;&#x60;    Learn more about [tailnet organization names](https://tailscale.com/kb/1217/tailnet-name#organization-name).  | 
 **validate_and_test_policy_file_request** | [**ValidateAndTestPolicyFileRequest**](ValidateAndTestPolicyFileRequest.md)|  | [optional] 

### Return type

[**ValidateAndTestPolicyFile200Response**](ValidateAndTestPolicyFile200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/husjon
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Validation or tests have run. An empty response body implies passing validation or tests. |  -  |
**400** |  |  -  |
**403** |  |  -  |
**404** | Tailnet not found. |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

