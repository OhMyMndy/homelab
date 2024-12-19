# github_openapi.CopilotApi

All URIs are relative to *https://api.github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copilot_add_copilot_seats_for_teams**](CopilotApi.md#copilot_add_copilot_seats_for_teams) | **POST** /orgs/{org}/copilot/billing/selected_teams | Add teams to the Copilot subscription for an organization
[**copilot_add_copilot_seats_for_users**](CopilotApi.md#copilot_add_copilot_seats_for_users) | **POST** /orgs/{org}/copilot/billing/selected_users | Add users to the Copilot subscription for an organization
[**copilot_cancel_copilot_seat_assignment_for_teams**](CopilotApi.md#copilot_cancel_copilot_seat_assignment_for_teams) | **DELETE** /orgs/{org}/copilot/billing/selected_teams | Remove teams from the Copilot subscription for an organization
[**copilot_cancel_copilot_seat_assignment_for_users**](CopilotApi.md#copilot_cancel_copilot_seat_assignment_for_users) | **DELETE** /orgs/{org}/copilot/billing/selected_users | Remove users from the Copilot subscription for an organization
[**copilot_copilot_metrics_for_organization**](CopilotApi.md#copilot_copilot_metrics_for_organization) | **GET** /orgs/{org}/copilot/metrics | Get Copilot metrics for an organization
[**copilot_copilot_metrics_for_team**](CopilotApi.md#copilot_copilot_metrics_for_team) | **GET** /orgs/{org}/team/{team_slug}/copilot/metrics | Get Copilot metrics for a team
[**copilot_get_copilot_organization_details**](CopilotApi.md#copilot_get_copilot_organization_details) | **GET** /orgs/{org}/copilot/billing | Get Copilot seat information and settings for an organization
[**copilot_get_copilot_seat_details_for_user**](CopilotApi.md#copilot_get_copilot_seat_details_for_user) | **GET** /orgs/{org}/members/{username}/copilot | Get Copilot seat assignment details for a user
[**copilot_list_copilot_seats**](CopilotApi.md#copilot_list_copilot_seats) | **GET** /orgs/{org}/copilot/billing/seats | List all Copilot seat assignments for an organization
[**copilot_usage_metrics_for_org**](CopilotApi.md#copilot_usage_metrics_for_org) | **GET** /orgs/{org}/copilot/usage | Get a summary of Copilot usage for organization members
[**copilot_usage_metrics_for_team**](CopilotApi.md#copilot_usage_metrics_for_team) | **GET** /orgs/{org}/team/{team_slug}/copilot/usage | Get a summary of Copilot usage for a team


# **copilot_add_copilot_seats_for_teams**
> CopilotAddCopilotSeatsForTeams201Response copilot_add_copilot_seats_for_teams(org, copilot_add_copilot_seats_for_teams_request)

Add teams to the Copilot subscription for an organization

> [!NOTE] > This endpoint is in public preview and is subject to change.  Purchases a GitHub Copilot seat for all users within each specified team. The organization will be billed for each seat based on the organization's Copilot plan. For more information about Copilot pricing, see \"[About billing for GitHub Copilot in your organization](https://docs.github.com/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-the-copilot-subscription-for-your-organization/about-billing-for-github-copilot-in-your-organization).\"  Only organization owners can purchase Copilot seats for their organization members. The organization must have a Copilot Business or Copilot Enterprise subscription and a configured suggestion matching policy. For more information about setting up a Copilot subscription, see \"[Subscribing to Copilot for your organization](https://docs.github.com/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-the-copilot-subscription-for-your-organization/subscribing-to-copilot-for-your-organization).\" For more information about setting a suggestion matching policy, see \"[Managing policies for Copilot in your organization](https://docs.github.com/copilot/managing-copilot/managing-github-copilot-in-your-organization/setting-policies-for-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization#policies-for-suggestion-matching).\"  The response contains the total number of new seats that were created and existing seats that were refreshed.  OAuth app tokens and personal access tokens (classic) need either the `manage_billing:copilot` or `admin:org` scopes to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.copilot_add_copilot_seats_for_teams201_response import CopilotAddCopilotSeatsForTeams201Response
from github_openapi.models.copilot_add_copilot_seats_for_teams_request import CopilotAddCopilotSeatsForTeamsRequest
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
    api_instance = github_openapi.CopilotApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    copilot_add_copilot_seats_for_teams_request = {"selected_teams":["engteam1","engteam2","engteam3"]} # CopilotAddCopilotSeatsForTeamsRequest | 

    try:
        # Add teams to the Copilot subscription for an organization
        api_response = api_instance.copilot_add_copilot_seats_for_teams(org, copilot_add_copilot_seats_for_teams_request)
        print("The response of CopilotApi->copilot_add_copilot_seats_for_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CopilotApi->copilot_add_copilot_seats_for_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **copilot_add_copilot_seats_for_teams_request** | [**CopilotAddCopilotSeatsForTeamsRequest**](CopilotAddCopilotSeatsForTeamsRequest.md)|  | 

### Return type

[**CopilotAddCopilotSeatsForTeams201Response**](CopilotAddCopilotSeatsForTeams201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**500** | Internal Error |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**422** | Copilot Business or Enterprise is not enabled for this organization, billing has not been set up for this organization, a public code suggestions policy has not been set for this organization, or the organization&#39;s Copilot access setting is set to enable Copilot for all users or is unconfigured. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copilot_add_copilot_seats_for_users**
> CopilotAddCopilotSeatsForUsers201Response copilot_add_copilot_seats_for_users(org, copilot_add_copilot_seats_for_users_request)

Add users to the Copilot subscription for an organization

> [!NOTE] > This endpoint is in public preview and is subject to change.  Purchases a GitHub Copilot seat for each user specified. The organization will be billed for each seat based on the organization's Copilot plan. For more information about Copilot pricing, see \"[About billing for GitHub Copilot in your organization](https://docs.github.com/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-the-copilot-subscription-for-your-organization/about-billing-for-github-copilot-in-your-organization).\"  Only organization owners can purchase Copilot seats for their organization members. The organization must have a Copilot Business or Copilot Enterprise subscription and a configured suggestion matching policy. For more information about setting up a Copilot subscription, see \"[Subscribing to Copilot for your organization](https://docs.github.com/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-the-copilot-subscription-for-your-organization/subscribing-to-copilot-for-your-organization).\" For more information about setting a suggestion matching policy, see \"[Managing policies for Copilot in your organization](https://docs.github.com/copilot/managing-copilot/managing-github-copilot-in-your-organization/setting-policies-for-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization#policies-for-suggestion-matching).\"  The response contains the total number of new seats that were created and existing seats that were refreshed.  OAuth app tokens and personal access tokens (classic) need either the `manage_billing:copilot` or `admin:org` scopes to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.copilot_add_copilot_seats_for_users201_response import CopilotAddCopilotSeatsForUsers201Response
from github_openapi.models.copilot_add_copilot_seats_for_users_request import CopilotAddCopilotSeatsForUsersRequest
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
    api_instance = github_openapi.CopilotApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    copilot_add_copilot_seats_for_users_request = {"selected_usernames":["cooluser1","hacker2","octocat"]} # CopilotAddCopilotSeatsForUsersRequest | 

    try:
        # Add users to the Copilot subscription for an organization
        api_response = api_instance.copilot_add_copilot_seats_for_users(org, copilot_add_copilot_seats_for_users_request)
        print("The response of CopilotApi->copilot_add_copilot_seats_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CopilotApi->copilot_add_copilot_seats_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **copilot_add_copilot_seats_for_users_request** | [**CopilotAddCopilotSeatsForUsersRequest**](CopilotAddCopilotSeatsForUsersRequest.md)|  | 

### Return type

[**CopilotAddCopilotSeatsForUsers201Response**](CopilotAddCopilotSeatsForUsers201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**500** | Internal Error |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**422** | Copilot Business or Enterprise is not enabled for this organization, billing has not been set up for this organization, a public code suggestions policy has not been set for this organization, or the organization&#39;s Copilot access setting is set to enable Copilot for all users or is unconfigured. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copilot_cancel_copilot_seat_assignment_for_teams**
> CopilotCancelCopilotSeatAssignmentForTeams200Response copilot_cancel_copilot_seat_assignment_for_teams(org, copilot_cancel_copilot_seat_assignment_for_teams_request)

Remove teams from the Copilot subscription for an organization

> [!NOTE] > This endpoint is in public preview and is subject to change.  Sets seats for all members of each team specified to \"pending cancellation\". This will cause the members of the specified team(s) to lose access to GitHub Copilot at the end of the current billing cycle unless they retain access through another team. For more information about disabling access to Copilot, see \"[Revoking access to Copilot for members of your organization](https://docs.github.com/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-access-to-github-copilot-in-your-organization/revoking-access-to-copilot-for-members-of-your-organization).\"  Only organization owners can cancel Copilot seats for their organization members.  The response contains the total number of seats set to \"pending cancellation\".  OAuth app tokens and personal access tokens (classic) need either the `manage_billing:copilot` or `admin:org` scopes to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.copilot_cancel_copilot_seat_assignment_for_teams200_response import CopilotCancelCopilotSeatAssignmentForTeams200Response
from github_openapi.models.copilot_cancel_copilot_seat_assignment_for_teams_request import CopilotCancelCopilotSeatAssignmentForTeamsRequest
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
    api_instance = github_openapi.CopilotApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    copilot_cancel_copilot_seat_assignment_for_teams_request = {"selected_teams":["engteam1","engteam2","engteam3"]} # CopilotCancelCopilotSeatAssignmentForTeamsRequest | 

    try:
        # Remove teams from the Copilot subscription for an organization
        api_response = api_instance.copilot_cancel_copilot_seat_assignment_for_teams(org, copilot_cancel_copilot_seat_assignment_for_teams_request)
        print("The response of CopilotApi->copilot_cancel_copilot_seat_assignment_for_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CopilotApi->copilot_cancel_copilot_seat_assignment_for_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **copilot_cancel_copilot_seat_assignment_for_teams_request** | [**CopilotCancelCopilotSeatAssignmentForTeamsRequest**](CopilotCancelCopilotSeatAssignmentForTeamsRequest.md)|  | 

### Return type

[**CopilotCancelCopilotSeatAssignmentForTeams200Response**](CopilotCancelCopilotSeatAssignmentForTeams200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Error |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**422** | Copilot Business or Enterprise is not enabled for this organization, billing has not been set up for this organization, a public code suggestions policy has not been set for this organization, or the organization&#39;s Copilot access setting is set to enable Copilot for all users or is unconfigured. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copilot_cancel_copilot_seat_assignment_for_users**
> CopilotCancelCopilotSeatAssignmentForUsers200Response copilot_cancel_copilot_seat_assignment_for_users(org, copilot_cancel_copilot_seat_assignment_for_users_request)

Remove users from the Copilot subscription for an organization

> [!NOTE] > This endpoint is in public preview and is subject to change.  Sets seats for all users specified to \"pending cancellation\". This will cause the specified users to lose access to GitHub Copilot at the end of the current billing cycle unless they retain access through team membership. For more information about disabling access to Copilot, see \"[Revoking access to Copilot for members of your organization](https://docs.github.com/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-access-to-github-copilot-in-your-organization/revoking-access-to-copilot-for-members-of-your-organization).\"  Only organization owners can cancel Copilot seats for their organization members.  The response contains the total number of seats set to \"pending cancellation\".  OAuth app tokens and personal access tokens (classic) need either the `manage_billing:copilot` or `admin:org` scopes to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.copilot_cancel_copilot_seat_assignment_for_users200_response import CopilotCancelCopilotSeatAssignmentForUsers200Response
from github_openapi.models.copilot_cancel_copilot_seat_assignment_for_users_request import CopilotCancelCopilotSeatAssignmentForUsersRequest
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
    api_instance = github_openapi.CopilotApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    copilot_cancel_copilot_seat_assignment_for_users_request = {"selected_usernames":["cooluser1","hacker2","octocat"]} # CopilotCancelCopilotSeatAssignmentForUsersRequest | 

    try:
        # Remove users from the Copilot subscription for an organization
        api_response = api_instance.copilot_cancel_copilot_seat_assignment_for_users(org, copilot_cancel_copilot_seat_assignment_for_users_request)
        print("The response of CopilotApi->copilot_cancel_copilot_seat_assignment_for_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CopilotApi->copilot_cancel_copilot_seat_assignment_for_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **copilot_cancel_copilot_seat_assignment_for_users_request** | [**CopilotCancelCopilotSeatAssignmentForUsersRequest**](CopilotCancelCopilotSeatAssignmentForUsersRequest.md)|  | 

### Return type

[**CopilotCancelCopilotSeatAssignmentForUsers200Response**](CopilotCancelCopilotSeatAssignmentForUsers200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Error |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**422** | Copilot Business or Enterprise is not enabled for this organization, billing has not been set up for this organization, a public code suggestions policy has not been set for this organization, the seat management setting is set to enable Copilot for all users or is unconfigured, or a user&#39;s seat cannot be cancelled because it was assigned to them via a team. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copilot_copilot_metrics_for_organization**
> List[CopilotUsageMetricsDay] copilot_copilot_metrics_for_organization(org, since=since, until=until, page=page, per_page=per_page)

Get Copilot metrics for an organization

Use this endpoint to see a breakdown of aggregated metrics for various GitHub Copilot features. See the response schema tab for detailed metrics definitions.  > [!NOTE] > This endpoint will only return results for a given day if the organization contained **five or more members with active Copilot licenses** on that day, as evaluated at the end of that day.  The response contains metrics for up to 28 days prior. Metrics are processed once per day for the previous day, and the response will only include data up until yesterday. In order for an end user to be counted towards these metrics, they must have telemetry enabled in their IDE.  To access this endpoint, the Copilot Metrics API access policy must be enabled for the organization. Only organization owners and owners and billing managers of the parent enterprise can view Copilot metrics.  OAuth app tokens and personal access tokens (classic) need either the `manage_billing:copilot`, `read:org`, or `read:enterprise` scopes to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.copilot_usage_metrics_day import CopilotUsageMetricsDay
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
    api_instance = github_openapi.CopilotApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    since = 'since_example' # str | Show usage metrics since this date. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format (`YYYY-MM-DDTHH:MM:SSZ`). Maximum value is 28 days ago. (optional)
    until = 'until_example' # str | Show usage metrics until this date. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format (`YYYY-MM-DDTHH:MM:SSZ`) and should not preceed the `since` date if it is passed. (optional)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    per_page = 28 # int | The number of days of metrics to display per page (max 28). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 28)

    try:
        # Get Copilot metrics for an organization
        api_response = api_instance.copilot_copilot_metrics_for_organization(org, since=since, until=until, page=page, per_page=per_page)
        print("The response of CopilotApi->copilot_copilot_metrics_for_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CopilotApi->copilot_copilot_metrics_for_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **since** | **str**| Show usage metrics since this date. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format (&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;). Maximum value is 28 days ago. | [optional] 
 **until** | **str**| Show usage metrics until this date. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format (&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;) and should not preceed the &#x60;since&#x60; date if it is passed. | [optional] 
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **per_page** | **int**| The number of days of metrics to display per page (max 28). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 28]

### Return type

[**List[CopilotUsageMetricsDay]**](CopilotUsageMetricsDay.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**500** | Internal Error |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**422** | Copilot Usage Merics API setting is disabled at the organization or enterprise level. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copilot_copilot_metrics_for_team**
> List[CopilotUsageMetricsDay] copilot_copilot_metrics_for_team(org, team_slug, since=since, until=until, page=page, per_page=per_page)

Get Copilot metrics for a team

Use this endpoint to see a breakdown of aggregated metrics for various GitHub Copilot features. See the response schema tab for detailed metrics definitions.  > [!NOTE] > This endpoint will only return results for a given day if the team had **five or more members with active Copilot licenses** on that day, as evaluated at the end of that day.  The response contains metrics for up to 28 days prior. Metrics are processed once per day for the previous day, and the response will only include data up until yesterday. In order for an end user to be counted towards these metrics, they must have telemetry enabled in their IDE.  To access this endpoint, the Copilot Metrics API access policy must be enabled for the organization containing the team within GitHub settings. Only organization owners for the organization that contains this team and owners and billing managers of the parent enterprise can view Copilot metrics for a team.  OAuth app tokens and personal access tokens (classic) need either the `manage_billing:copilot`, `read:org`, or `read:enterprise` scopes to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.copilot_usage_metrics_day import CopilotUsageMetricsDay
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
    api_instance = github_openapi.CopilotApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    since = 'since_example' # str | Show usage metrics since this date. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format (`YYYY-MM-DDTHH:MM:SSZ`). Maximum value is 28 days ago. (optional)
    until = 'until_example' # str | Show usage metrics until this date. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format (`YYYY-MM-DDTHH:MM:SSZ`) and should not preceed the `since` date if it is passed. (optional)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    per_page = 28 # int | The number of days of metrics to display per page (max 28). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 28)

    try:
        # Get Copilot metrics for a team
        api_response = api_instance.copilot_copilot_metrics_for_team(org, team_slug, since=since, until=until, page=page, per_page=per_page)
        print("The response of CopilotApi->copilot_copilot_metrics_for_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CopilotApi->copilot_copilot_metrics_for_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
 **since** | **str**| Show usage metrics since this date. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format (&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;). Maximum value is 28 days ago. | [optional] 
 **until** | **str**| Show usage metrics until this date. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format (&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;) and should not preceed the &#x60;since&#x60; date if it is passed. | [optional] 
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **per_page** | **int**| The number of days of metrics to display per page (max 28). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 28]

### Return type

[**List[CopilotUsageMetricsDay]**](CopilotUsageMetricsDay.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**500** | Internal Error |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**422** | Copilot Usage Merics API setting is disabled at the organization or enterprise level. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copilot_get_copilot_organization_details**
> CopilotOrganizationDetails copilot_get_copilot_organization_details(org)

Get Copilot seat information and settings for an organization

> [!NOTE] > This endpoint is in public preview and is subject to change.  Gets information about an organization's Copilot subscription, including seat breakdown and feature policies. To configure these settings, go to your organization's settings on GitHub.com. For more information, see \"[Managing policies for Copilot in your organization](https://docs.github.com/copilot/managing-copilot/managing-policies-for-copilot-business-in-your-organization).\"  Only organization owners can view details about the organization's Copilot Business or Copilot Enterprise subscription.  OAuth app tokens and personal access tokens (classic) need either the `manage_billing:copilot` or `read:org` scopes to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.copilot_organization_details import CopilotOrganizationDetails
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
    api_instance = github_openapi.CopilotApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.

    try:
        # Get Copilot seat information and settings for an organization
        api_response = api_instance.copilot_get_copilot_organization_details(org)
        print("The response of CopilotApi->copilot_get_copilot_organization_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CopilotApi->copilot_get_copilot_organization_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 

### Return type

[**CopilotOrganizationDetails**](CopilotOrganizationDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Error |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**422** | There is a problem with your account&#39;s associated payment method. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copilot_get_copilot_seat_details_for_user**
> CopilotSeatDetails copilot_get_copilot_seat_details_for_user(org, username)

Get Copilot seat assignment details for a user

> [!NOTE] > This endpoint is in public preview and is subject to change.  Gets the GitHub Copilot seat details for a member of an organization who currently has access to GitHub Copilot.  The seat object contains information about the user's most recent Copilot activity. Users must have telemetry enabled in their IDE for Copilot in the IDE activity to be reflected in `last_activity_at`. For more information about activity data, see \"[Reviewing user activity data for Copilot in your organization](https://docs.github.com/copilot/managing-copilot/managing-github-copilot-in-your-organization/reviewing-activity-related-to-github-copilot-in-your-organization/reviewing-user-activity-data-for-copilot-in-your-organization).\"  Only organization owners can view Copilot seat assignment details for members of their organization.  OAuth app tokens and personal access tokens (classic) need either the `manage_billing:copilot` or `read:org` scopes to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.copilot_seat_details import CopilotSeatDetails
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
    api_instance = github_openapi.CopilotApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Get Copilot seat assignment details for a user
        api_response = api_instance.copilot_get_copilot_seat_details_for_user(org, username)
        print("The response of CopilotApi->copilot_get_copilot_seat_details_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CopilotApi->copilot_get_copilot_seat_details_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **username** | **str**| The handle for the GitHub user account. | 

### Return type

[**CopilotSeatDetails**](CopilotSeatDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user&#39;s GitHub Copilot seat details, including usage. |  -  |
**500** | Internal Error |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**422** | Copilot Business or Enterprise is not enabled for this organization or the user has a pending organization invitation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copilot_list_copilot_seats**
> CopilotListCopilotSeats200Response copilot_list_copilot_seats(org, page=page, per_page=per_page)

List all Copilot seat assignments for an organization

> [!NOTE] > This endpoint is in public preview and is subject to change.  Lists all Copilot seats for which an organization with a Copilot Business or Copilot Enterprise subscription is currently being billed. Only organization owners can view assigned seats.  Each seat object contains information about the assigned user's most recent Copilot activity. Users must have telemetry enabled in their IDE for Copilot in the IDE activity to be reflected in `last_activity_at`. For more information about activity data, see \"[Reviewing user activity data for Copilot in your organization](https://docs.github.com/copilot/managing-copilot/managing-github-copilot-in-your-organization/reviewing-activity-related-to-github-copilot-in-your-organization/reviewing-user-activity-data-for-copilot-in-your-organization).\"  OAuth app tokens and personal access tokens (classic) need either the `manage_billing:copilot` or `read:org` scopes to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.copilot_list_copilot_seats200_response import CopilotListCopilotSeats200Response
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
    api_instance = github_openapi.CopilotApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    per_page = 50 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 50)

    try:
        # List all Copilot seat assignments for an organization
        api_response = api_instance.copilot_list_copilot_seats(org, page=page, per_page=per_page)
        print("The response of CopilotApi->copilot_list_copilot_seats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CopilotApi->copilot_list_copilot_seats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 50]

### Return type

[**CopilotListCopilotSeats200Response**](CopilotListCopilotSeats200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |
**500** | Internal Error |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copilot_usage_metrics_for_org**
> List[CopilotUsageMetrics] copilot_usage_metrics_for_org(org, since=since, until=until, page=page, per_page=per_page)

Get a summary of Copilot usage for organization members

> [!NOTE] > This endpoint is in public preview and is subject to change.  You can use this endpoint to see a daily breakdown of aggregated usage metrics for Copilot completions and Copilot Chat in the IDE across an organization, with a further breakdown of suggestions, acceptances, and number of active users by editor and language for each day. See the response schema tab for detailed metrics definitions.  The response contains metrics for up to 28 days prior. Usage metrics are processed once per day for the previous day, and the response will only include data up until yesterday. In order for an end user to be counted towards these metrics, they must have telemetry enabled in their IDE.  Organization owners, and owners and billing managers of the parent enterprise, can view Copilot usage metrics.  OAuth app tokens and personal access tokens (classic) need either the `manage_billing:copilot`, `read:org`, or `read:enterprise` scopes to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.copilot_usage_metrics import CopilotUsageMetrics
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
    api_instance = github_openapi.CopilotApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    since = 'since_example' # str | Show usage metrics since this date. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format (`YYYY-MM-DDTHH:MM:SSZ`). Maximum value is 28 days ago. (optional)
    until = 'until_example' # str | Show usage metrics until this date. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format (`YYYY-MM-DDTHH:MM:SSZ`) and should not preceed the `since` date if it is passed. (optional)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    per_page = 28 # int | The number of days of metrics to display per page (max 28). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 28)

    try:
        # Get a summary of Copilot usage for organization members
        api_response = api_instance.copilot_usage_metrics_for_org(org, since=since, until=until, page=page, per_page=per_page)
        print("The response of CopilotApi->copilot_usage_metrics_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CopilotApi->copilot_usage_metrics_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **since** | **str**| Show usage metrics since this date. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format (&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;). Maximum value is 28 days ago. | [optional] 
 **until** | **str**| Show usage metrics until this date. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format (&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;) and should not preceed the &#x60;since&#x60; date if it is passed. | [optional] 
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **per_page** | **int**| The number of days of metrics to display per page (max 28). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 28]

### Return type

[**List[CopilotUsageMetrics]**](CopilotUsageMetrics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**500** | Internal Error |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copilot_usage_metrics_for_team**
> List[CopilotUsageMetrics] copilot_usage_metrics_for_team(org, team_slug, since=since, until=until, page=page, per_page=per_page)

Get a summary of Copilot usage for a team

> [!NOTE] > This endpoint is in public preview and is subject to change.  You can use this endpoint to see a daily breakdown of aggregated usage metrics for Copilot completions and Copilot Chat in the IDE for users within a team, with a further breakdown of suggestions, acceptances, and number of active users by editor and language for each day. See the response schema tab for detailed metrics definitions.  The response contains metrics for up to 28 days prior. Usage metrics are processed once per day for the previous day, and the response will only include data up until yesterday. In order for an end user to be counted towards these metrics, they must have telemetry enabled in their IDE.  > [!NOTE] > This endpoint will only return results for a given day if the team had five or more members with active Copilot licenses, as evaluated at the end of that day.  Organization owners for the organization that contains this team, and owners and billing managers of the parent enterprise can view Copilot usage metrics for a team.  OAuth app tokens and personal access tokens (classic) need either the `manage_billing:copilot`, `read:org`, or `read:enterprise` scopes to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.copilot_usage_metrics import CopilotUsageMetrics
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
    api_instance = github_openapi.CopilotApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    since = 'since_example' # str | Show usage metrics since this date. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format (`YYYY-MM-DDTHH:MM:SSZ`). Maximum value is 28 days ago. (optional)
    until = 'until_example' # str | Show usage metrics until this date. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format (`YYYY-MM-DDTHH:MM:SSZ`) and should not preceed the `since` date if it is passed. (optional)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    per_page = 28 # int | The number of days of metrics to display per page (max 28). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 28)

    try:
        # Get a summary of Copilot usage for a team
        api_response = api_instance.copilot_usage_metrics_for_team(org, team_slug, since=since, until=until, page=page, per_page=per_page)
        print("The response of CopilotApi->copilot_usage_metrics_for_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CopilotApi->copilot_usage_metrics_for_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
 **since** | **str**| Show usage metrics since this date. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format (&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;). Maximum value is 28 days ago. | [optional] 
 **until** | **str**| Show usage metrics until this date. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format (&#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;) and should not preceed the &#x60;since&#x60; date if it is passed. | [optional] 
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **per_page** | **int**| The number of days of metrics to display per page (max 28). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 28]

### Return type

[**List[CopilotUsageMetrics]**](CopilotUsageMetrics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**500** | Internal Error |  -  |
**401** | Requires authentication |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

