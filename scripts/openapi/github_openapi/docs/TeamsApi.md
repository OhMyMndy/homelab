# github_openapi.TeamsApi

All URIs are relative to *https://api.github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**teams_add_member_legacy**](TeamsApi.md#teams_add_member_legacy) | **PUT** /teams/{team_id}/members/{username} | Add team member (Legacy)
[**teams_add_or_update_membership_for_user_in_org**](TeamsApi.md#teams_add_or_update_membership_for_user_in_org) | **PUT** /orgs/{org}/teams/{team_slug}/memberships/{username} | Add or update team membership for a user
[**teams_add_or_update_membership_for_user_legacy**](TeamsApi.md#teams_add_or_update_membership_for_user_legacy) | **PUT** /teams/{team_id}/memberships/{username} | Add or update team membership for a user (Legacy)
[**teams_add_or_update_project_permissions_in_org**](TeamsApi.md#teams_add_or_update_project_permissions_in_org) | **PUT** /orgs/{org}/teams/{team_slug}/projects/{project_id} | Add or update team project permissions
[**teams_add_or_update_project_permissions_legacy**](TeamsApi.md#teams_add_or_update_project_permissions_legacy) | **PUT** /teams/{team_id}/projects/{project_id} | Add or update team project permissions (Legacy)
[**teams_add_or_update_repo_permissions_in_org**](TeamsApi.md#teams_add_or_update_repo_permissions_in_org) | **PUT** /orgs/{org}/teams/{team_slug}/repos/{owner}/{repo} | Add or update team repository permissions
[**teams_add_or_update_repo_permissions_legacy**](TeamsApi.md#teams_add_or_update_repo_permissions_legacy) | **PUT** /teams/{team_id}/repos/{owner}/{repo} | Add or update team repository permissions (Legacy)
[**teams_check_permissions_for_project_in_org**](TeamsApi.md#teams_check_permissions_for_project_in_org) | **GET** /orgs/{org}/teams/{team_slug}/projects/{project_id} | Check team permissions for a project
[**teams_check_permissions_for_project_legacy**](TeamsApi.md#teams_check_permissions_for_project_legacy) | **GET** /teams/{team_id}/projects/{project_id} | Check team permissions for a project (Legacy)
[**teams_check_permissions_for_repo_in_org**](TeamsApi.md#teams_check_permissions_for_repo_in_org) | **GET** /orgs/{org}/teams/{team_slug}/repos/{owner}/{repo} | Check team permissions for a repository
[**teams_check_permissions_for_repo_legacy**](TeamsApi.md#teams_check_permissions_for_repo_legacy) | **GET** /teams/{team_id}/repos/{owner}/{repo} | Check team permissions for a repository (Legacy)
[**teams_create**](TeamsApi.md#teams_create) | **POST** /orgs/{org}/teams | Create a team
[**teams_create_discussion_comment_in_org**](TeamsApi.md#teams_create_discussion_comment_in_org) | **POST** /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments | Create a discussion comment
[**teams_create_discussion_comment_legacy**](TeamsApi.md#teams_create_discussion_comment_legacy) | **POST** /teams/{team_id}/discussions/{discussion_number}/comments | Create a discussion comment (Legacy)
[**teams_create_discussion_in_org**](TeamsApi.md#teams_create_discussion_in_org) | **POST** /orgs/{org}/teams/{team_slug}/discussions | Create a discussion
[**teams_create_discussion_legacy**](TeamsApi.md#teams_create_discussion_legacy) | **POST** /teams/{team_id}/discussions | Create a discussion (Legacy)
[**teams_delete_discussion_comment_in_org**](TeamsApi.md#teams_delete_discussion_comment_in_org) | **DELETE** /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number} | Delete a discussion comment
[**teams_delete_discussion_comment_legacy**](TeamsApi.md#teams_delete_discussion_comment_legacy) | **DELETE** /teams/{team_id}/discussions/{discussion_number}/comments/{comment_number} | Delete a discussion comment (Legacy)
[**teams_delete_discussion_in_org**](TeamsApi.md#teams_delete_discussion_in_org) | **DELETE** /orgs/{org}/teams/{team_slug}/discussions/{discussion_number} | Delete a discussion
[**teams_delete_discussion_legacy**](TeamsApi.md#teams_delete_discussion_legacy) | **DELETE** /teams/{team_id}/discussions/{discussion_number} | Delete a discussion (Legacy)
[**teams_delete_in_org**](TeamsApi.md#teams_delete_in_org) | **DELETE** /orgs/{org}/teams/{team_slug} | Delete a team
[**teams_delete_legacy**](TeamsApi.md#teams_delete_legacy) | **DELETE** /teams/{team_id} | Delete a team (Legacy)
[**teams_get_by_name**](TeamsApi.md#teams_get_by_name) | **GET** /orgs/{org}/teams/{team_slug} | Get a team by name
[**teams_get_discussion_comment_in_org**](TeamsApi.md#teams_get_discussion_comment_in_org) | **GET** /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number} | Get a discussion comment
[**teams_get_discussion_comment_legacy**](TeamsApi.md#teams_get_discussion_comment_legacy) | **GET** /teams/{team_id}/discussions/{discussion_number}/comments/{comment_number} | Get a discussion comment (Legacy)
[**teams_get_discussion_in_org**](TeamsApi.md#teams_get_discussion_in_org) | **GET** /orgs/{org}/teams/{team_slug}/discussions/{discussion_number} | Get a discussion
[**teams_get_discussion_legacy**](TeamsApi.md#teams_get_discussion_legacy) | **GET** /teams/{team_id}/discussions/{discussion_number} | Get a discussion (Legacy)
[**teams_get_legacy**](TeamsApi.md#teams_get_legacy) | **GET** /teams/{team_id} | Get a team (Legacy)
[**teams_get_member_legacy**](TeamsApi.md#teams_get_member_legacy) | **GET** /teams/{team_id}/members/{username} | Get team member (Legacy)
[**teams_get_membership_for_user_in_org**](TeamsApi.md#teams_get_membership_for_user_in_org) | **GET** /orgs/{org}/teams/{team_slug}/memberships/{username} | Get team membership for a user
[**teams_get_membership_for_user_legacy**](TeamsApi.md#teams_get_membership_for_user_legacy) | **GET** /teams/{team_id}/memberships/{username} | Get team membership for a user (Legacy)
[**teams_list**](TeamsApi.md#teams_list) | **GET** /orgs/{org}/teams | List teams
[**teams_list_child_in_org**](TeamsApi.md#teams_list_child_in_org) | **GET** /orgs/{org}/teams/{team_slug}/teams | List child teams
[**teams_list_child_legacy**](TeamsApi.md#teams_list_child_legacy) | **GET** /teams/{team_id}/teams | List child teams (Legacy)
[**teams_list_discussion_comments_in_org**](TeamsApi.md#teams_list_discussion_comments_in_org) | **GET** /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments | List discussion comments
[**teams_list_discussion_comments_legacy**](TeamsApi.md#teams_list_discussion_comments_legacy) | **GET** /teams/{team_id}/discussions/{discussion_number}/comments | List discussion comments (Legacy)
[**teams_list_discussions_in_org**](TeamsApi.md#teams_list_discussions_in_org) | **GET** /orgs/{org}/teams/{team_slug}/discussions | List discussions
[**teams_list_discussions_legacy**](TeamsApi.md#teams_list_discussions_legacy) | **GET** /teams/{team_id}/discussions | List discussions (Legacy)
[**teams_list_for_authenticated_user**](TeamsApi.md#teams_list_for_authenticated_user) | **GET** /user/teams | List teams for the authenticated user
[**teams_list_members_in_org**](TeamsApi.md#teams_list_members_in_org) | **GET** /orgs/{org}/teams/{team_slug}/members | List team members
[**teams_list_members_legacy**](TeamsApi.md#teams_list_members_legacy) | **GET** /teams/{team_id}/members | List team members (Legacy)
[**teams_list_pending_invitations_in_org**](TeamsApi.md#teams_list_pending_invitations_in_org) | **GET** /orgs/{org}/teams/{team_slug}/invitations | List pending team invitations
[**teams_list_pending_invitations_legacy**](TeamsApi.md#teams_list_pending_invitations_legacy) | **GET** /teams/{team_id}/invitations | List pending team invitations (Legacy)
[**teams_list_projects_in_org**](TeamsApi.md#teams_list_projects_in_org) | **GET** /orgs/{org}/teams/{team_slug}/projects | List team projects
[**teams_list_projects_legacy**](TeamsApi.md#teams_list_projects_legacy) | **GET** /teams/{team_id}/projects | List team projects (Legacy)
[**teams_list_repos_in_org**](TeamsApi.md#teams_list_repos_in_org) | **GET** /orgs/{org}/teams/{team_slug}/repos | List team repositories
[**teams_list_repos_legacy**](TeamsApi.md#teams_list_repos_legacy) | **GET** /teams/{team_id}/repos | List team repositories (Legacy)
[**teams_remove_member_legacy**](TeamsApi.md#teams_remove_member_legacy) | **DELETE** /teams/{team_id}/members/{username} | Remove team member (Legacy)
[**teams_remove_membership_for_user_in_org**](TeamsApi.md#teams_remove_membership_for_user_in_org) | **DELETE** /orgs/{org}/teams/{team_slug}/memberships/{username} | Remove team membership for a user
[**teams_remove_membership_for_user_legacy**](TeamsApi.md#teams_remove_membership_for_user_legacy) | **DELETE** /teams/{team_id}/memberships/{username} | Remove team membership for a user (Legacy)
[**teams_remove_project_in_org**](TeamsApi.md#teams_remove_project_in_org) | **DELETE** /orgs/{org}/teams/{team_slug}/projects/{project_id} | Remove a project from a team
[**teams_remove_project_legacy**](TeamsApi.md#teams_remove_project_legacy) | **DELETE** /teams/{team_id}/projects/{project_id} | Remove a project from a team (Legacy)
[**teams_remove_repo_in_org**](TeamsApi.md#teams_remove_repo_in_org) | **DELETE** /orgs/{org}/teams/{team_slug}/repos/{owner}/{repo} | Remove a repository from a team
[**teams_remove_repo_legacy**](TeamsApi.md#teams_remove_repo_legacy) | **DELETE** /teams/{team_id}/repos/{owner}/{repo} | Remove a repository from a team (Legacy)
[**teams_update_discussion_comment_in_org**](TeamsApi.md#teams_update_discussion_comment_in_org) | **PATCH** /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number} | Update a discussion comment
[**teams_update_discussion_comment_legacy**](TeamsApi.md#teams_update_discussion_comment_legacy) | **PATCH** /teams/{team_id}/discussions/{discussion_number}/comments/{comment_number} | Update a discussion comment (Legacy)
[**teams_update_discussion_in_org**](TeamsApi.md#teams_update_discussion_in_org) | **PATCH** /orgs/{org}/teams/{team_slug}/discussions/{discussion_number} | Update a discussion
[**teams_update_discussion_legacy**](TeamsApi.md#teams_update_discussion_legacy) | **PATCH** /teams/{team_id}/discussions/{discussion_number} | Update a discussion (Legacy)
[**teams_update_in_org**](TeamsApi.md#teams_update_in_org) | **PATCH** /orgs/{org}/teams/{team_slug} | Update a team
[**teams_update_legacy**](TeamsApi.md#teams_update_legacy) | **PATCH** /teams/{team_id} | Update a team (Legacy)


# **teams_add_member_legacy**
> teams_add_member_legacy(team_id, username)

Add team member (Legacy)

The \"Add team member\" endpoint (described below) is closing down.  We recommend using the [Add or update team membership for a user](https://docs.github.com/rest/teams/members#add-or-update-team-membership-for-a-user) endpoint instead. It allows you to invite new organization members to your teams.  Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  To add someone to a team, the authenticated user must be an organization owner or a team maintainer in the team they're changing. The person being added to the team must be a member of the team's organization.  > [!NOTE] > When you have team synchronization set up for a team with your organization's identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team's membership. If you have access to manage group membership in your IdP, you can manage GitHub team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see \"[Synchronizing teams between your identity provider and GitHub](https://docs.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/).\"  Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see \"[HTTP method](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#http-method).\"

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
    api_instance = github_openapi.TeamsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Add team member (Legacy)
        api_instance.teams_add_member_legacy(team_id, username)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_add_member_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
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
**404** | Not Found if team synchronization is set up |  -  |
**422** | Unprocessable Entity if you attempt to add an organization to a team or you attempt to add a user to a team when they are not a member of at least one other team in the same organization |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_add_or_update_membership_for_user_in_org**
> TeamMembership teams_add_or_update_membership_for_user_in_org(org, team_slug, username, teams_add_or_update_membership_for_user_in_org_request=teams_add_or_update_membership_for_user_in_org_request)

Add or update team membership for a user

Adds an organization member to a team. An authenticated organization owner or team maintainer can add organization members to a team.  Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  > [!NOTE] > When you have team synchronization set up for a team with your organization's identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team's membership. If you have access to manage group membership in your IdP, you can manage GitHub team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see \"[Synchronizing teams between your identity provider and GitHub](https://docs.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/).\"  An organization owner can add someone who is not part of the team's organization to a team. When an organization owner adds someone to a team who is not an organization member, this endpoint will send an invitation to the person via email. This newly-created membership will be in the \"pending\" state until the person accepts the invitation, at which point the membership will transition to the \"active\" state and the user will be added as a member of the team.  If the user is already a member of the team, this endpoint will update the role of the team member's role. To update the membership of a team member, the authenticated user must be an organization owner or a team maintainer.  > [!NOTE] > You can also specify a team by `org_id` and `team_id` using the route `PUT /organizations/{org_id}/team/{team_id}/memberships/{username}`.

### Example


```python
import github_openapi
from github_openapi.models.team_membership import TeamMembership
from github_openapi.models.teams_add_or_update_membership_for_user_in_org_request import TeamsAddOrUpdateMembershipForUserInOrgRequest
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
    api_instance = github_openapi.TeamsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    username = 'username_example' # str | The handle for the GitHub user account.
    teams_add_or_update_membership_for_user_in_org_request = {"role":"maintainer"} # TeamsAddOrUpdateMembershipForUserInOrgRequest |  (optional)

    try:
        # Add or update team membership for a user
        api_response = api_instance.teams_add_or_update_membership_for_user_in_org(org, team_slug, username, teams_add_or_update_membership_for_user_in_org_request=teams_add_or_update_membership_for_user_in_org_request)
        print("The response of TeamsApi->teams_add_or_update_membership_for_user_in_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_add_or_update_membership_for_user_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
 **username** | **str**| The handle for the GitHub user account. | 
 **teams_add_or_update_membership_for_user_in_org_request** | [**TeamsAddOrUpdateMembershipForUserInOrgRequest**](TeamsAddOrUpdateMembershipForUserInOrgRequest.md)|  | [optional] 

### Return type

[**TeamMembership**](TeamMembership.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**403** | Forbidden if team synchronization is set up |  -  |
**422** | Unprocessable Entity if you attempt to add an organization to a team |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_add_or_update_membership_for_user_legacy**
> TeamMembership teams_add_or_update_membership_for_user_legacy(team_id, username, teams_add_or_update_membership_for_user_in_org_request=teams_add_or_update_membership_for_user_in_org_request)

Add or update team membership for a user (Legacy)

> [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the new [Add or update team membership for a user](https://docs.github.com/rest/teams/members#add-or-update-team-membership-for-a-user) endpoint.  Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  If the user is already a member of the team's organization, this endpoint will add the user to the team. To add a membership between an organization member and a team, the authenticated user must be an organization owner or a team maintainer.  > [!NOTE] > When you have team synchronization set up for a team with your organization's identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team's membership. If you have access to manage group membership in your IdP, you can manage GitHub team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see \"[Synchronizing teams between your identity provider and GitHub](https://docs.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/).\"  If the user is unaffiliated with the team's organization, this endpoint will send an invitation to the user via email. This newly-created membership will be in the \"pending\" state until the user accepts the invitation, at which point the membership will transition to the \"active\" state and the user will be added as a member of the team. To add a membership between an unaffiliated user and a team, the authenticated user must be an organization owner.  If the user is already a member of the team, this endpoint will update the role of the team member's role. To update the membership of a team member, the authenticated user must be an organization owner or a team maintainer.

### Example


```python
import github_openapi
from github_openapi.models.team_membership import TeamMembership
from github_openapi.models.teams_add_or_update_membership_for_user_in_org_request import TeamsAddOrUpdateMembershipForUserInOrgRequest
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
    api_instance = github_openapi.TeamsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    username = 'username_example' # str | The handle for the GitHub user account.
    teams_add_or_update_membership_for_user_in_org_request = {"role":"member"} # TeamsAddOrUpdateMembershipForUserInOrgRequest |  (optional)

    try:
        # Add or update team membership for a user (Legacy)
        api_response = api_instance.teams_add_or_update_membership_for_user_legacy(team_id, username, teams_add_or_update_membership_for_user_in_org_request=teams_add_or_update_membership_for_user_in_org_request)
        print("The response of TeamsApi->teams_add_or_update_membership_for_user_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_add_or_update_membership_for_user_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
 **username** | **str**| The handle for the GitHub user account. | 
 **teams_add_or_update_membership_for_user_in_org_request** | [**TeamsAddOrUpdateMembershipForUserInOrgRequest**](TeamsAddOrUpdateMembershipForUserInOrgRequest.md)|  | [optional] 

### Return type

[**TeamMembership**](TeamMembership.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**403** | Forbidden if team synchronization is set up |  -  |
**422** | Unprocessable Entity if you attempt to add an organization to a team |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_add_or_update_project_permissions_in_org**
> teams_add_or_update_project_permissions_in_org(org, team_slug, project_id, teams_add_or_update_project_permissions_in_org_request=teams_add_or_update_project_permissions_in_org_request)

Add or update team project permissions

Adds an organization project to a team. To add a project to a team or update the team's permission on a project, the authenticated user must have `admin` permissions for the project. The project and team must be part of the same organization.  > [!NOTE] > You can also specify a team by `org_id` and `team_id` using the route `PUT /organizations/{org_id}/team/{team_id}/projects/{project_id}`.

### Example


```python
import github_openapi
from github_openapi.models.teams_add_or_update_project_permissions_in_org_request import TeamsAddOrUpdateProjectPermissionsInOrgRequest
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
    api_instance = github_openapi.TeamsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    project_id = 56 # int | The unique identifier of the project.
    teams_add_or_update_project_permissions_in_org_request = {"permission":"write"} # TeamsAddOrUpdateProjectPermissionsInOrgRequest |  (optional)

    try:
        # Add or update team project permissions
        api_instance.teams_add_or_update_project_permissions_in_org(org, team_slug, project_id, teams_add_or_update_project_permissions_in_org_request=teams_add_or_update_project_permissions_in_org_request)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_add_or_update_project_permissions_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
 **project_id** | **int**| The unique identifier of the project. | 
 **teams_add_or_update_project_permissions_in_org_request** | [**TeamsAddOrUpdateProjectPermissionsInOrgRequest**](TeamsAddOrUpdateProjectPermissionsInOrgRequest.md)|  | [optional] 

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
**204** | Response |  -  |
**403** | Forbidden if the project is not owned by the organization |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_add_or_update_project_permissions_legacy**
> teams_add_or_update_project_permissions_legacy(team_id, project_id, teams_add_or_update_project_permissions_legacy_request=teams_add_or_update_project_permissions_legacy_request)

Add or update team project permissions (Legacy)

> [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the new [Add or update team project permissions](https://docs.github.com/rest/teams/teams#add-or-update-team-project-permissions) endpoint.  Adds an organization project to a team. To add a project to a team or update the team's permission on a project, the authenticated user must have `admin` permissions for the project. The project and team must be part of the same organization.

### Example


```python
import github_openapi
from github_openapi.models.teams_add_or_update_project_permissions_legacy_request import TeamsAddOrUpdateProjectPermissionsLegacyRequest
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
    api_instance = github_openapi.TeamsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    project_id = 56 # int | The unique identifier of the project.
    teams_add_or_update_project_permissions_legacy_request = {"permission":"read"} # TeamsAddOrUpdateProjectPermissionsLegacyRequest |  (optional)

    try:
        # Add or update team project permissions (Legacy)
        api_instance.teams_add_or_update_project_permissions_legacy(team_id, project_id, teams_add_or_update_project_permissions_legacy_request=teams_add_or_update_project_permissions_legacy_request)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_add_or_update_project_permissions_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
 **project_id** | **int**| The unique identifier of the project. | 
 **teams_add_or_update_project_permissions_legacy_request** | [**TeamsAddOrUpdateProjectPermissionsLegacyRequest**](TeamsAddOrUpdateProjectPermissionsLegacyRequest.md)|  | [optional] 

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
**204** | Response |  -  |
**403** | Forbidden if the project is not owned by the organization |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_add_or_update_repo_permissions_in_org**
> teams_add_or_update_repo_permissions_in_org(org, team_slug, owner, repo, teams_add_or_update_repo_permissions_in_org_request=teams_add_or_update_repo_permissions_in_org_request)

Add or update team repository permissions

To add a repository to a team or update the team's permission on a repository, the authenticated user must have admin access to the repository, and must be able to see the team. The repository must be owned by the organization, or a direct fork of a repository owned by the organization. You will get a `422 Unprocessable Entity` status if you attempt to add a repository to a team that is not owned by the organization. Note that, if you choose not to pass any parameters, you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see \"[HTTP method](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#http-method).\"  > [!NOTE] > You can also specify a team by `org_id` and `team_id` using the route `PUT /organizations/{org_id}/team/{team_id}/repos/{owner}/{repo}`.  For more information about the permission levels, see \"[Repository permission levels for an organization](https://docs.github.com/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization#permission-levels-for-repositories-owned-by-an-organization)\".

### Example


```python
import github_openapi
from github_openapi.models.teams_add_or_update_repo_permissions_in_org_request import TeamsAddOrUpdateRepoPermissionsInOrgRequest
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
    api_instance = github_openapi.TeamsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    teams_add_or_update_repo_permissions_in_org_request = {"permission":"push"} # TeamsAddOrUpdateRepoPermissionsInOrgRequest |  (optional)

    try:
        # Add or update team repository permissions
        api_instance.teams_add_or_update_repo_permissions_in_org(org, team_slug, owner, repo, teams_add_or_update_repo_permissions_in_org_request=teams_add_or_update_repo_permissions_in_org_request)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_add_or_update_repo_permissions_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **teams_add_or_update_repo_permissions_in_org_request** | [**TeamsAddOrUpdateRepoPermissionsInOrgRequest**](TeamsAddOrUpdateRepoPermissionsInOrgRequest.md)|  | [optional] 

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
**204** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_add_or_update_repo_permissions_legacy**
> teams_add_or_update_repo_permissions_legacy(team_id, owner, repo, teams_add_or_update_repo_permissions_legacy_request=teams_add_or_update_repo_permissions_legacy_request)

Add or update team repository permissions (Legacy)

> [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the new \"[Add or update team repository permissions](https://docs.github.com/rest/teams/teams#add-or-update-team-repository-permissions)\" endpoint.  To add a repository to a team or update the team's permission on a repository, the authenticated user must have admin access to the repository, and must be able to see the team. The repository must be owned by the organization, or a direct fork of a repository owned by the organization. You will get a `422 Unprocessable Entity` status if you attempt to add a repository to a team that is not owned by the organization.  Note that, if you choose not to pass any parameters, you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see \"[HTTP method](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#http-method).\"

### Example


```python
import github_openapi
from github_openapi.models.teams_add_or_update_repo_permissions_legacy_request import TeamsAddOrUpdateRepoPermissionsLegacyRequest
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
    api_instance = github_openapi.TeamsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    teams_add_or_update_repo_permissions_legacy_request = {"permission":"push"} # TeamsAddOrUpdateRepoPermissionsLegacyRequest |  (optional)

    try:
        # Add or update team repository permissions (Legacy)
        api_instance.teams_add_or_update_repo_permissions_legacy(team_id, owner, repo, teams_add_or_update_repo_permissions_legacy_request=teams_add_or_update_repo_permissions_legacy_request)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_add_or_update_repo_permissions_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **teams_add_or_update_repo_permissions_legacy_request** | [**TeamsAddOrUpdateRepoPermissionsLegacyRequest**](TeamsAddOrUpdateRepoPermissionsLegacyRequest.md)|  | [optional] 

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
**204** | Response |  -  |
**403** | Forbidden |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_check_permissions_for_project_in_org**
> TeamProject teams_check_permissions_for_project_in_org(org, team_slug, project_id)

Check team permissions for a project

Checks whether a team has `read`, `write`, or `admin` permissions for an organization project. The response includes projects inherited from a parent team.  > [!NOTE] > You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/projects/{project_id}`.

### Example


```python
import github_openapi
from github_openapi.models.team_project import TeamProject
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
    api_instance = github_openapi.TeamsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    project_id = 56 # int | The unique identifier of the project.

    try:
        # Check team permissions for a project
        api_response = api_instance.teams_check_permissions_for_project_in_org(org, team_slug, project_id)
        print("The response of TeamsApi->teams_check_permissions_for_project_in_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_check_permissions_for_project_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
 **project_id** | **int**| The unique identifier of the project. | 

### Return type

[**TeamProject**](TeamProject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Not Found if project is not managed by this team |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_check_permissions_for_project_legacy**
> TeamProject teams_check_permissions_for_project_legacy(team_id, project_id)

Check team permissions for a project (Legacy)

> [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the new [Check team permissions for a project](https://docs.github.com/rest/teams/teams#check-team-permissions-for-a-project) endpoint.  Checks whether a team has `read`, `write`, or `admin` permissions for an organization project. The response includes projects inherited from a parent team.

### Example


```python
import github_openapi
from github_openapi.models.team_project import TeamProject
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
    api_instance = github_openapi.TeamsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    project_id = 56 # int | The unique identifier of the project.

    try:
        # Check team permissions for a project (Legacy)
        api_response = api_instance.teams_check_permissions_for_project_legacy(team_id, project_id)
        print("The response of TeamsApi->teams_check_permissions_for_project_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_check_permissions_for_project_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
 **project_id** | **int**| The unique identifier of the project. | 

### Return type

[**TeamProject**](TeamProject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | Not Found if project is not managed by this team |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_check_permissions_for_repo_in_org**
> TeamRepository teams_check_permissions_for_repo_in_org(org, team_slug, owner, repo)

Check team permissions for a repository

Checks whether a team has `admin`, `push`, `maintain`, `triage`, or `pull` permission for a repository. Repositories inherited through a parent team will also be checked.  You can also get information about the specified repository, including what permissions the team grants on it, by passing the following custom [media type](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types/) via the `application/vnd.github.v3.repository+json` accept header.  If a team doesn't have permission for the repository, you will receive a `404 Not Found` response status.  If the repository is private, you must have at least `read` permission for that repository, and your token must have the `repo` or `admin:org` scope. Otherwise, you will receive a `404 Not Found` response status.  > [!NOTE] > You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/repos/{owner}/{repo}`.

### Example


```python
import github_openapi
from github_openapi.models.team_repository import TeamRepository
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
    api_instance = github_openapi.TeamsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Check team permissions for a repository
        api_response = api_instance.teams_check_permissions_for_repo_in_org(org, team_slug, owner, repo)
        print("The response of TeamsApi->teams_check_permissions_for_repo_in_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_check_permissions_for_repo_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**TeamRepository**](TeamRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Alternative response with repository permissions |  -  |
**204** | Response if team has permission for the repository. This is the response when the repository media type hasn&#39;t been provded in the Accept header. |  -  |
**404** | Not Found if team does not have permission for the repository |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_check_permissions_for_repo_legacy**
> TeamRepository teams_check_permissions_for_repo_legacy(team_id, owner, repo)

Check team permissions for a repository (Legacy)

> [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the new [Check team permissions for a repository](https://docs.github.com/rest/teams/teams#check-team-permissions-for-a-repository) endpoint.  > [!NOTE] > Repositories inherited through a parent team will also be checked.  You can also get information about the specified repository, including what permissions the team grants on it, by passing the following custom [media type](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types/) via the `Accept` header:

### Example


```python
import github_openapi
from github_openapi.models.team_repository import TeamRepository
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
    api_instance = github_openapi.TeamsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Check team permissions for a repository (Legacy)
        api_response = api_instance.teams_check_permissions_for_repo_legacy(team_id, owner, repo)
        print("The response of TeamsApi->teams_check_permissions_for_repo_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_check_permissions_for_repo_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 

### Return type

[**TeamRepository**](TeamRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Alternative response with extra repository information |  -  |
**204** | Response if repository is managed by this team |  -  |
**404** | Not Found if repository is not managed by this team |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_create**
> TeamFull teams_create(org, teams_create_request)

Create a team

To create a team, the authenticated user must be a member or owner of `{org}`. By default, organization members can create teams. Organization owners can limit team creation to organization owners. For more information, see \"[Setting team creation permissions](https://docs.github.com/articles/setting-team-creation-permissions-in-your-organization).\"  When you create a new team, you automatically become a team maintainer without explicitly adding yourself to the optional array of `maintainers`. For more information, see \"[About teams](https://docs.github.com/github/setting-up-and-managing-organizations-and-teams/about-teams)\".

### Example


```python
import github_openapi
from github_openapi.models.team_full import TeamFull
from github_openapi.models.teams_create_request import TeamsCreateRequest
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
    api_instance = github_openapi.TeamsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    teams_create_request = {"name":"Justice League","description":"A great team","permission":"push","notification_setting":"notifications_enabled","privacy":"closed"} # TeamsCreateRequest | 

    try:
        # Create a team
        api_response = api_instance.teams_create(org, teams_create_request)
        print("The response of TeamsApi->teams_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **teams_create_request** | [**TeamsCreateRequest**](TeamsCreateRequest.md)|  | 

### Return type

[**TeamFull**](TeamFull.md)

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_create_discussion_comment_in_org**
> TeamDiscussionComment teams_create_discussion_comment_in_org(org, team_slug, discussion_number, teams_create_discussion_comment_in_org_request)

Create a discussion comment

Creates a new comment on a team discussion.  This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. For more information, see \"[Rate limits for the API](https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits)\" and \"[Best practices for using the REST API](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api).\"  > [!NOTE] > You can also specify a team by `org_id` and `team_id` using the route `POST /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}/comments`.  OAuth app tokens and personal access tokens (classic) need the `write:discussion` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.team_discussion_comment import TeamDiscussionComment
from github_openapi.models.teams_create_discussion_comment_in_org_request import TeamsCreateDiscussionCommentInOrgRequest
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
    api_instance = github_openapi.TeamsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    discussion_number = 56 # int | The number that identifies the discussion.
    teams_create_discussion_comment_in_org_request = {"body":"Do you like apples?"} # TeamsCreateDiscussionCommentInOrgRequest | 

    try:
        # Create a discussion comment
        api_response = api_instance.teams_create_discussion_comment_in_org(org, team_slug, discussion_number, teams_create_discussion_comment_in_org_request)
        print("The response of TeamsApi->teams_create_discussion_comment_in_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_create_discussion_comment_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
 **discussion_number** | **int**| The number that identifies the discussion. | 
 **teams_create_discussion_comment_in_org_request** | [**TeamsCreateDiscussionCommentInOrgRequest**](TeamsCreateDiscussionCommentInOrgRequest.md)|  | 

### Return type

[**TeamDiscussionComment**](TeamDiscussionComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_create_discussion_comment_legacy**
> TeamDiscussionComment teams_create_discussion_comment_legacy(team_id, discussion_number, teams_create_discussion_comment_in_org_request)

Create a discussion comment (Legacy)

> [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the new [Create a discussion comment](https://docs.github.com/rest/teams/discussion-comments#create-a-discussion-comment) endpoint.  Creates a new comment on a team discussion.  This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. For more information, see \"[Rate limits for the API](https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits)\" and \"[Best practices for using the REST API](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api).\"  OAuth app tokens and personal access tokens (classic) need the `write:discussion` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.team_discussion_comment import TeamDiscussionComment
from github_openapi.models.teams_create_discussion_comment_in_org_request import TeamsCreateDiscussionCommentInOrgRequest
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
    api_instance = github_openapi.TeamsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    discussion_number = 56 # int | The number that identifies the discussion.
    teams_create_discussion_comment_in_org_request = {"body":"Do you like apples?"} # TeamsCreateDiscussionCommentInOrgRequest | 

    try:
        # Create a discussion comment (Legacy)
        api_response = api_instance.teams_create_discussion_comment_legacy(team_id, discussion_number, teams_create_discussion_comment_in_org_request)
        print("The response of TeamsApi->teams_create_discussion_comment_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_create_discussion_comment_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
 **discussion_number** | **int**| The number that identifies the discussion. | 
 **teams_create_discussion_comment_in_org_request** | [**TeamsCreateDiscussionCommentInOrgRequest**](TeamsCreateDiscussionCommentInOrgRequest.md)|  | 

### Return type

[**TeamDiscussionComment**](TeamDiscussionComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_create_discussion_in_org**
> TeamDiscussion teams_create_discussion_in_org(org, team_slug, teams_create_discussion_in_org_request)

Create a discussion

Creates a new discussion post on a team's page.  This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. For more information, see \"[Rate limits for the API](https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits)\" and \"[Best practices for using the REST API](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api).\"  > [!NOTE] > You can also specify a team by `org_id` and `team_id` using the route `POST /organizations/{org_id}/team/{team_id}/discussions`.  OAuth app tokens and personal access tokens (classic) need the `write:discussion` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.team_discussion import TeamDiscussion
from github_openapi.models.teams_create_discussion_in_org_request import TeamsCreateDiscussionInOrgRequest
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
    api_instance = github_openapi.TeamsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    teams_create_discussion_in_org_request = {"title":"Our first team post","body":"Hi! This is an area for us to collaborate as a team."} # TeamsCreateDiscussionInOrgRequest | 

    try:
        # Create a discussion
        api_response = api_instance.teams_create_discussion_in_org(org, team_slug, teams_create_discussion_in_org_request)
        print("The response of TeamsApi->teams_create_discussion_in_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_create_discussion_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
 **teams_create_discussion_in_org_request** | [**TeamsCreateDiscussionInOrgRequest**](TeamsCreateDiscussionInOrgRequest.md)|  | 

### Return type

[**TeamDiscussion**](TeamDiscussion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_create_discussion_legacy**
> TeamDiscussion teams_create_discussion_legacy(team_id, teams_create_discussion_in_org_request)

Create a discussion (Legacy)

> [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the new [`Create a discussion`](https://docs.github.com/rest/teams/discussions#create-a-discussion) endpoint.  Creates a new discussion post on a team's page.  This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. For more information, see \"[Rate limits for the API](https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits)\" and \"[Best practices for using the REST API](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api).\"  OAuth app tokens and personal access tokens (classic) need the `write:discussion` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.team_discussion import TeamDiscussion
from github_openapi.models.teams_create_discussion_in_org_request import TeamsCreateDiscussionInOrgRequest
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
    api_instance = github_openapi.TeamsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    teams_create_discussion_in_org_request = {"title":"Our first team post","body":"Hi! This is an area for us to collaborate as a team."} # TeamsCreateDiscussionInOrgRequest | 

    try:
        # Create a discussion (Legacy)
        api_response = api_instance.teams_create_discussion_legacy(team_id, teams_create_discussion_in_org_request)
        print("The response of TeamsApi->teams_create_discussion_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_create_discussion_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
 **teams_create_discussion_in_org_request** | [**TeamsCreateDiscussionInOrgRequest**](TeamsCreateDiscussionInOrgRequest.md)|  | 

### Return type

[**TeamDiscussion**](TeamDiscussion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_delete_discussion_comment_in_org**
> teams_delete_discussion_comment_in_org(org, team_slug, discussion_number, comment_number)

Delete a discussion comment

Deletes a comment on a team discussion.  > [!NOTE] > You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}/comments/{comment_number}`.  OAuth app tokens and personal access tokens (classic) need the `write:discussion` scope to use this endpoint.

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
    api_instance = github_openapi.TeamsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    discussion_number = 56 # int | The number that identifies the discussion.
    comment_number = 56 # int | The number that identifies the comment.

    try:
        # Delete a discussion comment
        api_instance.teams_delete_discussion_comment_in_org(org, team_slug, discussion_number, comment_number)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_delete_discussion_comment_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
 **discussion_number** | **int**| The number that identifies the discussion. | 
 **comment_number** | **int**| The number that identifies the comment. | 

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

# **teams_delete_discussion_comment_legacy**
> teams_delete_discussion_comment_legacy(team_id, discussion_number, comment_number)

Delete a discussion comment (Legacy)

> [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the new [Delete a discussion comment](https://docs.github.com/rest/teams/discussion-comments#delete-a-discussion-comment) endpoint.  Deletes a comment on a team discussion.  OAuth app tokens and personal access tokens (classic) need the `write:discussion` scope to use this endpoint.

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
    api_instance = github_openapi.TeamsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    discussion_number = 56 # int | The number that identifies the discussion.
    comment_number = 56 # int | The number that identifies the comment.

    try:
        # Delete a discussion comment (Legacy)
        api_instance.teams_delete_discussion_comment_legacy(team_id, discussion_number, comment_number)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_delete_discussion_comment_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
 **discussion_number** | **int**| The number that identifies the discussion. | 
 **comment_number** | **int**| The number that identifies the comment. | 

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

# **teams_delete_discussion_in_org**
> teams_delete_discussion_in_org(org, team_slug, discussion_number)

Delete a discussion

Delete a discussion from a team's page.  > [!NOTE] > You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}`.  OAuth app tokens and personal access tokens (classic) need the `write:discussion` scope to use this endpoint.

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
    api_instance = github_openapi.TeamsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    discussion_number = 56 # int | The number that identifies the discussion.

    try:
        # Delete a discussion
        api_instance.teams_delete_discussion_in_org(org, team_slug, discussion_number)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_delete_discussion_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
 **discussion_number** | **int**| The number that identifies the discussion. | 

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

# **teams_delete_discussion_legacy**
> teams_delete_discussion_legacy(team_id, discussion_number)

Delete a discussion (Legacy)

> [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the new [`Delete a discussion`](https://docs.github.com/rest/teams/discussions#delete-a-discussion) endpoint.  Delete a discussion from a team's page.  OAuth app tokens and personal access tokens (classic) need the `write:discussion` scope to use this endpoint.

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
    api_instance = github_openapi.TeamsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    discussion_number = 56 # int | The number that identifies the discussion.

    try:
        # Delete a discussion (Legacy)
        api_instance.teams_delete_discussion_legacy(team_id, discussion_number)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_delete_discussion_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
 **discussion_number** | **int**| The number that identifies the discussion. | 

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

# **teams_delete_in_org**
> teams_delete_in_org(org, team_slug)

Delete a team

To delete a team, the authenticated user must be an organization owner or team maintainer.  If you are an organization owner, deleting a parent team will delete all of its child teams as well.  > [!NOTE] > You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/{org_id}/team/{team_id}`.

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
    api_instance = github_openapi.TeamsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.

    try:
        # Delete a team
        api_instance.teams_delete_in_org(org, team_slug)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_delete_in_org: %s\n" % e)
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

# **teams_delete_legacy**
> teams_delete_legacy(team_id)

Delete a team (Legacy)

> [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the new [Delete a team](https://docs.github.com/rest/teams/teams#delete-a-team) endpoint.  To delete a team, the authenticated user must be an organization owner or team maintainer.  If you are an organization owner, deleting a parent team will delete all of its child teams as well.

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
    api_instance = github_openapi.TeamsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.

    try:
        # Delete a team (Legacy)
        api_instance.teams_delete_legacy(team_id)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_delete_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 

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
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_get_by_name**
> TeamFull teams_get_by_name(org, team_slug)

Get a team by name

Gets a team using the team's `slug`. To create the `slug`, GitHub replaces special characters in the `name` string, changes all words to lowercase, and replaces spaces with a `-` separator. For example, `\"My TEam Näme\"` would become `my-team-name`.  > [!NOTE] > You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}`.

### Example


```python
import github_openapi
from github_openapi.models.team_full import TeamFull
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
    api_instance = github_openapi.TeamsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.

    try:
        # Get a team by name
        api_response = api_instance.teams_get_by_name(org, team_slug)
        print("The response of TeamsApi->teams_get_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_get_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 

### Return type

[**TeamFull**](TeamFull.md)

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

# **teams_get_discussion_comment_in_org**
> TeamDiscussionComment teams_get_discussion_comment_in_org(org, team_slug, discussion_number, comment_number)

Get a discussion comment

Get a specific comment on a team discussion.  > [!NOTE] > You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}/comments/{comment_number}`.  OAuth app tokens and personal access tokens (classic) need the `read:discussion` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.team_discussion_comment import TeamDiscussionComment
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
    api_instance = github_openapi.TeamsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    discussion_number = 56 # int | The number that identifies the discussion.
    comment_number = 56 # int | The number that identifies the comment.

    try:
        # Get a discussion comment
        api_response = api_instance.teams_get_discussion_comment_in_org(org, team_slug, discussion_number, comment_number)
        print("The response of TeamsApi->teams_get_discussion_comment_in_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_get_discussion_comment_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
 **discussion_number** | **int**| The number that identifies the discussion. | 
 **comment_number** | **int**| The number that identifies the comment. | 

### Return type

[**TeamDiscussionComment**](TeamDiscussionComment.md)

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

# **teams_get_discussion_comment_legacy**
> TeamDiscussionComment teams_get_discussion_comment_legacy(team_id, discussion_number, comment_number)

Get a discussion comment (Legacy)

> [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the new [Get a discussion comment](https://docs.github.com/rest/teams/discussion-comments#get-a-discussion-comment) endpoint.  Get a specific comment on a team discussion.  OAuth app tokens and personal access tokens (classic) need the `read:discussion` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.team_discussion_comment import TeamDiscussionComment
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
    api_instance = github_openapi.TeamsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    discussion_number = 56 # int | The number that identifies the discussion.
    comment_number = 56 # int | The number that identifies the comment.

    try:
        # Get a discussion comment (Legacy)
        api_response = api_instance.teams_get_discussion_comment_legacy(team_id, discussion_number, comment_number)
        print("The response of TeamsApi->teams_get_discussion_comment_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_get_discussion_comment_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
 **discussion_number** | **int**| The number that identifies the discussion. | 
 **comment_number** | **int**| The number that identifies the comment. | 

### Return type

[**TeamDiscussionComment**](TeamDiscussionComment.md)

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

# **teams_get_discussion_in_org**
> TeamDiscussion teams_get_discussion_in_org(org, team_slug, discussion_number)

Get a discussion

Get a specific discussion on a team's page.  > [!NOTE] > You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}`.  OAuth app tokens and personal access tokens (classic) need the `read:discussion` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.team_discussion import TeamDiscussion
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
    api_instance = github_openapi.TeamsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    discussion_number = 56 # int | The number that identifies the discussion.

    try:
        # Get a discussion
        api_response = api_instance.teams_get_discussion_in_org(org, team_slug, discussion_number)
        print("The response of TeamsApi->teams_get_discussion_in_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_get_discussion_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
 **discussion_number** | **int**| The number that identifies the discussion. | 

### Return type

[**TeamDiscussion**](TeamDiscussion.md)

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

# **teams_get_discussion_legacy**
> TeamDiscussion teams_get_discussion_legacy(team_id, discussion_number)

Get a discussion (Legacy)

> [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the new [Get a discussion](https://docs.github.com/rest/teams/discussions#get-a-discussion) endpoint.  Get a specific discussion on a team's page.  OAuth app tokens and personal access tokens (classic) need the `read:discussion` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.team_discussion import TeamDiscussion
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
    api_instance = github_openapi.TeamsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    discussion_number = 56 # int | The number that identifies the discussion.

    try:
        # Get a discussion (Legacy)
        api_response = api_instance.teams_get_discussion_legacy(team_id, discussion_number)
        print("The response of TeamsApi->teams_get_discussion_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_get_discussion_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
 **discussion_number** | **int**| The number that identifies the discussion. | 

### Return type

[**TeamDiscussion**](TeamDiscussion.md)

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

# **teams_get_legacy**
> TeamFull teams_get_legacy(team_id)

Get a team (Legacy)

> [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the [Get a team by name](https://docs.github.com/rest/teams/teams#get-a-team-by-name) endpoint.

### Example


```python
import github_openapi
from github_openapi.models.team_full import TeamFull
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
    api_instance = github_openapi.TeamsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.

    try:
        # Get a team (Legacy)
        api_response = api_instance.teams_get_legacy(team_id)
        print("The response of TeamsApi->teams_get_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_get_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 

### Return type

[**TeamFull**](TeamFull.md)

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

# **teams_get_member_legacy**
> teams_get_member_legacy(team_id, username)

Get team member (Legacy)

The \"Get team member\" endpoint (described below) is closing down.  We recommend using the [Get team membership for a user](https://docs.github.com/rest/teams/members#get-team-membership-for-a-user) endpoint instead. It allows you to get both active and pending memberships.  To list members in a team, the team must be visible to the authenticated user.

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
    api_instance = github_openapi.TeamsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Get team member (Legacy)
        api_instance.teams_get_member_legacy(team_id, username)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_get_member_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
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
**204** | if user is a member |  -  |
**404** | if user is not a member |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_get_membership_for_user_in_org**
> TeamMembership teams_get_membership_for_user_in_org(org, team_slug, username)

Get team membership for a user

Team members will include the members of child teams.  To get a user's membership with a team, the team must be visible to the authenticated user.  > [!NOTE] > You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/memberships/{username}`.  > [!NOTE] > The response contains the `state` of the membership and the member's `role`.  The `role` for organization owners is set to `maintainer`. For more information about `maintainer` roles, see [Create a team](https://docs.github.com/rest/teams/teams#create-a-team).

### Example


```python
import github_openapi
from github_openapi.models.team_membership import TeamMembership
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
    api_instance = github_openapi.TeamsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Get team membership for a user
        api_response = api_instance.teams_get_membership_for_user_in_org(org, team_slug, username)
        print("The response of TeamsApi->teams_get_membership_for_user_in_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_get_membership_for_user_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
 **username** | **str**| The handle for the GitHub user account. | 

### Return type

[**TeamMembership**](TeamMembership.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**404** | if user has no team membership |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_get_membership_for_user_legacy**
> TeamMembership teams_get_membership_for_user_legacy(team_id, username)

Get team membership for a user (Legacy)

> [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the new [Get team membership for a user](https://docs.github.com/rest/teams/members#get-team-membership-for-a-user) endpoint.  Team members will include the members of child teams.  To get a user's membership with a team, the team must be visible to the authenticated user.  **Note:** The response contains the `state` of the membership and the member's `role`.  The `role` for organization owners is set to `maintainer`. For more information about `maintainer` roles, see [Create a team](https://docs.github.com/rest/teams/teams#create-a-team).

### Example


```python
import github_openapi
from github_openapi.models.team_membership import TeamMembership
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
    api_instance = github_openapi.TeamsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Get team membership for a user (Legacy)
        api_response = api_instance.teams_get_membership_for_user_legacy(team_id, username)
        print("The response of TeamsApi->teams_get_membership_for_user_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_get_membership_for_user_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
 **username** | **str**| The handle for the GitHub user account. | 

### Return type

[**TeamMembership**](TeamMembership.md)

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

# **teams_list**
> List[Team] teams_list(org, per_page=per_page, page=page)

List teams

Lists all teams in an organization that are visible to the authenticated user.

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
    api_instance = github_openapi.TeamsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List teams
        api_response = api_instance.teams_list(org, per_page=per_page, page=page)
        print("The response of TeamsApi->teams_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_list_child_in_org**
> List[Team] teams_list_child_in_org(org, team_slug, per_page=per_page, page=page)

List child teams

Lists the child teams of the team specified by `{team_slug}`.  > [!NOTE] > You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/teams`.

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
    api_instance = github_openapi.TeamsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List child teams
        api_response = api_instance.teams_list_child_in_org(org, team_slug, per_page=per_page, page=page)
        print("The response of TeamsApi->teams_list_child_in_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_list_child_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
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
**200** | if child teams exist |  * Link -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_list_child_legacy**
> List[Team] teams_list_child_legacy(team_id, per_page=per_page, page=page)

List child teams (Legacy)

> [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List child teams`](https://docs.github.com/rest/teams/teams#list-child-teams) endpoint.

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
    api_instance = github_openapi.TeamsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List child teams (Legacy)
        api_response = api_instance.teams_list_child_legacy(team_id, per_page=per_page, page=page)
        print("The response of TeamsApi->teams_list_child_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_list_child_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
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
**200** | if child teams exist |  * Link -  <br>  |
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_list_discussion_comments_in_org**
> List[TeamDiscussionComment] teams_list_discussion_comments_in_org(org, team_slug, discussion_number, direction=direction, per_page=per_page, page=page)

List discussion comments

List all comments on a team discussion.  > [!NOTE] > You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}/comments`.  OAuth app tokens and personal access tokens (classic) need the `read:discussion` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.team_discussion_comment import TeamDiscussionComment
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
    api_instance = github_openapi.TeamsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    discussion_number = 56 # int | The number that identifies the discussion.
    direction = desc # str | The direction to sort the results by. (optional) (default to desc)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List discussion comments
        api_response = api_instance.teams_list_discussion_comments_in_org(org, team_slug, discussion_number, direction=direction, per_page=per_page, page=page)
        print("The response of TeamsApi->teams_list_discussion_comments_in_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_list_discussion_comments_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
 **discussion_number** | **int**| The number that identifies the discussion. | 
 **direction** | **str**| The direction to sort the results by. | [optional] [default to desc]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[TeamDiscussionComment]**](TeamDiscussionComment.md)

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

# **teams_list_discussion_comments_legacy**
> List[TeamDiscussionComment] teams_list_discussion_comments_legacy(team_id, discussion_number, direction=direction, per_page=per_page, page=page)

List discussion comments (Legacy)

> [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the new [List discussion comments](https://docs.github.com/rest/teams/discussion-comments#list-discussion-comments) endpoint.  List all comments on a team discussion.  OAuth app tokens and personal access tokens (classic) need the `read:discussion` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.team_discussion_comment import TeamDiscussionComment
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
    api_instance = github_openapi.TeamsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    discussion_number = 56 # int | The number that identifies the discussion.
    direction = desc # str | The direction to sort the results by. (optional) (default to desc)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List discussion comments (Legacy)
        api_response = api_instance.teams_list_discussion_comments_legacy(team_id, discussion_number, direction=direction, per_page=per_page, page=page)
        print("The response of TeamsApi->teams_list_discussion_comments_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_list_discussion_comments_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
 **discussion_number** | **int**| The number that identifies the discussion. | 
 **direction** | **str**| The direction to sort the results by. | [optional] [default to desc]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[TeamDiscussionComment]**](TeamDiscussionComment.md)

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

# **teams_list_discussions_in_org**
> List[TeamDiscussion] teams_list_discussions_in_org(org, team_slug, direction=direction, per_page=per_page, page=page, pinned=pinned)

List discussions

List all discussions on a team's page.  > [!NOTE] > You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/discussions`.  OAuth app tokens and personal access tokens (classic) need the `read:discussion` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.team_discussion import TeamDiscussion
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
    api_instance = github_openapi.TeamsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    direction = desc # str | The direction to sort the results by. (optional) (default to desc)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)
    pinned = 'pinned_example' # str | Pinned discussions only filter (optional)

    try:
        # List discussions
        api_response = api_instance.teams_list_discussions_in_org(org, team_slug, direction=direction, per_page=per_page, page=page, pinned=pinned)
        print("The response of TeamsApi->teams_list_discussions_in_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_list_discussions_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
 **direction** | **str**| The direction to sort the results by. | [optional] [default to desc]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]
 **pinned** | **str**| Pinned discussions only filter | [optional] 

### Return type

[**List[TeamDiscussion]**](TeamDiscussion.md)

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

# **teams_list_discussions_legacy**
> List[TeamDiscussion] teams_list_discussions_legacy(team_id, direction=direction, per_page=per_page, page=page)

List discussions (Legacy)

> [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List discussions`](https://docs.github.com/rest/teams/discussions#list-discussions) endpoint.  List all discussions on a team's page.  OAuth app tokens and personal access tokens (classic) need the `read:discussion` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.team_discussion import TeamDiscussion
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
    api_instance = github_openapi.TeamsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    direction = desc # str | The direction to sort the results by. (optional) (default to desc)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List discussions (Legacy)
        api_response = api_instance.teams_list_discussions_legacy(team_id, direction=direction, per_page=per_page, page=page)
        print("The response of TeamsApi->teams_list_discussions_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_list_discussions_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
 **direction** | **str**| The direction to sort the results by. | [optional] [default to desc]
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[TeamDiscussion]**](TeamDiscussion.md)

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

# **teams_list_for_authenticated_user**
> List[TeamFull] teams_list_for_authenticated_user(per_page=per_page, page=page)

List teams for the authenticated user

List all of the teams across all of the organizations to which the authenticated user belongs.  OAuth app tokens and personal access tokens (classic) need the `user`, `repo`, or `read:org` scope to use this endpoint.  When using a fine-grained personal access token, the resource owner of the token must be a single organization, and the response will only include the teams from that organization.

### Example


```python
import github_openapi
from github_openapi.models.team_full import TeamFull
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
    api_instance = github_openapi.TeamsApi(api_client)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List teams for the authenticated user
        api_response = api_instance.teams_list_for_authenticated_user(per_page=per_page, page=page)
        print("The response of TeamsApi->teams_list_for_authenticated_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_list_for_authenticated_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[TeamFull]**](TeamFull.md)

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
**404** | Resource not found |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_list_members_in_org**
> List[SimpleUser] teams_list_members_in_org(org, team_slug, role=role, per_page=per_page, page=page)

List team members

Team members will include the members of child teams.  To list members in a team, the team must be visible to the authenticated user.

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
    api_instance = github_openapi.TeamsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    role = all # str | Filters members returned by their role in the team. (optional) (default to all)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List team members
        api_response = api_instance.teams_list_members_in_org(org, team_slug, role=role, per_page=per_page, page=page)
        print("The response of TeamsApi->teams_list_members_in_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_list_members_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
 **role** | **str**| Filters members returned by their role in the team. | [optional] [default to all]
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

# **teams_list_members_legacy**
> List[SimpleUser] teams_list_members_legacy(team_id, role=role, per_page=per_page, page=page)

List team members (Legacy)

> [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List team members`](https://docs.github.com/rest/teams/members#list-team-members) endpoint.  Team members will include the members of child teams.

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
    api_instance = github_openapi.TeamsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    role = all # str | Filters members returned by their role in the team. (optional) (default to all)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List team members (Legacy)
        api_response = api_instance.teams_list_members_legacy(team_id, role=role, per_page=per_page, page=page)
        print("The response of TeamsApi->teams_list_members_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_list_members_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
 **role** | **str**| Filters members returned by their role in the team. | [optional] [default to all]
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
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_list_pending_invitations_in_org**
> List[OrganizationInvitation] teams_list_pending_invitations_in_org(org, team_slug, per_page=per_page, page=page)

List pending team invitations

The return hash contains a `role` field which refers to the Organization Invitation role and will be one of the following values: `direct_member`, `admin`, `billing_manager`, `hiring_manager`, or `reinstate`. If the invitee is not a GitHub member, the `login` field in the return hash will be `null`.  > [!NOTE] > You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/invitations`.

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
    api_instance = github_openapi.TeamsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List pending team invitations
        api_response = api_instance.teams_list_pending_invitations_in_org(org, team_slug, per_page=per_page, page=page)
        print("The response of TeamsApi->teams_list_pending_invitations_in_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_list_pending_invitations_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_list_pending_invitations_legacy**
> List[OrganizationInvitation] teams_list_pending_invitations_legacy(team_id, per_page=per_page, page=page)

List pending team invitations (Legacy)

> [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List pending team invitations`](https://docs.github.com/rest/teams/members#list-pending-team-invitations) endpoint.  The return hash contains a `role` field which refers to the Organization Invitation role and will be one of the following values: `direct_member`, `admin`, `billing_manager`, `hiring_manager`, or `reinstate`. If the invitee is not a GitHub member, the `login` field in the return hash will be `null`.

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
    api_instance = github_openapi.TeamsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List pending team invitations (Legacy)
        api_response = api_instance.teams_list_pending_invitations_legacy(team_id, per_page=per_page, page=page)
        print("The response of TeamsApi->teams_list_pending_invitations_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_list_pending_invitations_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_list_projects_in_org**
> List[TeamProject] teams_list_projects_in_org(org, team_slug, per_page=per_page, page=page)

List team projects

Lists the organization projects for a team.  > [!NOTE] > You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/projects`.

### Example


```python
import github_openapi
from github_openapi.models.team_project import TeamProject
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
    api_instance = github_openapi.TeamsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List team projects
        api_response = api_instance.teams_list_projects_in_org(org, team_slug, per_page=per_page, page=page)
        print("The response of TeamsApi->teams_list_projects_in_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_list_projects_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[TeamProject]**](TeamProject.md)

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

# **teams_list_projects_legacy**
> List[TeamProject] teams_list_projects_legacy(team_id, per_page=per_page, page=page)

List team projects (Legacy)

> [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List team projects`](https://docs.github.com/rest/teams/teams#list-team-projects) endpoint.  Lists the organization projects for a team.

### Example


```python
import github_openapi
from github_openapi.models.team_project import TeamProject
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
    api_instance = github_openapi.TeamsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List team projects (Legacy)
        api_response = api_instance.teams_list_projects_legacy(team_id, per_page=per_page, page=page)
        print("The response of TeamsApi->teams_list_projects_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_list_projects_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[TeamProject]**](TeamProject.md)

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

# **teams_list_repos_in_org**
> List[MinimalRepository] teams_list_repos_in_org(org, team_slug, per_page=per_page, page=page)

List team repositories

Lists a team's repositories visible to the authenticated user.  > [!NOTE] > You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/repos`.

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
    api_instance = github_openapi.TeamsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List team repositories
        api_response = api_instance.teams_list_repos_in_org(org, team_slug, per_page=per_page, page=page)
        print("The response of TeamsApi->teams_list_repos_in_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_list_repos_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
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

# **teams_list_repos_legacy**
> List[MinimalRepository] teams_list_repos_legacy(team_id, per_page=per_page, page=page)

List team repositories (Legacy)

> [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the new [List team repositories](https://docs.github.com/rest/teams/teams#list-team-repositories) endpoint.

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
    api_instance = github_openapi.TeamsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List team repositories (Legacy)
        api_response = api_instance.teams_list_repos_legacy(team_id, per_page=per_page, page=page)
        print("The response of TeamsApi->teams_list_repos_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_list_repos_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
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

# **teams_remove_member_legacy**
> teams_remove_member_legacy(team_id, username)

Remove team member (Legacy)

The \"Remove team member\" endpoint (described below) is closing down.  We recommend using the [Remove team membership for a user](https://docs.github.com/rest/teams/members#remove-team-membership-for-a-user) endpoint instead. It allows you to remove both active and pending memberships.  Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  To remove a team member, the authenticated user must have 'admin' permissions to the team or be an owner of the org that the team is associated with. Removing a team member does not delete the user, it just removes them from the team.  > [!NOTE] > When you have team synchronization set up for a team with your organization's identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team's membership. If you have access to manage group membership in your IdP, you can manage GitHub team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see \"[Synchronizing teams between your identity provider and GitHub](https://docs.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/).\"

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
    api_instance = github_openapi.TeamsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Remove team member (Legacy)
        api_instance.teams_remove_member_legacy(team_id, username)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_remove_member_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
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
**404** | Not Found if team synchronization is setup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_remove_membership_for_user_in_org**
> teams_remove_membership_for_user_in_org(org, team_slug, username)

Remove team membership for a user

To remove a membership between a user and a team, the authenticated user must have 'admin' permissions to the team or be an owner of the organization that the team is associated with. Removing team membership does not delete the user, it just removes their membership from the team.  Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  > [!NOTE] > When you have team synchronization set up for a team with your organization's identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team's membership. If you have access to manage group membership in your IdP, you can manage GitHub team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see \"[Synchronizing teams between your identity provider and GitHub](https://docs.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/).\"  > [!NOTE] > You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/{org_id}/team/{team_id}/memberships/{username}`.

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
    api_instance = github_openapi.TeamsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Remove team membership for a user
        api_instance.teams_remove_membership_for_user_in_org(org, team_slug, username)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_remove_membership_for_user_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
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
**403** | Forbidden if team synchronization is set up |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_remove_membership_for_user_legacy**
> teams_remove_membership_for_user_legacy(team_id, username)

Remove team membership for a user (Legacy)

> [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the new [Remove team membership for a user](https://docs.github.com/rest/teams/members#remove-team-membership-for-a-user) endpoint.  Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  To remove a membership between a user and a team, the authenticated user must have 'admin' permissions to the team or be an owner of the organization that the team is associated with. Removing team membership does not delete the user, it just removes their membership from the team.  > [!NOTE] > When you have team synchronization set up for a team with your organization's identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team's membership. If you have access to manage group membership in your IdP, you can manage GitHub team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see \"[Synchronizing teams between your identity provider and GitHub](https://docs.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/).\"

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
    api_instance = github_openapi.TeamsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    username = 'username_example' # str | The handle for the GitHub user account.

    try:
        # Remove team membership for a user (Legacy)
        api_instance.teams_remove_membership_for_user_legacy(team_id, username)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_remove_membership_for_user_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
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
**403** | if team synchronization is set up |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_remove_project_in_org**
> teams_remove_project_in_org(org, team_slug, project_id)

Remove a project from a team

Removes an organization project from a team. An organization owner or a team maintainer can remove any project from the team. To remove a project from a team as an organization member, the authenticated user must have `read` access to both the team and project, or `admin` access to the team or project. This endpoint removes the project from the team, but does not delete the project.  > [!NOTE] > You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/{org_id}/team/{team_id}/projects/{project_id}`.

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
    api_instance = github_openapi.TeamsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    project_id = 56 # int | The unique identifier of the project.

    try:
        # Remove a project from a team
        api_instance.teams_remove_project_in_org(org, team_slug, project_id)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_remove_project_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
 **project_id** | **int**| The unique identifier of the project. | 

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

# **teams_remove_project_legacy**
> teams_remove_project_legacy(team_id, project_id)

Remove a project from a team (Legacy)

> [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the new [Remove a project from a team](https://docs.github.com/rest/teams/teams#remove-a-project-from-a-team) endpoint.  Removes an organization project from a team. An organization owner or a team maintainer can remove any project from the team. To remove a project from a team as an organization member, the authenticated user must have `read` access to both the team and project, or `admin` access to the team or project. **Note:** This endpoint removes the project from the team, but does not delete it.

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
    api_instance = github_openapi.TeamsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    project_id = 56 # int | The unique identifier of the project.

    try:
        # Remove a project from a team (Legacy)
        api_instance.teams_remove_project_legacy(team_id, project_id)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_remove_project_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
 **project_id** | **int**| The unique identifier of the project. | 

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
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_remove_repo_in_org**
> teams_remove_repo_in_org(org, team_slug, owner, repo)

Remove a repository from a team

If the authenticated user is an organization owner or a team maintainer, they can remove any repositories from the team. To remove a repository from a team as an organization member, the authenticated user must have admin access to the repository and must be able to see the team. This does not delete the repository, it just removes it from the team.  > [!NOTE] > You can also specify a team by `org_id` and `team_id` using the route `DELETE /organizations/{org_id}/team/{team_id}/repos/{owner}/{repo}`.

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
    api_instance = github_openapi.TeamsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Remove a repository from a team
        api_instance.teams_remove_repo_in_org(org, team_slug, owner, repo)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_remove_repo_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
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

# **teams_remove_repo_legacy**
> teams_remove_repo_legacy(team_id, owner, repo)

Remove a repository from a team (Legacy)

> [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the new [Remove a repository from a team](https://docs.github.com/rest/teams/teams#remove-a-repository-from-a-team) endpoint.  If the authenticated user is an organization owner or a team maintainer, they can remove any repositories from the team. To remove a repository from a team as an organization member, the authenticated user must have admin access to the repository and must be able to see the team. NOTE: This does not delete the repository, it just removes it from the team.

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
    api_instance = github_openapi.TeamsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.

    try:
        # Remove a repository from a team (Legacy)
        api_instance.teams_remove_repo_legacy(team_id, owner, repo)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_remove_repo_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
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

# **teams_update_discussion_comment_in_org**
> TeamDiscussionComment teams_update_discussion_comment_in_org(org, team_slug, discussion_number, comment_number, teams_create_discussion_comment_in_org_request)

Update a discussion comment

Edits the body text of a discussion comment.  > [!NOTE] > You can also specify a team by `org_id` and `team_id` using the route `PATCH /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}/comments/{comment_number}`.  OAuth app tokens and personal access tokens (classic) need the `write:discussion` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.team_discussion_comment import TeamDiscussionComment
from github_openapi.models.teams_create_discussion_comment_in_org_request import TeamsCreateDiscussionCommentInOrgRequest
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
    api_instance = github_openapi.TeamsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    discussion_number = 56 # int | The number that identifies the discussion.
    comment_number = 56 # int | The number that identifies the comment.
    teams_create_discussion_comment_in_org_request = {"body":"Do you like pineapples?"} # TeamsCreateDiscussionCommentInOrgRequest | 

    try:
        # Update a discussion comment
        api_response = api_instance.teams_update_discussion_comment_in_org(org, team_slug, discussion_number, comment_number, teams_create_discussion_comment_in_org_request)
        print("The response of TeamsApi->teams_update_discussion_comment_in_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_update_discussion_comment_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
 **discussion_number** | **int**| The number that identifies the discussion. | 
 **comment_number** | **int**| The number that identifies the comment. | 
 **teams_create_discussion_comment_in_org_request** | [**TeamsCreateDiscussionCommentInOrgRequest**](TeamsCreateDiscussionCommentInOrgRequest.md)|  | 

### Return type

[**TeamDiscussionComment**](TeamDiscussionComment.md)

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

# **teams_update_discussion_comment_legacy**
> TeamDiscussionComment teams_update_discussion_comment_legacy(team_id, discussion_number, comment_number, teams_create_discussion_comment_in_org_request)

Update a discussion comment (Legacy)

> [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the new [Update a discussion comment](https://docs.github.com/rest/teams/discussion-comments#update-a-discussion-comment) endpoint.  Edits the body text of a discussion comment.  OAuth app tokens and personal access tokens (classic) need the `write:discussion` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.team_discussion_comment import TeamDiscussionComment
from github_openapi.models.teams_create_discussion_comment_in_org_request import TeamsCreateDiscussionCommentInOrgRequest
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
    api_instance = github_openapi.TeamsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    discussion_number = 56 # int | The number that identifies the discussion.
    comment_number = 56 # int | The number that identifies the comment.
    teams_create_discussion_comment_in_org_request = {"body":"Do you like pineapples?"} # TeamsCreateDiscussionCommentInOrgRequest | 

    try:
        # Update a discussion comment (Legacy)
        api_response = api_instance.teams_update_discussion_comment_legacy(team_id, discussion_number, comment_number, teams_create_discussion_comment_in_org_request)
        print("The response of TeamsApi->teams_update_discussion_comment_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_update_discussion_comment_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
 **discussion_number** | **int**| The number that identifies the discussion. | 
 **comment_number** | **int**| The number that identifies the comment. | 
 **teams_create_discussion_comment_in_org_request** | [**TeamsCreateDiscussionCommentInOrgRequest**](TeamsCreateDiscussionCommentInOrgRequest.md)|  | 

### Return type

[**TeamDiscussionComment**](TeamDiscussionComment.md)

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

# **teams_update_discussion_in_org**
> TeamDiscussion teams_update_discussion_in_org(org, team_slug, discussion_number, teams_update_discussion_in_org_request=teams_update_discussion_in_org_request)

Update a discussion

Edits the title and body text of a discussion post. Only the parameters you provide are updated.  > [!NOTE] > You can also specify a team by `org_id` and `team_id` using the route `PATCH /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}`.  OAuth app tokens and personal access tokens (classic) need the `write:discussion` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.team_discussion import TeamDiscussion
from github_openapi.models.teams_update_discussion_in_org_request import TeamsUpdateDiscussionInOrgRequest
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
    api_instance = github_openapi.TeamsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    discussion_number = 56 # int | The number that identifies the discussion.
    teams_update_discussion_in_org_request = {"title":"Welcome to our first team post"} # TeamsUpdateDiscussionInOrgRequest |  (optional)

    try:
        # Update a discussion
        api_response = api_instance.teams_update_discussion_in_org(org, team_slug, discussion_number, teams_update_discussion_in_org_request=teams_update_discussion_in_org_request)
        print("The response of TeamsApi->teams_update_discussion_in_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_update_discussion_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
 **discussion_number** | **int**| The number that identifies the discussion. | 
 **teams_update_discussion_in_org_request** | [**TeamsUpdateDiscussionInOrgRequest**](TeamsUpdateDiscussionInOrgRequest.md)|  | [optional] 

### Return type

[**TeamDiscussion**](TeamDiscussion.md)

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

# **teams_update_discussion_legacy**
> TeamDiscussion teams_update_discussion_legacy(team_id, discussion_number, teams_update_discussion_in_org_request=teams_update_discussion_in_org_request)

Update a discussion (Legacy)

> [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the new [Update a discussion](https://docs.github.com/rest/teams/discussions#update-a-discussion) endpoint.  Edits the title and body text of a discussion post. Only the parameters you provide are updated.  OAuth app tokens and personal access tokens (classic) need the `write:discussion` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.team_discussion import TeamDiscussion
from github_openapi.models.teams_update_discussion_in_org_request import TeamsUpdateDiscussionInOrgRequest
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
    api_instance = github_openapi.TeamsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    discussion_number = 56 # int | The number that identifies the discussion.
    teams_update_discussion_in_org_request = {"title":"Welcome to our first team post"} # TeamsUpdateDiscussionInOrgRequest |  (optional)

    try:
        # Update a discussion (Legacy)
        api_response = api_instance.teams_update_discussion_legacy(team_id, discussion_number, teams_update_discussion_in_org_request=teams_update_discussion_in_org_request)
        print("The response of TeamsApi->teams_update_discussion_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_update_discussion_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
 **discussion_number** | **int**| The number that identifies the discussion. | 
 **teams_update_discussion_in_org_request** | [**TeamsUpdateDiscussionInOrgRequest**](TeamsUpdateDiscussionInOrgRequest.md)|  | [optional] 

### Return type

[**TeamDiscussion**](TeamDiscussion.md)

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

# **teams_update_in_org**
> TeamFull teams_update_in_org(org, team_slug, teams_update_in_org_request=teams_update_in_org_request)

Update a team

To edit a team, the authenticated user must either be an organization owner or a team maintainer.  > [!NOTE] > You can also specify a team by `org_id` and `team_id` using the route `PATCH /organizations/{org_id}/team/{team_id}`.

### Example


```python
import github_openapi
from github_openapi.models.team_full import TeamFull
from github_openapi.models.teams_update_in_org_request import TeamsUpdateInOrgRequest
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
    api_instance = github_openapi.TeamsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    teams_update_in_org_request = {"name":"new team name","description":"new team description","privacy":"closed","notification_setting":"notifications_enabled"} # TeamsUpdateInOrgRequest |  (optional)

    try:
        # Update a team
        api_response = api_instance.teams_update_in_org(org, team_slug, teams_update_in_org_request=teams_update_in_org_request)
        print("The response of TeamsApi->teams_update_in_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_update_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
 **teams_update_in_org_request** | [**TeamsUpdateInOrgRequest**](TeamsUpdateInOrgRequest.md)|  | [optional] 

### Return type

[**TeamFull**](TeamFull.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response when the updated information already exists |  -  |
**201** | Response |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_update_legacy**
> TeamFull teams_update_legacy(team_id, teams_update_legacy_request)

Update a team (Legacy)

> [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the new [Update a team](https://docs.github.com/rest/teams/teams#update-a-team) endpoint.  To edit a team, the authenticated user must either be an organization owner or a team maintainer.  > [!NOTE] > With nested teams, the `privacy` for parent teams cannot be `secret`.

### Example


```python
import github_openapi
from github_openapi.models.team_full import TeamFull
from github_openapi.models.teams_update_legacy_request import TeamsUpdateLegacyRequest
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
    api_instance = github_openapi.TeamsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    teams_update_legacy_request = {"name":"new team name","description":"new team description","privacy":"closed","notification_setting":"notifications_enabled"} # TeamsUpdateLegacyRequest | 

    try:
        # Update a team (Legacy)
        api_response = api_instance.teams_update_legacy(team_id, teams_update_legacy_request)
        print("The response of TeamsApi->teams_update_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TeamsApi->teams_update_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
 **teams_update_legacy_request** | [**TeamsUpdateLegacyRequest**](TeamsUpdateLegacyRequest.md)|  | 

### Return type

[**TeamFull**](TeamFull.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response when the updated information already exists |  -  |
**201** | Response |  -  |
**404** | Resource not found |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

