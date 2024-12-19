# github_openapi.SecretScanningApi

All URIs are relative to *https://api.github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secret_scanning_create_push_protection_bypass**](SecretScanningApi.md#secret_scanning_create_push_protection_bypass) | **POST** /repos/{owner}/{repo}/secret-scanning/push-protection-bypasses | Create a push protection bypass
[**secret_scanning_get_alert**](SecretScanningApi.md#secret_scanning_get_alert) | **GET** /repos/{owner}/{repo}/secret-scanning/alerts/{alert_number} | Get a secret scanning alert
[**secret_scanning_get_scan_history**](SecretScanningApi.md#secret_scanning_get_scan_history) | **GET** /repos/{owner}/{repo}/secret-scanning/scan-history | Get secret scanning scan history for a repository
[**secret_scanning_list_alerts_for_enterprise**](SecretScanningApi.md#secret_scanning_list_alerts_for_enterprise) | **GET** /enterprises/{enterprise}/secret-scanning/alerts | List secret scanning alerts for an enterprise
[**secret_scanning_list_alerts_for_org**](SecretScanningApi.md#secret_scanning_list_alerts_for_org) | **GET** /orgs/{org}/secret-scanning/alerts | List secret scanning alerts for an organization
[**secret_scanning_list_alerts_for_repo**](SecretScanningApi.md#secret_scanning_list_alerts_for_repo) | **GET** /repos/{owner}/{repo}/secret-scanning/alerts | List secret scanning alerts for a repository
[**secret_scanning_list_locations_for_alert**](SecretScanningApi.md#secret_scanning_list_locations_for_alert) | **GET** /repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}/locations | List locations for a secret scanning alert
[**secret_scanning_update_alert**](SecretScanningApi.md#secret_scanning_update_alert) | **PATCH** /repos/{owner}/{repo}/secret-scanning/alerts/{alert_number} | Update a secret scanning alert


# **secret_scanning_create_push_protection_bypass**
> SecretScanningPushProtectionBypass secret_scanning_create_push_protection_bypass(owner, repo, secret_scanning_create_push_protection_bypass_request)

Create a push protection bypass

Creates a bypass for a previously push protected secret.  The authenticated user must be the original author of the committed secret.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.secret_scanning_create_push_protection_bypass_request import SecretScanningCreatePushProtectionBypassRequest
from github_openapi.models.secret_scanning_push_protection_bypass import SecretScanningPushProtectionBypass
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
    api_instance = github_openapi.SecretScanningApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    secret_scanning_create_push_protection_bypass_request = {"reason":"will_fix_later","placeholder_id":"2k4dM4tseyC5lPIsjl5emX9sPNk"} # SecretScanningCreatePushProtectionBypassRequest | 

    try:
        # Create a push protection bypass
        api_response = api_instance.secret_scanning_create_push_protection_bypass(owner, repo, secret_scanning_create_push_protection_bypass_request)
        print("The response of SecretScanningApi->secret_scanning_create_push_protection_bypass:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretScanningApi->secret_scanning_create_push_protection_bypass: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **secret_scanning_create_push_protection_bypass_request** | [**SecretScanningCreatePushProtectionBypassRequest**](SecretScanningCreatePushProtectionBypassRequest.md)|  | 

### Return type

[**SecretScanningPushProtectionBypass**](SecretScanningPushProtectionBypass.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**403** | User does not have enough permissions to perform this action. |  -  |
**404** | Placeholder ID not found, or push protection is disabled on this repository. |  -  |
**422** | Bad request, input data missing or incorrect. |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_scanning_get_alert**
> SecretScanningAlert secret_scanning_get_alert(owner, repo, alert_number)

Get a secret scanning alert

Gets a single secret scanning alert detected in an eligible repository.  The authenticated user must be an administrator for the repository or for the organization that owns the repository to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` or `security_events` scope to use this endpoint. If this endpoint is only used with public repositories, the token can use the `public_repo` scope instead.

### Example


```python
import github_openapi
from github_openapi.models.secret_scanning_alert import SecretScanningAlert
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
    api_instance = github_openapi.SecretScanningApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    alert_number = 56 # int | The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the `number` field in the response from the `GET /repos/{owner}/{repo}/code-scanning/alerts` operation.

    try:
        # Get a secret scanning alert
        api_response = api_instance.secret_scanning_get_alert(owner, repo, alert_number)
        print("The response of SecretScanningApi->secret_scanning_get_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretScanningApi->secret_scanning_get_alert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **alert_number** | **int**| The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the &#x60;number&#x60; field in the response from the &#x60;GET /repos/{owner}/{repo}/code-scanning/alerts&#x60; operation. | 

### Return type

[**SecretScanningAlert**](SecretScanningAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**304** | Not modified |  -  |
**404** | Repository is public, or secret scanning is disabled for the repository, or the resource is not found |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_scanning_get_scan_history**
> SecretScanningScanHistory secret_scanning_get_scan_history(owner, repo)

Get secret scanning scan history for a repository

Lists the latest incremental and backfill scans by type for a repository.  OAuth app tokens and personal access tokens (classic) need the `repo` or `security_events` scope to use this endpoint. If this endpoint is only used with public repositories, the token can use the `public_repo` scope instead.

### Example


```python
import github_openapi
from github_openapi.models.secret_scanning_scan_history import SecretScanningScanHistory
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
    api_instance = github_openapi.SecretScanningApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Get secret scanning scan history for a repository
        api_response = api_instance.secret_scanning_get_scan_history(owner, repo)
        print("The response of SecretScanningApi->secret_scanning_get_scan_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretScanningApi->secret_scanning_get_scan_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**SecretScanningScanHistory**](SecretScanningScanHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Repository does not have GitHub Advanced Security or secret scanning enabled |  -  |
**503** | Service unavailable |  -  |
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_scanning_list_alerts_for_enterprise**
> List[OrganizationSecretScanningAlert] secret_scanning_list_alerts_for_enterprise(enterprise, state=state, secret_type=secret_type, resolution=resolution, sort=sort, direction=direction, per_page=per_page, before=before, after=after, validity=validity, is_publicly_leaked=is_publicly_leaked, is_multi_repo=is_multi_repo)

List secret scanning alerts for an enterprise

Lists secret scanning alerts for eligible repositories in an enterprise, from newest to oldest.  Alerts are only returned for organizations in the enterprise for which the authenticated user is an organization owner or a [security manager](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization).  The authenticated user must be a member of the enterprise in order to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope or `security_events` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.organization_secret_scanning_alert import OrganizationSecretScanningAlert
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
    api_instance = github_openapi.SecretScanningApi(api_client)
    enterprise = 'enterprise_example' # str | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    state = 'state_example' # str | Set to `open` or `resolved` to only list secret scanning alerts in a specific state. (optional)
    secret_type = 'secret_type_example' # str | A comma-separated list of secret types to return. All default secret patterns are returned. To return experimental patterns, pass the token name(s) in the parameter. See \"[Supported secret scanning patterns](https://docs.github.com/enterprise-cloud@latest/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#supported-secrets)\" for a complete list of secret types. (optional)
    resolution = 'resolution_example' # str | A comma-separated list of resolutions. Only secret scanning alerts with one of these resolutions are listed. Valid resolutions are `false_positive`, `wont_fix`, `revoked`, `pattern_edited`, `pattern_deleted` or `used_in_tests`. (optional)
    sort = created # str | The property to sort the results by. `created` means when the alert was created. `updated` means when the alert was updated or resolved. (optional) (default to created)
    direction = desc # str | The direction to sort the results by. (optional) (default to desc)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    before = 'before_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)
    after = 'after_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)
    validity = 'validity_example' # str | A comma-separated list of validities that, when present, will return alerts that match the validities in this list. Valid options are `active`, `inactive`, and `unknown`. (optional)
    is_publicly_leaked = False # bool | A boolean value representing whether or not to filter alerts by the publicly-leaked tag being present. (optional) (default to False)
    is_multi_repo = False # bool | A boolean value representing whether or not to filter alerts by the multi-repo tag being present. (optional) (default to False)

    try:
        # List secret scanning alerts for an enterprise
        api_response = api_instance.secret_scanning_list_alerts_for_enterprise(enterprise, state=state, secret_type=secret_type, resolution=resolution, sort=sort, direction=direction, per_page=per_page, before=before, after=after, validity=validity, is_publicly_leaked=is_publicly_leaked, is_multi_repo=is_multi_repo)
        print("The response of SecretScanningApi->secret_scanning_list_alerts_for_enterprise:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretScanningApi->secret_scanning_list_alerts_for_enterprise: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enterprise** | **str**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **state** | **str**| Set to &#x60;open&#x60; or &#x60;resolved&#x60; to only list secret scanning alerts in a specific state. | [optional] 
 **secret_type** | **str**| A comma-separated list of secret types to return. All default secret patterns are returned. To return experimental patterns, pass the token name(s) in the parameter. See \&quot;[Supported secret scanning patterns](https://docs.github.com/enterprise-cloud@latest/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#supported-secrets)\&quot; for a complete list of secret types. | [optional] 
 **resolution** | **str**| A comma-separated list of resolutions. Only secret scanning alerts with one of these resolutions are listed. Valid resolutions are &#x60;false_positive&#x60;, &#x60;wont_fix&#x60;, &#x60;revoked&#x60;, &#x60;pattern_edited&#x60;, &#x60;pattern_deleted&#x60; or &#x60;used_in_tests&#x60;. | [optional] 
 **sort** | **str**| The property to sort the results by. &#x60;created&#x60; means when the alert was created. &#x60;updated&#x60; means when the alert was updated or resolved. | [optional] [default to created]
 **direction** | **str**| The direction to sort the results by. | [optional] [default to desc]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **before** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 
 **after** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 
 **validity** | **str**| A comma-separated list of validities that, when present, will return alerts that match the validities in this list. Valid options are &#x60;active&#x60;, &#x60;inactive&#x60;, and &#x60;unknown&#x60;. | [optional] 
 **is_publicly_leaked** | **bool**| A boolean value representing whether or not to filter alerts by the publicly-leaked tag being present. | [optional] [default to False]
 **is_multi_repo** | **bool**| A boolean value representing whether or not to filter alerts by the multi-repo tag being present. | [optional] [default to False]

### Return type

[**List[OrganizationSecretScanningAlert]**](OrganizationSecretScanningAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |
**404** | Resource not found |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_scanning_list_alerts_for_org**
> List[OrganizationSecretScanningAlert] secret_scanning_list_alerts_for_org(org, state=state, secret_type=secret_type, resolution=resolution, sort=sort, direction=direction, page=page, per_page=per_page, before=before, after=after, validity=validity, is_publicly_leaked=is_publicly_leaked, is_multi_repo=is_multi_repo)

List secret scanning alerts for an organization

Lists secret scanning alerts for eligible repositories in an organization, from newest to oldest.  The authenticated user must be an administrator or security manager for the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` or `security_events` scope to use this endpoint. If this endpoint is only used with public repositories, the token can use the `public_repo` scope instead.

### Example


```python
import github_openapi
from github_openapi.models.organization_secret_scanning_alert import OrganizationSecretScanningAlert
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
    api_instance = github_openapi.SecretScanningApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    state = 'state_example' # str | Set to `open` or `resolved` to only list secret scanning alerts in a specific state. (optional)
    secret_type = 'secret_type_example' # str | A comma-separated list of secret types to return. All default secret patterns are returned. To return experimental patterns, pass the token name(s) in the parameter. See \"[Supported secret scanning patterns](https://docs.github.com/enterprise-cloud@latest/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#supported-secrets)\" for a complete list of secret types. (optional)
    resolution = 'resolution_example' # str | A comma-separated list of resolutions. Only secret scanning alerts with one of these resolutions are listed. Valid resolutions are `false_positive`, `wont_fix`, `revoked`, `pattern_edited`, `pattern_deleted` or `used_in_tests`. (optional)
    sort = created # str | The property to sort the results by. `created` means when the alert was created. `updated` means when the alert was updated or resolved. (optional) (default to created)
    direction = desc # str | The direction to sort the results by. (optional) (default to desc)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    before = 'before_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for events before this cursor. To receive an initial cursor on your first request, include an empty \"before\" query string. (optional)
    after = 'after_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for events after this cursor.  To receive an initial cursor on your first request, include an empty \"after\" query string. (optional)
    validity = 'validity_example' # str | A comma-separated list of validities that, when present, will return alerts that match the validities in this list. Valid options are `active`, `inactive`, and `unknown`. (optional)
    is_publicly_leaked = False # bool | A boolean value representing whether or not to filter alerts by the publicly-leaked tag being present. (optional) (default to False)
    is_multi_repo = False # bool | A boolean value representing whether or not to filter alerts by the multi-repo tag being present. (optional) (default to False)

    try:
        # List secret scanning alerts for an organization
        api_response = api_instance.secret_scanning_list_alerts_for_org(org, state=state, secret_type=secret_type, resolution=resolution, sort=sort, direction=direction, page=page, per_page=per_page, before=before, after=after, validity=validity, is_publicly_leaked=is_publicly_leaked, is_multi_repo=is_multi_repo)
        print("The response of SecretScanningApi->secret_scanning_list_alerts_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretScanningApi->secret_scanning_list_alerts_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **state** | **str**| Set to &#x60;open&#x60; or &#x60;resolved&#x60; to only list secret scanning alerts in a specific state. | [optional] 
 **secret_type** | **str**| A comma-separated list of secret types to return. All default secret patterns are returned. To return experimental patterns, pass the token name(s) in the parameter. See \&quot;[Supported secret scanning patterns](https://docs.github.com/enterprise-cloud@latest/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#supported-secrets)\&quot; for a complete list of secret types. | [optional] 
 **resolution** | **str**| A comma-separated list of resolutions. Only secret scanning alerts with one of these resolutions are listed. Valid resolutions are &#x60;false_positive&#x60;, &#x60;wont_fix&#x60;, &#x60;revoked&#x60;, &#x60;pattern_edited&#x60;, &#x60;pattern_deleted&#x60; or &#x60;used_in_tests&#x60;. | [optional] 
 **sort** | **str**| The property to sort the results by. &#x60;created&#x60; means when the alert was created. &#x60;updated&#x60; means when the alert was updated or resolved. | [optional] [default to created]
 **direction** | **str**| The direction to sort the results by. | [optional] [default to desc]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **before** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for events before this cursor. To receive an initial cursor on your first request, include an empty \&quot;before\&quot; query string. | [optional] 
 **after** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for events after this cursor.  To receive an initial cursor on your first request, include an empty \&quot;after\&quot; query string. | [optional] 
 **validity** | **str**| A comma-separated list of validities that, when present, will return alerts that match the validities in this list. Valid options are &#x60;active&#x60;, &#x60;inactive&#x60;, and &#x60;unknown&#x60;. | [optional] 
 **is_publicly_leaked** | **bool**| A boolean value representing whether or not to filter alerts by the publicly-leaked tag being present. | [optional] [default to False]
 **is_multi_repo** | **bool**| A boolean value representing whether or not to filter alerts by the multi-repo tag being present. | [optional] [default to False]

### Return type

[**List[OrganizationSecretScanningAlert]**](OrganizationSecretScanningAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |
**404** | Resource not found |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_scanning_list_alerts_for_repo**
> List[SecretScanningAlert] secret_scanning_list_alerts_for_repo(owner, repo, state=state, secret_type=secret_type, resolution=resolution, sort=sort, direction=direction, page=page, per_page=per_page, before=before, after=after, validity=validity, is_publicly_leaked=is_publicly_leaked, is_multi_repo=is_multi_repo)

List secret scanning alerts for a repository

Lists secret scanning alerts for an eligible repository, from newest to oldest.  The authenticated user must be an administrator for the repository or for the organization that owns the repository to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` or `security_events` scope to use this endpoint. If this endpoint is only used with public repositories, the token can use the `public_repo` scope instead.

### Example


```python
import github_openapi
from github_openapi.models.secret_scanning_alert import SecretScanningAlert
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
    api_instance = github_openapi.SecretScanningApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    state = 'state_example' # str | Set to `open` or `resolved` to only list secret scanning alerts in a specific state. (optional)
    secret_type = 'secret_type_example' # str | A comma-separated list of secret types to return. All default secret patterns are returned. To return experimental patterns, pass the token name(s) in the parameter. See \"[Supported secret scanning patterns](https://docs.github.com/enterprise-cloud@latest/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#supported-secrets)\" for a complete list of secret types. (optional)
    resolution = 'resolution_example' # str | A comma-separated list of resolutions. Only secret scanning alerts with one of these resolutions are listed. Valid resolutions are `false_positive`, `wont_fix`, `revoked`, `pattern_edited`, `pattern_deleted` or `used_in_tests`. (optional)
    sort = created # str | The property to sort the results by. `created` means when the alert was created. `updated` means when the alert was updated or resolved. (optional) (default to created)
    direction = desc # str | The direction to sort the results by. (optional) (default to desc)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    before = 'before_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for events before this cursor. To receive an initial cursor on your first request, include an empty \"before\" query string. (optional)
    after = 'after_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for events after this cursor.  To receive an initial cursor on your first request, include an empty \"after\" query string. (optional)
    validity = 'validity_example' # str | A comma-separated list of validities that, when present, will return alerts that match the validities in this list. Valid options are `active`, `inactive`, and `unknown`. (optional)
    is_publicly_leaked = False # bool | A boolean value representing whether or not to filter alerts by the publicly-leaked tag being present. (optional) (default to False)
    is_multi_repo = False # bool | A boolean value representing whether or not to filter alerts by the multi-repo tag being present. (optional) (default to False)

    try:
        # List secret scanning alerts for a repository
        api_response = api_instance.secret_scanning_list_alerts_for_repo(owner, repo, state=state, secret_type=secret_type, resolution=resolution, sort=sort, direction=direction, page=page, per_page=per_page, before=before, after=after, validity=validity, is_publicly_leaked=is_publicly_leaked, is_multi_repo=is_multi_repo)
        print("The response of SecretScanningApi->secret_scanning_list_alerts_for_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretScanningApi->secret_scanning_list_alerts_for_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **state** | **str**| Set to &#x60;open&#x60; or &#x60;resolved&#x60; to only list secret scanning alerts in a specific state. | [optional] 
 **secret_type** | **str**| A comma-separated list of secret types to return. All default secret patterns are returned. To return experimental patterns, pass the token name(s) in the parameter. See \&quot;[Supported secret scanning patterns](https://docs.github.com/enterprise-cloud@latest/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#supported-secrets)\&quot; for a complete list of secret types. | [optional] 
 **resolution** | **str**| A comma-separated list of resolutions. Only secret scanning alerts with one of these resolutions are listed. Valid resolutions are &#x60;false_positive&#x60;, &#x60;wont_fix&#x60;, &#x60;revoked&#x60;, &#x60;pattern_edited&#x60;, &#x60;pattern_deleted&#x60; or &#x60;used_in_tests&#x60;. | [optional] 
 **sort** | **str**| The property to sort the results by. &#x60;created&#x60; means when the alert was created. &#x60;updated&#x60; means when the alert was updated or resolved. | [optional] [default to created]
 **direction** | **str**| The direction to sort the results by. | [optional] [default to desc]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **before** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for events before this cursor. To receive an initial cursor on your first request, include an empty \&quot;before\&quot; query string. | [optional] 
 **after** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for events after this cursor.  To receive an initial cursor on your first request, include an empty \&quot;after\&quot; query string. | [optional] 
 **validity** | **str**| A comma-separated list of validities that, when present, will return alerts that match the validities in this list. Valid options are &#x60;active&#x60;, &#x60;inactive&#x60;, and &#x60;unknown&#x60;. | [optional] 
 **is_publicly_leaked** | **bool**| A boolean value representing whether or not to filter alerts by the publicly-leaked tag being present. | [optional] [default to False]
 **is_multi_repo** | **bool**| A boolean value representing whether or not to filter alerts by the multi-repo tag being present. | [optional] [default to False]

### Return type

[**List[SecretScanningAlert]**](SecretScanningAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Repository is public or secret scanning is disabled for the repository |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_scanning_list_locations_for_alert**
> List[SecretScanningLocation] secret_scanning_list_locations_for_alert(owner, repo, alert_number, page=page, per_page=per_page)

List locations for a secret scanning alert

Lists all locations for a given secret scanning alert for an eligible repository.  The authenticated user must be an administrator for the repository or for the organization that owns the repository to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` or `security_events` scope to use this endpoint. If this endpoint is only used with public repositories, the token can use the `public_repo` scope instead.

### Example


```python
import github_openapi
from github_openapi.models.secret_scanning_location import SecretScanningLocation
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
    api_instance = github_openapi.SecretScanningApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    alert_number = 56 # int | The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the `number` field in the response from the `GET /repos/{owner}/{repo}/code-scanning/alerts` operation.
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)

    try:
        # List locations for a secret scanning alert
        api_response = api_instance.secret_scanning_list_locations_for_alert(owner, repo, alert_number, page=page, per_page=per_page)
        print("The response of SecretScanningApi->secret_scanning_list_locations_for_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretScanningApi->secret_scanning_list_locations_for_alert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **alert_number** | **int**| The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the &#x60;number&#x60; field in the response from the &#x60;GET /repos/{owner}/{repo}/code-scanning/alerts&#x60; operation. | 
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]

### Return type

[**List[SecretScanningLocation]**](SecretScanningLocation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |
**404** | Repository is public, or secret scanning is disabled for the repository, or the resource is not found |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secret_scanning_update_alert**
> SecretScanningAlert secret_scanning_update_alert(owner, repo, alert_number, secret_scanning_update_alert_request)

Update a secret scanning alert

Updates the status of a secret scanning alert in an eligible repository.  The authenticated user must be an administrator for the repository or for the organization that owns the repository to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` or `security_events` scope to use this endpoint. If this endpoint is only used with public repositories, the token can use the `public_repo` scope instead.

### Example


```python
import github_openapi
from github_openapi.models.secret_scanning_alert import SecretScanningAlert
from github_openapi.models.secret_scanning_update_alert_request import SecretScanningUpdateAlertRequest
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
    api_instance = github_openapi.SecretScanningApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    alert_number = 56 # int | The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the `number` field in the response from the `GET /repos/{owner}/{repo}/code-scanning/alerts` operation.
    secret_scanning_update_alert_request = {"state":"resolved","resolution":"false_positive"} # SecretScanningUpdateAlertRequest | 

    try:
        # Update a secret scanning alert
        api_response = api_instance.secret_scanning_update_alert(owner, repo, alert_number, secret_scanning_update_alert_request)
        print("The response of SecretScanningApi->secret_scanning_update_alert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecretScanningApi->secret_scanning_update_alert: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **alert_number** | **int**| The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the &#x60;number&#x60; field in the response from the &#x60;GET /repos/{owner}/{repo}/code-scanning/alerts&#x60; operation. | 
 **secret_scanning_update_alert_request** | [**SecretScanningUpdateAlertRequest**](SecretScanningUpdateAlertRequest.md)|  | 

### Return type

[**SecretScanningAlert**](SecretScanningAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**400** | Bad request, resolution comment is invalid or the resolution was not changed. |  -  |
**404** | Repository is public, or secret scanning is disabled for the repository, or the resource is not found |  -  |
**422** | State does not match the resolution or resolution comment |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

