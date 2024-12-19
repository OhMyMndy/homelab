# github_openapi.ClassroomApi

All URIs are relative to *https://api.github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**classroom_get_a_classroom**](ClassroomApi.md#classroom_get_a_classroom) | **GET** /classrooms/{classroom_id} | Get a classroom
[**classroom_get_an_assignment**](ClassroomApi.md#classroom_get_an_assignment) | **GET** /assignments/{assignment_id} | Get an assignment
[**classroom_get_assignment_grades**](ClassroomApi.md#classroom_get_assignment_grades) | **GET** /assignments/{assignment_id}/grades | Get assignment grades
[**classroom_list_accepted_assignments_for_an_assignment**](ClassroomApi.md#classroom_list_accepted_assignments_for_an_assignment) | **GET** /assignments/{assignment_id}/accepted_assignments | List accepted assignments for an assignment
[**classroom_list_assignments_for_a_classroom**](ClassroomApi.md#classroom_list_assignments_for_a_classroom) | **GET** /classrooms/{classroom_id}/assignments | List assignments for a classroom
[**classroom_list_classrooms**](ClassroomApi.md#classroom_list_classrooms) | **GET** /classrooms | List classrooms


# **classroom_get_a_classroom**
> Classroom classroom_get_a_classroom(classroom_id)

Get a classroom

Gets a GitHub Classroom classroom for the current user. Classroom will only be returned if the current user is an administrator of the GitHub Classroom.

### Example


```python
import github_openapi
from github_openapi.models.classroom import Classroom
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
    api_instance = github_openapi.ClassroomApi(api_client)
    classroom_id = 56 # int | The unique identifier of the classroom.

    try:
        # Get a classroom
        api_response = api_instance.classroom_get_a_classroom(classroom_id)
        print("The response of ClassroomApi->classroom_get_a_classroom:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassroomApi->classroom_get_a_classroom: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classroom_id** | **int**| The unique identifier of the classroom. | 

### Return type

[**Classroom**](Classroom.md)

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

# **classroom_get_an_assignment**
> ClassroomAssignment classroom_get_an_assignment(assignment_id)

Get an assignment

Gets a GitHub Classroom assignment. Assignment will only be returned if the current user is an administrator of the GitHub Classroom for the assignment.

### Example


```python
import github_openapi
from github_openapi.models.classroom_assignment import ClassroomAssignment
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
    api_instance = github_openapi.ClassroomApi(api_client)
    assignment_id = 56 # int | The unique identifier of the classroom assignment.

    try:
        # Get an assignment
        api_response = api_instance.classroom_get_an_assignment(assignment_id)
        print("The response of ClassroomApi->classroom_get_an_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassroomApi->classroom_get_an_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **int**| The unique identifier of the classroom assignment. | 

### Return type

[**ClassroomAssignment**](ClassroomAssignment.md)

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

# **classroom_get_assignment_grades**
> List[ClassroomAssignmentGrade] classroom_get_assignment_grades(assignment_id)

Get assignment grades

Gets grades for a GitHub Classroom assignment. Grades will only be returned if the current user is an administrator of the GitHub Classroom for the assignment.

### Example


```python
import github_openapi
from github_openapi.models.classroom_assignment_grade import ClassroomAssignmentGrade
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
    api_instance = github_openapi.ClassroomApi(api_client)
    assignment_id = 56 # int | The unique identifier of the classroom assignment.

    try:
        # Get assignment grades
        api_response = api_instance.classroom_get_assignment_grades(assignment_id)
        print("The response of ClassroomApi->classroom_get_assignment_grades:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassroomApi->classroom_get_assignment_grades: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **int**| The unique identifier of the classroom assignment. | 

### Return type

[**List[ClassroomAssignmentGrade]**](ClassroomAssignmentGrade.md)

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

# **classroom_list_accepted_assignments_for_an_assignment**
> List[ClassroomAcceptedAssignment] classroom_list_accepted_assignments_for_an_assignment(assignment_id, page=page, per_page=per_page)

List accepted assignments for an assignment

Lists any assignment repositories that have been created by students accepting a GitHub Classroom assignment. Accepted assignments will only be returned if the current user is an administrator of the GitHub Classroom for the assignment.

### Example


```python
import github_openapi
from github_openapi.models.classroom_accepted_assignment import ClassroomAcceptedAssignment
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
    api_instance = github_openapi.ClassroomApi(api_client)
    assignment_id = 56 # int | The unique identifier of the classroom assignment.
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)

    try:
        # List accepted assignments for an assignment
        api_response = api_instance.classroom_list_accepted_assignments_for_an_assignment(assignment_id, page=page, per_page=per_page)
        print("The response of ClassroomApi->classroom_list_accepted_assignments_for_an_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassroomApi->classroom_list_accepted_assignments_for_an_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **int**| The unique identifier of the classroom assignment. | 
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]

### Return type

[**List[ClassroomAcceptedAssignment]**](ClassroomAcceptedAssignment.md)

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

# **classroom_list_assignments_for_a_classroom**
> List[SimpleClassroomAssignment] classroom_list_assignments_for_a_classroom(classroom_id, page=page, per_page=per_page)

List assignments for a classroom

Lists GitHub Classroom assignments for a classroom. Assignments will only be returned if the current user is an administrator of the GitHub Classroom.

### Example


```python
import github_openapi
from github_openapi.models.simple_classroom_assignment import SimpleClassroomAssignment
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
    api_instance = github_openapi.ClassroomApi(api_client)
    classroom_id = 56 # int | The unique identifier of the classroom.
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)

    try:
        # List assignments for a classroom
        api_response = api_instance.classroom_list_assignments_for_a_classroom(classroom_id, page=page, per_page=per_page)
        print("The response of ClassroomApi->classroom_list_assignments_for_a_classroom:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassroomApi->classroom_list_assignments_for_a_classroom: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classroom_id** | **int**| The unique identifier of the classroom. | 
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]

### Return type

[**List[SimpleClassroomAssignment]**](SimpleClassroomAssignment.md)

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

# **classroom_list_classrooms**
> List[SimpleClassroom] classroom_list_classrooms(page=page, per_page=per_page)

List classrooms

Lists GitHub Classroom classrooms for the current user. Classrooms will only be returned if the current user is an administrator of one or more GitHub Classrooms.

### Example


```python
import github_openapi
from github_openapi.models.simple_classroom import SimpleClassroom
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
    api_instance = github_openapi.ClassroomApi(api_client)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)

    try:
        # List classrooms
        api_response = api_instance.classroom_list_classrooms(page=page, per_page=per_page)
        print("The response of ClassroomApi->classroom_list_classrooms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClassroomApi->classroom_list_classrooms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]

### Return type

[**List[SimpleClassroom]**](SimpleClassroom.md)

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

