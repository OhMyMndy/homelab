# github_openapi.MigrationsApi

All URIs are relative to *https://api.github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**migrations_cancel_import**](MigrationsApi.md#migrations_cancel_import) | **DELETE** /repos/{owner}/{repo}/import | Cancel an import
[**migrations_delete_archive_for_authenticated_user**](MigrationsApi.md#migrations_delete_archive_for_authenticated_user) | **DELETE** /user/migrations/{migration_id}/archive | Delete a user migration archive
[**migrations_delete_archive_for_org**](MigrationsApi.md#migrations_delete_archive_for_org) | **DELETE** /orgs/{org}/migrations/{migration_id}/archive | Delete an organization migration archive
[**migrations_download_archive_for_org**](MigrationsApi.md#migrations_download_archive_for_org) | **GET** /orgs/{org}/migrations/{migration_id}/archive | Download an organization migration archive
[**migrations_get_archive_for_authenticated_user**](MigrationsApi.md#migrations_get_archive_for_authenticated_user) | **GET** /user/migrations/{migration_id}/archive | Download a user migration archive
[**migrations_get_commit_authors**](MigrationsApi.md#migrations_get_commit_authors) | **GET** /repos/{owner}/{repo}/import/authors | Get commit authors
[**migrations_get_import_status**](MigrationsApi.md#migrations_get_import_status) | **GET** /repos/{owner}/{repo}/import | Get an import status
[**migrations_get_large_files**](MigrationsApi.md#migrations_get_large_files) | **GET** /repos/{owner}/{repo}/import/large_files | Get large files
[**migrations_get_status_for_authenticated_user**](MigrationsApi.md#migrations_get_status_for_authenticated_user) | **GET** /user/migrations/{migration_id} | Get a user migration status
[**migrations_get_status_for_org**](MigrationsApi.md#migrations_get_status_for_org) | **GET** /orgs/{org}/migrations/{migration_id} | Get an organization migration status
[**migrations_list_for_authenticated_user**](MigrationsApi.md#migrations_list_for_authenticated_user) | **GET** /user/migrations | List user migrations
[**migrations_list_for_org**](MigrationsApi.md#migrations_list_for_org) | **GET** /orgs/{org}/migrations | List organization migrations
[**migrations_list_repos_for_authenticated_user**](MigrationsApi.md#migrations_list_repos_for_authenticated_user) | **GET** /user/migrations/{migration_id}/repositories | List repositories for a user migration
[**migrations_list_repos_for_org**](MigrationsApi.md#migrations_list_repos_for_org) | **GET** /orgs/{org}/migrations/{migration_id}/repositories | List repositories in an organization migration
[**migrations_map_commit_author**](MigrationsApi.md#migrations_map_commit_author) | **PATCH** /repos/{owner}/{repo}/import/authors/{author_id} | Map a commit author
[**migrations_set_lfs_preference**](MigrationsApi.md#migrations_set_lfs_preference) | **PATCH** /repos/{owner}/{repo}/import/lfs | Update Git LFS preference
[**migrations_start_for_authenticated_user**](MigrationsApi.md#migrations_start_for_authenticated_user) | **POST** /user/migrations | Start a user migration
[**migrations_start_for_org**](MigrationsApi.md#migrations_start_for_org) | **POST** /orgs/{org}/migrations | Start an organization migration
[**migrations_start_import**](MigrationsApi.md#migrations_start_import) | **PUT** /repos/{owner}/{repo}/import | Start an import
[**migrations_unlock_repo_for_authenticated_user**](MigrationsApi.md#migrations_unlock_repo_for_authenticated_user) | **DELETE** /user/migrations/{migration_id}/repos/{repo_name}/lock | Unlock a user repository
[**migrations_unlock_repo_for_org**](MigrationsApi.md#migrations_unlock_repo_for_org) | **DELETE** /orgs/{org}/migrations/{migration_id}/repos/{repo_name}/lock | Unlock an organization repository
[**migrations_update_import**](MigrationsApi.md#migrations_update_import) | **PATCH** /repos/{owner}/{repo}/import | Update an import


# **migrations_cancel_import**
> migrations_cancel_import(owner, repo)

Cancel an import

Stop an import for a repository.  > [!WARNING] > **Endpoint closing down notice:** Due to very low levels of usage and available alternatives, this endpoint is closing down and will no longer be available from 00:00 UTC on April 12, 2024. For more details and alternatives, see the [changelog](https://gh.io/source-imports-api-deprecation).

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
    api_instance = github_openapi.MigrationsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Cancel an import
        api_instance.migrations_cancel_import(owner, repo)
    except Exception as e:
        print("Exception when calling MigrationsApi->migrations_cancel_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |
**503** | Unavailable due to service under maintenance. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrations_delete_archive_for_authenticated_user**
> migrations_delete_archive_for_authenticated_user(migration_id)

Delete a user migration archive

Deletes a previous migration archive. Downloadable migration archives are automatically deleted after seven days. Migration metadata, which is returned in the [List user migrations](https://docs.github.com/rest/migrations/users#list-user-migrations) and [Get a user migration status](https://docs.github.com/rest/migrations/users#get-a-user-migration-status) endpoints, will continue to be available even after an archive is deleted.

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
    api_instance = github_openapi.MigrationsApi(api_client)
    migration_id = 56 # int | The unique identifier of the migration.

    try:
        # Delete a user migration archive
        api_instance.migrations_delete_archive_for_authenticated_user(migration_id)
    except Exception as e:
        print("Exception when calling MigrationsApi->migrations_delete_archive_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **migration_id** | **int**| The unique identifier of the migration. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |
**404** | Resource not found |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrations_delete_archive_for_org**
> migrations_delete_archive_for_org(org, migration_id)

Delete an organization migration archive

Deletes a previous migration archive. Migration archives are automatically deleted after seven days.

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
    api_instance = github_openapi.MigrationsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    migration_id = 56 # int | The unique identifier of the migration.

    try:
        # Delete an organization migration archive
        api_instance.migrations_delete_archive_for_org(org, migration_id)
    except Exception as e:
        print("Exception when calling MigrationsApi->migrations_delete_archive_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **migration_id** | **int**| The unique identifier of the migration. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrations_download_archive_for_org**
> migrations_download_archive_for_org(org, migration_id)

Download an organization migration archive

Fetches the URL to a migration archive.

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
    api_instance = github_openapi.MigrationsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    migration_id = 56 # int | The unique identifier of the migration.

    try:
        # Download an organization migration archive
        api_instance.migrations_download_archive_for_org(org, migration_id)
    except Exception as e:
        print("Exception when calling MigrationsApi->migrations_download_archive_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **migration_id** | **int**| The unique identifier of the migration. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrations_get_archive_for_authenticated_user**
> migrations_get_archive_for_authenticated_user(migration_id)

Download a user migration archive

Fetches the URL to download the migration archive as a `tar.gz` file. Depending on the resources your repository uses, the migration archive can contain JSON files with data for these objects:  *   attachments *   bases *   commit\\_comments *   issue\\_comments *   issue\\_events *   issues *   milestones *   organizations *   projects *   protected\\_branches *   pull\\_request\\_reviews *   pull\\_requests *   releases *   repositories *   review\\_comments *   schema *   users  The archive will also contain an `attachments` directory that includes all attachment files uploaded to GitHub.com and a `repositories` directory that contains the repository's Git data.

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
    api_instance = github_openapi.MigrationsApi(api_client)
    migration_id = 56 # int | The unique identifier of the migration.

    try:
        # Download a user migration archive
        api_instance.migrations_get_archive_for_authenticated_user(migration_id)
    except Exception as e:
        print("Exception when calling MigrationsApi->migrations_get_archive_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **migration_id** | **int**| The unique identifier of the migration. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Response |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrations_get_commit_authors**
> List[PorterAuthor] migrations_get_commit_authors(owner, repo, since=since)

Get commit authors

Each type of source control system represents authors in a different way. For example, a Git commit author has a display name and an email address, but a Subversion commit author just has a username. The GitHub Importer will make the author information valid, but the author might not be correct. For example, it will change the bare Subversion username `hubot` into something like `hubot <hubot@12341234-abab-fefe-8787-fedcba987654>`.  This endpoint and the [Map a commit author](https://docs.github.com/rest/migrations/source-imports#map-a-commit-author) endpoint allow you to provide correct Git author information.  > [!WARNING] > **Endpoint closing down notice:** Due to very low levels of usage and available alternatives, this endpoint is closing down and will no longer be available from 00:00 UTC on April 12, 2024. For more details and alternatives, see the [changelog](https://gh.io/source-imports-api-deprecation).

### Example


```python
import github_openapi
from github_openapi.models.porter_author import PorterAuthor
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
    api_instance = github_openapi.MigrationsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    since = 56 # int | A user ID. Only return users with an ID greater than this ID. (optional)

    try:
        # Get commit authors
        api_response = api_instance.migrations_get_commit_authors(owner, repo, since=since)
        print("The response of MigrationsApi->migrations_get_commit_authors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MigrationsApi->migrations_get_commit_authors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **since** | **int**| A user ID. Only return users with an ID greater than this ID. | [optional] 

### Return type

[**List[PorterAuthor]**](PorterAuthor.md)

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
**503** | Unavailable due to service under maintenance. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrations_get_import_status**
> ModelImport migrations_get_import_status(owner, repo)

Get an import status

View the progress of an import.  > [!WARNING] > **Endpoint closing down notice:** Due to very low levels of usage and available alternatives, this endpoint is closing down and will no longer be available from 00:00 UTC on April 12, 2024. For more details and alternatives, see the [changelog](https://gh.io/source-imports-api-deprecation).  **Import status**  This section includes details about the possible values of the `status` field of the Import Progress response.  An import that does not have errors will progress through these steps:  *   `detecting` - the \"detection\" step of the import is in progress because the request did not include a `vcs` parameter. The import is identifying the type of source control present at the URL. *   `importing` - the \"raw\" step of the import is in progress. This is where commit data is fetched from the original repository. The import progress response will include `commit_count` (the total number of raw commits that will be imported) and `percent` (0 - 100, the current progress through the import). *   `mapping` - the \"rewrite\" step of the import is in progress. This is where SVN branches are converted to Git branches, and where author updates are applied. The import progress response does not include progress information. *   `pushing` - the \"push\" step of the import is in progress. This is where the importer updates the repository on GitHub. The import progress response will include `push_percent`, which is the percent value reported by `git push` when it is \"Writing objects\". *   `complete` - the import is complete, and the repository is ready on GitHub.  If there are problems, you will see one of these in the `status` field:  *   `auth_failed` - the import requires authentication in order to connect to the original repository. To update authentication for the import, please see the [Update an import](https://docs.github.com/rest/migrations/source-imports#update-an-import) section. *   `error` - the import encountered an error. The import progress response will include the `failed_step` and an error message. Contact [GitHub Support](https://support.github.com/contact?tags=dotcom-rest-api) for more information. *   `detection_needs_auth` - the importer requires authentication for the originating repository to continue detection. To update authentication for the import, please see the [Update an import](https://docs.github.com/rest/migrations/source-imports#update-an-import) section. *   `detection_found_nothing` - the importer didn't recognize any source control at the URL. To resolve, [Cancel the import](https://docs.github.com/rest/migrations/source-imports#cancel-an-import) and [retry](https://docs.github.com/rest/migrations/source-imports#start-an-import) with the correct URL. *   `detection_found_multiple` - the importer found several projects or repositories at the provided URL. When this is the case, the Import Progress response will also include a `project_choices` field with the possible project choices as values. To update project choice, please see the [Update an import](https://docs.github.com/rest/migrations/source-imports#update-an-import) section.  **The project_choices field**  When multiple projects are found at the provided URL, the response hash will include a `project_choices` field, the value of which is an array of hashes each representing a project choice. The exact key/value pairs of the project hashes will differ depending on the version control type.  **Git LFS related fields**  This section includes details about Git LFS related fields that may be present in the Import Progress response.  *   `use_lfs` - describes whether the import has been opted in or out of using Git LFS. The value can be `opt_in`, `opt_out`, or `undecided` if no action has been taken. *   `has_large_files` - the boolean value describing whether files larger than 100MB were found during the `importing` step. *   `large_files_size` - the total size in gigabytes of files larger than 100MB found in the originating repository. *   `large_files_count` - the total number of files larger than 100MB found in the originating repository. To see a list of these files, make a \"Get Large Files\" request.

### Example


```python
import github_openapi
from github_openapi.models.model_import import ModelImport
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
    api_instance = github_openapi.MigrationsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Get an import status
        api_response = api_instance.migrations_get_import_status(owner, repo)
        print("The response of MigrationsApi->migrations_get_import_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MigrationsApi->migrations_get_import_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**ModelImport**](ModelImport.md)

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
**503** | Unavailable due to service under maintenance. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrations_get_large_files**
> List[PorterLargeFile] migrations_get_large_files(owner, repo)

Get large files

List files larger than 100MB found during the import  > [!WARNING] > **Endpoint closing down notice:** Due to very low levels of usage and available alternatives, this endpoint is closing down and will no longer be available from 00:00 UTC on April 12, 2024. For more details and alternatives, see the [changelog](https://gh.io/source-imports-api-deprecation).

### Example


```python
import github_openapi
from github_openapi.models.porter_large_file import PorterLargeFile
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
    api_instance = github_openapi.MigrationsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Get large files
        api_response = api_instance.migrations_get_large_files(owner, repo)
        print("The response of MigrationsApi->migrations_get_large_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MigrationsApi->migrations_get_large_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**List[PorterLargeFile]**](PorterLargeFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**503** | Unavailable due to service under maintenance. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrations_get_status_for_authenticated_user**
> Migration migrations_get_status_for_authenticated_user(migration_id, exclude=exclude)

Get a user migration status

Fetches a single user migration. The response includes the `state` of the migration, which can be one of the following values:  *   `pending` - the migration hasn't started yet. *   `exporting` - the migration is in progress. *   `exported` - the migration finished successfully. *   `failed` - the migration failed.  Once the migration has been `exported` you can [download the migration archive](https://docs.github.com/rest/migrations/users#download-a-user-migration-archive).

### Example


```python
import github_openapi
from github_openapi.models.migration import Migration
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
    api_instance = github_openapi.MigrationsApi(api_client)
    migration_id = 56 # int | The unique identifier of the migration.
    exclude = ['exclude_example'] # List[str] |  (optional)

    try:
        # Get a user migration status
        api_response = api_instance.migrations_get_status_for_authenticated_user(migration_id, exclude=exclude)
        print("The response of MigrationsApi->migrations_get_status_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MigrationsApi->migrations_get_status_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **migration_id** | **int**| The unique identifier of the migration. | 
 **exclude** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**Migration**](Migration.md)

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
**304** | Not modified |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrations_get_status_for_org**
> Migration migrations_get_status_for_org(org, migration_id, exclude=exclude)

Get an organization migration status

Fetches the status of a migration.  The `state` of a migration can be one of the following values:  *   `pending`, which means the migration hasn't started yet. *   `exporting`, which means the migration is in progress. *   `exported`, which means the migration finished successfully. *   `failed`, which means the migration failed.

### Example


```python
import github_openapi
from github_openapi.models.migration import Migration
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
    api_instance = github_openapi.MigrationsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    migration_id = 56 # int | The unique identifier of the migration.
    exclude = ['exclude_example'] # List[str] | Exclude attributes from the API response to improve performance (optional)

    try:
        # Get an organization migration status
        api_response = api_instance.migrations_get_status_for_org(org, migration_id, exclude=exclude)
        print("The response of MigrationsApi->migrations_get_status_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MigrationsApi->migrations_get_status_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **migration_id** | **int**| The unique identifier of the migration. | 
 **exclude** | [**List[str]**](str.md)| Exclude attributes from the API response to improve performance | [optional] 

### Return type

[**Migration**](Migration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | *   &#x60;pending&#x60;, which means the migration hasn&#39;t started yet. *   &#x60;exporting&#x60;, which means the migration is in progress. *   &#x60;exported&#x60;, which means the migration finished successfully. *   &#x60;failed&#x60;, which means the migration failed. |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrations_list_for_authenticated_user**
> List[Migration] migrations_list_for_authenticated_user(per_page=per_page, page=page)

List user migrations

Lists all migrations a user has started.

### Example


```python
import github_openapi
from github_openapi.models.migration import Migration
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
    api_instance = github_openapi.MigrationsApi(api_client)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List user migrations
        api_response = api_instance.migrations_list_for_authenticated_user(per_page=per_page, page=page)
        print("The response of MigrationsApi->migrations_list_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MigrationsApi->migrations_list_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Migration]**](Migration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrations_list_for_org**
> List[Migration] migrations_list_for_org(org, per_page=per_page, page=page, exclude=exclude)

List organization migrations

Lists the most recent migrations, including both exports (which can be started through the REST API) and imports (which cannot be started using the REST API).  A list of `repositories` is only returned for export migrations.

### Example


```python
import github_openapi
from github_openapi.models.migration import Migration
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
    api_instance = github_openapi.MigrationsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    exclude = ['exclude_example'] # List[str] | Exclude attributes from the API response to improve performance (optional)

    try:
        # List organization migrations
        api_response = api_instance.migrations_list_for_org(org, per_page=per_page, page=page, exclude=exclude)
        print("The response of MigrationsApi->migrations_list_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MigrationsApi->migrations_list_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **exclude** | [**List[str]**](str.md)| Exclude attributes from the API response to improve performance | [optional] 

### Return type

[**List[Migration]**](Migration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrations_list_repos_for_authenticated_user**
> List[MinimalRepository] migrations_list_repos_for_authenticated_user(migration_id, per_page=per_page, page=page)

List repositories for a user migration

Lists all the repositories for this user migration.

### Example


```python
import github_openapi
from github_openapi.models.minimal_repository import MinimalRepository
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
    api_instance = github_openapi.MigrationsApi(api_client)
    migration_id = 56 # int | The unique identifier of the migration.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List repositories for a user migration
        api_response = api_instance.migrations_list_repos_for_authenticated_user(migration_id, per_page=per_page, page=page)
        print("The response of MigrationsApi->migrations_list_repos_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MigrationsApi->migrations_list_repos_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **migration_id** | **int**| The unique identifier of the migration. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[MinimalRepository]**](MinimalRepository.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrations_list_repos_for_org**
> List[MinimalRepository] migrations_list_repos_for_org(org, migration_id, per_page=per_page, page=page)

List repositories in an organization migration

List all the repositories for this organization migration.

### Example


```python
import github_openapi
from github_openapi.models.minimal_repository import MinimalRepository
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
    api_instance = github_openapi.MigrationsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    migration_id = 56 # int | The unique identifier of the migration.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List repositories in an organization migration
        api_response = api_instance.migrations_list_repos_for_org(org, migration_id, per_page=per_page, page=page)
        print("The response of MigrationsApi->migrations_list_repos_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MigrationsApi->migrations_list_repos_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **migration_id** | **int**| The unique identifier of the migration. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[MinimalRepository]**](MinimalRepository.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrations_map_commit_author**
> PorterAuthor migrations_map_commit_author(owner, repo, author_id, migrations_map_commit_author_request=migrations_map_commit_author_request)

Map a commit author

Update an author's identity for the import. Your application can continue updating authors any time before you push new commits to the repository.  > [!WARNING] > **Endpoint closing down notice:** Due to very low levels of usage and available alternatives, this endpoint is closing down and will no longer be available from 00:00 UTC on April 12, 2024. For more details and alternatives, see the [changelog](https://gh.io/source-imports-api-deprecation).

### Example


```python
import github_openapi
from github_openapi.models.migrations_map_commit_author_request import MigrationsMapCommitAuthorRequest
from github_openapi.models.porter_author import PorterAuthor
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
    api_instance = github_openapi.MigrationsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    author_id = 56 # int | 
    migrations_map_commit_author_request = {"email":"hubot@github.com","name":"Hubot the Robot"} # MigrationsMapCommitAuthorRequest |  (optional)

    try:
        # Map a commit author
        api_response = api_instance.migrations_map_commit_author(owner, repo, author_id, migrations_map_commit_author_request=migrations_map_commit_author_request)
        print("The response of MigrationsApi->migrations_map_commit_author:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MigrationsApi->migrations_map_commit_author: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **author_id** | **int**|  | 
 **migrations_map_commit_author_request** | [**MigrationsMapCommitAuthorRequest**](MigrationsMapCommitAuthorRequest.md)|  | [optional] 

### Return type

[**PorterAuthor**](PorterAuthor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**404** | Resource not found |  -  |
**503** | Unavailable due to service under maintenance. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrations_set_lfs_preference**
> ModelImport migrations_set_lfs_preference(owner, repo, migrations_set_lfs_preference_request)

Update Git LFS preference

You can import repositories from Subversion, Mercurial, and TFS that include files larger than 100MB. This ability is powered by [Git LFS](https://git-lfs.com).  You can learn more about our LFS feature and working with large files [on our help site](https://docs.github.com/repositories/working-with-files/managing-large-files).  > [!WARNING] > **Endpoint closing down notice:** Due to very low levels of usage and available alternatives, this endpoint is closing down and will no longer be available from 00:00 UTC on April 12, 2024. For more details and alternatives, see the [changelog](https://gh.io/source-imports-api-deprecation).

### Example


```python
import github_openapi
from github_openapi.models.migrations_set_lfs_preference_request import MigrationsSetLfsPreferenceRequest
from github_openapi.models.model_import import ModelImport
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
    api_instance = github_openapi.MigrationsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    migrations_set_lfs_preference_request = {"use_lfs":"opt_in"} # MigrationsSetLfsPreferenceRequest | 

    try:
        # Update Git LFS preference
        api_response = api_instance.migrations_set_lfs_preference(owner, repo, migrations_set_lfs_preference_request)
        print("The response of MigrationsApi->migrations_set_lfs_preference:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MigrationsApi->migrations_set_lfs_preference: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **migrations_set_lfs_preference_request** | [**MigrationsSetLfsPreferenceRequest**](MigrationsSetLfsPreferenceRequest.md)|  | 

### Return type

[**ModelImport**](ModelImport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**503** | Unavailable due to service under maintenance. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrations_start_for_authenticated_user**
> Migration migrations_start_for_authenticated_user(migrations_start_for_authenticated_user_request)

Start a user migration

Initiates the generation of a user migration archive.

### Example


```python
import github_openapi
from github_openapi.models.migration import Migration
from github_openapi.models.migrations_start_for_authenticated_user_request import MigrationsStartForAuthenticatedUserRequest
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
    api_instance = github_openapi.MigrationsApi(api_client)
    migrations_start_for_authenticated_user_request = {"repositories":["octocat/Hello-World"],"lock_repositories":true} # MigrationsStartForAuthenticatedUserRequest | 

    try:
        # Start a user migration
        api_response = api_instance.migrations_start_for_authenticated_user(migrations_start_for_authenticated_user_request)
        print("The response of MigrationsApi->migrations_start_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MigrationsApi->migrations_start_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **migrations_start_for_authenticated_user_request** | [**MigrationsStartForAuthenticatedUserRequest**](MigrationsStartForAuthenticatedUserRequest.md)|  | 

### Return type

[**Migration**](Migration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrations_start_for_org**
> Migration migrations_start_for_org(org, migrations_start_for_org_request)

Start an organization migration

Initiates the generation of a migration archive.

### Example


```python
import github_openapi
from github_openapi.models.migration import Migration
from github_openapi.models.migrations_start_for_org_request import MigrationsStartForOrgRequest
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
    api_instance = github_openapi.MigrationsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    migrations_start_for_org_request = {"repositories":["github/Hello-World"],"lock_repositories":true} # MigrationsStartForOrgRequest | 

    try:
        # Start an organization migration
        api_response = api_instance.migrations_start_for_org(org, migrations_start_for_org_request)
        print("The response of MigrationsApi->migrations_start_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MigrationsApi->migrations_start_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **migrations_start_for_org_request** | [**MigrationsStartForOrgRequest**](MigrationsStartForOrgRequest.md)|  | 

### Return type

[**Migration**](Migration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrations_start_import**
> ModelImport migrations_start_import(owner, repo, migrations_start_import_request)

Start an import

Start a source import to a GitHub repository using GitHub Importer. Importing into a GitHub repository with GitHub Actions enabled is not supported and will return a status `422 Unprocessable Entity` response.  > [!WARNING] > **Endpoint closing down notice:** Due to very low levels of usage and available alternatives, this endpoint is closing down and will no longer be available from 00:00 UTC on April 12, 2024. For more details and alternatives, see the [changelog](https://gh.io/source-imports-api-deprecation).

### Example


```python
import github_openapi
from github_openapi.models.migrations_start_import_request import MigrationsStartImportRequest
from github_openapi.models.model_import import ModelImport
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
    api_instance = github_openapi.MigrationsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    migrations_start_import_request = {"vcs":"subversion","vcs_url":"http://svn.mycompany.com/svn/myproject","vcs_username":"octocat","vcs_password":"secret"} # MigrationsStartImportRequest | 

    try:
        # Start an import
        api_response = api_instance.migrations_start_import(owner, repo, migrations_start_import_request)
        print("The response of MigrationsApi->migrations_start_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MigrationsApi->migrations_start_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **migrations_start_import_request** | [**MigrationsStartImportRequest**](MigrationsStartImportRequest.md)|  | 

### Return type

[**ModelImport**](ModelImport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  * Location -  <br>  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**404** | Resource not found |  -  |
**503** | Unavailable due to service under maintenance. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrations_unlock_repo_for_authenticated_user**
> migrations_unlock_repo_for_authenticated_user(migration_id, repo_name)

Unlock a user repository

Unlocks a repository. You can lock repositories when you [start a user migration](https://docs.github.com/rest/migrations/users#start-a-user-migration). Once the migration is complete you can unlock each repository to begin using it again or [delete the repository](https://docs.github.com/rest/repos/repos#delete-a-repository) if you no longer need the source data. Returns a status of `404 Not Found` if the repository is not locked.

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
    api_instance = github_openapi.MigrationsApi(api_client)
    migration_id = 56 # int | The unique identifier of the migration.
    repo_name = 'repo_name_example' # str | repo_name parameter

    try:
        # Unlock a user repository
        api_instance.migrations_unlock_repo_for_authenticated_user(migration_id, repo_name)
    except Exception as e:
        print("Exception when calling MigrationsApi->migrations_unlock_repo_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **migration_id** | **int**| The unique identifier of the migration. | 
 **repo_name** | **str**| repo_name parameter | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |
**304** | Not modified |  -  |
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrations_unlock_repo_for_org**
> migrations_unlock_repo_for_org(org, migration_id, repo_name)

Unlock an organization repository

Unlocks a repository that was locked for migration. You should unlock each migrated repository and [delete them](https://docs.github.com/rest/repos/repos#delete-a-repository) when the migration is complete and you no longer need the source data.

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
    api_instance = github_openapi.MigrationsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    migration_id = 56 # int | The unique identifier of the migration.
    repo_name = 'repo_name_example' # str | repo_name parameter

    try:
        # Unlock an organization repository
        api_instance.migrations_unlock_repo_for_org(org, migration_id, repo_name)
    except Exception as e:
        print("Exception when calling MigrationsApi->migrations_unlock_repo_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **migration_id** | **int**| The unique identifier of the migration. | 
 **repo_name** | **str**| repo_name parameter | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **migrations_update_import**
> ModelImport migrations_update_import(owner, repo, migrations_update_import_request=migrations_update_import_request)

Update an import

An import can be updated with credentials or a project choice by passing in the appropriate parameters in this API request. If no parameters are provided, the import will be restarted.  Some servers (e.g. TFS servers) can have several projects at a single URL. In those cases the import progress will have the status `detection_found_multiple` and the Import Progress response will include a `project_choices` array. You can select the project to import by providing one of the objects in the `project_choices` array in the update request.  > [!WARNING] > **Endpoint closing down notice:** Due to very low levels of usage and available alternatives, this endpoint is closing down and will no longer be available from 00:00 UTC on April 12, 2024. For more details and alternatives, see the [changelog](https://gh.io/source-imports-api-deprecation).

### Example


```python
import github_openapi
from github_openapi.models.migrations_update_import_request import MigrationsUpdateImportRequest
from github_openapi.models.model_import import ModelImport
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
    api_instance = github_openapi.MigrationsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    migrations_update_import_request = {"vcs_username":"octocat","vcs_password":"secret"} # MigrationsUpdateImportRequest |  (optional)

    try:
        # Update an import
        api_response = api_instance.migrations_update_import(owner, repo, migrations_update_import_request=migrations_update_import_request)
        print("The response of MigrationsApi->migrations_update_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MigrationsApi->migrations_update_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **migrations_update_import_request** | [**MigrationsUpdateImportRequest**](MigrationsUpdateImportRequest.md)|  | [optional] 

### Return type

[**ModelImport**](ModelImport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**503** | Unavailable due to service under maintenance. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

