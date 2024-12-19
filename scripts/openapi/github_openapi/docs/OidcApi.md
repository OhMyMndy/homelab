# github_openapi.OidcApi

All URIs are relative to *https://api.github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oidc_get_oidc_custom_sub_template_for_org**](OidcApi.md#oidc_get_oidc_custom_sub_template_for_org) | **GET** /orgs/{org}/actions/oidc/customization/sub | Get the customization template for an OIDC subject claim for an organization
[**oidc_update_oidc_custom_sub_template_for_org**](OidcApi.md#oidc_update_oidc_custom_sub_template_for_org) | **PUT** /orgs/{org}/actions/oidc/customization/sub | Set the customization template for an OIDC subject claim for an organization


# **oidc_get_oidc_custom_sub_template_for_org**
> OidcCustomSub oidc_get_oidc_custom_sub_template_for_org(org)

Get the customization template for an OIDC subject claim for an organization

Gets the customization template for an OpenID Connect (OIDC) subject claim.  OAuth app tokens and personal access tokens (classic) need the `read:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.oidc_custom_sub import OidcCustomSub
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
    api_instance = github_openapi.OidcApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.

    try:
        # Get the customization template for an OIDC subject claim for an organization
        api_response = api_instance.oidc_get_oidc_custom_sub_template_for_org(org)
        print("The response of OidcApi->oidc_get_oidc_custom_sub_template_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OidcApi->oidc_get_oidc_custom_sub_template_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 

### Return type

[**OidcCustomSub**](OidcCustomSub.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON serialized template for OIDC subject claim customization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oidc_update_oidc_custom_sub_template_for_org**
> object oidc_update_oidc_custom_sub_template_for_org(org, oidc_custom_sub)

Set the customization template for an OIDC subject claim for an organization

Creates or updates the customization template for an OpenID Connect (OIDC) subject claim.  OAuth app tokens and personal access tokens (classic) need the `write:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.oidc_custom_sub import OidcCustomSub
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
    api_instance = github_openapi.OidcApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    oidc_custom_sub = github_openapi.OidcCustomSub() # OidcCustomSub | 

    try:
        # Set the customization template for an OIDC subject claim for an organization
        api_response = api_instance.oidc_update_oidc_custom_sub_template_for_org(org, oidc_custom_sub)
        print("The response of OidcApi->oidc_update_oidc_custom_sub_template_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OidcApi->oidc_update_oidc_custom_sub_template_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **oidc_custom_sub** | [**OidcCustomSub**](OidcCustomSub.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Empty response |  -  |
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

