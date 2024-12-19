# authentik_openapi.FlowsApi

All URIs are relative to *https://auth.home.ohmymndy.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**flows_bindings_create**](FlowsApi.md#flows_bindings_create) | **POST** /flows/bindings/ | 
[**flows_bindings_destroy**](FlowsApi.md#flows_bindings_destroy) | **DELETE** /flows/bindings/{fsb_uuid}/ | 
[**flows_bindings_list**](FlowsApi.md#flows_bindings_list) | **GET** /flows/bindings/ | 
[**flows_bindings_partial_update**](FlowsApi.md#flows_bindings_partial_update) | **PATCH** /flows/bindings/{fsb_uuid}/ | 
[**flows_bindings_retrieve**](FlowsApi.md#flows_bindings_retrieve) | **GET** /flows/bindings/{fsb_uuid}/ | 
[**flows_bindings_update**](FlowsApi.md#flows_bindings_update) | **PUT** /flows/bindings/{fsb_uuid}/ | 
[**flows_bindings_used_by_list**](FlowsApi.md#flows_bindings_used_by_list) | **GET** /flows/bindings/{fsb_uuid}/used_by/ | 
[**flows_executor_get**](FlowsApi.md#flows_executor_get) | **GET** /flows/executor/{flow_slug}/ | 
[**flows_executor_solve**](FlowsApi.md#flows_executor_solve) | **POST** /flows/executor/{flow_slug}/ | 
[**flows_inspector_get**](FlowsApi.md#flows_inspector_get) | **GET** /flows/inspector/{flow_slug}/ | 
[**flows_instances_cache_clear_create**](FlowsApi.md#flows_instances_cache_clear_create) | **POST** /flows/instances/cache_clear/ | 
[**flows_instances_cache_info_retrieve**](FlowsApi.md#flows_instances_cache_info_retrieve) | **GET** /flows/instances/cache_info/ | 
[**flows_instances_create**](FlowsApi.md#flows_instances_create) | **POST** /flows/instances/ | 
[**flows_instances_destroy**](FlowsApi.md#flows_instances_destroy) | **DELETE** /flows/instances/{slug}/ | 
[**flows_instances_diagram_retrieve**](FlowsApi.md#flows_instances_diagram_retrieve) | **GET** /flows/instances/{slug}/diagram/ | 
[**flows_instances_execute_retrieve**](FlowsApi.md#flows_instances_execute_retrieve) | **GET** /flows/instances/{slug}/execute/ | 
[**flows_instances_export_retrieve**](FlowsApi.md#flows_instances_export_retrieve) | **GET** /flows/instances/{slug}/export/ | 
[**flows_instances_import_create**](FlowsApi.md#flows_instances_import_create) | **POST** /flows/instances/import/ | 
[**flows_instances_list**](FlowsApi.md#flows_instances_list) | **GET** /flows/instances/ | 
[**flows_instances_partial_update**](FlowsApi.md#flows_instances_partial_update) | **PATCH** /flows/instances/{slug}/ | 
[**flows_instances_retrieve**](FlowsApi.md#flows_instances_retrieve) | **GET** /flows/instances/{slug}/ | 
[**flows_instances_set_background_create**](FlowsApi.md#flows_instances_set_background_create) | **POST** /flows/instances/{slug}/set_background/ | 
[**flows_instances_set_background_url_create**](FlowsApi.md#flows_instances_set_background_url_create) | **POST** /flows/instances/{slug}/set_background_url/ | 
[**flows_instances_update**](FlowsApi.md#flows_instances_update) | **PUT** /flows/instances/{slug}/ | 
[**flows_instances_used_by_list**](FlowsApi.md#flows_instances_used_by_list) | **GET** /flows/instances/{slug}/used_by/ | 


# **flows_bindings_create**
> FlowStageBinding flows_bindings_create(flow_stage_binding_request)



FlowStageBinding Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.flow_stage_binding import FlowStageBinding
from authentik_openapi.models.flow_stage_binding_request import FlowStageBindingRequest
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
    api_instance = authentik_openapi.FlowsApi(api_client)
    flow_stage_binding_request = authentik_openapi.FlowStageBindingRequest() # FlowStageBindingRequest | 

    try:
        api_response = api_instance.flows_bindings_create(flow_stage_binding_request)
        print("The response of FlowsApi->flows_bindings_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->flows_bindings_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_stage_binding_request** | [**FlowStageBindingRequest**](FlowStageBindingRequest.md)|  | 

### Return type

[**FlowStageBinding**](FlowStageBinding.md)

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

# **flows_bindings_destroy**
> flows_bindings_destroy(fsb_uuid)



FlowStageBinding Viewset

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
    api_instance = authentik_openapi.FlowsApi(api_client)
    fsb_uuid = 'fsb_uuid_example' # str | A UUID string identifying this Flow Stage Binding.

    try:
        api_instance.flows_bindings_destroy(fsb_uuid)
    except Exception as e:
        print("Exception when calling FlowsApi->flows_bindings_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fsb_uuid** | **str**| A UUID string identifying this Flow Stage Binding. | 

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

# **flows_bindings_list**
> PaginatedFlowStageBindingList flows_bindings_list(evaluate_on_plan=evaluate_on_plan, fsb_uuid=fsb_uuid, invalid_response_action=invalid_response_action, order=order, ordering=ordering, page=page, page_size=page_size, pbm_uuid=pbm_uuid, policies=policies, policy_engine_mode=policy_engine_mode, re_evaluate_policies=re_evaluate_policies, search=search, stage=stage, target=target)



FlowStageBinding Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_flow_stage_binding_list import PaginatedFlowStageBindingList
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
    api_instance = authentik_openapi.FlowsApi(api_client)
    evaluate_on_plan = True # bool |  (optional)
    fsb_uuid = 'fsb_uuid_example' # str |  (optional)
    invalid_response_action = 'invalid_response_action_example' # str | Configure how the flow executor should handle an invalid response to a challenge. RETRY returns the error message and a similar challenge to the executor. RESTART restarts the flow from the beginning, and RESTART_WITH_CONTEXT restarts the flow while keeping the current context.   (optional)
    order = 56 # int |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    pbm_uuid = 'pbm_uuid_example' # str |  (optional)
    policies = ['policies_example'] # List[str] |  (optional)
    policy_engine_mode = 'policy_engine_mode_example' # str |  (optional)
    re_evaluate_policies = True # bool |  (optional)
    search = 'search_example' # str | A search term. (optional)
    stage = 'stage_example' # str |  (optional)
    target = 'target_example' # str |  (optional)

    try:
        api_response = api_instance.flows_bindings_list(evaluate_on_plan=evaluate_on_plan, fsb_uuid=fsb_uuid, invalid_response_action=invalid_response_action, order=order, ordering=ordering, page=page, page_size=page_size, pbm_uuid=pbm_uuid, policies=policies, policy_engine_mode=policy_engine_mode, re_evaluate_policies=re_evaluate_policies, search=search, stage=stage, target=target)
        print("The response of FlowsApi->flows_bindings_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->flows_bindings_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **evaluate_on_plan** | **bool**|  | [optional] 
 **fsb_uuid** | **str**|  | [optional] 
 **invalid_response_action** | **str**| Configure how the flow executor should handle an invalid response to a challenge. RETRY returns the error message and a similar challenge to the executor. RESTART restarts the flow from the beginning, and RESTART_WITH_CONTEXT restarts the flow while keeping the current context.   | [optional] 
 **order** | **int**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **pbm_uuid** | **str**|  | [optional] 
 **policies** | [**List[str]**](str.md)|  | [optional] 
 **policy_engine_mode** | **str**|  | [optional] 
 **re_evaluate_policies** | **bool**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **stage** | **str**|  | [optional] 
 **target** | **str**|  | [optional] 

### Return type

[**PaginatedFlowStageBindingList**](PaginatedFlowStageBindingList.md)

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

# **flows_bindings_partial_update**
> FlowStageBinding flows_bindings_partial_update(fsb_uuid, patched_flow_stage_binding_request=patched_flow_stage_binding_request)



FlowStageBinding Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.flow_stage_binding import FlowStageBinding
from authentik_openapi.models.patched_flow_stage_binding_request import PatchedFlowStageBindingRequest
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
    api_instance = authentik_openapi.FlowsApi(api_client)
    fsb_uuid = 'fsb_uuid_example' # str | A UUID string identifying this Flow Stage Binding.
    patched_flow_stage_binding_request = authentik_openapi.PatchedFlowStageBindingRequest() # PatchedFlowStageBindingRequest |  (optional)

    try:
        api_response = api_instance.flows_bindings_partial_update(fsb_uuid, patched_flow_stage_binding_request=patched_flow_stage_binding_request)
        print("The response of FlowsApi->flows_bindings_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->flows_bindings_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fsb_uuid** | **str**| A UUID string identifying this Flow Stage Binding. | 
 **patched_flow_stage_binding_request** | [**PatchedFlowStageBindingRequest**](PatchedFlowStageBindingRequest.md)|  | [optional] 

### Return type

[**FlowStageBinding**](FlowStageBinding.md)

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

# **flows_bindings_retrieve**
> FlowStageBinding flows_bindings_retrieve(fsb_uuid)



FlowStageBinding Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.flow_stage_binding import FlowStageBinding
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
    api_instance = authentik_openapi.FlowsApi(api_client)
    fsb_uuid = 'fsb_uuid_example' # str | A UUID string identifying this Flow Stage Binding.

    try:
        api_response = api_instance.flows_bindings_retrieve(fsb_uuid)
        print("The response of FlowsApi->flows_bindings_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->flows_bindings_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fsb_uuid** | **str**| A UUID string identifying this Flow Stage Binding. | 

### Return type

[**FlowStageBinding**](FlowStageBinding.md)

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

# **flows_bindings_update**
> FlowStageBinding flows_bindings_update(fsb_uuid, flow_stage_binding_request)



FlowStageBinding Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.flow_stage_binding import FlowStageBinding
from authentik_openapi.models.flow_stage_binding_request import FlowStageBindingRequest
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
    api_instance = authentik_openapi.FlowsApi(api_client)
    fsb_uuid = 'fsb_uuid_example' # str | A UUID string identifying this Flow Stage Binding.
    flow_stage_binding_request = authentik_openapi.FlowStageBindingRequest() # FlowStageBindingRequest | 

    try:
        api_response = api_instance.flows_bindings_update(fsb_uuid, flow_stage_binding_request)
        print("The response of FlowsApi->flows_bindings_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->flows_bindings_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fsb_uuid** | **str**| A UUID string identifying this Flow Stage Binding. | 
 **flow_stage_binding_request** | [**FlowStageBindingRequest**](FlowStageBindingRequest.md)|  | 

### Return type

[**FlowStageBinding**](FlowStageBinding.md)

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

# **flows_bindings_used_by_list**
> List[UsedBy] flows_bindings_used_by_list(fsb_uuid)



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
    api_instance = authentik_openapi.FlowsApi(api_client)
    fsb_uuid = 'fsb_uuid_example' # str | A UUID string identifying this Flow Stage Binding.

    try:
        api_response = api_instance.flows_bindings_used_by_list(fsb_uuid)
        print("The response of FlowsApi->flows_bindings_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->flows_bindings_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fsb_uuid** | **str**| A UUID string identifying this Flow Stage Binding. | 

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

# **flows_executor_get**
> ChallengeTypes flows_executor_get(flow_slug, query)



Get the next pending challenge from the currently active flow.

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.challenge_types import ChallengeTypes
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
    api_instance = authentik_openapi.FlowsApi(api_client)
    flow_slug = 'flow_slug_example' # str | 
    query = 'query_example' # str | Querystring as received

    try:
        api_response = api_instance.flows_executor_get(flow_slug, query)
        print("The response of FlowsApi->flows_executor_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->flows_executor_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_slug** | **str**|  | 
 **query** | **str**| Querystring as received | 

### Return type

[**ChallengeTypes**](ChallengeTypes.md)

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

# **flows_executor_solve**
> ChallengeTypes flows_executor_solve(flow_slug, query, flow_challenge_response_request=flow_challenge_response_request)



Solve the previously retrieved challenge and advanced to the next stage.

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.challenge_types import ChallengeTypes
from authentik_openapi.models.flow_challenge_response_request import FlowChallengeResponseRequest
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
    api_instance = authentik_openapi.FlowsApi(api_client)
    flow_slug = 'flow_slug_example' # str | 
    query = 'query_example' # str | Querystring as received
    flow_challenge_response_request = authentik_openapi.FlowChallengeResponseRequest() # FlowChallengeResponseRequest |  (optional)

    try:
        api_response = api_instance.flows_executor_solve(flow_slug, query, flow_challenge_response_request=flow_challenge_response_request)
        print("The response of FlowsApi->flows_executor_solve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->flows_executor_solve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_slug** | **str**|  | 
 **query** | **str**| Querystring as received | 
 **flow_challenge_response_request** | [**FlowChallengeResponseRequest**](FlowChallengeResponseRequest.md)|  | [optional] 

### Return type

[**ChallengeTypes**](ChallengeTypes.md)

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

# **flows_inspector_get**
> FlowInspection flows_inspector_get(flow_slug)



Get current flow state and record it

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.flow_inspection import FlowInspection
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
    api_instance = authentik_openapi.FlowsApi(api_client)
    flow_slug = 'flow_slug_example' # str | 

    try:
        api_response = api_instance.flows_inspector_get(flow_slug)
        print("The response of FlowsApi->flows_inspector_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->flows_inspector_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_slug** | **str**|  | 

### Return type

[**FlowInspection**](FlowInspection.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | No flow plan in session. |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flows_instances_cache_clear_create**
> flows_instances_cache_clear_create()



Clear flow cache

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
    api_instance = authentik_openapi.FlowsApi(api_client)

    try:
        api_instance.flows_instances_cache_clear_create()
    except Exception as e:
        print("Exception when calling FlowsApi->flows_instances_cache_clear_create: %s\n" % e)
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
**204** | Successfully cleared cache |  -  |
**400** | Bad request |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flows_instances_cache_info_retrieve**
> Cache flows_instances_cache_info_retrieve()



Info about cached flows

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.cache import Cache
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
    api_instance = authentik_openapi.FlowsApi(api_client)

    try:
        api_response = api_instance.flows_instances_cache_info_retrieve()
        print("The response of FlowsApi->flows_instances_cache_info_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->flows_instances_cache_info_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Cache**](Cache.md)

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

# **flows_instances_create**
> Flow flows_instances_create(flow_request)



Flow Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.flow import Flow
from authentik_openapi.models.flow_request import FlowRequest
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
    api_instance = authentik_openapi.FlowsApi(api_client)
    flow_request = authentik_openapi.FlowRequest() # FlowRequest | 

    try:
        api_response = api_instance.flows_instances_create(flow_request)
        print("The response of FlowsApi->flows_instances_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->flows_instances_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow_request** | [**FlowRequest**](FlowRequest.md)|  | 

### Return type

[**Flow**](Flow.md)

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

# **flows_instances_destroy**
> flows_instances_destroy(slug)



Flow Viewset

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
    api_instance = authentik_openapi.FlowsApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_instance.flows_instances_destroy(slug)
    except Exception as e:
        print("Exception when calling FlowsApi->flows_instances_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

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

# **flows_instances_diagram_retrieve**
> FlowDiagram flows_instances_diagram_retrieve(slug)



Return diagram for flow with slug `slug`, in the format used by flowchart.js

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.flow_diagram import FlowDiagram
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
    api_instance = authentik_openapi.FlowsApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.flows_instances_diagram_retrieve(slug)
        print("The response of FlowsApi->flows_instances_diagram_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->flows_instances_diagram_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**FlowDiagram**](FlowDiagram.md)

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

# **flows_instances_execute_retrieve**
> Link flows_instances_execute_retrieve(slug)



Execute flow for current user

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.link import Link
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
    api_instance = authentik_openapi.FlowsApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.flows_instances_execute_retrieve(slug)
        print("The response of FlowsApi->flows_instances_execute_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->flows_instances_execute_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**Link**](Link.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Flow not applicable |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flows_instances_export_retrieve**
> bytearray flows_instances_export_retrieve(slug)



Export flow to .yaml file

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
    api_instance = authentik_openapi.FlowsApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.flows_instances_export_retrieve(slug)
        print("The response of FlowsApi->flows_instances_export_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->flows_instances_export_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

**bytearray**

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

# **flows_instances_import_create**
> FlowImportResult flows_instances_import_create(file=file, clear=clear)



Import flow from .yaml file

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.flow_import_result import FlowImportResult
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
    api_instance = authentik_openapi.FlowsApi(api_client)
    file = None # bytearray |  (optional)
    clear = False # bool |  (optional) (default to False)

    try:
        api_response = api_instance.flows_instances_import_create(file=file, clear=clear)
        print("The response of FlowsApi->flows_instances_import_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->flows_instances_import_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | [optional] 
 **clear** | **bool**|  | [optional] [default to False]

### Return type

[**FlowImportResult**](FlowImportResult.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flows_instances_list**
> PaginatedFlowList flows_instances_list(denied_action=denied_action, designation=designation, flow_uuid=flow_uuid, name=name, ordering=ordering, page=page, page_size=page_size, search=search, slug=slug)



Flow Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.paginated_flow_list import PaginatedFlowList
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
    api_instance = authentik_openapi.FlowsApi(api_client)
    denied_action = 'denied_action_example' # str | Configure what should happen when a flow denies access to a user.   (optional)
    designation = 'designation_example' # str | Decides what this Flow is used for. For example, the Authentication flow is redirect to when an un-authenticated user visits authentik.   (optional)
    flow_uuid = 'flow_uuid_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    slug = 'slug_example' # str |  (optional)

    try:
        api_response = api_instance.flows_instances_list(denied_action=denied_action, designation=designation, flow_uuid=flow_uuid, name=name, ordering=ordering, page=page, page_size=page_size, search=search, slug=slug)
        print("The response of FlowsApi->flows_instances_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->flows_instances_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **denied_action** | **str**| Configure what should happen when a flow denies access to a user.   | [optional] 
 **designation** | **str**| Decides what this Flow is used for. For example, the Authentication flow is redirect to when an un-authenticated user visits authentik.   | [optional] 
 **flow_uuid** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **slug** | **str**|  | [optional] 

### Return type

[**PaginatedFlowList**](PaginatedFlowList.md)

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

# **flows_instances_partial_update**
> Flow flows_instances_partial_update(slug, patched_flow_request=patched_flow_request)



Flow Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.flow import Flow
from authentik_openapi.models.patched_flow_request import PatchedFlowRequest
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
    api_instance = authentik_openapi.FlowsApi(api_client)
    slug = 'slug_example' # str | 
    patched_flow_request = authentik_openapi.PatchedFlowRequest() # PatchedFlowRequest |  (optional)

    try:
        api_response = api_instance.flows_instances_partial_update(slug, patched_flow_request=patched_flow_request)
        print("The response of FlowsApi->flows_instances_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->flows_instances_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **patched_flow_request** | [**PatchedFlowRequest**](PatchedFlowRequest.md)|  | [optional] 

### Return type

[**Flow**](Flow.md)

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

# **flows_instances_retrieve**
> Flow flows_instances_retrieve(slug)



Flow Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.flow import Flow
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
    api_instance = authentik_openapi.FlowsApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.flows_instances_retrieve(slug)
        print("The response of FlowsApi->flows_instances_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->flows_instances_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**Flow**](Flow.md)

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

# **flows_instances_set_background_create**
> flows_instances_set_background_create(slug, file=file, clear=clear)



Set Flow background

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
    api_instance = authentik_openapi.FlowsApi(api_client)
    slug = 'slug_example' # str | 
    file = None # bytearray |  (optional)
    clear = False # bool |  (optional) (default to False)

    try:
        api_instance.flows_instances_set_background_create(slug, file=file, clear=clear)
    except Exception as e:
        print("Exception when calling FlowsApi->flows_instances_set_background_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **file** | **bytearray**|  | [optional] 
 **clear** | **bool**|  | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flows_instances_set_background_url_create**
> flows_instances_set_background_url_create(slug, file_path_request)



Set Flow background (as URL)

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.file_path_request import FilePathRequest
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
    api_instance = authentik_openapi.FlowsApi(api_client)
    slug = 'slug_example' # str | 
    file_path_request = authentik_openapi.FilePathRequest() # FilePathRequest | 

    try:
        api_instance.flows_instances_set_background_url_create(slug, file_path_request)
    except Exception as e:
        print("Exception when calling FlowsApi->flows_instances_set_background_url_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **file_path_request** | [**FilePathRequest**](FilePathRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flows_instances_update**
> Flow flows_instances_update(slug, flow_request)



Flow Viewset

### Example

* Bearer Authentication (authentik):

```python
import authentik_openapi
from authentik_openapi.models.flow import Flow
from authentik_openapi.models.flow_request import FlowRequest
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
    api_instance = authentik_openapi.FlowsApi(api_client)
    slug = 'slug_example' # str | 
    flow_request = authentik_openapi.FlowRequest() # FlowRequest | 

    try:
        api_response = api_instance.flows_instances_update(slug, flow_request)
        print("The response of FlowsApi->flows_instances_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->flows_instances_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **flow_request** | [**FlowRequest**](FlowRequest.md)|  | 

### Return type

[**Flow**](Flow.md)

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

# **flows_instances_used_by_list**
> List[UsedBy] flows_instances_used_by_list(slug)



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
    api_instance = authentik_openapi.FlowsApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.flows_instances_used_by_list(slug)
        print("The response of FlowsApi->flows_instances_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FlowsApi->flows_instances_used_by_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

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

