# github_openapi.BillingApi

All URIs are relative to *https://api.github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billing_get_github_actions_billing_org**](BillingApi.md#billing_get_github_actions_billing_org) | **GET** /orgs/{org}/settings/billing/actions | Get GitHub Actions billing for an organization
[**billing_get_github_actions_billing_user**](BillingApi.md#billing_get_github_actions_billing_user) | **GET** /users/{username}/settings/billing/actions | Get GitHub Actions billing for a user
[**billing_get_github_billing_usage_report_org**](BillingApi.md#billing_get_github_billing_usage_report_org) | **GET** /organizations/{org}/settings/billing/usage | Get billing usage report for an organization
[**billing_get_github_packages_billing_org**](BillingApi.md#billing_get_github_packages_billing_org) | **GET** /orgs/{org}/settings/billing/packages | Get GitHub Packages billing for an organization
[**billing_get_github_packages_billing_user**](BillingApi.md#billing_get_github_packages_billing_user) | **GET** /users/{username}/settings/billing/packages | Get GitHub Packages billing for a user
[**billing_get_shared_storage_billing_org**](BillingApi.md#billing_get_shared_storage_billing_org) | **GET** /orgs/{org}/settings/billing/shared-storage | Get shared storage billing for an organization
[**billing_get_shared_storage_billing_user**](BillingApi.md#billing_get_shared_storage_billing_user) | **GET** /users/{username}/settings/billing/shared-storage | Get shared storage billing for a user


# **billing_get_github_actions_billing_org**
> ActionsBillingUsage billing_get_github_actions_billing_org(org)

Get GitHub Actions billing for an organization

Gets the summary of the free and paid GitHub Actions minutes used.  Paid minutes only apply to workflows in private repositories that use GitHub-hosted runners. Minutes used is listed for each GitHub-hosted runner operating system. Any job re-runs are also included in the usage. The usage returned includes any minute multipliers for macOS and Windows runners, and is rounded up to the nearest whole minute. For more information, see \"[Managing billing for GitHub Actions](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-actions)\".  OAuth app tokens and personal access tokens (classic) need the `repo` or `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_billing_usage import ActionsBillingUsage
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
    api_instance = github_openapi.BillingApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.

    try:
        # Get GitHub Actions billing for an organization
        api_response = api_instance.billing_get_github_actions_billing_org(org)
        print("The response of BillingApi->billing_get_github_actions_billing_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->billing_get_github_actions_billing_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 

### Return type

[**ActionsBillingUsage**](ActionsBillingUsage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billing_get_github_actions_billing_user**
> ActionsBillingUsage billing_get_github_actions_billing_user(username)

Get GitHub Actions billing for a user

Gets the summary of the free and paid GitHub Actions minutes used.  Paid minutes only apply to workflows in private repositories that use GitHub-hosted runners. Minutes used is listed for each GitHub-hosted runner operating system. Any job re-runs are also included in the usage. The usage returned includes any minute multipliers for macOS and Windows runners, and is rounded up to the nearest whole minute. For more information, see \"[Managing billing for GitHub Actions](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-actions)\".  OAuth app tokens and personal access tokens (classic) need the `user` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.actions_billing_usage import ActionsBillingUsage
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
    api_instance = github_openapi.BillingApi(api_client)
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Get GitHub Actions billing for a user
        api_response = api_instance.billing_get_github_actions_billing_user(username)
        print("The response of BillingApi->billing_get_github_actions_billing_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->billing_get_github_actions_billing_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The handle for the GitHub user account. | 

### Return type

[**ActionsBillingUsage**](ActionsBillingUsage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billing_get_github_billing_usage_report_org**
> BillingUsageReport billing_get_github_billing_usage_report_org(org, year=year, month=month, day=day, hour=hour)

Get billing usage report for an organization

Gets a report of the total usage for an organization. To use this endpoint, you must be an administrator of an organization within an enterprise or an organization account.  **Note:** This endpoint is only available to organizations with access to the enhanced billing platform. For more information, see \"[About the enhanced billing platform](https://docs.github.com/billing/using-the-new-billing-platform).\"

### Example


```python
import github_openapi
from github_openapi.models.billing_usage_report import BillingUsageReport
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
    api_instance = github_openapi.BillingApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    year = 56 # int | If specified, only return results for a single year. The value of `year` is an integer with four digits representing a year. For example, `2024`. Default value is the current year. (optional)
    month = 56 # int | If specified, only return results for a single month. The value of `month` is an integer between `1` and `12`. (optional)
    day = 56 # int | If specified, only return results for a single day. The value of `day` is an integer between `1` and `31`. (optional)
    hour = 56 # int | If specified, only return results for a single hour. The value of `hour` is an integer between `0` and `23`. (optional)

    try:
        # Get billing usage report for an organization
        api_response = api_instance.billing_get_github_billing_usage_report_org(org, year=year, month=month, day=day, hour=hour)
        print("The response of BillingApi->billing_get_github_billing_usage_report_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->billing_get_github_billing_usage_report_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **year** | **int**| If specified, only return results for a single year. The value of &#x60;year&#x60; is an integer with four digits representing a year. For example, &#x60;2024&#x60;. Default value is the current year. | [optional] 
 **month** | **int**| If specified, only return results for a single month. The value of &#x60;month&#x60; is an integer between &#x60;1&#x60; and &#x60;12&#x60;. | [optional] 
 **day** | **int**| If specified, only return results for a single day. The value of &#x60;day&#x60; is an integer between &#x60;1&#x60; and &#x60;31&#x60;. | [optional] 
 **hour** | **int**| If specified, only return results for a single hour. The value of &#x60;hour&#x60; is an integer between &#x60;0&#x60; and &#x60;23&#x60;. | [optional] 

### Return type

[**BillingUsageReport**](BillingUsageReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Billing usage report response for an organization |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**500** | Internal Error |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billing_get_github_packages_billing_org**
> PackagesBillingUsage billing_get_github_packages_billing_org(org)

Get GitHub Packages billing for an organization

Gets the free and paid storage used for GitHub Packages in gigabytes.  Paid minutes only apply to packages stored for private repositories. For more information, see \"[Managing billing for GitHub Packages](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-packages).\"  OAuth app tokens and personal access tokens (classic) need the `repo` or `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.packages_billing_usage import PackagesBillingUsage
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
    api_instance = github_openapi.BillingApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.

    try:
        # Get GitHub Packages billing for an organization
        api_response = api_instance.billing_get_github_packages_billing_org(org)
        print("The response of BillingApi->billing_get_github_packages_billing_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->billing_get_github_packages_billing_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 

### Return type

[**PackagesBillingUsage**](PackagesBillingUsage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billing_get_github_packages_billing_user**
> PackagesBillingUsage billing_get_github_packages_billing_user(username)

Get GitHub Packages billing for a user

Gets the free and paid storage used for GitHub Packages in gigabytes.  Paid minutes only apply to packages stored for private repositories. For more information, see \"[Managing billing for GitHub Packages](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-packages).\"  OAuth app tokens and personal access tokens (classic) need the `user` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.packages_billing_usage import PackagesBillingUsage
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
    api_instance = github_openapi.BillingApi(api_client)
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Get GitHub Packages billing for a user
        api_response = api_instance.billing_get_github_packages_billing_user(username)
        print("The response of BillingApi->billing_get_github_packages_billing_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->billing_get_github_packages_billing_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The handle for the GitHub user account. | 

### Return type

[**PackagesBillingUsage**](PackagesBillingUsage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billing_get_shared_storage_billing_org**
> CombinedBillingUsage billing_get_shared_storage_billing_org(org)

Get shared storage billing for an organization

Gets the estimated paid and estimated total storage used for GitHub Actions and GitHub Packages.  Paid minutes only apply to packages stored for private repositories. For more information, see \"[Managing billing for GitHub Packages](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-packages).\"  OAuth app tokens and personal access tokens (classic) need the `repo` or `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.combined_billing_usage import CombinedBillingUsage
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
    api_instance = github_openapi.BillingApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.

    try:
        # Get shared storage billing for an organization
        api_response = api_instance.billing_get_shared_storage_billing_org(org)
        print("The response of BillingApi->billing_get_shared_storage_billing_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->billing_get_shared_storage_billing_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 

### Return type

[**CombinedBillingUsage**](CombinedBillingUsage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **billing_get_shared_storage_billing_user**
> CombinedBillingUsage billing_get_shared_storage_billing_user(username)

Get shared storage billing for a user

Gets the estimated paid and estimated total storage used for GitHub Actions and GitHub Packages.  Paid minutes only apply to packages stored for private repositories. For more information, see \"[Managing billing for GitHub Packages](https://docs.github.com/github/setting-up-and-managing-billing-and-payments-on-github/managing-billing-for-github-packages).\"  OAuth app tokens and personal access tokens (classic) need the `user` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.combined_billing_usage import CombinedBillingUsage
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
    api_instance = github_openapi.BillingApi(api_client)
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Get shared storage billing for a user
        api_response = api_instance.billing_get_shared_storage_billing_user(username)
        print("The response of BillingApi->billing_get_shared_storage_billing_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->billing_get_shared_storage_billing_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The handle for the GitHub user account. | 

### Return type

[**CombinedBillingUsage**](CombinedBillingUsage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

