# github_openapi.OrgsApi

All URIs are relative to *https://api.github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_insights_get_route_stats_by_actor**](OrgsApi.md#api_insights_get_route_stats_by_actor) | **GET** /orgs/{org}/insights/api/route-stats/{actor_type}/{actor_id} | Get route stats by actor
[**api_insights_get_subject_stats**](OrgsApi.md#api_insights_get_subject_stats) | **GET** /orgs/{org}/insights/api/subject-stats | Get subject stats
[**api_insights_get_summary_stats**](OrgsApi.md#api_insights_get_summary_stats) | **GET** /orgs/{org}/insights/api/summary-stats | Get summary stats
[**api_insights_get_summary_stats_by_actor**](OrgsApi.md#api_insights_get_summary_stats_by_actor) | **GET** /orgs/{org}/insights/api/summary-stats/{actor_type}/{actor_id} | Get summary stats by actor
[**api_insights_get_summary_stats_by_user**](OrgsApi.md#api_insights_get_summary_stats_by_user) | **GET** /orgs/{org}/insights/api/summary-stats/users/{user_id} | Get summary stats by user
[**api_insights_get_time_stats**](OrgsApi.md#api_insights_get_time_stats) | **GET** /orgs/{org}/insights/api/time-stats | Get time stats
[**api_insights_get_time_stats_by_actor**](OrgsApi.md#api_insights_get_time_stats_by_actor) | **GET** /orgs/{org}/insights/api/time-stats/{actor_type}/{actor_id} | Get time stats by actor
[**api_insights_get_time_stats_by_user**](OrgsApi.md#api_insights_get_time_stats_by_user) | **GET** /orgs/{org}/insights/api/time-stats/users/{user_id} | Get time stats by user
[**api_insights_get_user_stats**](OrgsApi.md#api_insights_get_user_stats) | **GET** /orgs/{org}/insights/api/user-stats/{user_id} | Get user stats
[**orgs_add_security_manager_team**](OrgsApi.md#orgs_add_security_manager_team) | **PUT** /orgs/{org}/security-managers/teams/{team_slug} | Add a security manager team
[**orgs_assign_team_to_org_role**](OrgsApi.md#orgs_assign_team_to_org_role) | **PUT** /orgs/{org}/organization-roles/teams/{team_slug}/{role_id} | Assign an organization role to a team
[**orgs_assign_user_to_org_role**](OrgsApi.md#orgs_assign_user_to_org_role) | **PUT** /orgs/{org}/organization-roles/users/{username}/{role_id} | Assign an organization role to a user
[**orgs_block_user**](OrgsApi.md#orgs_block_user) | **PUT** /orgs/{org}/blocks/{username} | Block a user from an organization
[**orgs_cancel_invitation**](OrgsApi.md#orgs_cancel_invitation) | **DELETE** /orgs/{org}/invitations/{invitation_id} | Cancel an organization invitation
[**orgs_check_blocked_user**](OrgsApi.md#orgs_check_blocked_user) | **GET** /orgs/{org}/blocks/{username} | Check if a user is blocked by an organization
[**orgs_check_membership_for_user**](OrgsApi.md#orgs_check_membership_for_user) | **GET** /orgs/{org}/members/{username} | Check organization membership for a user
[**orgs_check_public_membership_for_user**](OrgsApi.md#orgs_check_public_membership_for_user) | **GET** /orgs/{org}/public_members/{username} | Check public organization membership for a user
[**orgs_convert_member_to_outside_collaborator**](OrgsApi.md#orgs_convert_member_to_outside_collaborator) | **PUT** /orgs/{org}/outside_collaborators/{username} | Convert an organization member to outside collaborator
[**orgs_create_invitation**](OrgsApi.md#orgs_create_invitation) | **POST** /orgs/{org}/invitations | Create an organization invitation
[**orgs_create_or_update_custom_properties**](OrgsApi.md#orgs_create_or_update_custom_properties) | **PATCH** /orgs/{org}/properties/schema | Create or update custom properties for an organization
[**orgs_create_or_update_custom_properties_values_for_repos**](OrgsApi.md#orgs_create_or_update_custom_properties_values_for_repos) | **PATCH** /orgs/{org}/properties/values | Create or update custom property values for organization repositories
[**orgs_create_or_update_custom_property**](OrgsApi.md#orgs_create_or_update_custom_property) | **PUT** /orgs/{org}/properties/schema/{custom_property_name} | Create or update a custom property for an organization
[**orgs_create_webhook**](OrgsApi.md#orgs_create_webhook) | **POST** /orgs/{org}/hooks | Create an organization webhook
[**orgs_delete**](OrgsApi.md#orgs_delete) | **DELETE** /orgs/{org} | Delete an organization
[**orgs_delete_webhook**](OrgsApi.md#orgs_delete_webhook) | **DELETE** /orgs/{org}/hooks/{hook_id} | Delete an organization webhook
[**orgs_enable_or_disable_security_product_on_all_org_repos**](OrgsApi.md#orgs_enable_or_disable_security_product_on_all_org_repos) | **POST** /orgs/{org}/{security_product}/{enablement} | Enable or disable a security feature for an organization
[**orgs_get**](OrgsApi.md#orgs_get) | **GET** /orgs/{org} | Get an organization
[**orgs_get_all_custom_properties**](OrgsApi.md#orgs_get_all_custom_properties) | **GET** /orgs/{org}/properties/schema | Get all custom properties for an organization
[**orgs_get_custom_property**](OrgsApi.md#orgs_get_custom_property) | **GET** /orgs/{org}/properties/schema/{custom_property_name} | Get a custom property for an organization
[**orgs_get_membership_for_authenticated_user**](OrgsApi.md#orgs_get_membership_for_authenticated_user) | **GET** /user/memberships/orgs/{org} | Get an organization membership for the authenticated user
[**orgs_get_membership_for_user**](OrgsApi.md#orgs_get_membership_for_user) | **GET** /orgs/{org}/memberships/{username} | Get organization membership for a user
[**orgs_get_org_role**](OrgsApi.md#orgs_get_org_role) | **GET** /orgs/{org}/organization-roles/{role_id} | Get an organization role
[**orgs_get_webhook**](OrgsApi.md#orgs_get_webhook) | **GET** /orgs/{org}/hooks/{hook_id} | Get an organization webhook
[**orgs_get_webhook_config_for_org**](OrgsApi.md#orgs_get_webhook_config_for_org) | **GET** /orgs/{org}/hooks/{hook_id}/config | Get a webhook configuration for an organization
[**orgs_get_webhook_delivery**](OrgsApi.md#orgs_get_webhook_delivery) | **GET** /orgs/{org}/hooks/{hook_id}/deliveries/{delivery_id} | Get a webhook delivery for an organization webhook
[**orgs_list**](OrgsApi.md#orgs_list) | **GET** /organizations | List organizations
[**orgs_list_app_installations**](OrgsApi.md#orgs_list_app_installations) | **GET** /orgs/{org}/installations | List app installations for an organization
[**orgs_list_attestations**](OrgsApi.md#orgs_list_attestations) | **GET** /orgs/{org}/attestations/{subject_digest} | List attestations
[**orgs_list_blocked_users**](OrgsApi.md#orgs_list_blocked_users) | **GET** /orgs/{org}/blocks | List users blocked by an organization
[**orgs_list_custom_properties_values_for_repos**](OrgsApi.md#orgs_list_custom_properties_values_for_repos) | **GET** /orgs/{org}/properties/values | List custom property values for organization repositories
[**orgs_list_failed_invitations**](OrgsApi.md#orgs_list_failed_invitations) | **GET** /orgs/{org}/failed_invitations | List failed organization invitations
[**orgs_list_for_authenticated_user**](OrgsApi.md#orgs_list_for_authenticated_user) | **GET** /user/orgs | List organizations for the authenticated user
[**orgs_list_for_user**](OrgsApi.md#orgs_list_for_user) | **GET** /users/{username}/orgs | List organizations for a user
[**orgs_list_invitation_teams**](OrgsApi.md#orgs_list_invitation_teams) | **GET** /orgs/{org}/invitations/{invitation_id}/teams | List organization invitation teams
[**orgs_list_members**](OrgsApi.md#orgs_list_members) | **GET** /orgs/{org}/members | List organization members
[**orgs_list_memberships_for_authenticated_user**](OrgsApi.md#orgs_list_memberships_for_authenticated_user) | **GET** /user/memberships/orgs | List organization memberships for the authenticated user
[**orgs_list_org_role_teams**](OrgsApi.md#orgs_list_org_role_teams) | **GET** /orgs/{org}/organization-roles/{role_id}/teams | List teams that are assigned to an organization role
[**orgs_list_org_role_users**](OrgsApi.md#orgs_list_org_role_users) | **GET** /orgs/{org}/organization-roles/{role_id}/users | List users that are assigned to an organization role
[**orgs_list_org_roles**](OrgsApi.md#orgs_list_org_roles) | **GET** /orgs/{org}/organization-roles | Get all organization roles for an organization
[**orgs_list_outside_collaborators**](OrgsApi.md#orgs_list_outside_collaborators) | **GET** /orgs/{org}/outside_collaborators | List outside collaborators for an organization
[**orgs_list_pat_grant_repositories**](OrgsApi.md#orgs_list_pat_grant_repositories) | **GET** /orgs/{org}/personal-access-tokens/{pat_id}/repositories | List repositories a fine-grained personal access token has access to
[**orgs_list_pat_grant_request_repositories**](OrgsApi.md#orgs_list_pat_grant_request_repositories) | **GET** /orgs/{org}/personal-access-token-requests/{pat_request_id}/repositories | List repositories requested to be accessed by a fine-grained personal access token
[**orgs_list_pat_grant_requests**](OrgsApi.md#orgs_list_pat_grant_requests) | **GET** /orgs/{org}/personal-access-token-requests | List requests to access organization resources with fine-grained personal access tokens
[**orgs_list_pat_grants**](OrgsApi.md#orgs_list_pat_grants) | **GET** /orgs/{org}/personal-access-tokens | List fine-grained personal access tokens with access to organization resources
[**orgs_list_pending_invitations**](OrgsApi.md#orgs_list_pending_invitations) | **GET** /orgs/{org}/invitations | List pending organization invitations
[**orgs_list_public_members**](OrgsApi.md#orgs_list_public_members) | **GET** /orgs/{org}/public_members | List public organization members
[**orgs_list_security_manager_teams**](OrgsApi.md#orgs_list_security_manager_teams) | **GET** /orgs/{org}/security-managers | List security manager teams
[**orgs_list_webhook_deliveries**](OrgsApi.md#orgs_list_webhook_deliveries) | **GET** /orgs/{org}/hooks/{hook_id}/deliveries | List deliveries for an organization webhook
[**orgs_list_webhooks**](OrgsApi.md#orgs_list_webhooks) | **GET** /orgs/{org}/hooks | List organization webhooks
[**orgs_ping_webhook**](OrgsApi.md#orgs_ping_webhook) | **POST** /orgs/{org}/hooks/{hook_id}/pings | Ping an organization webhook
[**orgs_redeliver_webhook_delivery**](OrgsApi.md#orgs_redeliver_webhook_delivery) | **POST** /orgs/{org}/hooks/{hook_id}/deliveries/{delivery_id}/attempts | Redeliver a delivery for an organization webhook
[**orgs_remove_custom_property**](OrgsApi.md#orgs_remove_custom_property) | **DELETE** /orgs/{org}/properties/schema/{custom_property_name} | Remove a custom property for an organization
[**orgs_remove_member**](OrgsApi.md#orgs_remove_member) | **DELETE** /orgs/{org}/members/{username} | Remove an organization member
[**orgs_remove_membership_for_user**](OrgsApi.md#orgs_remove_membership_for_user) | **DELETE** /orgs/{org}/memberships/{username} | Remove organization membership for a user
[**orgs_remove_outside_collaborator**](OrgsApi.md#orgs_remove_outside_collaborator) | **DELETE** /orgs/{org}/outside_collaborators/{username} | Remove outside collaborator from an organization
[**orgs_remove_public_membership_for_authenticated_user**](OrgsApi.md#orgs_remove_public_membership_for_authenticated_user) | **DELETE** /orgs/{org}/public_members/{username} | Remove public organization membership for the authenticated user
[**orgs_remove_security_manager_team**](OrgsApi.md#orgs_remove_security_manager_team) | **DELETE** /orgs/{org}/security-managers/teams/{team_slug} | Remove a security manager team
[**orgs_review_pat_grant_request**](OrgsApi.md#orgs_review_pat_grant_request) | **POST** /orgs/{org}/personal-access-token-requests/{pat_request_id} | Review a request to access organization resources with a fine-grained personal access token
[**orgs_review_pat_grant_requests_in_bulk**](OrgsApi.md#orgs_review_pat_grant_requests_in_bulk) | **POST** /orgs/{org}/personal-access-token-requests | Review requests to access organization resources with fine-grained personal access tokens
[**orgs_revoke_all_org_roles_team**](OrgsApi.md#orgs_revoke_all_org_roles_team) | **DELETE** /orgs/{org}/organization-roles/teams/{team_slug} | Remove all organization roles for a team
[**orgs_revoke_all_org_roles_user**](OrgsApi.md#orgs_revoke_all_org_roles_user) | **DELETE** /orgs/{org}/organization-roles/users/{username} | Remove all organization roles for a user
[**orgs_revoke_org_role_team**](OrgsApi.md#orgs_revoke_org_role_team) | **DELETE** /orgs/{org}/organization-roles/teams/{team_slug}/{role_id} | Remove an organization role from a team
[**orgs_revoke_org_role_user**](OrgsApi.md#orgs_revoke_org_role_user) | **DELETE** /orgs/{org}/organization-roles/users/{username}/{role_id} | Remove an organization role from a user
[**orgs_set_membership_for_user**](OrgsApi.md#orgs_set_membership_for_user) | **PUT** /orgs/{org}/memberships/{username} | Set organization membership for a user
[**orgs_set_public_membership_for_authenticated_user**](OrgsApi.md#orgs_set_public_membership_for_authenticated_user) | **PUT** /orgs/{org}/public_members/{username} | Set public organization membership for the authenticated user
[**orgs_unblock_user**](OrgsApi.md#orgs_unblock_user) | **DELETE** /orgs/{org}/blocks/{username} | Unblock a user from an organization
[**orgs_update**](OrgsApi.md#orgs_update) | **PATCH** /orgs/{org} | Update an organization
[**orgs_update_membership_for_authenticated_user**](OrgsApi.md#orgs_update_membership_for_authenticated_user) | **PATCH** /user/memberships/orgs/{org} | Update an organization membership for the authenticated user
[**orgs_update_pat_access**](OrgsApi.md#orgs_update_pat_access) | **POST** /orgs/{org}/personal-access-tokens/{pat_id} | Update the access a fine-grained personal access token has to organization resources
[**orgs_update_pat_accesses**](OrgsApi.md#orgs_update_pat_accesses) | **POST** /orgs/{org}/personal-access-tokens | Update the access to organization resources via fine-grained personal access tokens
[**orgs_update_webhook**](OrgsApi.md#orgs_update_webhook) | **PATCH** /orgs/{org}/hooks/{hook_id} | Update an organization webhook
[**orgs_update_webhook_config_for_org**](OrgsApi.md#orgs_update_webhook_config_for_org) | **PATCH** /orgs/{org}/hooks/{hook_id}/config | Update a webhook configuration for an organization


# **api_insights_get_route_stats_by_actor**
> List[ApiInsightsRouteStatsInner] api_insights_get_route_stats_by_actor(org, actor_type, actor_id, min_timestamp, max_timestamp=max_timestamp, page=page, per_page=per_page, direction=direction, sort=sort, api_route_substring=api_route_substring)

Get route stats by actor

Get API request count statistics for an actor broken down by route within a specified time frame.

### Example


```python
import github_openapi
from github_openapi.models.api_insights_route_stats_inner import ApiInsightsRouteStatsInner
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    actor_type = 'actor_type_example' # str | The type of the actor
    actor_id = 56 # int | The ID of the actor
    min_timestamp = 'min_timestamp_example' # str | The minimum timestamp to query for stats. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
    max_timestamp = 'max_timestamp_example' # str | The maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. (optional)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    direction = desc # str | The direction to sort the results by. (optional) (default to desc)
    sort = ['sort_example'] # List[str] | The property to sort the results by. (optional)
    api_route_substring = 'api_route_substring_example' # str | Providing a substring will filter results where the API route contains the substring. This is a case-insensitive search. (optional)

    try:
        # Get route stats by actor
        api_response = api_instance.api_insights_get_route_stats_by_actor(org, actor_type, actor_id, min_timestamp, max_timestamp=max_timestamp, page=page, per_page=per_page, direction=direction, sort=sort, api_route_substring=api_route_substring)
        print("The response of OrgsApi->api_insights_get_route_stats_by_actor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->api_insights_get_route_stats_by_actor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **actor_type** | **str**| The type of the actor | 
 **actor_id** | **int**| The ID of the actor | 
 **min_timestamp** | **str**| The minimum timestamp to query for stats. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | 
 **max_timestamp** | **str**| The maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **direction** | **str**| The direction to sort the results by. | [optional] [default to desc]
 **sort** | [**List[str]**](str.md)| The property to sort the results by. | [optional] 
 **api_route_substring** | **str**| Providing a substring will filter results where the API route contains the substring. This is a case-insensitive search. | [optional] 

### Return type

[**List[ApiInsightsRouteStatsInner]**](ApiInsightsRouteStatsInner.md)

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

# **api_insights_get_subject_stats**
> List[ApiInsightsSubjectStatsInner] api_insights_get_subject_stats(org, min_timestamp, max_timestamp=max_timestamp, page=page, per_page=per_page, direction=direction, sort=sort, subject_name_substring=subject_name_substring)

Get subject stats

Get API request statistics for all subjects within an organization within a specified time frame. Subjects can be users or GitHub Apps.

### Example


```python
import github_openapi
from github_openapi.models.api_insights_subject_stats_inner import ApiInsightsSubjectStatsInner
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    min_timestamp = 'min_timestamp_example' # str | The minimum timestamp to query for stats. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
    max_timestamp = 'max_timestamp_example' # str | The maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. (optional)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    direction = desc # str | The direction to sort the results by. (optional) (default to desc)
    sort = ['sort_example'] # List[str] | The property to sort the results by. (optional)
    subject_name_substring = 'subject_name_substring_example' # str | Providing a substring will filter results where the subject name contains the substring. This is a case-insensitive search. (optional)

    try:
        # Get subject stats
        api_response = api_instance.api_insights_get_subject_stats(org, min_timestamp, max_timestamp=max_timestamp, page=page, per_page=per_page, direction=direction, sort=sort, subject_name_substring=subject_name_substring)
        print("The response of OrgsApi->api_insights_get_subject_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->api_insights_get_subject_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **min_timestamp** | **str**| The minimum timestamp to query for stats. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | 
 **max_timestamp** | **str**| The maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **direction** | **str**| The direction to sort the results by. | [optional] [default to desc]
 **sort** | [**List[str]**](str.md)| The property to sort the results by. | [optional] 
 **subject_name_substring** | **str**| Providing a substring will filter results where the subject name contains the substring. This is a case-insensitive search. | [optional] 

### Return type

[**List[ApiInsightsSubjectStatsInner]**](ApiInsightsSubjectStatsInner.md)

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

# **api_insights_get_summary_stats**
> ApiInsightsSummaryStats api_insights_get_summary_stats(org, min_timestamp, max_timestamp=max_timestamp)

Get summary stats

Get overall statistics of API requests made within an organization by all users and apps within a specified time frame.

### Example


```python
import github_openapi
from github_openapi.models.api_insights_summary_stats import ApiInsightsSummaryStats
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    min_timestamp = 'min_timestamp_example' # str | The minimum timestamp to query for stats. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
    max_timestamp = 'max_timestamp_example' # str | The maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. (optional)

    try:
        # Get summary stats
        api_response = api_instance.api_insights_get_summary_stats(org, min_timestamp, max_timestamp=max_timestamp)
        print("The response of OrgsApi->api_insights_get_summary_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->api_insights_get_summary_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **min_timestamp** | **str**| The minimum timestamp to query for stats. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | 
 **max_timestamp** | **str**| The maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 

### Return type

[**ApiInsightsSummaryStats**](ApiInsightsSummaryStats.md)

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

# **api_insights_get_summary_stats_by_actor**
> ApiInsightsSummaryStats api_insights_get_summary_stats_by_actor(org, min_timestamp, actor_type, actor_id, max_timestamp=max_timestamp)

Get summary stats by actor

Get overall statistics of API requests within the organization made by a specific actor. Actors can be GitHub App installations, OAuth apps or other tokens on behalf of a user.

### Example


```python
import github_openapi
from github_openapi.models.api_insights_summary_stats import ApiInsightsSummaryStats
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    min_timestamp = 'min_timestamp_example' # str | The minimum timestamp to query for stats. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
    actor_type = 'actor_type_example' # str | The type of the actor
    actor_id = 56 # int | The ID of the actor
    max_timestamp = 'max_timestamp_example' # str | The maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. (optional)

    try:
        # Get summary stats by actor
        api_response = api_instance.api_insights_get_summary_stats_by_actor(org, min_timestamp, actor_type, actor_id, max_timestamp=max_timestamp)
        print("The response of OrgsApi->api_insights_get_summary_stats_by_actor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->api_insights_get_summary_stats_by_actor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **min_timestamp** | **str**| The minimum timestamp to query for stats. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | 
 **actor_type** | **str**| The type of the actor | 
 **actor_id** | **int**| The ID of the actor | 
 **max_timestamp** | **str**| The maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 

### Return type

[**ApiInsightsSummaryStats**](ApiInsightsSummaryStats.md)

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

# **api_insights_get_summary_stats_by_user**
> ApiInsightsSummaryStats api_insights_get_summary_stats_by_user(org, user_id, min_timestamp, max_timestamp=max_timestamp)

Get summary stats by user

Get overall statistics of API requests within the organization for a user.

### Example


```python
import github_openapi
from github_openapi.models.api_insights_summary_stats import ApiInsightsSummaryStats
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    user_id = 'user_id_example' # str | The ID of the user to query for stats
    min_timestamp = 'min_timestamp_example' # str | The minimum timestamp to query for stats. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
    max_timestamp = 'max_timestamp_example' # str | The maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. (optional)

    try:
        # Get summary stats by user
        api_response = api_instance.api_insights_get_summary_stats_by_user(org, user_id, min_timestamp, max_timestamp=max_timestamp)
        print("The response of OrgsApi->api_insights_get_summary_stats_by_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->api_insights_get_summary_stats_by_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **user_id** | **str**| The ID of the user to query for stats | 
 **min_timestamp** | **str**| The minimum timestamp to query for stats. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | 
 **max_timestamp** | **str**| The maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 

### Return type

[**ApiInsightsSummaryStats**](ApiInsightsSummaryStats.md)

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

# **api_insights_get_time_stats**
> List[ApiInsightsTimeStatsInner] api_insights_get_time_stats(org, min_timestamp, timestamp_increment, max_timestamp=max_timestamp)

Get time stats

Get the number of API requests and rate-limited requests made within an organization over a specified time period.

### Example


```python
import github_openapi
from github_openapi.models.api_insights_time_stats_inner import ApiInsightsTimeStatsInner
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    min_timestamp = 'min_timestamp_example' # str | The minimum timestamp to query for stats. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
    timestamp_increment = 'timestamp_increment_example' # str | The increment of time used to breakdown the query results (5m, 10m, 1h, etc.)
    max_timestamp = 'max_timestamp_example' # str | The maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. (optional)

    try:
        # Get time stats
        api_response = api_instance.api_insights_get_time_stats(org, min_timestamp, timestamp_increment, max_timestamp=max_timestamp)
        print("The response of OrgsApi->api_insights_get_time_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->api_insights_get_time_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **min_timestamp** | **str**| The minimum timestamp to query for stats. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | 
 **timestamp_increment** | **str**| The increment of time used to breakdown the query results (5m, 10m, 1h, etc.) | 
 **max_timestamp** | **str**| The maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 

### Return type

[**List[ApiInsightsTimeStatsInner]**](ApiInsightsTimeStatsInner.md)

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

# **api_insights_get_time_stats_by_actor**
> List[ApiInsightsTimeStatsInner] api_insights_get_time_stats_by_actor(org, actor_type, actor_id, min_timestamp, timestamp_increment, max_timestamp=max_timestamp)

Get time stats by actor

Get the number of API requests and rate-limited requests made within an organization by a specific actor within a specified time period.

### Example


```python
import github_openapi
from github_openapi.models.api_insights_time_stats_inner import ApiInsightsTimeStatsInner
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    actor_type = 'actor_type_example' # str | The type of the actor
    actor_id = 56 # int | The ID of the actor
    min_timestamp = 'min_timestamp_example' # str | The minimum timestamp to query for stats. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
    timestamp_increment = 'timestamp_increment_example' # str | The increment of time used to breakdown the query results (5m, 10m, 1h, etc.)
    max_timestamp = 'max_timestamp_example' # str | The maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. (optional)

    try:
        # Get time stats by actor
        api_response = api_instance.api_insights_get_time_stats_by_actor(org, actor_type, actor_id, min_timestamp, timestamp_increment, max_timestamp=max_timestamp)
        print("The response of OrgsApi->api_insights_get_time_stats_by_actor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->api_insights_get_time_stats_by_actor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **actor_type** | **str**| The type of the actor | 
 **actor_id** | **int**| The ID of the actor | 
 **min_timestamp** | **str**| The minimum timestamp to query for stats. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | 
 **timestamp_increment** | **str**| The increment of time used to breakdown the query results (5m, 10m, 1h, etc.) | 
 **max_timestamp** | **str**| The maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 

### Return type

[**List[ApiInsightsTimeStatsInner]**](ApiInsightsTimeStatsInner.md)

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

# **api_insights_get_time_stats_by_user**
> List[ApiInsightsTimeStatsInner] api_insights_get_time_stats_by_user(org, user_id, min_timestamp, timestamp_increment, max_timestamp=max_timestamp)

Get time stats by user

Get the number of API requests and rate-limited requests made within an organization by a specific user over a specified time period.

### Example


```python
import github_openapi
from github_openapi.models.api_insights_time_stats_inner import ApiInsightsTimeStatsInner
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    user_id = 'user_id_example' # str | The ID of the user to query for stats
    min_timestamp = 'min_timestamp_example' # str | The minimum timestamp to query for stats. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
    timestamp_increment = 'timestamp_increment_example' # str | The increment of time used to breakdown the query results (5m, 10m, 1h, etc.)
    max_timestamp = 'max_timestamp_example' # str | The maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. (optional)

    try:
        # Get time stats by user
        api_response = api_instance.api_insights_get_time_stats_by_user(org, user_id, min_timestamp, timestamp_increment, max_timestamp=max_timestamp)
        print("The response of OrgsApi->api_insights_get_time_stats_by_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->api_insights_get_time_stats_by_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **user_id** | **str**| The ID of the user to query for stats | 
 **min_timestamp** | **str**| The minimum timestamp to query for stats. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | 
 **timestamp_increment** | **str**| The increment of time used to breakdown the query results (5m, 10m, 1h, etc.) | 
 **max_timestamp** | **str**| The maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 

### Return type

[**List[ApiInsightsTimeStatsInner]**](ApiInsightsTimeStatsInner.md)

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

# **api_insights_get_user_stats**
> List[ApiInsightsUserStatsInner] api_insights_get_user_stats(org, user_id, min_timestamp, max_timestamp=max_timestamp, page=page, per_page=per_page, direction=direction, sort=sort, actor_name_substring=actor_name_substring)

Get user stats

Get API usage statistics within an organization for a user broken down by the type of access.

### Example


```python
import github_openapi
from github_openapi.models.api_insights_user_stats_inner import ApiInsightsUserStatsInner
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    user_id = 'user_id_example' # str | The ID of the user to query for stats
    min_timestamp = 'min_timestamp_example' # str | The minimum timestamp to query for stats. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
    max_timestamp = 'max_timestamp_example' # str | The maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. (optional)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    direction = desc # str | The direction to sort the results by. (optional) (default to desc)
    sort = ['sort_example'] # List[str] | The property to sort the results by. (optional)
    actor_name_substring = 'actor_name_substring_example' # str | Providing a substring will filter results where the actor name contains the substring. This is a case-insensitive search. (optional)

    try:
        # Get user stats
        api_response = api_instance.api_insights_get_user_stats(org, user_id, min_timestamp, max_timestamp=max_timestamp, page=page, per_page=per_page, direction=direction, sort=sort, actor_name_substring=actor_name_substring)
        print("The response of OrgsApi->api_insights_get_user_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->api_insights_get_user_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **user_id** | **str**| The ID of the user to query for stats | 
 **min_timestamp** | **str**| The minimum timestamp to query for stats. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | 
 **max_timestamp** | **str**| The maximum timestamp to query for stats. Defaults to the time 30 days ago. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **direction** | **str**| The direction to sort the results by. | [optional] [default to desc]
 **sort** | [**List[str]**](str.md)| The property to sort the results by. | [optional] 
 **actor_name_substring** | **str**| Providing a substring will filter results where the actor name contains the substring. This is a case-insensitive search. | [optional] 

### Return type

[**List[ApiInsightsUserStatsInner]**](ApiInsightsUserStatsInner.md)

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

# **orgs_add_security_manager_team**
> orgs_add_security_manager_team(org, team_slug)

Add a security manager team

> [!WARNING] > **Closing down notice:** This operation is closing down and will be removed starting January 1, 2026. Please use the \"[Organization Roles](https://docs.github.com/rest/orgs/organization-roles)\" endpoints instead.

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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.

    try:
        # Add a security manager team
        api_instance.orgs_add_security_manager_team(org, team_slug)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_add_security_manager_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 

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

# **orgs_assign_team_to_org_role**
> orgs_assign_team_to_org_role(org, team_slug, role_id)

Assign an organization role to a team

Assigns an organization role to a team in an organization. For more information on organization roles, see \"[Using organization roles](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/using-organization-roles).\"  The authenticated user must be an administrator for the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    role_id = 56 # int | The unique identifier of the role.

    try:
        # Assign an organization role to a team
        api_instance.orgs_assign_team_to_org_role(org, team_slug, role_id)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_assign_team_to_org_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
 **role_id** | **int**| The unique identifier of the role. | 

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
**404** | Response if the organization, team or role does not exist. |  -  |
**422** | Response if the organization roles feature is not enabled for the organization, or validation failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_assign_user_to_org_role**
> orgs_assign_user_to_org_role(org, username, role_id)

Assign an organization role to a user

Assigns an organization role to a member of an organization. For more information on organization roles, see \"[Using organization roles](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/using-organization-roles).\"  The authenticated user must be an administrator for the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    username = 'username_example' # str | The handle for the GitHub user account.
    role_id = 56 # int | The unique identifier of the role.

    try:
        # Assign an organization role to a user
        api_instance.orgs_assign_user_to_org_role(org, username, role_id)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_assign_user_to_org_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **username** | **str**| The handle for the GitHub user account. | 
 **role_id** | **int**| The unique identifier of the role. | 

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
**404** | Response if the organization, user or role does not exist. |  -  |
**422** | Response if the organization roles feature is not enabled enabled for the organization, the validation failed, or the user is not an organization member. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_block_user**
> orgs_block_user(org, username)

Block a user from an organization

Blocks the given user on behalf of the specified organization and returns a 204. If the organization cannot block the given user a 422 is returned.

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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Block a user from an organization
        api_instance.orgs_block_user(org, username)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_block_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **username** | **str**| The handle for the GitHub user account. | 

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
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_cancel_invitation**
> orgs_cancel_invitation(org, invitation_id)

Cancel an organization invitation

Cancel an organization invitation. In order to cancel an organization invitation, the authenticated user must be an organization owner.  This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications).

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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    invitation_id = 56 # int | The unique identifier of the invitation.

    try:
        # Cancel an organization invitation
        api_instance.orgs_cancel_invitation(org, invitation_id)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_cancel_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **invitation_id** | **int**| The unique identifier of the invitation. | 

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
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_check_blocked_user**
> orgs_check_blocked_user(org, username)

Check if a user is blocked by an organization

Returns a 204 if the given user is blocked by the given organization. Returns a 404 if the organization is not blocking the user, or if the user account has been identified as spam by GitHub.

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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Check if a user is blocked by an organization
        api_instance.orgs_check_blocked_user(org, username)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_check_blocked_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **username** | **str**| The handle for the GitHub user account. | 

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
**204** | If the user is blocked |  -  |
**404** | If the user is not blocked |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_check_membership_for_user**
> orgs_check_membership_for_user(org, username)

Check organization membership for a user

Check if a user is, publicly or privately, a member of the organization.

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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Check organization membership for a user
        api_instance.orgs_check_membership_for_user(org, username)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_check_membership_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **username** | **str**| The handle for the GitHub user account. | 

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
**204** | Response if requester is an organization member and user is a member |  -  |
**302** | Response if requester is not an organization member |  * Location -  <br>  |
**404** | Not Found if requester is an organization member and user is not a member |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_check_public_membership_for_user**
> orgs_check_public_membership_for_user(org, username)

Check public organization membership for a user

Check if the provided user is a public member of the organization.

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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Check public organization membership for a user
        api_instance.orgs_check_public_membership_for_user(org, username)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_check_public_membership_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **username** | **str**| The handle for the GitHub user account. | 

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
**204** | Response if user is a public member |  -  |
**404** | Not Found if user is not a public member |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_convert_member_to_outside_collaborator**
> object orgs_convert_member_to_outside_collaborator(org, username, orgs_convert_member_to_outside_collaborator_request=orgs_convert_member_to_outside_collaborator_request)

Convert an organization member to outside collaborator

When an organization member is converted to an outside collaborator, they'll only have access to the repositories that their current team membership allows. The user will no longer be a member of the organization. For more information, see \"[Converting an organization member to an outside collaborator](https://docs.github.com/articles/converting-an-organization-member-to-an-outside-collaborator/)\". Converting an organization member to an outside collaborator may be restricted by enterprise administrators. For more information, see \"[Enforcing repository management policies in your enterprise](https://docs.github.com/admin/policies/enforcing-policies-for-your-enterprise/enforcing-repository-management-policies-in-your-enterprise#enforcing-a-policy-for-inviting-outside-collaborators-to-repositories).\"

### Example


```python
import github_openapi
from github_openapi.models.orgs_convert_member_to_outside_collaborator_request import OrgsConvertMemberToOutsideCollaboratorRequest
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    username = 'username_example' # str | The handle for the GitHub user account.
    orgs_convert_member_to_outside_collaborator_request = {"async":true} # OrgsConvertMemberToOutsideCollaboratorRequest |  (optional)

    try:
        # Convert an organization member to outside collaborator
        api_response = api_instance.orgs_convert_member_to_outside_collaborator(org, username, orgs_convert_member_to_outside_collaborator_request=orgs_convert_member_to_outside_collaborator_request)
        print("The response of OrgsApi->orgs_convert_member_to_outside_collaborator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_convert_member_to_outside_collaborator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **username** | **str**| The handle for the GitHub user account. | 
 **orgs_convert_member_to_outside_collaborator_request** | [**OrgsConvertMemberToOutsideCollaboratorRequest**](OrgsConvertMemberToOutsideCollaboratorRequest.md)|  | [optional] 

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
**202** | User is getting converted asynchronously |  -  |
**204** | User was converted |  -  |
**403** | Forbidden if user is the last owner of the organization, not a member of the organization, or if the enterprise enforces a policy for inviting outside collaborators. For more information, see \&quot;[Enforcing repository management policies in your enterprise](https://docs.github.com/admin/policies/enforcing-policies-for-your-enterprise/enforcing-repository-management-policies-in-your-enterprise#enforcing-a-policy-for-inviting-outside-collaborators-to-repositories).\&quot; |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_create_invitation**
> OrganizationInvitation orgs_create_invitation(org, orgs_create_invitation_request=orgs_create_invitation_request)

Create an organization invitation

Invite people to an organization by using their GitHub user ID or their email address. In order to create invitations in an organization, the authenticated user must be an organization owner.  This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. For more information, see \"[Rate limits for the API](https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits)\" and \"[Best practices for using the REST API](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api).\"

### Example


```python
import github_openapi
from github_openapi.models.organization_invitation import OrganizationInvitation
from github_openapi.models.orgs_create_invitation_request import OrgsCreateInvitationRequest
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    orgs_create_invitation_request = {"email":"octocat@github.com","role":"direct_member","team_ids":[12,26]} # OrgsCreateInvitationRequest |  (optional)

    try:
        # Create an organization invitation
        api_response = api_instance.orgs_create_invitation(org, orgs_create_invitation_request=orgs_create_invitation_request)
        print("The response of OrgsApi->orgs_create_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_create_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **orgs_create_invitation_request** | [**OrgsCreateInvitationRequest**](OrgsCreateInvitationRequest.md)|  | [optional] 

### Return type

[**OrganizationInvitation**](OrganizationInvitation.md)

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
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_create_or_update_custom_properties**
> List[CustomProperty] orgs_create_or_update_custom_properties(org, orgs_create_or_update_custom_properties_request)

Create or update custom properties for an organization

Creates new or updates existing custom properties defined for an organization in a batch.  To use this endpoint, the authenticated user must be one of:   - An administrator for the organization.   - A user, or a user on a team, with the fine-grained permission of `custom_properties_org_definitions_manager` in the organization.

### Example


```python
import github_openapi
from github_openapi.models.custom_property import CustomProperty
from github_openapi.models.orgs_create_or_update_custom_properties_request import OrgsCreateOrUpdateCustomPropertiesRequest
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    orgs_create_or_update_custom_properties_request = {"properties":[{"property_name":"environment","value_type":"single_select","required":true,"default_value":"production","description":"Prod or dev environment","allowed_values":["production","development"],"values_editable_by":"org_actors"},{"property_name":"service","value_type":"string"},{"property_name":"team","value_type":"string","description":"Team owning the repository"}]} # OrgsCreateOrUpdateCustomPropertiesRequest | 

    try:
        # Create or update custom properties for an organization
        api_response = api_instance.orgs_create_or_update_custom_properties(org, orgs_create_or_update_custom_properties_request)
        print("The response of OrgsApi->orgs_create_or_update_custom_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_create_or_update_custom_properties: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **orgs_create_or_update_custom_properties_request** | [**OrgsCreateOrUpdateCustomPropertiesRequest**](OrgsCreateOrUpdateCustomPropertiesRequest.md)|  | 

### Return type

[**List[CustomProperty]**](CustomProperty.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_create_or_update_custom_properties_values_for_repos**
> orgs_create_or_update_custom_properties_values_for_repos(org, orgs_create_or_update_custom_properties_values_for_repos_request)

Create or update custom property values for organization repositories

Create new or update existing custom property values for repositories in a batch that belong to an organization. Each target repository will have its custom property values updated to match the values provided in the request.  A maximum of 30 repositories can be updated in a single request.  Using a value of `null` for a custom property will remove or 'unset' the property value from the repository.  To use this endpoint, the authenticated user must be one of:   - An administrator for the organization.   - A user, or a user on a team, with the fine-grained permission of `custom_properties_org_values_editor` in the organization.

### Example


```python
import github_openapi
from github_openapi.models.orgs_create_or_update_custom_properties_values_for_repos_request import OrgsCreateOrUpdateCustomPropertiesValuesForReposRequest
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    orgs_create_or_update_custom_properties_values_for_repos_request = github_openapi.OrgsCreateOrUpdateCustomPropertiesValuesForReposRequest() # OrgsCreateOrUpdateCustomPropertiesValuesForReposRequest | 

    try:
        # Create or update custom property values for organization repositories
        api_instance.orgs_create_or_update_custom_properties_values_for_repos(org, orgs_create_or_update_custom_properties_values_for_repos_request)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_create_or_update_custom_properties_values_for_repos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **orgs_create_or_update_custom_properties_values_for_repos_request** | [**OrgsCreateOrUpdateCustomPropertiesValuesForReposRequest**](OrgsCreateOrUpdateCustomPropertiesValuesForReposRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content when custom property values are successfully created or updated |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_create_or_update_custom_property**
> CustomProperty orgs_create_or_update_custom_property(org, custom_property_name, custom_property_set_payload)

Create or update a custom property for an organization

Creates a new or updates an existing custom property that is defined for an organization.  To use this endpoint, the authenticated user must be one of: - An administrator for the organization. - A user, or a user on a team, with the fine-grained permission of `custom_properties_org_definitions_manager` in the organization.

### Example


```python
import github_openapi
from github_openapi.models.custom_property import CustomProperty
from github_openapi.models.custom_property_set_payload import CustomPropertySetPayload
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    custom_property_name = 'custom_property_name_example' # str | The custom property name
    custom_property_set_payload = {"value_type":"single_select","required":true,"default_value":"production","description":"Prod or dev environment","allowed_values":["production","development"]} # CustomPropertySetPayload | 

    try:
        # Create or update a custom property for an organization
        api_response = api_instance.orgs_create_or_update_custom_property(org, custom_property_name, custom_property_set_payload)
        print("The response of OrgsApi->orgs_create_or_update_custom_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_create_or_update_custom_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **custom_property_name** | **str**| The custom property name | 
 **custom_property_set_payload** | [**CustomPropertySetPayload**](CustomPropertySetPayload.md)|  | 

### Return type

[**CustomProperty**](CustomProperty.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_create_webhook**
> OrgHook orgs_create_webhook(org, orgs_create_webhook_request)

Create an organization webhook

Create a hook that posts payloads in JSON format.  You must be an organization owner to use this endpoint.  OAuth app tokens and personal access tokens (classic) need `admin:org_hook` scope. OAuth apps cannot list, view, or edit webhooks that they did not create and users cannot list, view, or edit webhooks that were created by OAuth apps.

### Example


```python
import github_openapi
from github_openapi.models.org_hook import OrgHook
from github_openapi.models.orgs_create_webhook_request import OrgsCreateWebhookRequest
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    orgs_create_webhook_request = {"name":"web","active":true,"events":["push","pull_request"],"config":{"url":"http://example.com/webhook","content_type":"json"}} # OrgsCreateWebhookRequest | 

    try:
        # Create an organization webhook
        api_response = api_instance.orgs_create_webhook(org, orgs_create_webhook_request)
        print("The response of OrgsApi->orgs_create_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_create_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **orgs_create_webhook_request** | [**OrgsCreateWebhookRequest**](OrgsCreateWebhookRequest.md)|  | 

### Return type

[**OrgHook**](OrgHook.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_delete**
> object orgs_delete(org)

Delete an organization

Deletes an organization and all its repositories.  The organization login will be unavailable for 90 days after deletion.  Please review the Terms of Service regarding account deletion before using this endpoint:  https://docs.github.com/site-policy/github-terms/github-terms-of-service

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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.

    try:
        # Delete an organization
        api_response = api_instance.orgs_delete(org)
        print("The response of OrgsApi->orgs_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_delete_webhook**
> orgs_delete_webhook(org, hook_id)

Delete an organization webhook

Delete a webhook for an organization.  The authenticated user must be an organization owner to use this endpoint.  OAuth app tokens and personal access tokens (classic) need `admin:org_hook` scope. OAuth apps cannot list, view, or edit webhooks that they did not create and users cannot list, view, or edit webhooks that were created by OAuth apps.

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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    hook_id = 56 # int | The unique identifier of the hook. You can find this value in the `X-GitHub-Hook-ID` header of a webhook delivery.

    try:
        # Delete an organization webhook
        api_instance.orgs_delete_webhook(org, hook_id)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_delete_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **hook_id** | **int**| The unique identifier of the hook. You can find this value in the &#x60;X-GitHub-Hook-ID&#x60; header of a webhook delivery. | 

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

# **orgs_enable_or_disable_security_product_on_all_org_repos**
> orgs_enable_or_disable_security_product_on_all_org_repos(org, security_product, enablement, orgs_enable_or_disable_security_product_on_all_org_repos_request=orgs_enable_or_disable_security_product_on_all_org_repos_request)

Enable or disable a security feature for an organization

> [!WARNING] > **Closing down notice:** The ability to enable or disable a security feature for all eligible repositories in an organization is closing down. Please use [code security configurations](https://docs.github.com/rest/code-security/configurations) instead. For more information, see the [changelog](https://github.blog/changelog/2024-07-22-deprecation-of-api-endpoint-to-enable-or-disable-a-security-feature-for-an-organization/).  Enables or disables the specified security feature for all eligible repositories in an organization. For more information, see \"[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization).\"  The authenticated user must be an organization owner or be member of a team with the security manager role to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:org`, `write:org`, or `repo` scopes to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.orgs_enable_or_disable_security_product_on_all_org_repos_request import OrgsEnableOrDisableSecurityProductOnAllOrgReposRequest
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    security_product = 'security_product_example' # str | The security feature to enable or disable.
    enablement = 'enablement_example' # str | The action to take.  `enable_all` means to enable the specified security feature for all repositories in the organization. `disable_all` means to disable the specified security feature for all repositories in the organization.
    orgs_enable_or_disable_security_product_on_all_org_repos_request = github_openapi.OrgsEnableOrDisableSecurityProductOnAllOrgReposRequest() # OrgsEnableOrDisableSecurityProductOnAllOrgReposRequest |  (optional)

    try:
        # Enable or disable a security feature for an organization
        api_instance.orgs_enable_or_disable_security_product_on_all_org_repos(org, security_product, enablement, orgs_enable_or_disable_security_product_on_all_org_repos_request=orgs_enable_or_disable_security_product_on_all_org_repos_request)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_enable_or_disable_security_product_on_all_org_repos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **security_product** | **str**| The security feature to enable or disable. | 
 **enablement** | **str**| The action to take.  &#x60;enable_all&#x60; means to enable the specified security feature for all repositories in the organization. &#x60;disable_all&#x60; means to disable the specified security feature for all repositories in the organization. | 
 **orgs_enable_or_disable_security_product_on_all_org_repos_request** | [**OrgsEnableOrDisableSecurityProductOnAllOrgReposRequest**](OrgsEnableOrDisableSecurityProductOnAllOrgReposRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Action started |  -  |
**422** | The action could not be taken due to an in progress enablement, or a policy is preventing enablement |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_get**
> OrganizationFull orgs_get(org)

Get an organization

Gets information about an organization.  When the value of `two_factor_requirement_enabled` is `true`, the organization requires all members, billing managers, and outside collaborators to enable [two-factor authentication](https://docs.github.com/articles/securing-your-account-with-two-factor-authentication-2fa/).  To see the full details about an organization, the authenticated user must be an organization owner.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to see the full details about an organization.  To see information about an organization's GitHub plan, GitHub Apps need the `Organization plan` permission.

### Example


```python
import github_openapi
from github_openapi.models.organization_full import OrganizationFull
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.

    try:
        # Get an organization
        api_response = api_instance.orgs_get(org)
        print("The response of OrgsApi->orgs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 

### Return type

[**OrganizationFull**](OrganizationFull.md)

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

# **orgs_get_all_custom_properties**
> List[CustomProperty] orgs_get_all_custom_properties(org)

Get all custom properties for an organization

Gets all custom properties defined for an organization. Organization members can read these properties.

### Example


```python
import github_openapi
from github_openapi.models.custom_property import CustomProperty
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.

    try:
        # Get all custom properties for an organization
        api_response = api_instance.orgs_get_all_custom_properties(org)
        print("The response of OrgsApi->orgs_get_all_custom_properties:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_get_all_custom_properties: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 

### Return type

[**List[CustomProperty]**](CustomProperty.md)

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

# **orgs_get_custom_property**
> CustomProperty orgs_get_custom_property(org, custom_property_name)

Get a custom property for an organization

Gets a custom property that is defined for an organization. Organization members can read these properties.

### Example


```python
import github_openapi
from github_openapi.models.custom_property import CustomProperty
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    custom_property_name = 'custom_property_name_example' # str | The custom property name

    try:
        # Get a custom property for an organization
        api_response = api_instance.orgs_get_custom_property(org, custom_property_name)
        print("The response of OrgsApi->orgs_get_custom_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_get_custom_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **custom_property_name** | **str**| The custom property name | 

### Return type

[**CustomProperty**](CustomProperty.md)

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

# **orgs_get_membership_for_authenticated_user**
> OrgMembership orgs_get_membership_for_authenticated_user(org)

Get an organization membership for the authenticated user

If the authenticated user is an active or pending member of the organization, this endpoint will return the user's membership. If the authenticated user is not affiliated with the organization, a `404` is returned. This endpoint will return a `403` if the request is made by a GitHub App that is blocked by the organization.

### Example


```python
import github_openapi
from github_openapi.models.org_membership import OrgMembership
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.

    try:
        # Get an organization membership for the authenticated user
        api_response = api_instance.orgs_get_membership_for_authenticated_user(org)
        print("The response of OrgsApi->orgs_get_membership_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_get_membership_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 

### Return type

[**OrgMembership**](OrgMembership.md)

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

# **orgs_get_membership_for_user**
> OrgMembership orgs_get_membership_for_user(org, username)

Get organization membership for a user

In order to get a user's membership with an organization, the authenticated user must be an organization member. The `state` parameter in the response can be used to identify the user's membership status.

### Example


```python
import github_openapi
from github_openapi.models.org_membership import OrgMembership
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Get organization membership for a user
        api_response = api_instance.orgs_get_membership_for_user(org, username)
        print("The response of OrgsApi->orgs_get_membership_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_get_membership_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **username** | **str**| The handle for the GitHub user account. | 

### Return type

[**OrgMembership**](OrgMembership.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_get_org_role**
> OrganizationRole orgs_get_org_role(org, role_id)

Get an organization role

Gets an organization role that is available to this organization. For more information on organization roles, see \"[Using organization roles](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/using-organization-roles).\"  To use this endpoint, the authenticated user must be one of:  - An administrator for the organization. - A user, or a user on a team, with the fine-grained permissions of `read_organization_custom_org_role` in the organization.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.organization_role import OrganizationRole
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    role_id = 56 # int | The unique identifier of the role.

    try:
        # Get an organization role
        api_response = api_instance.orgs_get_org_role(org, role_id)
        print("The response of OrgsApi->orgs_get_org_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_get_org_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **role_id** | **int**| The unique identifier of the role. | 

### Return type

[**OrganizationRole**](OrganizationRole.md)

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
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_get_webhook**
> OrgHook orgs_get_webhook(org, hook_id)

Get an organization webhook

Returns a webhook configured in an organization. To get only the webhook `config` properties, see \"[Get a webhook configuration for an organization](/rest/orgs/webhooks#get-a-webhook-configuration-for-an-organization).  You must be an organization owner to use this endpoint.  OAuth app tokens and personal access tokens (classic) need `admin:org_hook` scope. OAuth apps cannot list, view, or edit webhooks that they did not create and users cannot list, view, or edit webhooks that were created by OAuth apps.

### Example


```python
import github_openapi
from github_openapi.models.org_hook import OrgHook
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    hook_id = 56 # int | The unique identifier of the hook. You can find this value in the `X-GitHub-Hook-ID` header of a webhook delivery.

    try:
        # Get an organization webhook
        api_response = api_instance.orgs_get_webhook(org, hook_id)
        print("The response of OrgsApi->orgs_get_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_get_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **hook_id** | **int**| The unique identifier of the hook. You can find this value in the &#x60;X-GitHub-Hook-ID&#x60; header of a webhook delivery. | 

### Return type

[**OrgHook**](OrgHook.md)

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

# **orgs_get_webhook_config_for_org**
> WebhookConfig orgs_get_webhook_config_for_org(org, hook_id)

Get a webhook configuration for an organization

Returns the webhook configuration for an organization. To get more information about the webhook, including the `active` state and `events`, use \"[Get an organization webhook ](/rest/orgs/webhooks#get-an-organization-webhook).\"  You must be an organization owner to use this endpoint.  OAuth app tokens and personal access tokens (classic) need `admin:org_hook` scope. OAuth apps cannot list, view, or edit webhooks that they did not create and users cannot list, view, or edit webhooks that were created by OAuth apps.

### Example


```python
import github_openapi
from github_openapi.models.webhook_config import WebhookConfig
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    hook_id = 56 # int | The unique identifier of the hook. You can find this value in the `X-GitHub-Hook-ID` header of a webhook delivery.

    try:
        # Get a webhook configuration for an organization
        api_response = api_instance.orgs_get_webhook_config_for_org(org, hook_id)
        print("The response of OrgsApi->orgs_get_webhook_config_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_get_webhook_config_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **hook_id** | **int**| The unique identifier of the hook. You can find this value in the &#x60;X-GitHub-Hook-ID&#x60; header of a webhook delivery. | 

### Return type

[**WebhookConfig**](WebhookConfig.md)

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

# **orgs_get_webhook_delivery**
> HookDelivery orgs_get_webhook_delivery(org, hook_id, delivery_id)

Get a webhook delivery for an organization webhook

Returns a delivery for a webhook configured in an organization.  You must be an organization owner to use this endpoint.  OAuth app tokens and personal access tokens (classic) need `admin:org_hook` scope. OAuth apps cannot list, view, or edit webhooks that they did not create and users cannot list, view, or edit webhooks that were created by OAuth apps.

### Example


```python
import github_openapi
from github_openapi.models.hook_delivery import HookDelivery
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    hook_id = 56 # int | The unique identifier of the hook. You can find this value in the `X-GitHub-Hook-ID` header of a webhook delivery.
    delivery_id = 56 # int | 

    try:
        # Get a webhook delivery for an organization webhook
        api_response = api_instance.orgs_get_webhook_delivery(org, hook_id, delivery_id)
        print("The response of OrgsApi->orgs_get_webhook_delivery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_get_webhook_delivery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **hook_id** | **int**| The unique identifier of the hook. You can find this value in the &#x60;X-GitHub-Hook-ID&#x60; header of a webhook delivery. | 
 **delivery_id** | **int**|  | 

### Return type

[**HookDelivery**](HookDelivery.md)

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
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_list**
> List[OrganizationSimple] orgs_list(since=since, per_page=per_page)

List organizations

Lists all organizations, in the order that they were created.  > [!NOTE] > Pagination is powered exclusively by the `since` parameter. Use the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers) to get the URL for the next page of organizations.

### Example


```python
import github_openapi
from github_openapi.models.organization_simple import OrganizationSimple
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
    api_instance = github_openapi.OrgsApi(api_client)
    since = 56 # int | An organization ID. Only return organizations with an ID greater than this ID. (optional)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)

    try:
        # List organizations
        api_response = api_instance.orgs_list(since=since, per_page=per_page)
        print("The response of OrgsApi->orgs_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **int**| An organization ID. Only return organizations with an ID greater than this ID. | [optional] 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]

### Return type

[**List[OrganizationSimple]**](OrganizationSimple.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_list_app_installations**
> OrgsListAppInstallations200Response orgs_list_app_installations(org, per_page=per_page, page=page)

List app installations for an organization

Lists all GitHub Apps in an organization. The installation count includes all GitHub Apps installed on repositories in the organization.  The authenticated user must be an organization owner to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:read` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.orgs_list_app_installations200_response import OrgsListAppInstallations200Response
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List app installations for an organization
        api_response = api_instance.orgs_list_app_installations(org, per_page=per_page, page=page)
        print("The response of OrgsApi->orgs_list_app_installations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_list_app_installations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**OrgsListAppInstallations200Response**](OrgsListAppInstallations200Response.md)

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

# **orgs_list_attestations**
> OrgsListAttestations200Response orgs_list_attestations(org, subject_digest, per_page=per_page, before=before, after=after)

List attestations

List a collection of artifact attestations with a given subject digest that are associated with repositories owned by an organization.  The collection of attestations returned by this endpoint is filtered according to the authenticated user's permissions; if the authenticated user cannot read a repository, the attestations associated with that repository will not be included in the response. In addition, when using a fine-grained access token the `attestations:read` permission is required.  **Please note:** in order to offer meaningful security benefits, an attestation's signature and timestamps **must** be cryptographically verified, and the identity of the attestation signer **must** be validated. Attestations can be verified using the [GitHub CLI `attestation verify` command](https://cli.github.com/manual/gh_attestation_verify). For more information, see [our guide on how to use artifact attestations to establish a build's provenance](https://docs.github.com/actions/security-guides/using-artifact-attestations-to-establish-provenance-for-builds).

### Example


```python
import github_openapi
from github_openapi.models.orgs_list_attestations200_response import OrgsListAttestations200Response
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    subject_digest = 'subject_digest_example' # str | The parameter should be set to the attestation's subject's SHA256 digest, in the form `sha256:HEX_DIGEST`.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    before = 'before_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)
    after = 'after_example' # str | A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional)

    try:
        # List attestations
        api_response = api_instance.orgs_list_attestations(org, subject_digest, per_page=per_page, before=before, after=after)
        print("The response of OrgsApi->orgs_list_attestations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_list_attestations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **subject_digest** | **str**| The parameter should be set to the attestation&#39;s subject&#39;s SHA256 digest, in the form &#x60;sha256:HEX_DIGEST&#x60;. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **before** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results before this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 
 **after** | **str**| A cursor, as given in the [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers). If specified, the query only searches for results after this cursor. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] 

### Return type

[**OrgsListAttestations200Response**](OrgsListAttestations200Response.md)

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

# **orgs_list_blocked_users**
> List[SimpleUser] orgs_list_blocked_users(org, per_page=per_page, page=page)

List users blocked by an organization

List the users blocked by an organization.

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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List users blocked by an organization
        api_response = api_instance.orgs_list_blocked_users(org, per_page=per_page, page=page)
        print("The response of OrgsApi->orgs_list_blocked_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_list_blocked_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
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
**200** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_list_custom_properties_values_for_repos**
> List[OrgRepoCustomPropertyValues] orgs_list_custom_properties_values_for_repos(org, per_page=per_page, page=page, repository_query=repository_query)

List custom property values for organization repositories

Lists organization repositories with all of their custom property values. Organization members can read these properties.

### Example


```python
import github_openapi
from github_openapi.models.org_repo_custom_property_values import OrgRepoCustomPropertyValues
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    repository_query = 'repository_query_example' # str | Finds repositories in the organization with a query containing one or more search keywords and qualifiers. Qualifiers allow you to limit your search to specific areas of GitHub. The REST API supports the same qualifiers as the web interface for GitHub. To learn more about the format of the query, see [Constructing a search query](https://docs.github.com/rest/search/search#constructing-a-search-query). See \"[Searching for repositories](https://docs.github.com/articles/searching-for-repositories/)\" for a detailed list of qualifiers. (optional)

    try:
        # List custom property values for organization repositories
        api_response = api_instance.orgs_list_custom_properties_values_for_repos(org, per_page=per_page, page=page, repository_query=repository_query)
        print("The response of OrgsApi->orgs_list_custom_properties_values_for_repos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_list_custom_properties_values_for_repos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **repository_query** | **str**| Finds repositories in the organization with a query containing one or more search keywords and qualifiers. Qualifiers allow you to limit your search to specific areas of GitHub. The REST API supports the same qualifiers as the web interface for GitHub. To learn more about the format of the query, see [Constructing a search query](https://docs.github.com/rest/search/search#constructing-a-search-query). See \&quot;[Searching for repositories](https://docs.github.com/articles/searching-for-repositories/)\&quot; for a detailed list of qualifiers. | [optional] 

### Return type

[**List[OrgRepoCustomPropertyValues]**](OrgRepoCustomPropertyValues.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  * Link -  <br>  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_list_failed_invitations**
> List[OrganizationInvitation] orgs_list_failed_invitations(org, per_page=per_page, page=page)

List failed organization invitations

The return hash contains `failed_at` and `failed_reason` fields which represent the time at which the invitation failed and the reason for the failure.

### Example


```python
import github_openapi
from github_openapi.models.organization_invitation import OrganizationInvitation
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List failed organization invitations
        api_response = api_instance.orgs_list_failed_invitations(org, per_page=per_page, page=page)
        print("The response of OrgsApi->orgs_list_failed_invitations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_list_failed_invitations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[OrganizationInvitation]**](OrganizationInvitation.md)

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

# **orgs_list_for_authenticated_user**
> List[OrganizationSimple] orgs_list_for_authenticated_user(per_page=per_page, page=page)

List organizations for the authenticated user

List organizations for the authenticated user.  For OAuth app tokens and personal access tokens (classic), this endpoint only lists organizations that your authorization allows you to operate on in some way (e.g., you can list teams with `read:org` scope, you can publicize your organization membership with `user` scope, etc.). Therefore, this API requires at least `user` or `read:org` scope for OAuth app tokens and personal access tokens (classic). Requests with insufficient scope will receive a `403 Forbidden` response.  > [!NOTE] > Requests using a fine-grained access token will receive a `200 Success` response with an empty list.

### Example


```python
import github_openapi
from github_openapi.models.organization_simple import OrganizationSimple
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
    api_instance = github_openapi.OrgsApi(api_client)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List organizations for the authenticated user
        api_response = api_instance.orgs_list_for_authenticated_user(per_page=per_page, page=page)
        print("The response of OrgsApi->orgs_list_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_list_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[OrganizationSimple]**](OrganizationSimple.md)

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

# **orgs_list_for_user**
> List[OrganizationSimple] orgs_list_for_user(username, per_page=per_page, page=page)

List organizations for a user

List [public organization memberships](https://docs.github.com/articles/publicizing-or-concealing-organization-membership) for the specified user.  This method only lists _public_ memberships, regardless of authentication. If you need to fetch all of the organization memberships (public and private) for the authenticated user, use the [List organizations for the authenticated user](https://docs.github.com/rest/orgs/orgs#list-organizations-for-the-authenticated-user) API instead.

### Example


```python
import github_openapi
from github_openapi.models.organization_simple import OrganizationSimple
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
    api_instance = github_openapi.OrgsApi(api_client)
    username = 'username_example' # str | The handle for the GitHub user account.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List organizations for a user
        api_response = api_instance.orgs_list_for_user(username, per_page=per_page, page=page)
        print("The response of OrgsApi->orgs_list_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_list_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The handle for the GitHub user account. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[OrganizationSimple]**](OrganizationSimple.md)

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

# **orgs_list_invitation_teams**
> List[Team] orgs_list_invitation_teams(org, invitation_id, per_page=per_page, page=page)

List organization invitation teams

List all teams associated with an invitation. In order to see invitations in an organization, the authenticated user must be an organization owner.

### Example


```python
import github_openapi
from github_openapi.models.team import Team
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    invitation_id = 56 # int | The unique identifier of the invitation.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List organization invitation teams
        api_response = api_instance.orgs_list_invitation_teams(org, invitation_id, per_page=per_page, page=page)
        print("The response of OrgsApi->orgs_list_invitation_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_list_invitation_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **invitation_id** | **int**| The unique identifier of the invitation. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Team]**](Team.md)

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

# **orgs_list_members**
> List[SimpleUser] orgs_list_members(org, filter=filter, role=role, per_page=per_page, page=page)

List organization members

List all users who are members of an organization. If the authenticated user is also a member of this organization then both concealed and public members will be returned.

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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    filter = all # str | Filter members returned in the list. `2fa_disabled` means that only members without [two-factor authentication](https://github.com/blog/1614-two-factor-authentication) enabled will be returned. This options is only available for organization owners. (optional) (default to all)
    role = all # str | Filter members returned by their role. (optional) (default to all)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List organization members
        api_response = api_instance.orgs_list_members(org, filter=filter, role=role, per_page=per_page, page=page)
        print("The response of OrgsApi->orgs_list_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_list_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **filter** | **str**| Filter members returned in the list. &#x60;2fa_disabled&#x60; means that only members without [two-factor authentication](https://github.com/blog/1614-two-factor-authentication) enabled will be returned. This options is only available for organization owners. | [optional] [default to all]
 **role** | **str**| Filter members returned by their role. | [optional] [default to all]
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
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_list_memberships_for_authenticated_user**
> List[OrgMembership] orgs_list_memberships_for_authenticated_user(state=state, per_page=per_page, page=page)

List organization memberships for the authenticated user

Lists all of the authenticated user's organization memberships.

### Example


```python
import github_openapi
from github_openapi.models.org_membership import OrgMembership
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
    api_instance = github_openapi.OrgsApi(api_client)
    state = 'state_example' # str | Indicates the state of the memberships to return. If not specified, the API returns both active and pending memberships. (optional)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List organization memberships for the authenticated user
        api_response = api_instance.orgs_list_memberships_for_authenticated_user(state=state, per_page=per_page, page=page)
        print("The response of OrgsApi->orgs_list_memberships_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_list_memberships_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| Indicates the state of the memberships to return. If not specified, the API returns both active and pending memberships. | [optional] 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[OrgMembership]**](OrgMembership.md)

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

# **orgs_list_org_role_teams**
> List[TeamRoleAssignment] orgs_list_org_role_teams(org, role_id, per_page=per_page, page=page)

List teams that are assigned to an organization role

Lists the teams that are assigned to an organization role. For more information on organization roles, see \"[Using organization roles](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/using-organization-roles).\"  To use this endpoint, you must be an administrator for the organization.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.team_role_assignment import TeamRoleAssignment
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    role_id = 56 # int | The unique identifier of the role.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List teams that are assigned to an organization role
        api_response = api_instance.orgs_list_org_role_teams(org, role_id, per_page=per_page, page=page)
        print("The response of OrgsApi->orgs_list_org_role_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_list_org_role_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **role_id** | **int**| The unique identifier of the role. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[TeamRoleAssignment]**](TeamRoleAssignment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response - List of assigned teams |  * Link -  <br>  |
**404** | Response if the organization or role does not exist. |  -  |
**422** | Response if the organization roles feature is not enabled or validation failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_list_org_role_users**
> List[UserRoleAssignment] orgs_list_org_role_users(org, role_id, per_page=per_page, page=page)

List users that are assigned to an organization role

Lists organization members that are assigned to an organization role. For more information on organization roles, see \"[Using organization roles](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/using-organization-roles).\"  To use this endpoint, you must be an administrator for the organization.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.user_role_assignment import UserRoleAssignment
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    role_id = 56 # int | The unique identifier of the role.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List users that are assigned to an organization role
        api_response = api_instance.orgs_list_org_role_users(org, role_id, per_page=per_page, page=page)
        print("The response of OrgsApi->orgs_list_org_role_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_list_org_role_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **role_id** | **int**| The unique identifier of the role. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[UserRoleAssignment]**](UserRoleAssignment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response - List of assigned users |  * Link -  <br>  |
**404** | Response if the organization or role does not exist. |  -  |
**422** | Response if the organization roles feature is not enabled or validation failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_list_org_roles**
> OrgsListOrgRoles200Response orgs_list_org_roles(org)

Get all organization roles for an organization

Lists the organization roles available in this organization. For more information on organization roles, see \"[Using organization roles](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/using-organization-roles).\"  To use this endpoint, the authenticated user must be one of:  - An administrator for the organization. - A user, or a user on a team, with the fine-grained permissions of `read_organization_custom_org_role` in the organization.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.orgs_list_org_roles200_response import OrgsListOrgRoles200Response
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.

    try:
        # Get all organization roles for an organization
        api_response = api_instance.orgs_list_org_roles(org)
        print("The response of OrgsApi->orgs_list_org_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_list_org_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 

### Return type

[**OrgsListOrgRoles200Response**](OrgsListOrgRoles200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response - list of organization roles |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_list_outside_collaborators**
> List[SimpleUser] orgs_list_outside_collaborators(org, filter=filter, per_page=per_page, page=page)

List outside collaborators for an organization

List all users who are outside collaborators of an organization.

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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    filter = all # str | Filter the list of outside collaborators. `2fa_disabled` means that only outside collaborators without [two-factor authentication](https://github.com/blog/1614-two-factor-authentication) enabled will be returned. (optional) (default to all)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List outside collaborators for an organization
        api_response = api_instance.orgs_list_outside_collaborators(org, filter=filter, per_page=per_page, page=page)
        print("The response of OrgsApi->orgs_list_outside_collaborators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_list_outside_collaborators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **filter** | **str**| Filter the list of outside collaborators. &#x60;2fa_disabled&#x60; means that only outside collaborators without [two-factor authentication](https://github.com/blog/1614-two-factor-authentication) enabled will be returned. | [optional] [default to all]
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

# **orgs_list_pat_grant_repositories**
> List[MinimalRepository] orgs_list_pat_grant_repositories(org, pat_id, per_page=per_page, page=page)

List repositories a fine-grained personal access token has access to

Lists the repositories a fine-grained personal access token has access to.  Only GitHub Apps can use this endpoint.

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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    pat_id = 56 # int | Unique identifier of the fine-grained personal access token.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List repositories a fine-grained personal access token has access to
        api_response = api_instance.orgs_list_pat_grant_repositories(org, pat_id, per_page=per_page, page=page)
        print("The response of OrgsApi->orgs_list_pat_grant_repositories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_list_pat_grant_repositories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **pat_id** | **int**| Unique identifier of the fine-grained personal access token. | 
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
**500** | Internal Error |  -  |
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |
**200** | Response |  * Link -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_list_pat_grant_request_repositories**
> List[MinimalRepository] orgs_list_pat_grant_request_repositories(org, pat_request_id, per_page=per_page, page=page)

List repositories requested to be accessed by a fine-grained personal access token

Lists the repositories a fine-grained personal access token request is requesting access to.  Only GitHub Apps can use this endpoint.

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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    pat_request_id = 56 # int | Unique identifier of the request for access via fine-grained personal access token.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List repositories requested to be accessed by a fine-grained personal access token
        api_response = api_instance.orgs_list_pat_grant_request_repositories(org, pat_request_id, per_page=per_page, page=page)
        print("The response of OrgsApi->orgs_list_pat_grant_request_repositories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_list_pat_grant_request_repositories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **pat_request_id** | **int**| Unique identifier of the request for access via fine-grained personal access token. | 
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
**500** | Internal Error |  -  |
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |
**200** | Response |  * Link -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_list_pat_grant_requests**
> List[OrganizationProgrammaticAccessGrantRequest] orgs_list_pat_grant_requests(org, per_page=per_page, page=page, sort=sort, direction=direction, owner=owner, repository=repository, permission=permission, last_used_before=last_used_before, last_used_after=last_used_after)

List requests to access organization resources with fine-grained personal access tokens

Lists requests from organization members to access organization resources with a fine-grained personal access token.  Only GitHub Apps can use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.organization_programmatic_access_grant_request import OrganizationProgrammaticAccessGrantRequest
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    sort = created_at # str | The property by which to sort the results. (optional) (default to created_at)
    direction = desc # str | The direction to sort the results by. (optional) (default to desc)
    owner = ['owner[]=octocat1,owner[]=octocat2'] # List[str] | A list of owner usernames to use to filter the results. (optional)
    repository = 'Hello-World' # str | The name of the repository to use to filter the results. (optional)
    permission = 'issues_read' # str | The permission to use to filter the results. (optional)
    last_used_before = '2013-10-20T19:20:30+01:00' # datetime | Only show fine-grained personal access tokens used before the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. (optional)
    last_used_after = '2013-10-20T19:20:30+01:00' # datetime | Only show fine-grained personal access tokens used after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. (optional)

    try:
        # List requests to access organization resources with fine-grained personal access tokens
        api_response = api_instance.orgs_list_pat_grant_requests(org, per_page=per_page, page=page, sort=sort, direction=direction, owner=owner, repository=repository, permission=permission, last_used_before=last_used_before, last_used_after=last_used_after)
        print("The response of OrgsApi->orgs_list_pat_grant_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_list_pat_grant_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **sort** | **str**| The property by which to sort the results. | [optional] [default to created_at]
 **direction** | **str**| The direction to sort the results by. | [optional] [default to desc]
 **owner** | [**List[str]**](str.md)| A list of owner usernames to use to filter the results. | [optional] 
 **repository** | **str**| The name of the repository to use to filter the results. | [optional] 
 **permission** | **str**| The permission to use to filter the results. | [optional] 
 **last_used_before** | **datetime**| Only show fine-grained personal access tokens used before the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
 **last_used_after** | **datetime**| Only show fine-grained personal access tokens used after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 

### Return type

[**List[OrganizationProgrammaticAccessGrantRequest]**](OrganizationProgrammaticAccessGrantRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Error |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |
**200** | Response |  * Link -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_list_pat_grants**
> List[OrganizationProgrammaticAccessGrant] orgs_list_pat_grants(org, per_page=per_page, page=page, sort=sort, direction=direction, owner=owner, repository=repository, permission=permission, last_used_before=last_used_before, last_used_after=last_used_after)

List fine-grained personal access tokens with access to organization resources

Lists approved fine-grained personal access tokens owned by organization members that can access organization resources.  Only GitHub Apps can use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.organization_programmatic_access_grant import OrganizationProgrammaticAccessGrant
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    sort = created_at # str | The property by which to sort the results. (optional) (default to created_at)
    direction = desc # str | The direction to sort the results by. (optional) (default to desc)
    owner = ['owner[]=octocat1,owner[]=octocat2'] # List[str] | A list of owner usernames to use to filter the results. (optional)
    repository = 'Hello-World' # str | The name of the repository to use to filter the results. (optional)
    permission = 'issues_read' # str | The permission to use to filter the results. (optional)
    last_used_before = '2013-10-20T19:20:30+01:00' # datetime | Only show fine-grained personal access tokens used before the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. (optional)
    last_used_after = '2013-10-20T19:20:30+01:00' # datetime | Only show fine-grained personal access tokens used after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`. (optional)

    try:
        # List fine-grained personal access tokens with access to organization resources
        api_response = api_instance.orgs_list_pat_grants(org, per_page=per_page, page=page, sort=sort, direction=direction, owner=owner, repository=repository, permission=permission, last_used_before=last_used_before, last_used_after=last_used_after)
        print("The response of OrgsApi->orgs_list_pat_grants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_list_pat_grants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **sort** | **str**| The property by which to sort the results. | [optional] [default to created_at]
 **direction** | **str**| The direction to sort the results by. | [optional] [default to desc]
 **owner** | [**List[str]**](str.md)| A list of owner usernames to use to filter the results. | [optional] 
 **repository** | **str**| The name of the repository to use to filter the results. | [optional] 
 **permission** | **str**| The permission to use to filter the results. | [optional] 
 **last_used_before** | **datetime**| Only show fine-grained personal access tokens used before the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
 **last_used_after** | **datetime**| Only show fine-grained personal access tokens used after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 

### Return type

[**List[OrganizationProgrammaticAccessGrant]**](OrganizationProgrammaticAccessGrant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Error |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |
**200** | Response |  * Link -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_list_pending_invitations**
> List[OrganizationInvitation] orgs_list_pending_invitations(org, per_page=per_page, page=page, role=role, invitation_source=invitation_source)

List pending organization invitations

The return hash contains a `role` field which refers to the Organization Invitation role and will be one of the following values: `direct_member`, `admin`, `billing_manager`, or `hiring_manager`. If the invitee is not a GitHub member, the `login` field in the return hash will be `null`.

### Example


```python
import github_openapi
from github_openapi.models.organization_invitation import OrganizationInvitation
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    role = all # str | Filter invitations by their member role. (optional) (default to all)
    invitation_source = all # str | Filter invitations by their invitation source. (optional) (default to all)

    try:
        # List pending organization invitations
        api_response = api_instance.orgs_list_pending_invitations(org, per_page=per_page, page=page, role=role, invitation_source=invitation_source)
        print("The response of OrgsApi->orgs_list_pending_invitations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_list_pending_invitations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **role** | **str**| Filter invitations by their member role. | [optional] [default to all]
 **invitation_source** | **str**| Filter invitations by their invitation source. | [optional] [default to all]

### Return type

[**List[OrganizationInvitation]**](OrganizationInvitation.md)

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

# **orgs_list_public_members**
> List[SimpleUser] orgs_list_public_members(org, per_page=per_page, page=page)

List public organization members

Members of an organization can choose to have their membership publicized or not.

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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List public organization members
        api_response = api_instance.orgs_list_public_members(org, per_page=per_page, page=page)
        print("The response of OrgsApi->orgs_list_public_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_list_public_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
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

# **orgs_list_security_manager_teams**
> List[TeamSimple] orgs_list_security_manager_teams(org)

List security manager teams

> [!WARNING] > **Closing down notice:** This operation is closing down and will be removed starting January 1, 2026. Please use the \"[Organization Roles](https://docs.github.com/rest/orgs/organization-roles)\" endpoints instead.

### Example


```python
import github_openapi
from github_openapi.models.team_simple import TeamSimple
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.

    try:
        # List security manager teams
        api_response = api_instance.orgs_list_security_manager_teams(org)
        print("The response of OrgsApi->orgs_list_security_manager_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_list_security_manager_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 

### Return type

[**List[TeamSimple]**](TeamSimple.md)

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

# **orgs_list_webhook_deliveries**
> List[HookDeliveryItem] orgs_list_webhook_deliveries(org, hook_id, per_page=per_page, cursor=cursor)

List deliveries for an organization webhook

Returns a list of webhook deliveries for a webhook configured in an organization.  You must be an organization owner to use this endpoint.  OAuth app tokens and personal access tokens (classic) need `admin:org_hook` scope. OAuth apps cannot list, view, or edit webhooks that they did not create and users cannot list, view, or edit webhooks that were created by OAuth apps.

### Example


```python
import github_openapi
from github_openapi.models.hook_delivery_item import HookDeliveryItem
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    hook_id = 56 # int | The unique identifier of the hook. You can find this value in the `X-GitHub-Hook-ID` header of a webhook delivery.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    cursor = 'cursor_example' # str | Used for pagination: the starting delivery from which the page of deliveries is fetched. Refer to the `link` header for the next and previous page cursors. (optional)

    try:
        # List deliveries for an organization webhook
        api_response = api_instance.orgs_list_webhook_deliveries(org, hook_id, per_page=per_page, cursor=cursor)
        print("The response of OrgsApi->orgs_list_webhook_deliveries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_list_webhook_deliveries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **hook_id** | **int**| The unique identifier of the hook. You can find this value in the &#x60;X-GitHub-Hook-ID&#x60; header of a webhook delivery. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **cursor** | **str**| Used for pagination: the starting delivery from which the page of deliveries is fetched. Refer to the &#x60;link&#x60; header for the next and previous page cursors. | [optional] 

### Return type

[**List[HookDeliveryItem]**](HookDeliveryItem.md)

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
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_list_webhooks**
> List[OrgHook] orgs_list_webhooks(org, per_page=per_page, page=page)

List organization webhooks

List webhooks for an organization.  The authenticated user must be an organization owner to use this endpoint.  OAuth app tokens and personal access tokens (classic) need `admin:org_hook` scope. OAuth apps cannot list, view, or edit webhooks that they did not create and users cannot list, view, or edit webhooks that were created by OAuth apps.

### Example


```python
import github_openapi
from github_openapi.models.org_hook import OrgHook
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List organization webhooks
        api_response = api_instance.orgs_list_webhooks(org, per_page=per_page, page=page)
        print("The response of OrgsApi->orgs_list_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_list_webhooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[OrgHook]**](OrgHook.md)

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

# **orgs_ping_webhook**
> orgs_ping_webhook(org, hook_id)

Ping an organization webhook

This will trigger a [ping event](https://docs.github.com/webhooks/#ping-event) to be sent to the hook.  You must be an organization owner to use this endpoint.  OAuth app tokens and personal access tokens (classic) need `admin:org_hook` scope. OAuth apps cannot list, view, or edit webhooks that they did not create and users cannot list, view, or edit webhooks that were created by OAuth apps.

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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    hook_id = 56 # int | The unique identifier of the hook. You can find this value in the `X-GitHub-Hook-ID` header of a webhook delivery.

    try:
        # Ping an organization webhook
        api_instance.orgs_ping_webhook(org, hook_id)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_ping_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **hook_id** | **int**| The unique identifier of the hook. You can find this value in the &#x60;X-GitHub-Hook-ID&#x60; header of a webhook delivery. | 

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

# **orgs_redeliver_webhook_delivery**
> object orgs_redeliver_webhook_delivery(org, hook_id, delivery_id)

Redeliver a delivery for an organization webhook

Redeliver a delivery for a webhook configured in an organization.  You must be an organization owner to use this endpoint.  OAuth app tokens and personal access tokens (classic) need `admin:org_hook` scope. OAuth apps cannot list, view, or edit webhooks that they did not create and users cannot list, view, or edit webhooks that were created by OAuth apps.

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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    hook_id = 56 # int | The unique identifier of the hook. You can find this value in the `X-GitHub-Hook-ID` header of a webhook delivery.
    delivery_id = 56 # int | 

    try:
        # Redeliver a delivery for an organization webhook
        api_response = api_instance.orgs_redeliver_webhook_delivery(org, hook_id, delivery_id)
        print("The response of OrgsApi->orgs_redeliver_webhook_delivery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_redeliver_webhook_delivery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **hook_id** | **int**| The unique identifier of the hook. You can find this value in the &#x60;X-GitHub-Hook-ID&#x60; header of a webhook delivery. | 
 **delivery_id** | **int**|  | 

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
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_remove_custom_property**
> orgs_remove_custom_property(org, custom_property_name)

Remove a custom property for an organization

Removes a custom property that is defined for an organization.  To use this endpoint, the authenticated user must be one of:   - An administrator for the organization.   - A user, or a user on a team, with the fine-grained permission of `custom_properties_org_definitions_manager` in the organization.

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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    custom_property_name = 'custom_property_name_example' # str | The custom property name

    try:
        # Remove a custom property for an organization
        api_instance.orgs_remove_custom_property(org, custom_property_name)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_remove_custom_property: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **custom_property_name** | **str**| The custom property name | 

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
**204** | A header with no content is returned. |  -  |
**403** | Forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_remove_member**
> orgs_remove_member(org, username)

Remove an organization member

Removing a user from this list will remove them from all teams and they will no longer have any access to the organization's repositories.

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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Remove an organization member
        api_instance.orgs_remove_member(org, username)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_remove_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **username** | **str**| The handle for the GitHub user account. | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_remove_membership_for_user**
> orgs_remove_membership_for_user(org, username)

Remove organization membership for a user

In order to remove a user's membership with an organization, the authenticated user must be an organization owner.  If the specified user is an active member of the organization, this will remove them from the organization. If the specified user has been invited to the organization, this will cancel their invitation. The specified user will receive an email notification in both cases.

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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Remove organization membership for a user
        api_instance.orgs_remove_membership_for_user(org, username)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_remove_membership_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **username** | **str**| The handle for the GitHub user account. | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_remove_outside_collaborator**
> orgs_remove_outside_collaborator(org, username)

Remove outside collaborator from an organization

Removing a user from this list will remove them from all the organization's repositories.

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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Remove outside collaborator from an organization
        api_instance.orgs_remove_outside_collaborator(org, username)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_remove_outside_collaborator: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **username** | **str**| The handle for the GitHub user account. | 

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
**422** | Unprocessable Entity if user is a member of the organization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_remove_public_membership_for_authenticated_user**
> orgs_remove_public_membership_for_authenticated_user(org, username)

Remove public organization membership for the authenticated user

Removes the public membership for the authenticated user from the specified organization, unless public visibility is enforced by default.

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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Remove public organization membership for the authenticated user
        api_instance.orgs_remove_public_membership_for_authenticated_user(org, username)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_remove_public_membership_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **username** | **str**| The handle for the GitHub user account. | 

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

# **orgs_remove_security_manager_team**
> orgs_remove_security_manager_team(org, team_slug)

Remove a security manager team

> [!WARNING] > **Closing down notice:** This operation is closing down and will be removed starting January 1, 2026. Please use the \"[Organization Roles](https://docs.github.com/rest/orgs/organization-roles)\" endpoints instead.

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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.

    try:
        # Remove a security manager team
        api_instance.orgs_remove_security_manager_team(org, team_slug)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_remove_security_manager_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 

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

# **orgs_review_pat_grant_request**
> orgs_review_pat_grant_request(org, pat_request_id, orgs_review_pat_grant_request_request)

Review a request to access organization resources with a fine-grained personal access token

Approves or denies a pending request to access organization resources via a fine-grained personal access token.  Only GitHub Apps can use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.orgs_review_pat_grant_request_request import OrgsReviewPatGrantRequestRequest
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    pat_request_id = 56 # int | Unique identifier of the request for access via fine-grained personal access token.
    orgs_review_pat_grant_request_request = {"action":"deny","reason":"This request is denied because the access is too broad."} # OrgsReviewPatGrantRequestRequest | 

    try:
        # Review a request to access organization resources with a fine-grained personal access token
        api_instance.orgs_review_pat_grant_request(org, pat_request_id, orgs_review_pat_grant_request_request)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_review_pat_grant_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **pat_request_id** | **int**| Unique identifier of the request for access via fine-grained personal access token. | 
 **orgs_review_pat_grant_request_request** | [**OrgsReviewPatGrantRequestRequest**](OrgsReviewPatGrantRequestRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Error |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |
**204** | A header with no content is returned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_review_pat_grant_requests_in_bulk**
> object orgs_review_pat_grant_requests_in_bulk(org, orgs_review_pat_grant_requests_in_bulk_request)

Review requests to access organization resources with fine-grained personal access tokens

Approves or denies multiple pending requests to access organization resources via a fine-grained personal access token.  Only GitHub Apps can use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.orgs_review_pat_grant_requests_in_bulk_request import OrgsReviewPatGrantRequestsInBulkRequest
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    orgs_review_pat_grant_requests_in_bulk_request = {"pat_request_ids":[42,73],"action":"deny","reason":"Access is too broad."} # OrgsReviewPatGrantRequestsInBulkRequest | 

    try:
        # Review requests to access organization resources with fine-grained personal access tokens
        api_response = api_instance.orgs_review_pat_grant_requests_in_bulk(org, orgs_review_pat_grant_requests_in_bulk_request)
        print("The response of OrgsApi->orgs_review_pat_grant_requests_in_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_review_pat_grant_requests_in_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **orgs_review_pat_grant_requests_in_bulk_request** | [**OrgsReviewPatGrantRequestsInBulkRequest**](OrgsReviewPatGrantRequestsInBulkRequest.md)|  | 

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
**500** | Internal Error |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_revoke_all_org_roles_team**
> orgs_revoke_all_org_roles_team(org, team_slug)

Remove all organization roles for a team

Removes all assigned organization roles from a team. For more information on organization roles, see \"[Using organization roles](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/using-organization-roles).\"  The authenticated user must be an administrator for the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.

    try:
        # Remove all organization roles for a team
        api_instance.orgs_revoke_all_org_roles_team(org, team_slug)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_revoke_all_org_roles_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 

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

# **orgs_revoke_all_org_roles_user**
> orgs_revoke_all_org_roles_user(org, username)

Remove all organization roles for a user

Revokes all assigned organization roles from a user. For more information on organization roles, see \"[Using organization roles](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/using-organization-roles).\"  The authenticated user must be an administrator for the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Remove all organization roles for a user
        api_instance.orgs_revoke_all_org_roles_user(org, username)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_revoke_all_org_roles_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **username** | **str**| The handle for the GitHub user account. | 

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

# **orgs_revoke_org_role_team**
> orgs_revoke_org_role_team(org, team_slug, role_id)

Remove an organization role from a team

Removes an organization role from a team. For more information on organization roles, see \"[Using organization roles](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/using-organization-roles).\"  The authenticated user must be an administrator for the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    role_id = 56 # int | The unique identifier of the role.

    try:
        # Remove an organization role from a team
        api_instance.orgs_revoke_org_role_team(org, team_slug, role_id)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_revoke_org_role_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
 **role_id** | **int**| The unique identifier of the role. | 

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

# **orgs_revoke_org_role_user**
> orgs_revoke_org_role_user(org, username, role_id)

Remove an organization role from a user

Remove an organization role from a user. For more information on organization roles, see \"[Using organization roles](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/using-organization-roles).\"  The authenticated user must be an administrator for the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.

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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    username = 'username_example' # str | The handle for the GitHub user account.
    role_id = 56 # int | The unique identifier of the role.

    try:
        # Remove an organization role from a user
        api_instance.orgs_revoke_org_role_user(org, username, role_id)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_revoke_org_role_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **username** | **str**| The handle for the GitHub user account. | 
 **role_id** | **int**| The unique identifier of the role. | 

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

# **orgs_set_membership_for_user**
> OrgMembership orgs_set_membership_for_user(org, username, orgs_set_membership_for_user_request=orgs_set_membership_for_user_request)

Set organization membership for a user

Only authenticated organization owners can add a member to the organization or update the member's role.  *   If the authenticated user is _adding_ a member to the organization, the invited user will receive an email inviting them to the organization. The user's [membership status](https://docs.github.com/rest/orgs/members#get-organization-membership-for-a-user) will be `pending` until they accept the invitation.      *   Authenticated users can _update_ a user's membership by passing the `role` parameter. If the authenticated user changes a member's role to `admin`, the affected user will receive an email notifying them that they've been made an organization owner. If the authenticated user changes an owner's role to `member`, no email will be sent.  **Rate limits**  To prevent abuse, organization owners are limited to creating 50 organization invitations for an organization within a 24 hour period. If the organization is more than one month old or on a paid plan, the limit is 500 invitations per 24 hour period.

### Example


```python
import github_openapi
from github_openapi.models.org_membership import OrgMembership
from github_openapi.models.orgs_set_membership_for_user_request import OrgsSetMembershipForUserRequest
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    username = 'username_example' # str | The handle for the GitHub user account.
    orgs_set_membership_for_user_request = {"role":"member"} # OrgsSetMembershipForUserRequest |  (optional)

    try:
        # Set organization membership for a user
        api_response = api_instance.orgs_set_membership_for_user(org, username, orgs_set_membership_for_user_request=orgs_set_membership_for_user_request)
        print("The response of OrgsApi->orgs_set_membership_for_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_set_membership_for_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **username** | **str**| The handle for the GitHub user account. | 
 **orgs_set_membership_for_user_request** | [**OrgsSetMembershipForUserRequest**](OrgsSetMembershipForUserRequest.md)|  | [optional] 

### Return type

[**OrgMembership**](OrgMembership.md)

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_set_public_membership_for_authenticated_user**
> orgs_set_public_membership_for_authenticated_user(org, username)

Set public organization membership for the authenticated user

The user can publicize their own membership. (A user cannot publicize the membership for another user.)  Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see \"[HTTP method](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#http-method).\"

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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Set public organization membership for the authenticated user
        api_instance.orgs_set_public_membership_for_authenticated_user(org, username)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_set_public_membership_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **username** | **str**| The handle for the GitHub user account. | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_unblock_user**
> orgs_unblock_user(org, username)

Unblock a user from an organization

Unblocks the given user on behalf of the specified organization.

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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Unblock a user from an organization
        api_instance.orgs_unblock_user(org, username)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_unblock_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **username** | **str**| The handle for the GitHub user account. | 

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

# **orgs_update**
> OrganizationFull orgs_update(org, orgs_update_request=orgs_update_request)

Update an organization

> [!WARNING] > **Closing down notice:** GitHub will replace and discontinue `members_allowed_repository_creation_type` in favor of more granular permissions. The new input parameters are `members_can_create_public_repositories`, `members_can_create_private_repositories` for all organizations and `members_can_create_internal_repositories` for organizations associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+. For more information, see the [blog post](https://developer.github.com/changes/2019-12-03-internal-visibility-changes).  > [!WARNING] > **Closing down notice:** Code security product enablement for new repositories through the organization API is closing down. Please use [code security configurations](https://docs.github.com/rest/code-security/configurations#set-a-code-security-configuration-as-a-default-for-an-organization) to set defaults instead. For more information on setting a default security configuration, see the [changelog](https://github.blog/changelog/2024-07-09-sunsetting-security-settings-defaults-parameters-in-the-organizations-rest-api/).  Updates the organization's profile and member privileges.  The authenticated user must be an organization owner to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:org` or `repo` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.organization_full import OrganizationFull
from github_openapi.models.orgs_update_request import OrgsUpdateRequest
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    orgs_update_request = {"billing_email":"mona@github.com","company":"GitHub","email":"mona@github.com","twitter_username":"github","location":"San Francisco","name":"github","description":"GitHub, the company.","default_repository_permission":"read","members_can_create_repositories":true,"members_allowed_repository_creation_type":"all"} # OrgsUpdateRequest |  (optional)

    try:
        # Update an organization
        api_response = api_instance.orgs_update(org, orgs_update_request=orgs_update_request)
        print("The response of OrgsApi->orgs_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **orgs_update_request** | [**OrgsUpdateRequest**](OrgsUpdateRequest.md)|  | [optional] 

### Return type

[**OrganizationFull**](OrganizationFull.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**422** | Validation failed |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_update_membership_for_authenticated_user**
> OrgMembership orgs_update_membership_for_authenticated_user(org, orgs_update_membership_for_authenticated_user_request)

Update an organization membership for the authenticated user

Converts the authenticated user to an active member of the organization, if that user has a pending invitation from the organization.

### Example


```python
import github_openapi
from github_openapi.models.org_membership import OrgMembership
from github_openapi.models.orgs_update_membership_for_authenticated_user_request import OrgsUpdateMembershipForAuthenticatedUserRequest
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    orgs_update_membership_for_authenticated_user_request = {"state":"active"} # OrgsUpdateMembershipForAuthenticatedUserRequest | 

    try:
        # Update an organization membership for the authenticated user
        api_response = api_instance.orgs_update_membership_for_authenticated_user(org, orgs_update_membership_for_authenticated_user_request)
        print("The response of OrgsApi->orgs_update_membership_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_update_membership_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **orgs_update_membership_for_authenticated_user_request** | [**OrgsUpdateMembershipForAuthenticatedUserRequest**](OrgsUpdateMembershipForAuthenticatedUserRequest.md)|  | 

### Return type

[**OrgMembership**](OrgMembership.md)

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

# **orgs_update_pat_access**
> orgs_update_pat_access(org, pat_id, orgs_update_pat_access_request)

Update the access a fine-grained personal access token has to organization resources

Updates the access an organization member has to organization resources via a fine-grained personal access token. Limited to revoking the token's existing access. Limited to revoking a token's existing access.  Only GitHub Apps can use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.orgs_update_pat_access_request import OrgsUpdatePatAccessRequest
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    pat_id = 56 # int | The unique identifier of the fine-grained personal access token.
    orgs_update_pat_access_request = {"action":"revoke"} # OrgsUpdatePatAccessRequest | 

    try:
        # Update the access a fine-grained personal access token has to organization resources
        api_instance.orgs_update_pat_access(org, pat_id, orgs_update_pat_access_request)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_update_pat_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **pat_id** | **int**| The unique identifier of the fine-grained personal access token. | 
 **orgs_update_pat_access_request** | [**OrgsUpdatePatAccessRequest**](OrgsUpdatePatAccessRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**500** | Internal Error |  -  |
**404** | Resource not found |  -  |
**204** | A header with no content is returned. |  -  |
**403** | Forbidden |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_update_pat_accesses**
> object orgs_update_pat_accesses(org, orgs_update_pat_accesses_request)

Update the access to organization resources via fine-grained personal access tokens

Updates the access organization members have to organization resources via fine-grained personal access tokens. Limited to revoking a token's existing access.  Only GitHub Apps can use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.orgs_update_pat_accesses_request import OrgsUpdatePatAccessesRequest
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    orgs_update_pat_accesses_request = {"action":"revoke","pat_ids":[1296269,1296280]} # OrgsUpdatePatAccessesRequest | 

    try:
        # Update the access to organization resources via fine-grained personal access tokens
        api_response = api_instance.orgs_update_pat_accesses(org, orgs_update_pat_accesses_request)
        print("The response of OrgsApi->orgs_update_pat_accesses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_update_pat_accesses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **orgs_update_pat_accesses_request** | [**OrgsUpdatePatAccessesRequest**](OrgsUpdatePatAccessesRequest.md)|  | 

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
**500** | Internal Error |  -  |
**404** | Resource not found |  -  |
**202** | Accepted |  -  |
**403** | Forbidden |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_update_webhook**
> OrgHook orgs_update_webhook(org, hook_id, orgs_update_webhook_request=orgs_update_webhook_request)

Update an organization webhook

Updates a webhook configured in an organization. When you update a webhook, the `secret` will be overwritten. If you previously had a `secret` set, you must provide the same `secret` or set a new `secret` or the secret will be removed. If you are only updating individual webhook `config` properties, use \"[Update a webhook configuration for an organization](/rest/orgs/webhooks#update-a-webhook-configuration-for-an-organization)\".  You must be an organization owner to use this endpoint.  OAuth app tokens and personal access tokens (classic) need `admin:org_hook` scope. OAuth apps cannot list, view, or edit webhooks that they did not create and users cannot list, view, or edit webhooks that were created by OAuth apps.

### Example


```python
import github_openapi
from github_openapi.models.org_hook import OrgHook
from github_openapi.models.orgs_update_webhook_request import OrgsUpdateWebhookRequest
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    hook_id = 56 # int | The unique identifier of the hook. You can find this value in the `X-GitHub-Hook-ID` header of a webhook delivery.
    orgs_update_webhook_request = {"active":true,"events":["pull_request"]} # OrgsUpdateWebhookRequest |  (optional)

    try:
        # Update an organization webhook
        api_response = api_instance.orgs_update_webhook(org, hook_id, orgs_update_webhook_request=orgs_update_webhook_request)
        print("The response of OrgsApi->orgs_update_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_update_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **hook_id** | **int**| The unique identifier of the hook. You can find this value in the &#x60;X-GitHub-Hook-ID&#x60; header of a webhook delivery. | 
 **orgs_update_webhook_request** | [**OrgsUpdateWebhookRequest**](OrgsUpdateWebhookRequest.md)|  | [optional] 

### Return type

[**OrgHook**](OrgHook.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orgs_update_webhook_config_for_org**
> WebhookConfig orgs_update_webhook_config_for_org(org, hook_id, apps_update_webhook_config_for_app_request=apps_update_webhook_config_for_app_request)

Update a webhook configuration for an organization

Updates the webhook configuration for an organization. To update more information about the webhook, including the `active` state and `events`, use \"[Update an organization webhook ](/rest/orgs/webhooks#update-an-organization-webhook).\"  You must be an organization owner to use this endpoint.  OAuth app tokens and personal access tokens (classic) need `admin:org_hook` scope. OAuth apps cannot list, view, or edit webhooks that they did not create and users cannot list, view, or edit webhooks that were created by OAuth apps.

### Example


```python
import github_openapi
from github_openapi.models.apps_update_webhook_config_for_app_request import AppsUpdateWebhookConfigForAppRequest
from github_openapi.models.webhook_config import WebhookConfig
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
    api_instance = github_openapi.OrgsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    hook_id = 56 # int | The unique identifier of the hook. You can find this value in the `X-GitHub-Hook-ID` header of a webhook delivery.
    apps_update_webhook_config_for_app_request = {"url":"http://example.com/webhook","content_type":"json","insecure_ssl":"0","secret":"********"} # AppsUpdateWebhookConfigForAppRequest |  (optional)

    try:
        # Update a webhook configuration for an organization
        api_response = api_instance.orgs_update_webhook_config_for_org(org, hook_id, apps_update_webhook_config_for_app_request=apps_update_webhook_config_for_app_request)
        print("The response of OrgsApi->orgs_update_webhook_config_for_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrgsApi->orgs_update_webhook_config_for_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **hook_id** | **int**| The unique identifier of the hook. You can find this value in the &#x60;X-GitHub-Hook-ID&#x60; header of a webhook delivery. | 
 **apps_update_webhook_config_for_app_request** | [**AppsUpdateWebhookConfigForAppRequest**](AppsUpdateWebhookConfigForAppRequest.md)|  | [optional] 

### Return type

[**WebhookConfig**](WebhookConfig.md)

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

