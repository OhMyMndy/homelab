# github_openapi.SecurityAdvisoriesApi

All URIs are relative to *https://api.github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**security_advisories_create_fork**](SecurityAdvisoriesApi.md#security_advisories_create_fork) | **POST** /repos/{owner}/{repo}/security-advisories/{ghsa_id}/forks | Create a temporary private fork
[**security_advisories_create_private_vulnerability_report**](SecurityAdvisoriesApi.md#security_advisories_create_private_vulnerability_report) | **POST** /repos/{owner}/{repo}/security-advisories/reports | Privately report a security vulnerability
[**security_advisories_create_repository_advisory**](SecurityAdvisoriesApi.md#security_advisories_create_repository_advisory) | **POST** /repos/{owner}/{repo}/security-advisories | Create a repository security advisory
[**security_advisories_create_repository_advisory_cve_request**](SecurityAdvisoriesApi.md#security_advisories_create_repository_advisory_cve_request) | **POST** /repos/{owner}/{repo}/security-advisories/{ghsa_id}/cve | Request a CVE for a repository security advisory
[**security_advisories_get_global_advisory**](SecurityAdvisoriesApi.md#security_advisories_get_global_advisory) | **GET** /advisories/{ghsa_id} | Get a global security advisory
[**security_advisories_get_repository_advisory**](SecurityAdvisoriesApi.md#security_advisories_get_repository_advisory) | **GET** /repos/{owner}/{repo}/security-advisories/{ghsa_id} | Get a repository security advisory
[**security_advisories_list_global_advisories**](SecurityAdvisoriesApi.md#security_advisories_list_global_advisories) | **GET** /advisories | List global security advisories
[**security_advisories_list_org_repository_advisories**](SecurityAdvisoriesApi.md#security_advisories_list_org_repository_advisories) | **GET** /orgs/{org}/security-advisories | List repository security advisories for an organization
[**security_advisories_list_repository_advisories**](SecurityAdvisoriesApi.md#security_advisories_list_repository_advisories) | **GET** /repos/{owner}/{repo}/security-advisories | List repository security advisories
[**security_advisories_update_repository_advisory**](SecurityAdvisoriesApi.md#security_advisories_update_repository_advisory) | **PATCH** /repos/{owner}/{repo}/security-advisories/{ghsa_id} | Update a repository security advisory


# **security_advisories_create_fork**
> FullRepository security_advisories_create_fork(owner, repo, ghsa_id)

Create a temporary private fork

Create a temporary private fork to collaborate on fixing a security vulnerability in your repository.  > [!NOTE] > Forking a repository happens asynchronously. You may have to wait up to 5 minutes before you can access the fork.

### Example


```python
import github_openapi
from github_openapi.models.full_repository import FullRepository
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
    api_instance = github_openapi.SecurityAdvisoriesApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    ghsa_id = 'ghsa_id_example' # str | The GHSA (GitHub Security Advisory) identifier of the advisory.

    try:
        # Create a temporary private fork
        api_response = api_instance.security_advisories_create_fork(owner, repo, ghsa_id)
        print("The response of SecurityAdvisoriesApi->security_advisories_create_fork:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityAdvisoriesApi->security_advisories_create_fork: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **ghsa_id** | **str**| The GHSA (GitHub Security Advisory) identifier of the advisory. | 

### Return type

[**FullRepository**](FullRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Response |  -  |
**400** | Bad Request |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **security_advisories_create_private_vulnerability_report**
> RepositoryAdvisory security_advisories_create_private_vulnerability_report(owner, repo, private_vulnerability_report_create)

Privately report a security vulnerability

Report a security vulnerability to the maintainers of the repository. See \"[Privately reporting a security vulnerability](https://docs.github.com/code-security/security-advisories/guidance-on-reporting-and-writing/privately-reporting-a-security-vulnerability)\" for more information about private vulnerability reporting.

### Example


```python
import github_openapi
from github_openapi.models.private_vulnerability_report_create import PrivateVulnerabilityReportCreate
from github_openapi.models.repository_advisory import RepositoryAdvisory
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
    api_instance = github_openapi.SecurityAdvisoriesApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    private_vulnerability_report_create = {"summary":"A newly discovered vulnerability","description":"A more in-depth description of what the problem is.","severity":"high","vulnerabilities":[{"package":{"name":"a-package","ecosystem":"npm"},"vulnerable_version_range":"< 1.0.0","patched_versions":"1.0.0","vulnerable_functions":["important_function"]}],"cwe_ids":["CWE-123"]} # PrivateVulnerabilityReportCreate | 

    try:
        # Privately report a security vulnerability
        api_response = api_instance.security_advisories_create_private_vulnerability_report(owner, repo, private_vulnerability_report_create)
        print("The response of SecurityAdvisoriesApi->security_advisories_create_private_vulnerability_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityAdvisoriesApi->security_advisories_create_private_vulnerability_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **private_vulnerability_report_create** | [**PrivateVulnerabilityReportCreate**](PrivateVulnerabilityReportCreate.md)|  | 

### Return type

[**RepositoryAdvisory**](RepositoryAdvisory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **security_advisories_create_repository_advisory**
> RepositoryAdvisory security_advisories_create_repository_advisory(owner, repo, repository_advisory_create)

Create a repository security advisory

Creates a new repository security advisory.  In order to create a draft repository security advisory, the authenticated user must be a security manager or administrator of that repository.  OAuth app tokens and personal access tokens (classic) need the `repo` or `repository_advisories:write` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.repository_advisory import RepositoryAdvisory
from github_openapi.models.repository_advisory_create import RepositoryAdvisoryCreate
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
    api_instance = github_openapi.SecurityAdvisoriesApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    repository_advisory_create = {"summary":"A new important advisory","description":"A more in-depth description of what the problem is.","severity":"high","cve_id":null,"vulnerabilities":[{"package":{"name":"a-package","ecosystem":"npm"},"vulnerable_version_range":"< 1.0.0","patched_versions":"1.0.0","vulnerable_functions":["important_function"]}],"cwe_ids":["CWE-1101","CWE-20"],"credits":[{"login":"monalisa","type":"reporter"},{"login":"octocat","type":"analyst"}]} # RepositoryAdvisoryCreate | 

    try:
        # Create a repository security advisory
        api_response = api_instance.security_advisories_create_repository_advisory(owner, repo, repository_advisory_create)
        print("The response of SecurityAdvisoriesApi->security_advisories_create_repository_advisory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityAdvisoriesApi->security_advisories_create_repository_advisory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **repository_advisory_create** | [**RepositoryAdvisoryCreate**](RepositoryAdvisoryCreate.md)|  | 

### Return type

[**RepositoryAdvisory**](RepositoryAdvisory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **security_advisories_create_repository_advisory_cve_request**
> object security_advisories_create_repository_advisory_cve_request(owner, repo, ghsa_id)

Request a CVE for a repository security advisory

If you want a CVE identification number for the security vulnerability in your project, and don't already have one, you can request a CVE identification number from GitHub. For more information see \"[Requesting a CVE identification number](https://docs.github.com/code-security/security-advisories/repository-security-advisories/publishing-a-repository-security-advisory#requesting-a-cve-identification-number-optional).\"  You may request a CVE for public repositories, but cannot do so for private repositories.  In order to request a CVE for a repository security advisory, the authenticated user must be a security manager or administrator of that repository.  OAuth app tokens and personal access tokens (classic) need the `repo` or `repository_advisories:write` scope to use this endpoint.

### Example


```python
import github_openapi
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
    api_instance = github_openapi.SecurityAdvisoriesApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    ghsa_id = 'ghsa_id_example' # str | The GHSA (GitHub Security Advisory) identifier of the advisory.

    try:
        # Request a CVE for a repository security advisory
        api_response = api_instance.security_advisories_create_repository_advisory_cve_request(owner, repo, ghsa_id)
        print("The response of SecurityAdvisoriesApi->security_advisories_create_repository_advisory_cve_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityAdvisoriesApi->security_advisories_create_repository_advisory_cve_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **ghsa_id** | **str**| The GHSA (GitHub Security Advisory) identifier of the advisory. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **security_advisories_get_global_advisory**
> GlobalAdvisory security_advisories_get_global_advisory(ghsa_id)

Get a global security advisory

Gets a global security advisory using its GitHub Security Advisory (GHSA) identifier.

### Example


```python
import github_openapi
from github_openapi.models.global_advisory import GlobalAdvisory
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
    api_instance = github_openapi.SecurityAdvisoriesApi(api_client)
    ghsa_id = 'ghsa_id_example' # str | The GHSA (GitHub Security Advisory) identifier of the advisory.

    try:
        # Get a global security advisory
        api_response = api_instance.security_advisories_get_global_advisory(ghsa_id)
        print("The response of SecurityAdvisoriesApi->security_advisories_get_global_advisory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityAdvisoriesApi->security_advisories_get_global_advisory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ghsa_id** | **str**| The GHSA (GitHub Security Advisory) identifier of the advisory. | 

### Return type

[**GlobalAdvisory**](GlobalAdvisory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **security_advisories_get_repository_advisory**
> RepositoryAdvisory security_advisories_get_repository_advisory(owner, repo, ghsa_id)

Get a repository security advisory

Get a repository security advisory using its GitHub Security Advisory (GHSA) identifier.  Anyone can access any published security advisory on a public repository.  The authenticated user can access an unpublished security advisory from a repository if they are a security manager or administrator of that repository, or if they are a collaborator on the security advisory.  OAuth app tokens and personal access tokens (classic) need the `repo` or `repository_advisories:read` scope to to get a published security advisory in a private repository, or any unpublished security advisory that the authenticated user has access to.

### Example


```python
import github_openapi
from github_openapi.models.repository_advisory import RepositoryAdvisory
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
    api_instance = github_openapi.SecurityAdvisoriesApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    ghsa_id = 'ghsa_id_example' # str | The GHSA (GitHub Security Advisory) identifier of the advisory.

    try:
        # Get a repository security advisory
        api_response = api_instance.security_advisories_get_repository_advisory(owner, repo, ghsa_id)
        print("The response of SecurityAdvisoriesApi->security_advisories_get_repository_advisory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityAdvisoriesApi->security_advisories_get_repository_advisory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **ghsa_id** | **str**| The GHSA (GitHub Security Advisory) identifier of the advisory. | 

### Return type

[**RepositoryAdvisory**](RepositoryAdvisory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **security_advisories_list_global_advisories**
> List[GlobalAdvisory] security_advisories_list_global_advisories(ghsa_id=ghsa_id, type=type, cve_id=cve_id, ecosystem=ecosystem, severity=severity, cwes=cwes, is_withdrawn=is_withdrawn, affects=affects, published=published, updated=updated, modified=modified, epss_percentage=epss_percentage, epss_percentile=epss_percentile, before=before, after=after, direction=direction, per_page=per_page, sort=sort)

List global security advisories

Lists all global security advisories that match the specified parameters. If no other parameters are defined, the request will return only GitHub-reviewed advisories that are not malware.  By default, all responses will exclude advisories for malware, because malware are not standard vulnerabilities. To list advisories for malware, you must include the `type` parameter in your request, with the value `malware`. For more information about the different types of security advisories, see \"[About the GitHub Advisory database](https://docs.github.com/code-security/security-advisories/global-security-advisories/about-the-github-advisory-database#about-types-of-security-advisories).\"

### Example


```python
import github_openapi
from github_openapi.models.global_advisory import GlobalAdvisory
from github_openapi.models.security_advisory_ecosystems import SecurityAdvisoryEcosystems
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
    api_instance = github_openapi.SecurityAdvisoriesApi(api_client)
    ghsa_id = 'ghsa_id_example' # str | If specified, only advisories with this GHSA (GitHub Security Advisory) identifier will be returned. (optional)
    type = reviewed # str | If specified, only advisories of this type will be returned. By default, a request with no other parameters defined will only return reviewed advisories that are not malware. (optional) (default to reviewed)
    cve_id = 'cve_id_example' # str | If specified, only advisories with this CVE (Common Vulnerabilities and Exposures) identifier will be returned. (optional)
    ecosystem = github_openapi.SecurityAdvisoryEcosystems() # SecurityAdvisoryEcosystems | If specified, only advisories for these ecosystems will be returned. (optional)
    severity = 'severity_example' # str | If specified, only advisories with these severities will be returned. (optional)
    cwes = github_openapi.SecurityAdvisoriesListGlobalAdvisoriesCwesParameter() # SecurityAdvisoriesListGlobalAdvisoriesCwesParameter | If specified, only advisories with these Common Weakness Enumerations (CWEs) will be returned.  Example: `cwes=79,284,22` or `cwes[]=79&cwes[]=284&cwes[]=22` (optional)
    is_withdrawn = True # bool | Whether to only return advisories that have been withdrawn. (optional)
    affects = github_openapi.SecurityAdvisoriesListGlobalAdvisoriesAffectsParameter() # SecurityAdvisoriesListGlobalAdvisoriesAffectsParameter | If specified, only return advisories that affect any of `package` or `package@version`. A maximum of 1000 packages can be specified. If the query parameter causes the URL to exceed the maximum URL length supported by your client, you must specify fewer packages.  Example: `affects=package1,package2@1.0.0,package3@^2.0.0` or `affects[]=package1&affects[]=package2@1.0.0` (optional)
    published = 'published_example' # str | If specified, only return advisories that were published on a date or date range.  For more information on the syntax of the date range, see \"[Understanding the search syntax](https://docs.github.com/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax#query-for-dates).\" (optional)
    updated = 'updated_example' # str | If specified, only return advisories that were updated on a date or date range.  For more information on the syntax of the date range, see \"[Understanding the search syntax](https://docs.github.com/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax#query-for-dates).\" (optional)
    modified = 'modified_example' # str | If specified, only show advisories that were updated or published on a date or date range.  For more information on the syntax of the date range, see \"[Understanding the search syntax](https://docs.github.com/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax#query-for-dates).\" (optional)
    epss_percentage = 'epss_percentage_example' # str | If specified, only return advisories that have an EPSS percentage score that matches the provided value. The EPSS percentage represents the likelihood of a CVE being exploited. (optional)
    epss_percentile = 'epss_percentile_example' # str | If specified, only return advisories that have an EPSS percentile score that matches the provided value. The EPSS percentile represents the relative rank of the CVE's likelihood of being exploited compared to other CVEs. (optional)
    before = 'before_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)
    after = 'after_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)
    direction = desc # str | The direction to sort the results by. (optional) (default to desc)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    sort = published # str | The property to sort the results by. (optional) (default to published)

    try:
        # List global security advisories
        api_response = api_instance.security_advisories_list_global_advisories(ghsa_id=ghsa_id, type=type, cve_id=cve_id, ecosystem=ecosystem, severity=severity, cwes=cwes, is_withdrawn=is_withdrawn, affects=affects, published=published, updated=updated, modified=modified, epss_percentage=epss_percentage, epss_percentile=epss_percentile, before=before, after=after, direction=direction, per_page=per_page, sort=sort)
        print("The response of SecurityAdvisoriesApi->security_advisories_list_global_advisories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityAdvisoriesApi->security_advisories_list_global_advisories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ghsa_id** | **str**| If specified, only advisories with this GHSA (GitHub Security Advisory) identifier will be returned. | [optional] 
 **type** | **str**| If specified, only advisories of this type will be returned. By default, a request with no other parameters defined will only return reviewed advisories that are not malware. | [optional] [default to reviewed]
 **cve_id** | **str**| If specified, only advisories with this CVE (Common Vulnerabilities and Exposures) identifier will be returned. | [optional] 
 **ecosystem** | [**SecurityAdvisoryEcosystems**](.md)| If specified, only advisories for these ecosystems will be returned. | [optional] 
 **severity** | **str**| If specified, only advisories with these severities will be returned. | [optional] 
 **cwes** | [**SecurityAdvisoriesListGlobalAdvisoriesCwesParameter**](.md)| If specified, only advisories with these Common Weakness Enumerations (CWEs) will be returned.  Example: &#x60;cwes&#x3D;79,284,22&#x60; or &#x60;cwes[]&#x3D;79&amp;cwes[]&#x3D;284&amp;cwes[]&#x3D;22&#x60; | [optional] 
 **is_withdrawn** | **bool**| Whether to only return advisories that have been withdrawn. | [optional] 
 **affects** | [**SecurityAdvisoriesListGlobalAdvisoriesAffectsParameter**](.md)| If specified, only return advisories that affect any of &#x60;package&#x60; or &#x60;package@version&#x60;. A maximum of 1000 packages can be specified. If the query parameter causes the URL to exceed the maximum URL length supported by your client, you must specify fewer packages.  Example: &#x60;affects&#x3D;package1,package2@1.0.0,package3@^2.0.0&#x60; or &#x60;affects[]&#x3D;package1&amp;affects[]&#x3D;package2@1.0.0&#x60; | [optional] 
 **published** | **str**| If specified, only return advisories that were published on a date or date range.  For more information on the syntax of the date range, see \&quot;[Understanding the search syntax](https://docs.github.com/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax#query-for-dates).\&quot; | [optional] 
 **updated** | **str**| If specified, only return advisories that were updated on a date or date range.  For more information on the syntax of the date range, see \&quot;[Understanding the search syntax](https://docs.github.com/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax#query-for-dates).\&quot; | [optional] 
 **modified** | **str**| If specified, only show advisories that were updated or published on a date or date range.  For more information on the syntax of the date range, see \&quot;[Understanding the search syntax](https://docs.github.com/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax#query-for-dates).\&quot; | [optional] 
 **epss_percentage** | **str**| If specified, only return advisories that have an EPSS percentage score that matches the provided value. The EPSS percentage represents the likelihood of a CVE being exploited. | [optional] 
 **epss_percentile** | **str**| If specified, only return advisories that have an EPSS percentile score that matches the provided value. The EPSS percentile represents the relative rank of the CVE&#39;s likelihood of being exploited compared to other CVEs. | [optional] 
 **before** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 
 **after** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 
 **direction** | **str**| The direction to sort the results by. | [optional] [default to desc]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **sort** | **str**| The property to sort the results by. | [optional] [default to published]

### Return type

[**List[GlobalAdvisory]**](GlobalAdvisory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**429** | Too many requests |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **security_advisories_list_org_repository_advisories**
> List[RepositoryAdvisory] security_advisories_list_org_repository_advisories(org, direction=direction, sort=sort, before=before, after=after, per_page=per_page, state=state)

List repository security advisories for an organization

Lists repository security advisories for an organization.  The authenticated user must be an owner or security manager for the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` or `repository_advisories:write` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.repository_advisory import RepositoryAdvisory
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
    api_instance = github_openapi.SecurityAdvisoriesApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    direction = desc # str | The direction to sort the results by. (optional) (default to desc)
    sort = created # str | The property to sort the results by. (optional) (default to created)
    before = 'before_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)
    after = 'after_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)
    per_page = 30 # int | The number of advisories to return per page. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    state = 'state_example' # str | Filter by the state of the repository advisories. Only advisories of this state will be returned. (optional)

    try:
        # List repository security advisories for an organization
        api_response = api_instance.security_advisories_list_org_repository_advisories(org, direction=direction, sort=sort, before=before, after=after, per_page=per_page, state=state)
        print("The response of SecurityAdvisoriesApi->security_advisories_list_org_repository_advisories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityAdvisoriesApi->security_advisories_list_org_repository_advisories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **direction** | **str**| The direction to sort the results by. | [optional] [default to desc]
 **sort** | **str**| The property to sort the results by. | [optional] [default to created]
 **before** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 
 **after** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 
 **per_page** | **int**| The number of advisories to return per page. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **state** | **str**| Filter by the state of the repository advisories. Only advisories of this state will be returned. | [optional] 

### Return type

[**List[RepositoryAdvisory]**](RepositoryAdvisory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**400** | Bad Request |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **security_advisories_list_repository_advisories**
> List[RepositoryAdvisory] security_advisories_list_repository_advisories(owner, repo, direction=direction, sort=sort, before=before, after=after, per_page=per_page, state=state)

List repository security advisories

Lists security advisories in a repository.  The authenticated user can access unpublished security advisories from a repository if they are a security manager or administrator of that repository, or if they are a collaborator on any security advisory.  OAuth app tokens and personal access tokens (classic) need the `repo` or `repository_advisories:read` scope to to get a published security advisory in a private repository, or any unpublished security advisory that the authenticated user has access to.

### Example


```python
import github_openapi
from github_openapi.models.repository_advisory import RepositoryAdvisory
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
    api_instance = github_openapi.SecurityAdvisoriesApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    direction = desc # str | The direction to sort the results by. (optional) (default to desc)
    sort = created # str | The property to sort the results by. (optional) (default to created)
    before = 'before_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)
    after = 'after_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)
    per_page = 30 # int | The number of advisories to return per page. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    state = 'state_example' # str | Filter by state of the repository advisories. Only advisories of this state will be returned. (optional)

    try:
        # List repository security advisories
        api_response = api_instance.security_advisories_list_repository_advisories(owner, repo, direction=direction, sort=sort, before=before, after=after, per_page=per_page, state=state)
        print("The response of SecurityAdvisoriesApi->security_advisories_list_repository_advisories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityAdvisoriesApi->security_advisories_list_repository_advisories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **direction** | **str**| The direction to sort the results by. | [optional] [default to desc]
 **sort** | **str**| The property to sort the results by. | [optional] [default to created]
 **before** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 
 **after** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 
 **per_page** | **int**| The number of advisories to return per page. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **state** | **str**| Filter by state of the repository advisories. Only advisories of this state will be returned. | [optional] 

### Return type

[**List[RepositoryAdvisory]**](RepositoryAdvisory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/scim+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**400** | Bad Request |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **security_advisories_update_repository_advisory**
> RepositoryAdvisory security_advisories_update_repository_advisory(owner, repo, ghsa_id, repository_advisory_update)

Update a repository security advisory

Update a repository security advisory using its GitHub Security Advisory (GHSA) identifier.  In order to update any security advisory, the authenticated user must be a security manager or administrator of that repository, or a collaborator on the repository security advisory.  OAuth app tokens and personal access tokens (classic) need the `repo` or `repository_advisories:write` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.repository_advisory import RepositoryAdvisory
from github_openapi.models.repository_advisory_update import RepositoryAdvisoryUpdate
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
    api_instance = github_openapi.SecurityAdvisoriesApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    ghsa_id = 'ghsa_id_example' # str | The GHSA (GitHub Security Advisory) identifier of the advisory.
    repository_advisory_update = {"severity":"critical","state":"published"} # RepositoryAdvisoryUpdate | 

    try:
        # Update a repository security advisory
        api_response = api_instance.security_advisories_update_repository_advisory(owner, repo, ghsa_id, repository_advisory_update)
        print("The response of SecurityAdvisoriesApi->security_advisories_update_repository_advisory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityAdvisoriesApi->security_advisories_update_repository_advisory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **ghsa_id** | **str**| The GHSA (GitHub Security Advisory) identifier of the advisory. | 
 **repository_advisory_update** | [**RepositoryAdvisoryUpdate**](RepositoryAdvisoryUpdate.md)|  | 

### Return type

[**RepositoryAdvisory**](RepositoryAdvisory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

