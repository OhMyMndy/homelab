# github_openapi.ActivityApi

All URIs are relative to *https://api.github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activity_check_repo_is_starred_by_authenticated_user**](ActivityApi.md#activity_check_repo_is_starred_by_authenticated_user) | **GET** /user/starred/{owner}/{repo} | Check if a repository is starred by the authenticated user
[**activity_delete_repo_subscription**](ActivityApi.md#activity_delete_repo_subscription) | **DELETE** /repos/{owner}/{repo}/subscription | Delete a repository subscription
[**activity_delete_thread_subscription**](ActivityApi.md#activity_delete_thread_subscription) | **DELETE** /notifications/threads/{thread_id}/subscription | Delete a thread subscription
[**activity_get_feeds**](ActivityApi.md#activity_get_feeds) | **GET** /feeds | Get feeds
[**activity_get_repo_subscription**](ActivityApi.md#activity_get_repo_subscription) | **GET** /repos/{owner}/{repo}/subscription | Get a repository subscription
[**activity_get_thread**](ActivityApi.md#activity_get_thread) | **GET** /notifications/threads/{thread_id} | Get a thread
[**activity_get_thread_subscription_for_authenticated_user**](ActivityApi.md#activity_get_thread_subscription_for_authenticated_user) | **GET** /notifications/threads/{thread_id}/subscription | Get a thread subscription for the authenticated user
[**activity_list_events_for_authenticated_user**](ActivityApi.md#activity_list_events_for_authenticated_user) | **GET** /users/{username}/events | List events for the authenticated user
[**activity_list_notifications_for_authenticated_user**](ActivityApi.md#activity_list_notifications_for_authenticated_user) | **GET** /notifications | List notifications for the authenticated user
[**activity_list_org_events_for_authenticated_user**](ActivityApi.md#activity_list_org_events_for_authenticated_user) | **GET** /users/{username}/events/orgs/{org} | List organization events for the authenticated user
[**activity_list_public_events**](ActivityApi.md#activity_list_public_events) | **GET** /events | List public events
[**activity_list_public_events_for_repo_network**](ActivityApi.md#activity_list_public_events_for_repo_network) | **GET** /networks/{owner}/{repo}/events | List public events for a network of repositories
[**activity_list_public_events_for_user**](ActivityApi.md#activity_list_public_events_for_user) | **GET** /users/{username}/events/public | List public events for a user
[**activity_list_public_org_events**](ActivityApi.md#activity_list_public_org_events) | **GET** /orgs/{org}/events | List public organization events
[**activity_list_received_events_for_user**](ActivityApi.md#activity_list_received_events_for_user) | **GET** /users/{username}/received_events | List events received by the authenticated user
[**activity_list_received_public_events_for_user**](ActivityApi.md#activity_list_received_public_events_for_user) | **GET** /users/{username}/received_events/public | List public events received by a user
[**activity_list_repo_events**](ActivityApi.md#activity_list_repo_events) | **GET** /repos/{owner}/{repo}/events | List repository events
[**activity_list_repo_notifications_for_authenticated_user**](ActivityApi.md#activity_list_repo_notifications_for_authenticated_user) | **GET** /repos/{owner}/{repo}/notifications | List repository notifications for the authenticated user
[**activity_list_repos_starred_by_authenticated_user**](ActivityApi.md#activity_list_repos_starred_by_authenticated_user) | **GET** /user/starred | List repositories starred by the authenticated user
[**activity_list_repos_starred_by_user**](ActivityApi.md#activity_list_repos_starred_by_user) | **GET** /users/{username}/starred | List repositories starred by a user
[**activity_list_repos_watched_by_user**](ActivityApi.md#activity_list_repos_watched_by_user) | **GET** /users/{username}/subscriptions | List repositories watched by a user
[**activity_list_stargazers_for_repo**](ActivityApi.md#activity_list_stargazers_for_repo) | **GET** /repos/{owner}/{repo}/stargazers | List stargazers
[**activity_list_watched_repos_for_authenticated_user**](ActivityApi.md#activity_list_watched_repos_for_authenticated_user) | **GET** /user/subscriptions | List repositories watched by the authenticated user
[**activity_list_watchers_for_repo**](ActivityApi.md#activity_list_watchers_for_repo) | **GET** /repos/{owner}/{repo}/subscribers | List watchers
[**activity_mark_notifications_as_read**](ActivityApi.md#activity_mark_notifications_as_read) | **PUT** /notifications | Mark notifications as read
[**activity_mark_repo_notifications_as_read**](ActivityApi.md#activity_mark_repo_notifications_as_read) | **PUT** /repos/{owner}/{repo}/notifications | Mark repository notifications as read
[**activity_mark_thread_as_done**](ActivityApi.md#activity_mark_thread_as_done) | **DELETE** /notifications/threads/{thread_id} | Mark a thread as done
[**activity_mark_thread_as_read**](ActivityApi.md#activity_mark_thread_as_read) | **PATCH** /notifications/threads/{thread_id} | Mark a thread as read
[**activity_set_repo_subscription**](ActivityApi.md#activity_set_repo_subscription) | **PUT** /repos/{owner}/{repo}/subscription | Set a repository subscription
[**activity_set_thread_subscription**](ActivityApi.md#activity_set_thread_subscription) | **PUT** /notifications/threads/{thread_id}/subscription | Set a thread subscription
[**activity_star_repo_for_authenticated_user**](ActivityApi.md#activity_star_repo_for_authenticated_user) | **PUT** /user/starred/{owner}/{repo} | Star a repository for the authenticated user
[**activity_unstar_repo_for_authenticated_user**](ActivityApi.md#activity_unstar_repo_for_authenticated_user) | **DELETE** /user/starred/{owner}/{repo} | Unstar a repository for the authenticated user


# **activity_check_repo_is_starred_by_authenticated_user**
> activity_check_repo_is_starred_by_authenticated_user(owner, repo)

Check if a repository is starred by the authenticated user

Whether the authenticated user has starred the repository.

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
    api_instance = github_openapi.ActivityApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Check if a repository is starred by the authenticated user
        api_instance.activity_check_repo_is_starred_by_authenticated_user(owner, repo)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_check_repo_is_starred_by_authenticated_user: %s\n" % e)
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
**204** | Response if this repository is starred by you |  -  |
**404** | Not Found if this repository is not starred by you |  -  |
**401** | Requires authentication |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activity_delete_repo_subscription**
> activity_delete_repo_subscription(owner, repo)

Delete a repository subscription

This endpoint should only be used to stop watching a repository. To control whether or not you wish to receive notifications from a repository, [set the repository's subscription manually](https://docs.github.com/rest/activity/watching#set-a-repository-subscription).

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
    api_instance = github_openapi.ActivityApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Delete a repository subscription
        api_instance.activity_delete_repo_subscription(owner, repo)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_delete_repo_subscription: %s\n" % e)
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
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activity_delete_thread_subscription**
> activity_delete_thread_subscription(thread_id)

Delete a thread subscription

Mutes all future notifications for a conversation until you comment on the thread or get an **@mention**. If you are watching the repository of the thread, you will still receive notifications. To ignore future notifications for a repository you are watching, use the [Set a thread subscription](https://docs.github.com/rest/activity/notifications#set-a-thread-subscription) endpoint and set `ignore` to `true`.

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
    api_instance = github_openapi.ActivityApi(api_client)
    thread_id = 56 # int | The unique identifier of the notification thread. This corresponds to the value returned in the `id` field when you retrieve notifications (for example with the [`GET /notifications` operation](https://docs.github.com/rest/activity/notifications#list-notifications-for-the-authenticated-user)).

    try:
        # Delete a thread subscription
        api_instance.activity_delete_thread_subscription(thread_id)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_delete_thread_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **int**| The unique identifier of the notification thread. This corresponds to the value returned in the &#x60;id&#x60; field when you retrieve notifications (for example with the [&#x60;GET /notifications&#x60; operation](https://docs.github.com/rest/activity/notifications#list-notifications-for-the-authenticated-user)). | 

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
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activity_get_feeds**
> Feed activity_get_feeds()

Get feeds

Lists the feeds available to the authenticated user. The response provides a URL for each feed. You can then get a specific feed by sending a request to one of the feed URLs.  *   **Timeline**: The GitHub global public timeline *   **User**: The public timeline for any user, using `uri_template`. For more information, see \"[Hypermedia](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#hypermedia).\" *   **Current user public**: The public timeline for the authenticated user *   **Current user**: The private timeline for the authenticated user *   **Current user actor**: The private timeline for activity created by the authenticated user *   **Current user organizations**: The private timeline for the organizations the authenticated user is a member of. *   **Security advisories**: A collection of public announcements that provide information about security-related vulnerabilities in software on GitHub.  By default, timeline resources are returned in JSON. You can specify the `application/atom+xml` type in the `Accept` header to return timeline resources in Atom format. For more information, see \"[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types).\"  > [!NOTE] > Private feeds are only returned when [authenticating via Basic Auth](https://docs.github.com/rest/authentication/authenticating-to-the-rest-api#using-basic-authentication) since current feed URIs use the older, non revocable auth tokens.

### Example


```python
import github_openapi
from github_openapi.models.feed import Feed
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
    api_instance = github_openapi.ActivityApi(api_client)

    try:
        # Get feeds
        api_response = api_instance.activity_get_feeds()
        print("The response of ActivityApi->activity_get_feeds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_get_feeds: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Feed**](Feed.md)

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

# **activity_get_repo_subscription**
> RepositorySubscription activity_get_repo_subscription(owner, repo)

Get a repository subscription

Gets information about whether the authenticated user is subscribed to the repository.

### Example


```python
import github_openapi
from github_openapi.models.repository_subscription import RepositorySubscription
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
    api_instance = github_openapi.ActivityApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Get a repository subscription
        api_response = api_instance.activity_get_repo_subscription(owner, repo)
        print("The response of ActivityApi->activity_get_repo_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_get_repo_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**RepositorySubscription**](RepositorySubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | if you subscribe to the repository |  -  |
**404** | Not Found if you don&#39;t subscribe to the repository |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activity_get_thread**
> Thread activity_get_thread(thread_id)

Get a thread

Gets information about a notification thread.

### Example


```python
import github_openapi
from github_openapi.models.thread import Thread
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
    api_instance = github_openapi.ActivityApi(api_client)
    thread_id = 56 # int | The unique identifier of the notification thread. This corresponds to the value returned in the `id` field when you retrieve notifications (for example with the [`GET /notifications` operation](https://docs.github.com/rest/activity/notifications#list-notifications-for-the-authenticated-user)).

    try:
        # Get a thread
        api_response = api_instance.activity_get_thread(thread_id)
        print("The response of ActivityApi->activity_get_thread:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_get_thread: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **int**| The unique identifier of the notification thread. This corresponds to the value returned in the &#x60;id&#x60; field when you retrieve notifications (for example with the [&#x60;GET /notifications&#x60; operation](https://docs.github.com/rest/activity/notifications#list-notifications-for-the-authenticated-user)). | 

### Return type

[**Thread**](Thread.md)

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
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activity_get_thread_subscription_for_authenticated_user**
> ThreadSubscription activity_get_thread_subscription_for_authenticated_user(thread_id)

Get a thread subscription for the authenticated user

This checks to see if the current user is subscribed to a thread. You can also [get a repository subscription](https://docs.github.com/rest/activity/watching#get-a-repository-subscription).  Note that subscriptions are only generated if a user is participating in a conversation--for example, they've replied to the thread, were **@mentioned**, or manually subscribe to a thread.

### Example


```python
import github_openapi
from github_openapi.models.thread_subscription import ThreadSubscription
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
    api_instance = github_openapi.ActivityApi(api_client)
    thread_id = 56 # int | The unique identifier of the notification thread. This corresponds to the value returned in the `id` field when you retrieve notifications (for example with the [`GET /notifications` operation](https://docs.github.com/rest/activity/notifications#list-notifications-for-the-authenticated-user)).

    try:
        # Get a thread subscription for the authenticated user
        api_response = api_instance.activity_get_thread_subscription_for_authenticated_user(thread_id)
        print("The response of ActivityApi->activity_get_thread_subscription_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_get_thread_subscription_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **int**| The unique identifier of the notification thread. This corresponds to the value returned in the &#x60;id&#x60; field when you retrieve notifications (for example with the [&#x60;GET /notifications&#x60; operation](https://docs.github.com/rest/activity/notifications#list-notifications-for-the-authenticated-user)). | 

### Return type

[**ThreadSubscription**](ThreadSubscription.md)

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
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activity_list_events_for_authenticated_user**
> List[Event] activity_list_events_for_authenticated_user(username, per_page=per_page, page=page)

List events for the authenticated user

If you are authenticated as the given user, you will see your private events. Otherwise, you'll only see public events. _Optional_: use the fine-grained token with following permission set to view private events: \"Events\" user permissions (read).  > [!NOTE] > This API is not built to serve real-time use cases. Depending on the time of day, event latency can be anywhere from 30s to 6h.

### Example


```python
import github_openapi
from github_openapi.models.event import Event
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
    api_instance = github_openapi.ActivityApi(api_client)
    username = 'username_example' # str | The handle for the GitHub user account.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List events for the authenticated user
        api_response = api_instance.activity_list_events_for_authenticated_user(username, per_page=per_page, page=page)
        print("The response of ActivityApi->activity_list_events_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_list_events_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The handle for the GitHub user account. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Event]**](Event.md)

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

# **activity_list_notifications_for_authenticated_user**
> List[Thread] activity_list_notifications_for_authenticated_user(all=all, participating=participating, since=since, before=before, page=page, per_page=per_page)

List notifications for the authenticated user

List all notifications for the current user, sorted by most recently updated.

### Example


```python
import github_openapi
from github_openapi.models.thread import Thread
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
    api_instance = github_openapi.ActivityApi(api_client)
    all = False # bool | If `true`, show notifications marked as read. (optional) (default to False)
    participating = False # bool | If `true`, only shows notifications in which the user is directly participating or mentioned. (optional) (default to False)
    since = '2013-10-20T19:20:30+01:00' # datetime | Only show results that were last updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. (optional)
    before = '2013-10-20T19:20:30+01:00' # datetime | Only show notifications updated before the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. (optional)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    per_page = 50 # int | The number of results per page (max 50). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 50)

    try:
        # List notifications for the authenticated user
        api_response = api_instance.activity_list_notifications_for_authenticated_user(all=all, participating=participating, since=since, before=before, page=page, per_page=per_page)
        print("The response of ActivityApi->activity_list_notifications_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_list_notifications_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all** | **bool**| If &#x60;true&#x60;, show notifications marked as read. | [optional] [default to False]
 **participating** | **bool**| If &#x60;true&#x60;, only shows notifications in which the user is directly participating or mentioned. | [optional] [default to False]
 **since** | **datetime**| Only show results that were last updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
 **before** | **datetime**| Only show notifications updated before the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **per_page** | **int**| The number of results per page (max 50). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 50]

### Return type

[**List[Thread]**](Thread.md)

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
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activity_list_org_events_for_authenticated_user**
> List[Event] activity_list_org_events_for_authenticated_user(username, org, per_page=per_page, page=page)

List organization events for the authenticated user

This is the user's organization dashboard. You must be authenticated as the user to view this.  > [!NOTE] > This API is not built to serve real-time use cases. Depending on the time of day, event latency can be anywhere from 30s to 6h.

### Example


```python
import github_openapi
from github_openapi.models.event import Event
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
    api_instance = github_openapi.ActivityApi(api_client)
    username = 'username_example' # str | The handle for the GitHub user account.
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List organization events for the authenticated user
        api_response = api_instance.activity_list_org_events_for_authenticated_user(username, org, per_page=per_page, page=page)
        print("The response of ActivityApi->activity_list_org_events_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_list_org_events_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The handle for the GitHub user account. | 
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Event]**](Event.md)

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

# **activity_list_public_events**
> List[Event] activity_list_public_events(per_page=per_page, page=page)

List public events

> [!NOTE] > This API is not built to serve real-time use cases. Depending on the time of day, event latency can be anywhere from 30s to 6h.

### Example


```python
import github_openapi
from github_openapi.models.event import Event
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
    api_instance = github_openapi.ActivityApi(api_client)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List public events
        api_response = api_instance.activity_list_public_events(per_page=per_page, page=page)
        print("The response of ActivityApi->activity_list_public_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_list_public_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Event]**](Event.md)

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
**403** | Forbidden |  -  |
**503** | Service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activity_list_public_events_for_repo_network**
> List[Event] activity_list_public_events_for_repo_network(owner, repo, per_page=per_page, page=page)

List public events for a network of repositories

> [!NOTE] > This API is not built to serve real-time use cases. Depending on the time of day, event latency can be anywhere from 30s to 6h.

### Example


```python
import github_openapi
from github_openapi.models.event import Event
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
    api_instance = github_openapi.ActivityApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List public events for a network of repositories
        api_response = api_instance.activity_list_public_events_for_repo_network(owner, repo, per_page=per_page, page=page)
        print("The response of ActivityApi->activity_list_public_events_for_repo_network:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_list_public_events_for_repo_network: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Event]**](Event.md)

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
**403** | Forbidden |  -  |
**304** | Not modified |  -  |
**301** | Moved permanently |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activity_list_public_events_for_user**
> List[Event] activity_list_public_events_for_user(username, per_page=per_page, page=page)

List public events for a user

> [!NOTE] > This API is not built to serve real-time use cases. Depending on the time of day, event latency can be anywhere from 30s to 6h.

### Example


```python
import github_openapi
from github_openapi.models.event import Event
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
    api_instance = github_openapi.ActivityApi(api_client)
    username = 'username_example' # str | The handle for the GitHub user account.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List public events for a user
        api_response = api_instance.activity_list_public_events_for_user(username, per_page=per_page, page=page)
        print("The response of ActivityApi->activity_list_public_events_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_list_public_events_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The handle for the GitHub user account. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Event]**](Event.md)

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

# **activity_list_public_org_events**
> List[Event] activity_list_public_org_events(org, per_page=per_page, page=page)

List public organization events

> [!NOTE] > This API is not built to serve real-time use cases. Depending on the time of day, event latency can be anywhere from 30s to 6h.

### Example


```python
import github_openapi
from github_openapi.models.event import Event
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
    api_instance = github_openapi.ActivityApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List public organization events
        api_response = api_instance.activity_list_public_org_events(org, per_page=per_page, page=page)
        print("The response of ActivityApi->activity_list_public_org_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_list_public_org_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Event]**](Event.md)

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

# **activity_list_received_events_for_user**
> List[Event] activity_list_received_events_for_user(username, per_page=per_page, page=page)

List events received by the authenticated user

These are events that you've received by watching repositories and following users. If you are authenticated as the given user, you will see private events. Otherwise, you'll only see public events.  > [!NOTE] > This API is not built to serve real-time use cases. Depending on the time of day, event latency can be anywhere from 30s to 6h.

### Example


```python
import github_openapi
from github_openapi.models.event import Event
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
    api_instance = github_openapi.ActivityApi(api_client)
    username = 'username_example' # str | The handle for the GitHub user account.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List events received by the authenticated user
        api_response = api_instance.activity_list_received_events_for_user(username, per_page=per_page, page=page)
        print("The response of ActivityApi->activity_list_received_events_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_list_received_events_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The handle for the GitHub user account. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Event]**](Event.md)

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

# **activity_list_received_public_events_for_user**
> List[Event] activity_list_received_public_events_for_user(username, per_page=per_page, page=page)

List public events received by a user

> [!NOTE] > This API is not built to serve real-time use cases. Depending on the time of day, event latency can be anywhere from 30s to 6h.

### Example


```python
import github_openapi
from github_openapi.models.event import Event
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
    api_instance = github_openapi.ActivityApi(api_client)
    username = 'username_example' # str | The handle for the GitHub user account.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List public events received by a user
        api_response = api_instance.activity_list_received_public_events_for_user(username, per_page=per_page, page=page)
        print("The response of ActivityApi->activity_list_received_public_events_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_list_received_public_events_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The handle for the GitHub user account. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Event]**](Event.md)

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

# **activity_list_repo_events**
> List[Event] activity_list_repo_events(owner, repo, per_page=per_page, page=page)

List repository events

> [!NOTE] > This API is not built to serve real-time use cases. Depending on the time of day, event latency can be anywhere from 30s to 6h.

### Example


```python
import github_openapi
from github_openapi.models.event import Event
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
    api_instance = github_openapi.ActivityApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List repository events
        api_response = api_instance.activity_list_repo_events(owner, repo, per_page=per_page, page=page)
        print("The response of ActivityApi->activity_list_repo_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_list_repo_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Event]**](Event.md)

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

# **activity_list_repo_notifications_for_authenticated_user**
> List[Thread] activity_list_repo_notifications_for_authenticated_user(owner, repo, all=all, participating=participating, since=since, before=before, per_page=per_page, page=page)

List repository notifications for the authenticated user

Lists all notifications for the current user in the specified repository.

### Example


```python
import github_openapi
from github_openapi.models.thread import Thread
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
    api_instance = github_openapi.ActivityApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    all = False # bool | If `true`, show notifications marked as read. (optional) (default to False)
    participating = False # bool | If `true`, only shows notifications in which the user is directly participating or mentioned. (optional) (default to False)
    since = '2013-10-20T19:20:30+01:00' # datetime | Only show results that were last updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. (optional)
    before = '2013-10-20T19:20:30+01:00' # datetime | Only show notifications updated before the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. (optional)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List repository notifications for the authenticated user
        api_response = api_instance.activity_list_repo_notifications_for_authenticated_user(owner, repo, all=all, participating=participating, since=since, before=before, per_page=per_page, page=page)
        print("The response of ActivityApi->activity_list_repo_notifications_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_list_repo_notifications_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **all** | **bool**| If &#x60;true&#x60;, show notifications marked as read. | [optional] [default to False]
 **participating** | **bool**| If &#x60;true&#x60;, only shows notifications in which the user is directly participating or mentioned. | [optional] [default to False]
 **since** | **datetime**| Only show results that were last updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
 **before** | **datetime**| Only show notifications updated before the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Thread]**](Thread.md)

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

# **activity_list_repos_starred_by_authenticated_user**
> List[Repository] activity_list_repos_starred_by_authenticated_user(sort=sort, direction=direction, per_page=per_page, page=page)

List repositories starred by the authenticated user

Lists repositories the authenticated user has starred.  This endpoint supports the following custom media types. For more information, see \"[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types).\"  - **`application/vnd.github.star+json`**: Includes a timestamp of when the star was created.

### Example


```python
import github_openapi
from github_openapi.models.repository import Repository
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
    api_instance = github_openapi.ActivityApi(api_client)
    sort = created # str | The property to sort the results by. `created` means when the repository was starred. `updated` means when the repository was last pushed to. (optional) (default to created)
    direction = desc # str | The direction to sort the results by. (optional) (default to desc)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List repositories starred by the authenticated user
        api_response = api_instance.activity_list_repos_starred_by_authenticated_user(sort=sort, direction=direction, per_page=per_page, page=page)
        print("The response of ActivityApi->activity_list_repos_starred_by_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_list_repos_starred_by_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The property to sort the results by. &#x60;created&#x60; means when the repository was starred. &#x60;updated&#x60; means when the repository was last pushed to. | [optional] [default to created]
 **direction** | **str**| The direction to sort the results by. | [optional] [default to desc]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Repository]**](Repository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.github.v3.star+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activity_list_repos_starred_by_user**
> ActivityListReposStarredByUser200Response activity_list_repos_starred_by_user(username, sort=sort, direction=direction, per_page=per_page, page=page)

List repositories starred by a user

Lists repositories a user has starred.  This endpoint supports the following custom media types. For more information, see \"[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types).\"  - **`application/vnd.github.star+json`**: Includes a timestamp of when the star was created.

### Example


```python
import github_openapi
from github_openapi.models.activity_list_repos_starred_by_user200_response import ActivityListReposStarredByUser200Response
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
    api_instance = github_openapi.ActivityApi(api_client)
    username = 'username_example' # str | The handle for the GitHub user account.
    sort = created # str | The property to sort the results by. `created` means when the repository was starred. `updated` means when the repository was last pushed to. (optional) (default to created)
    direction = desc # str | The direction to sort the results by. (optional) (default to desc)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List repositories starred by a user
        api_response = api_instance.activity_list_repos_starred_by_user(username, sort=sort, direction=direction, per_page=per_page, page=page)
        print("The response of ActivityApi->activity_list_repos_starred_by_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_list_repos_starred_by_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The handle for the GitHub user account. | 
 **sort** | **str**| The property to sort the results by. &#x60;created&#x60; means when the repository was starred. &#x60;updated&#x60; means when the repository was last pushed to. | [optional] [default to created]
 **direction** | **str**| The direction to sort the results by. | [optional] [default to desc]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**ActivityListReposStarredByUser200Response**](ActivityListReposStarredByUser200Response.md)

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

# **activity_list_repos_watched_by_user**
> List[MinimalRepository] activity_list_repos_watched_by_user(username, per_page=per_page, page=page)

List repositories watched by a user

Lists repositories a user is watching.

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
    api_instance = github_openapi.ActivityApi(api_client)
    username = 'username_example' # str | The handle for the GitHub user account.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List repositories watched by a user
        api_response = api_instance.activity_list_repos_watched_by_user(username, per_page=per_page, page=page)
        print("The response of ActivityApi->activity_list_repos_watched_by_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_list_repos_watched_by_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The handle for the GitHub user account. | 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activity_list_stargazers_for_repo**
> ActivityListStargazersForRepo200Response activity_list_stargazers_for_repo(owner, repo, per_page=per_page, page=page)

List stargazers

Lists the people that have starred the repository.  This endpoint supports the following custom media types. For more information, see \"[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types).\"  - **`application/vnd.github.star+json`**: Includes a timestamp of when the star was created.

### Example


```python
import github_openapi
from github_openapi.models.activity_list_stargazers_for_repo200_response import ActivityListStargazersForRepo200Response
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
    api_instance = github_openapi.ActivityApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List stargazers
        api_response = api_instance.activity_list_stargazers_for_repo(owner, repo, per_page=per_page, page=page)
        print("The response of ActivityApi->activity_list_stargazers_for_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_list_stargazers_for_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**ActivityListStargazersForRepo200Response**](ActivityListStargazersForRepo200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activity_list_watched_repos_for_authenticated_user**
> List[MinimalRepository] activity_list_watched_repos_for_authenticated_user(per_page=per_page, page=page)

List repositories watched by the authenticated user

Lists repositories the authenticated user is watching.

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
    api_instance = github_openapi.ActivityApi(api_client)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List repositories watched by the authenticated user
        api_response = api_instance.activity_list_watched_repos_for_authenticated_user(per_page=per_page, page=page)
        print("The response of ActivityApi->activity_list_watched_repos_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_list_watched_repos_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**304** | Not modified |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activity_list_watchers_for_repo**
> List[SimpleUser] activity_list_watchers_for_repo(owner, repo, per_page=per_page, page=page)

List watchers

Lists the people watching the specified repository.

### Example


```python
import github_openapi
from github_openapi.models.simple_user import SimpleUser
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
    api_instance = github_openapi.ActivityApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List watchers
        api_response = api_instance.activity_list_watchers_for_repo(owner, repo, per_page=per_page, page=page)
        print("The response of ActivityApi->activity_list_watchers_for_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_list_watchers_for_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[SimpleUser]**](SimpleUser.md)

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

# **activity_mark_notifications_as_read**
> ActivityMarkNotificationsAsRead202Response activity_mark_notifications_as_read(activity_mark_notifications_as_read_request=activity_mark_notifications_as_read_request)

Mark notifications as read

Marks all notifications as \"read\" for the current user. If the number of notifications is too large to complete in one request, you will receive a `202 Accepted` status and GitHub will run an asynchronous process to mark notifications as \"read.\" To check whether any \"unread\" notifications remain, you can use the [List notifications for the authenticated user](https://docs.github.com/rest/activity/notifications#list-notifications-for-the-authenticated-user) endpoint and pass the query parameter `all=false`.

### Example


```python
import github_openapi
from github_openapi.models.activity_mark_notifications_as_read202_response import ActivityMarkNotificationsAsRead202Response
from github_openapi.models.activity_mark_notifications_as_read_request import ActivityMarkNotificationsAsReadRequest
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
    api_instance = github_openapi.ActivityApi(api_client)
    activity_mark_notifications_as_read_request = {"last_read_at":"2022-06-10T00:00:00Z","read":true} # ActivityMarkNotificationsAsReadRequest |  (optional)

    try:
        # Mark notifications as read
        api_response = api_instance.activity_mark_notifications_as_read(activity_mark_notifications_as_read_request=activity_mark_notifications_as_read_request)
        print("The response of ActivityApi->activity_mark_notifications_as_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_mark_notifications_as_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_mark_notifications_as_read_request** | [**ActivityMarkNotificationsAsReadRequest**](ActivityMarkNotificationsAsReadRequest.md)|  | [optional] 

### Return type

[**ActivityMarkNotificationsAsRead202Response**](ActivityMarkNotificationsAsRead202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Response |  -  |
**205** | Reset Content |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activity_mark_repo_notifications_as_read**
> ActivityMarkRepoNotificationsAsRead202Response activity_mark_repo_notifications_as_read(owner, repo, activity_mark_repo_notifications_as_read_request=activity_mark_repo_notifications_as_read_request)

Mark repository notifications as read

Marks all notifications in a repository as \"read\" for the current user. If the number of notifications is too large to complete in one request, you will receive a `202 Accepted` status and GitHub will run an asynchronous process to mark notifications as \"read.\" To check whether any \"unread\" notifications remain, you can use the [List repository notifications for the authenticated user](https://docs.github.com/rest/activity/notifications#list-repository-notifications-for-the-authenticated-user) endpoint and pass the query parameter `all=false`.

### Example


```python
import github_openapi
from github_openapi.models.activity_mark_repo_notifications_as_read202_response import ActivityMarkRepoNotificationsAsRead202Response
from github_openapi.models.activity_mark_repo_notifications_as_read_request import ActivityMarkRepoNotificationsAsReadRequest
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
    api_instance = github_openapi.ActivityApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    activity_mark_repo_notifications_as_read_request = {"last_read_at":"2019-01-01T00:00:00Z"} # ActivityMarkRepoNotificationsAsReadRequest |  (optional)

    try:
        # Mark repository notifications as read
        api_response = api_instance.activity_mark_repo_notifications_as_read(owner, repo, activity_mark_repo_notifications_as_read_request=activity_mark_repo_notifications_as_read_request)
        print("The response of ActivityApi->activity_mark_repo_notifications_as_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_mark_repo_notifications_as_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **activity_mark_repo_notifications_as_read_request** | [**ActivityMarkRepoNotificationsAsReadRequest**](ActivityMarkRepoNotificationsAsReadRequest.md)|  | [optional] 

### Return type

[**ActivityMarkRepoNotificationsAsRead202Response**](ActivityMarkRepoNotificationsAsRead202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Response |  -  |
**205** | Reset Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activity_mark_thread_as_done**
> activity_mark_thread_as_done(thread_id)

Mark a thread as done

Marks a thread as \"done.\" Marking a thread as \"done\" is equivalent to marking a notification in your notification inbox on GitHub as done: https://github.com/notifications.

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
    api_instance = github_openapi.ActivityApi(api_client)
    thread_id = 56 # int | The unique identifier of the notification thread. This corresponds to the value returned in the `id` field when you retrieve notifications (for example with the [`GET /notifications` operation](https://docs.github.com/rest/activity/notifications#list-notifications-for-the-authenticated-user)).

    try:
        # Mark a thread as done
        api_instance.activity_mark_thread_as_done(thread_id)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_mark_thread_as_done: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **int**| The unique identifier of the notification thread. This corresponds to the value returned in the &#x60;id&#x60; field when you retrieve notifications (for example with the [&#x60;GET /notifications&#x60; operation](https://docs.github.com/rest/activity/notifications#list-notifications-for-the-authenticated-user)). | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activity_mark_thread_as_read**
> activity_mark_thread_as_read(thread_id)

Mark a thread as read

Marks a thread as \"read.\" Marking a thread as \"read\" is equivalent to clicking a notification in your notification inbox on GitHub: https://github.com/notifications.

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
    api_instance = github_openapi.ActivityApi(api_client)
    thread_id = 56 # int | The unique identifier of the notification thread. This corresponds to the value returned in the `id` field when you retrieve notifications (for example with the [`GET /notifications` operation](https://docs.github.com/rest/activity/notifications#list-notifications-for-the-authenticated-user)).

    try:
        # Mark a thread as read
        api_instance.activity_mark_thread_as_read(thread_id)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_mark_thread_as_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **int**| The unique identifier of the notification thread. This corresponds to the value returned in the &#x60;id&#x60; field when you retrieve notifications (for example with the [&#x60;GET /notifications&#x60; operation](https://docs.github.com/rest/activity/notifications#list-notifications-for-the-authenticated-user)). | 

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
**205** | Reset Content |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activity_set_repo_subscription**
> RepositorySubscription activity_set_repo_subscription(owner, repo, activity_set_repo_subscription_request=activity_set_repo_subscription_request)

Set a repository subscription

If you would like to watch a repository, set `subscribed` to `true`. If you would like to ignore notifications made within a repository, set `ignored` to `true`. If you would like to stop watching a repository, [delete the repository's subscription](https://docs.github.com/rest/activity/watching#delete-a-repository-subscription) completely.

### Example


```python
import github_openapi
from github_openapi.models.activity_set_repo_subscription_request import ActivitySetRepoSubscriptionRequest
from github_openapi.models.repository_subscription import RepositorySubscription
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
    api_instance = github_openapi.ActivityApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    activity_set_repo_subscription_request = {"subscribed":true,"ignored":false} # ActivitySetRepoSubscriptionRequest |  (optional)

    try:
        # Set a repository subscription
        api_response = api_instance.activity_set_repo_subscription(owner, repo, activity_set_repo_subscription_request=activity_set_repo_subscription_request)
        print("The response of ActivityApi->activity_set_repo_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_set_repo_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **activity_set_repo_subscription_request** | [**ActivitySetRepoSubscriptionRequest**](ActivitySetRepoSubscriptionRequest.md)|  | [optional] 

### Return type

[**RepositorySubscription**](RepositorySubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activity_set_thread_subscription**
> ThreadSubscription activity_set_thread_subscription(thread_id, activity_set_thread_subscription_request=activity_set_thread_subscription_request)

Set a thread subscription

If you are watching a repository, you receive notifications for all threads by default. Use this endpoint to ignore future notifications for threads until you comment on the thread or get an **@mention**.  You can also use this endpoint to subscribe to threads that you are currently not receiving notifications for or to subscribed to threads that you have previously ignored.  Unsubscribing from a conversation in a repository that you are not watching is functionally equivalent to the [Delete a thread subscription](https://docs.github.com/rest/activity/notifications#delete-a-thread-subscription) endpoint.

### Example


```python
import github_openapi
from github_openapi.models.activity_set_thread_subscription_request import ActivitySetThreadSubscriptionRequest
from github_openapi.models.thread_subscription import ThreadSubscription
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
    api_instance = github_openapi.ActivityApi(api_client)
    thread_id = 56 # int | The unique identifier of the notification thread. This corresponds to the value returned in the `id` field when you retrieve notifications (for example with the [`GET /notifications` operation](https://docs.github.com/rest/activity/notifications#list-notifications-for-the-authenticated-user)).
    activity_set_thread_subscription_request = {"ignored":false} # ActivitySetThreadSubscriptionRequest |  (optional)

    try:
        # Set a thread subscription
        api_response = api_instance.activity_set_thread_subscription(thread_id, activity_set_thread_subscription_request=activity_set_thread_subscription_request)
        print("The response of ActivityApi->activity_set_thread_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_set_thread_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **int**| The unique identifier of the notification thread. This corresponds to the value returned in the &#x60;id&#x60; field when you retrieve notifications (for example with the [&#x60;GET /notifications&#x60; operation](https://docs.github.com/rest/activity/notifications#list-notifications-for-the-authenticated-user)). | 
 **activity_set_thread_subscription_request** | [**ActivitySetThreadSubscriptionRequest**](ActivitySetThreadSubscriptionRequest.md)|  | [optional] 

### Return type

[**ThreadSubscription**](ThreadSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |
**401** | Requires authentication |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activity_star_repo_for_authenticated_user**
> activity_star_repo_for_authenticated_user(owner, repo)

Star a repository for the authenticated user

Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see \"[HTTP method](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#http-method).\"

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
    api_instance = github_openapi.ActivityApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Star a repository for the authenticated user
        api_instance.activity_star_repo_for_authenticated_user(owner, repo)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_star_repo_for_authenticated_user: %s\n" % e)
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
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**401** | Requires authentication |  -  |
**304** | Not modified |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activity_unstar_repo_for_authenticated_user**
> activity_unstar_repo_for_authenticated_user(owner, repo)

Unstar a repository for the authenticated user

Unstar a repository that the authenticated user has previously starred.

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
    api_instance = github_openapi.ActivityApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Unstar a repository for the authenticated user
        api_instance.activity_unstar_repo_for_authenticated_user(owner, repo)
    except Exception as e:
        print("Exception when calling ActivityApi->activity_unstar_repo_for_authenticated_user: %s\n" % e)
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
**404** | Resource not found |  -  |
**401** | Requires authentication |  -  |
**304** | Not modified |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

