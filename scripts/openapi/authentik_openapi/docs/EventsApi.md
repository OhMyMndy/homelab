# authentik_openapi.EventsApi

All URIs are relative to *https://auth.home.ohmymndy.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events_events_actions_list**](EventsApi.md#events_events_actions_list) | **GET** /events/events/actions/ | 
[**events_events_create**](EventsApi.md#events_events_create) | **POST** /events/events/ | 
[**events_events_destroy**](EventsApi.md#events_events_destroy) | **DELETE** /events/events/{event_uuid}/ | 
[**events_events_list**](EventsApi.md#events_events_list) | **GET** /events/events/ | 
[**events_events_partial_update**](EventsApi.md#events_events_partial_update) | **PATCH** /events/events/{event_uuid}/ | 
[**events_events_per_month_list**](EventsApi.md#events_events_per_month_list) | **GET** /events/events/per_month/ | 
[**events_events_retrieve**](EventsApi.md#events_events_retrieve) | **GET** /events/events/{event_uuid}/ | 
[**events_events_top_per_user_list**](EventsApi.md#events_events_top_per_user_list) | **GET** /events/events/top_per_user/ | 
[**events_events_update**](EventsApi.md#events_events_update) | **PUT** /events/events/{event_uuid}/ | 
[**events_events_volume_list**](EventsApi.md#events_events_volume_list) | **GET** /events/events/volume/ | 
[**events_notifications_destroy**](EventsApi.md#events_notifications_destroy) | **DELETE** /events/notifications/{uuid}/ | 
[**events_notifications_list**](EventsApi.md#events_notifications_list) | **GET** /events/notifications/ | 
[**events_notifications_mark_all_seen_create**](EventsApi.md#events_notifications_mark_all_seen_create) | **POST** /events/notifications/mark_all_seen/ | 
[**events_notifications_partial_update**](EventsApi.md#events_notifications_partial_update) | **PATCH** /events/notifications/{uuid}/ | 
[**events_notifications_retrieve**](EventsApi.md#events_notifications_retrieve) | **GET** /events/notifications/{uuid}/ | 
[**events_notifications_update**](EventsApi.md#events_notifications_update) | **PUT** /events/notifications/{uuid}/ | 
[**events_notifications_used_by_list**](EventsApi.md#events_notifications_used_by_list) | **GET** /events/notifications/{uuid}/used_by/ | 
[**events_rules_create**](EventsApi.md#events_rules_create) | **POST** /events/rules/ | 
[**events_rules_destroy**](EventsApi.md#events_rules_destroy) | **DELETE** /events/rules/{pbm_uuid}/ | 
[**events_rules_list**](EventsApi.md#events_rules_list) | **GET** /events/rules/ | 
[**events_rules_partial_update**](EventsApi.md#events_rules_partial_update) | **PATCH** /events/rules/{pbm_uuid}/ | 
[**events_rules_retrieve**](EventsApi.md#events_rules_retrieve) | **GET** /events/rules/{pbm_uuid}/ | 
[**events_rules_update**](EventsApi.md#events_rules_update) | **PUT** /events/rules/{pbm_uuid}/ | 
[**events_rules_used_by_list**](EventsApi.md#events_rules_used_by_list) | **GET** /events/rules/{pbm_uuid}/used_by/ | 
[**events_system_tasks_list**](EventsApi.md#events_system_tasks_list) | **GET** /events/system_tasks/ | 
[**events_system_tasks_retrieve**](EventsApi.md#events_system_tasks_retrieve) | **GET** /events/system_tasks/{uuid}/ | 
[**events_system_tasks_run_create**](EventsApi.md#events_system_tasks_run_create) | **POST** /events/system_tasks/{uuid}/run/ | 
[**events_transports_create**](EventsApi.md#events_transports_create) | **POST** /events/transports/ | 
[**events_transports_destroy**](EventsApi.md#events_transports_destroy) | **DELETE** /events/transports/{uuid}/ | 
[**events_transports_list**](EventsApi.md#events_transports_list) | **GET** /events/transports/ | 
[**events_transports_partial_update**](EventsApi.md#events_transports_partial_update) | **PATCH** /events/transports/{uuid}/ | 
[**events_transports_retrieve**](EventsApi.md#events_transports_retrieve) | **GET** /events/transports/{uuid}/ | 
[**events_transports_test_create**](EventsApi.md#events_transports_test_create) | **POST** /events/transports/{uuid}/test/ | 
[**events_transports_update**](EventsApi.md#events_transports_update) | **PUT** /events/transports/{uuid}/ | 
[**events_transports_used_by_list**](EventsApi.md#events_transports_used_by_list) | **GET** /events/transports/{uuid}/used_by/ | 


# **events_events_actions_list**
> List[TypeCreate] events_events_actions_list()



Get all actions

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.type_create import TypeCreate
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)

    try:
        api_response = api_instance.events_events_actions_list()
        print("The response of EventsApi->events_events_actions_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_events_actions_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[TypeCreate]**](TypeCreate.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_events_create**
> Event events_events_create(event_request)



Event Read-Only Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.event import Event
from authentik_openapi.models.event_request import EventRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    event_request = authentik_openapi.EventRequest() # EventRequest | 

    try:
        api_response = api_instance.events_events_create(event_request)
        print("The response of EventsApi->events_events_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_events_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_request** | [**EventRequest**](EventRequest.md)|  | 

### Return type

[**Event**](Event.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_events_destroy**
> events_events_destroy(event_uuid)



Event Read-Only Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    event_uuid = 'event_uuid_example' # str | A UUID string identifying this Event.

    try:
        api_instance.events_events_destroy(event_uuid)
    except Exception as e:
        print("Exception when calling EventsApi->events_events_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_uuid** | **str**| A UUID string identifying this Event. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_events_list**
> PaginatedEventList events_events_list(action=action, brand_name=brand_name, client_ip=client_ip, context_authorized_app=context_authorized_app, context_model_app=context_model_app, context_model_name=context_model_name, context_model_pk=context_model_pk, ordering=ordering, page=page, page_size=page_size, search=search, username=username)



Event Read-Only Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_event_list import PaginatedEventList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    action = 'action_example' # str |  (optional)
    brand_name = 'brand_name_example' # str | Brand name (optional)
    client_ip = 'client_ip_example' # str |  (optional)
    context_authorized_app = 'context_authorized_app_example' # str | Context Authorized application (optional)
    context_model_app = 'context_model_app_example' # str | Context Model App (optional)
    context_model_name = 'context_model_name_example' # str | Context Model Name (optional)
    context_model_pk = 'context_model_pk_example' # str | Context Model Primary Key (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    username = 'username_example' # str | Username (optional)

    try:
        api_response = api_instance.events_events_list(action=action, brand_name=brand_name, client_ip=client_ip, context_authorized_app=context_authorized_app, context_model_app=context_model_app, context_model_name=context_model_name, context_model_pk=context_model_pk, ordering=ordering, page=page, page_size=page_size, search=search, username=username)
        print("The response of EventsApi->events_events_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_events_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**|  | [optional] 
 **brand_name** | **str**| Brand name | [optional] 
 **client_ip** | **str**|  | [optional] 
 **context_authorized_app** | **str**| Context Authorized application | [optional] 
 **context_model_app** | **str**| Context Model App | [optional] 
 **context_model_name** | **str**| Context Model Name | [optional] 
 **context_model_pk** | **str**| Context Model Primary Key | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **username** | **str**| Username | [optional] 

### Return type

[**PaginatedEventList**](PaginatedEventList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_events_partial_update**
> Event events_events_partial_update(event_uuid, patched_event_request=patched_event_request)



Event Read-Only Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.event import Event
from authentik_openapi.models.patched_event_request import PatchedEventRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    event_uuid = 'event_uuid_example' # str | A UUID string identifying this Event.
    patched_event_request = authentik_openapi.PatchedEventRequest() # PatchedEventRequest |  (optional)

    try:
        api_response = api_instance.events_events_partial_update(event_uuid, patched_event_request=patched_event_request)
        print("The response of EventsApi->events_events_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_events_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_uuid** | **str**| A UUID string identifying this Event. | 
 **patched_event_request** | [**PatchedEventRequest**](PatchedEventRequest.md)|  | [optional] 

### Return type

[**Event**](Event.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_events_per_month_list**
> List[Coordinate] events_events_per_month_list(action=action, query=query)



Get the count of events per month

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.coordinate import Coordinate
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    action = 'action_example' # str |  (optional)
    query = 'query_example' # str |  (optional)

    try:
        api_response = api_instance.events_events_per_month_list(action=action, query=query)
        print("The response of EventsApi->events_events_per_month_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_events_per_month_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**|  | [optional] 
 **query** | **str**|  | [optional] 

### Return type

[**List[Coordinate]**](Coordinate.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_events_retrieve**
> Event events_events_retrieve(event_uuid)



Event Read-Only Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.event import Event
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    event_uuid = 'event_uuid_example' # str | A UUID string identifying this Event.

    try:
        api_response = api_instance.events_events_retrieve(event_uuid)
        print("The response of EventsApi->events_events_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_events_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_uuid** | **str**| A UUID string identifying this Event. | 

### Return type

[**Event**](Event.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_events_top_per_user_list**
> List[EventTopPerUser] events_events_top_per_user_list(action=action, top_n=top_n)



Get the top_n events grouped by user count

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.event_top_per_user import EventTopPerUser
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    action = 'action_example' # str |  (optional)
    top_n = 56 # int |  (optional)

    try:
        api_response = api_instance.events_events_top_per_user_list(action=action, top_n=top_n)
        print("The response of EventsApi->events_events_top_per_user_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_events_top_per_user_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**|  | [optional] 
 **top_n** | **int**|  | [optional] 

### Return type

[**List[EventTopPerUser]**](EventTopPerUser.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_events_update**
> Event events_events_update(event_uuid, event_request)



Event Read-Only Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.event import Event
from authentik_openapi.models.event_request import EventRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    event_uuid = 'event_uuid_example' # str | A UUID string identifying this Event.
    event_request = authentik_openapi.EventRequest() # EventRequest | 

    try:
        api_response = api_instance.events_events_update(event_uuid, event_request)
        print("The response of EventsApi->events_events_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_events_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_uuid** | **str**| A UUID string identifying this Event. | 
 **event_request** | [**EventRequest**](EventRequest.md)|  | 

### Return type

[**Event**](Event.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_events_volume_list**
> List[Coordinate] events_events_volume_list(action=action, brand_name=brand_name, client_ip=client_ip, context_authorized_app=context_authorized_app, context_model_app=context_model_app, context_model_name=context_model_name, context_model_pk=context_model_pk, ordering=ordering, search=search, username=username)



Get event volume for specified filters and timeframe

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.coordinate import Coordinate
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    action = 'action_example' # str |  (optional)
    brand_name = 'brand_name_example' # str | Brand name (optional)
    client_ip = 'client_ip_example' # str |  (optional)
    context_authorized_app = 'context_authorized_app_example' # str | Context Authorized application (optional)
    context_model_app = 'context_model_app_example' # str | Context Model App (optional)
    context_model_name = 'context_model_name_example' # str | Context Model Name (optional)
    context_model_pk = 'context_model_pk_example' # str | Context Model Primary Key (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    search = 'search_example' # str | A search term. (optional)
    username = 'username_example' # str | Username (optional)

    try:
        api_response = api_instance.events_events_volume_list(action=action, brand_name=brand_name, client_ip=client_ip, context_authorized_app=context_authorized_app, context_model_app=context_model_app, context_model_name=context_model_name, context_model_pk=context_model_pk, ordering=ordering, search=search, username=username)
        print("The response of EventsApi->events_events_volume_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_events_volume_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**|  | [optional] 
 **brand_name** | **str**| Brand name | [optional] 
 **client_ip** | **str**|  | [optional] 
 **context_authorized_app** | **str**| Context Authorized application | [optional] 
 **context_model_app** | **str**| Context Model App | [optional] 
 **context_model_name** | **str**| Context Model Name | [optional] 
 **context_model_pk** | **str**| Context Model Primary Key | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **username** | **str**| Username | [optional] 

### Return type

[**List[Coordinate]**](Coordinate.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_notifications_destroy**
> events_notifications_destroy(uuid)



Notification Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Notification.

    try:
        api_instance.events_notifications_destroy(uuid)
    except Exception as e:
        print("Exception when calling EventsApi->events_notifications_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Notification. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_notifications_list**
> PaginatedNotificationList events_notifications_list(body=body, created=created, event=event, ordering=ordering, page=page, page_size=page_size, search=search, seen=seen, severity=severity, user=user)



Notification Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_notification_list import PaginatedNotificationList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    body = 'body_example' # str |  (optional)
    created = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    event = 'event_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    seen = True # bool |  (optional)
    severity = 'severity_example' # str |  (optional)
    user = 56 # int |  (optional)

    try:
        api_response = api_instance.events_notifications_list(body=body, created=created, event=event, ordering=ordering, page=page, page_size=page_size, search=search, seen=seen, severity=severity, user=user)
        print("The response of EventsApi->events_notifications_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_notifications_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | [optional] 
 **created** | **datetime**|  | [optional] 
 **event** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **seen** | **bool**|  | [optional] 
 **severity** | **str**|  | [optional] 
 **user** | **int**|  | [optional] 

### Return type

[**PaginatedNotificationList**](PaginatedNotificationList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_notifications_mark_all_seen_create**
> events_notifications_mark_all_seen_create()



Mark all the user's notifications as seen

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)

    try:
        api_instance.events_notifications_mark_all_seen_create()
    except Exception as e:
        print("Exception when calling EventsApi->events_notifications_mark_all_seen_create: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Marked tasks as read successfully. |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_notifications_partial_update**
> Notification events_notifications_partial_update(uuid, patched_notification_request=patched_notification_request)



Notification Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.notification import Notification
from authentik_openapi.models.patched_notification_request import PatchedNotificationRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Notification.
    patched_notification_request = authentik_openapi.PatchedNotificationRequest() # PatchedNotificationRequest |  (optional)

    try:
        api_response = api_instance.events_notifications_partial_update(uuid, patched_notification_request=patched_notification_request)
        print("The response of EventsApi->events_notifications_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_notifications_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Notification. | 
 **patched_notification_request** | [**PatchedNotificationRequest**](PatchedNotificationRequest.md)|  | [optional] 

### Return type

[**Notification**](Notification.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_notifications_retrieve**
> Notification events_notifications_retrieve(uuid)



Notification Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.notification import Notification
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Notification.

    try:
        api_response = api_instance.events_notifications_retrieve(uuid)
        print("The response of EventsApi->events_notifications_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_notifications_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Notification. | 

### Return type

[**Notification**](Notification.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_notifications_update**
> Notification events_notifications_update(uuid, notification_request=notification_request)



Notification Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.notification import Notification
from authentik_openapi.models.notification_request import NotificationRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Notification.
    notification_request = authentik_openapi.NotificationRequest() # NotificationRequest |  (optional)

    try:
        api_response = api_instance.events_notifications_update(uuid, notification_request=notification_request)
        print("The response of EventsApi->events_notifications_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_notifications_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Notification. | 
 **notification_request** | [**NotificationRequest**](NotificationRequest.md)|  | [optional] 

### Return type

[**Notification**](Notification.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_notifications_used_by_list**
> List[UsedBy] events_notifications_used_by_list(uuid)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Notification.

    try:
        api_response = api_instance.events_notifications_used_by_list(uuid)
        print("The response of EventsApi->events_notifications_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_notifications_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Notification. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_rules_create**
> NotificationRule events_rules_create(notification_rule_request)



NotificationRule Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.notification_rule import NotificationRule
from authentik_openapi.models.notification_rule_request import NotificationRuleRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    notification_rule_request = authentik_openapi.NotificationRuleRequest() # NotificationRuleRequest | 

    try:
        api_response = api_instance.events_rules_create(notification_rule_request)
        print("The response of EventsApi->events_rules_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_rules_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_rule_request** | [**NotificationRuleRequest**](NotificationRuleRequest.md)|  | 

### Return type

[**NotificationRule**](NotificationRule.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_rules_destroy**
> events_rules_destroy(pbm_uuid)



NotificationRule Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    pbm_uuid = 'pbm_uuid_example' # str | A UUID string identifying this Notification Rule.

    try:
        api_instance.events_rules_destroy(pbm_uuid)
    except Exception as e:
        print("Exception when calling EventsApi->events_rules_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pbm_uuid** | **str**| A UUID string identifying this Notification Rule. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_rules_list**
> PaginatedNotificationRuleList events_rules_list(group__name=group__name, name=name, ordering=ordering, page=page, page_size=page_size, search=search, severity=severity)



NotificationRule Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_notification_rule_list import PaginatedNotificationRuleList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    group__name = 'group__name_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    severity = 'severity_example' # str | Controls which severity level the created notifications will have.   (optional)

    try:
        api_response = api_instance.events_rules_list(group__name=group__name, name=name, ordering=ordering, page=page, page_size=page_size, search=search, severity=severity)
        print("The response of EventsApi->events_rules_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_rules_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group__name** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **severity** | **str**| Controls which severity level the created notifications will have.   | [optional] 

### Return type

[**PaginatedNotificationRuleList**](PaginatedNotificationRuleList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_rules_partial_update**
> NotificationRule events_rules_partial_update(pbm_uuid, patched_notification_rule_request=patched_notification_rule_request)



NotificationRule Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.notification_rule import NotificationRule
from authentik_openapi.models.patched_notification_rule_request import PatchedNotificationRuleRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    pbm_uuid = 'pbm_uuid_example' # str | A UUID string identifying this Notification Rule.
    patched_notification_rule_request = authentik_openapi.PatchedNotificationRuleRequest() # PatchedNotificationRuleRequest |  (optional)

    try:
        api_response = api_instance.events_rules_partial_update(pbm_uuid, patched_notification_rule_request=patched_notification_rule_request)
        print("The response of EventsApi->events_rules_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_rules_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pbm_uuid** | **str**| A UUID string identifying this Notification Rule. | 
 **patched_notification_rule_request** | [**PatchedNotificationRuleRequest**](PatchedNotificationRuleRequest.md)|  | [optional] 

### Return type

[**NotificationRule**](NotificationRule.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_rules_retrieve**
> NotificationRule events_rules_retrieve(pbm_uuid)



NotificationRule Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.notification_rule import NotificationRule
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    pbm_uuid = 'pbm_uuid_example' # str | A UUID string identifying this Notification Rule.

    try:
        api_response = api_instance.events_rules_retrieve(pbm_uuid)
        print("The response of EventsApi->events_rules_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_rules_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pbm_uuid** | **str**| A UUID string identifying this Notification Rule. | 

### Return type

[**NotificationRule**](NotificationRule.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_rules_update**
> NotificationRule events_rules_update(pbm_uuid, notification_rule_request)



NotificationRule Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.notification_rule import NotificationRule
from authentik_openapi.models.notification_rule_request import NotificationRuleRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    pbm_uuid = 'pbm_uuid_example' # str | A UUID string identifying this Notification Rule.
    notification_rule_request = authentik_openapi.NotificationRuleRequest() # NotificationRuleRequest | 

    try:
        api_response = api_instance.events_rules_update(pbm_uuid, notification_rule_request)
        print("The response of EventsApi->events_rules_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_rules_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pbm_uuid** | **str**| A UUID string identifying this Notification Rule. | 
 **notification_rule_request** | [**NotificationRuleRequest**](NotificationRuleRequest.md)|  | 

### Return type

[**NotificationRule**](NotificationRule.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_rules_used_by_list**
> List[UsedBy] events_rules_used_by_list(pbm_uuid)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    pbm_uuid = 'pbm_uuid_example' # str | A UUID string identifying this Notification Rule.

    try:
        api_response = api_instance.events_rules_used_by_list(pbm_uuid)
        print("The response of EventsApi->events_rules_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_rules_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pbm_uuid** | **str**| A UUID string identifying this Notification Rule. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_system_tasks_list**
> PaginatedSystemTaskList events_system_tasks_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search, status=status, uid=uid)



Read-only view set that returns all background tasks

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_system_task_list import PaginatedSystemTaskList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    status = 'status_example' # str |  (optional)
    uid = 'uid_example' # str |  (optional)

    try:
        api_response = api_instance.events_system_tasks_list(name=name, ordering=ordering, page=page, page_size=page_size, search=search, status=status, uid=uid)
        print("The response of EventsApi->events_system_tasks_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_system_tasks_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **status** | **str**|  | [optional] 
 **uid** | **str**|  | [optional] 

### Return type

[**PaginatedSystemTaskList**](PaginatedSystemTaskList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_system_tasks_retrieve**
> SystemTask events_system_tasks_retrieve(uuid)



Read-only view set that returns all background tasks

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.system_task import SystemTask
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this System Task.

    try:
        api_response = api_instance.events_system_tasks_retrieve(uuid)
        print("The response of EventsApi->events_system_tasks_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_system_tasks_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this System Task. | 

### Return type

[**SystemTask**](SystemTask.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_system_tasks_run_create**
> events_system_tasks_run_create(uuid)



Run task

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this System Task.

    try:
        api_instance.events_system_tasks_run_create(uuid)
    except Exception as e:
        print("Exception when calling EventsApi->events_system_tasks_run_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this System Task. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Task retried successfully |  -  |
**404** | Task not found |  -  |
**500** | Failed to retry task |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_transports_create**
> NotificationTransport events_transports_create(notification_transport_request)



NotificationTransport Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.notification_transport import NotificationTransport
from authentik_openapi.models.notification_transport_request import NotificationTransportRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    notification_transport_request = authentik_openapi.NotificationTransportRequest() # NotificationTransportRequest | 

    try:
        api_response = api_instance.events_transports_create(notification_transport_request)
        print("The response of EventsApi->events_transports_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_transports_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_transport_request** | [**NotificationTransportRequest**](NotificationTransportRequest.md)|  | 

### Return type

[**NotificationTransport**](NotificationTransport.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_transports_destroy**
> events_transports_destroy(uuid)



NotificationTransport Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Notification Transport.

    try:
        api_instance.events_transports_destroy(uuid)
    except Exception as e:
        print("Exception when calling EventsApi->events_transports_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Notification Transport. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_transports_list**
> PaginatedNotificationTransportList events_transports_list(mode=mode, name=name, ordering=ordering, page=page, page_size=page_size, search=search, send_once=send_once, webhook_url=webhook_url)



NotificationTransport Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_notification_transport_list import PaginatedNotificationTransportList
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    mode = 'mode_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    send_once = True # bool |  (optional)
    webhook_url = 'webhook_url_example' # str |  (optional)

    try:
        api_response = api_instance.events_transports_list(mode=mode, name=name, ordering=ordering, page=page, page_size=page_size, search=search, send_once=send_once, webhook_url=webhook_url)
        print("The response of EventsApi->events_transports_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_transports_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mode** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **send_once** | **bool**|  | [optional] 
 **webhook_url** | **str**|  | [optional] 

### Return type

[**PaginatedNotificationTransportList**](PaginatedNotificationTransportList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_transports_partial_update**
> NotificationTransport events_transports_partial_update(uuid, patched_notification_transport_request=patched_notification_transport_request)



NotificationTransport Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.notification_transport import NotificationTransport
from authentik_openapi.models.patched_notification_transport_request import PatchedNotificationTransportRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Notification Transport.
    patched_notification_transport_request = authentik_openapi.PatchedNotificationTransportRequest() # PatchedNotificationTransportRequest |  (optional)

    try:
        api_response = api_instance.events_transports_partial_update(uuid, patched_notification_transport_request=patched_notification_transport_request)
        print("The response of EventsApi->events_transports_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_transports_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Notification Transport. | 
 **patched_notification_transport_request** | [**PatchedNotificationTransportRequest**](PatchedNotificationTransportRequest.md)|  | [optional] 

### Return type

[**NotificationTransport**](NotificationTransport.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_transports_retrieve**
> NotificationTransport events_transports_retrieve(uuid)



NotificationTransport Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.notification_transport import NotificationTransport
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Notification Transport.

    try:
        api_response = api_instance.events_transports_retrieve(uuid)
        print("The response of EventsApi->events_transports_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_transports_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Notification Transport. | 

### Return type

[**NotificationTransport**](NotificationTransport.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_transports_test_create**
> NotificationTransportTest events_transports_test_create(uuid)



Send example notification using selected transport. Requires Modify permissions.

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.notification_transport_test import NotificationTransportTest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Notification Transport.

    try:
        api_response = api_instance.events_transports_test_create(uuid)
        print("The response of EventsApi->events_transports_test_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_transports_test_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Notification Transport. | 

### Return type

[**NotificationTransportTest**](NotificationTransportTest.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**500** | Failed to test transport |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_transports_update**
> NotificationTransport events_transports_update(uuid, notification_transport_request)



NotificationTransport Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.notification_transport import NotificationTransport
from authentik_openapi.models.notification_transport_request import NotificationTransportRequest
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Notification Transport.
    notification_transport_request = authentik_openapi.NotificationTransportRequest() # NotificationTransportRequest | 

    try:
        api_response = api_instance.events_transports_update(uuid, notification_transport_request)
        print("The response of EventsApi->events_transports_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_transports_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Notification Transport. | 
 **notification_transport_request** | [**NotificationTransportRequest**](NotificationTransportRequest.md)|  | 

### Return type

[**NotificationTransport**](NotificationTransport.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_transports_used_by_list**
> List[UsedBy] events_transports_used_by_list(uuid)



Get a list of all objects that use this object

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://auth.home.ohmymndy.com/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik_openapi.Configuration(
    host = "https://auth.home.ohmymndy.com/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: authentik
configuration = authentik_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with authentik_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik_openapi.EventsApi(api_client)
    uuid = 'uuid_example' # str | A UUID string identifying this Notification Transport.

    try:
        api_response = api_instance.events_transports_used_by_list(uuid)
        print("The response of EventsApi->events_transports_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_transports_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| A UUID string identifying this Notification Transport. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

