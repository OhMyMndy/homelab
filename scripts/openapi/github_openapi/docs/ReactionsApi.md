# github_openapi.ReactionsApi

All URIs are relative to *https://api.github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reactions_create_for_commit_comment**](ReactionsApi.md#reactions_create_for_commit_comment) | **POST** /repos/{owner}/{repo}/comments/{comment_id}/reactions | Create reaction for a commit comment
[**reactions_create_for_issue**](ReactionsApi.md#reactions_create_for_issue) | **POST** /repos/{owner}/{repo}/issues/{issue_number}/reactions | Create reaction for an issue
[**reactions_create_for_issue_comment**](ReactionsApi.md#reactions_create_for_issue_comment) | **POST** /repos/{owner}/{repo}/issues/comments/{comment_id}/reactions | Create reaction for an issue comment
[**reactions_create_for_pull_request_review_comment**](ReactionsApi.md#reactions_create_for_pull_request_review_comment) | **POST** /repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions | Create reaction for a pull request review comment
[**reactions_create_for_release**](ReactionsApi.md#reactions_create_for_release) | **POST** /repos/{owner}/{repo}/releases/{release_id}/reactions | Create reaction for a release
[**reactions_create_for_team_discussion_comment_in_org**](ReactionsApi.md#reactions_create_for_team_discussion_comment_in_org) | **POST** /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions | Create reaction for a team discussion comment
[**reactions_create_for_team_discussion_comment_legacy**](ReactionsApi.md#reactions_create_for_team_discussion_comment_legacy) | **POST** /teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions | Create reaction for a team discussion comment (Legacy)
[**reactions_create_for_team_discussion_in_org**](ReactionsApi.md#reactions_create_for_team_discussion_in_org) | **POST** /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions | Create reaction for a team discussion
[**reactions_create_for_team_discussion_legacy**](ReactionsApi.md#reactions_create_for_team_discussion_legacy) | **POST** /teams/{team_id}/discussions/{discussion_number}/reactions | Create reaction for a team discussion (Legacy)
[**reactions_delete_for_commit_comment**](ReactionsApi.md#reactions_delete_for_commit_comment) | **DELETE** /repos/{owner}/{repo}/comments/{comment_id}/reactions/{reaction_id} | Delete a commit comment reaction
[**reactions_delete_for_issue**](ReactionsApi.md#reactions_delete_for_issue) | **DELETE** /repos/{owner}/{repo}/issues/{issue_number}/reactions/{reaction_id} | Delete an issue reaction
[**reactions_delete_for_issue_comment**](ReactionsApi.md#reactions_delete_for_issue_comment) | **DELETE** /repos/{owner}/{repo}/issues/comments/{comment_id}/reactions/{reaction_id} | Delete an issue comment reaction
[**reactions_delete_for_pull_request_comment**](ReactionsApi.md#reactions_delete_for_pull_request_comment) | **DELETE** /repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions/{reaction_id} | Delete a pull request comment reaction
[**reactions_delete_for_release**](ReactionsApi.md#reactions_delete_for_release) | **DELETE** /repos/{owner}/{repo}/releases/{release_id}/reactions/{reaction_id} | Delete a release reaction
[**reactions_delete_for_team_discussion**](ReactionsApi.md#reactions_delete_for_team_discussion) | **DELETE** /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions/{reaction_id} | Delete team discussion reaction
[**reactions_delete_for_team_discussion_comment**](ReactionsApi.md#reactions_delete_for_team_discussion_comment) | **DELETE** /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions/{reaction_id} | Delete team discussion comment reaction
[**reactions_list_for_commit_comment**](ReactionsApi.md#reactions_list_for_commit_comment) | **GET** /repos/{owner}/{repo}/comments/{comment_id}/reactions | List reactions for a commit comment
[**reactions_list_for_issue**](ReactionsApi.md#reactions_list_for_issue) | **GET** /repos/{owner}/{repo}/issues/{issue_number}/reactions | List reactions for an issue
[**reactions_list_for_issue_comment**](ReactionsApi.md#reactions_list_for_issue_comment) | **GET** /repos/{owner}/{repo}/issues/comments/{comment_id}/reactions | List reactions for an issue comment
[**reactions_list_for_pull_request_review_comment**](ReactionsApi.md#reactions_list_for_pull_request_review_comment) | **GET** /repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions | List reactions for a pull request review comment
[**reactions_list_for_release**](ReactionsApi.md#reactions_list_for_release) | **GET** /repos/{owner}/{repo}/releases/{release_id}/reactions | List reactions for a release
[**reactions_list_for_team_discussion_comment_in_org**](ReactionsApi.md#reactions_list_for_team_discussion_comment_in_org) | **GET** /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions | List reactions for a team discussion comment
[**reactions_list_for_team_discussion_comment_legacy**](ReactionsApi.md#reactions_list_for_team_discussion_comment_legacy) | **GET** /teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions | List reactions for a team discussion comment (Legacy)
[**reactions_list_for_team_discussion_in_org**](ReactionsApi.md#reactions_list_for_team_discussion_in_org) | **GET** /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions | List reactions for a team discussion
[**reactions_list_for_team_discussion_legacy**](ReactionsApi.md#reactions_list_for_team_discussion_legacy) | **GET** /teams/{team_id}/discussions/{discussion_number}/reactions | List reactions for a team discussion (Legacy)


# **reactions_create_for_commit_comment**
> Reaction reactions_create_for_commit_comment(owner, repo, comment_id, reactions_create_for_commit_comment_request)

Create reaction for a commit comment

Create a reaction to a [commit comment](https://docs.github.com/rest/commits/comments#get-a-commit-comment). A response with an HTTP `200` status means that you already added the reaction type to this commit comment.

### Example


```python
import github_openapi
from github_openapi.models.reaction import Reaction
from github_openapi.models.reactions_create_for_commit_comment_request import ReactionsCreateForCommitCommentRequest
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
    api_instance = github_openapi.ReactionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    comment_id = 56 # int | The unique identifier of the comment.
    reactions_create_for_commit_comment_request = {"content":"heart"} # ReactionsCreateForCommitCommentRequest | 

    try:
        # Create reaction for a commit comment
        api_response = api_instance.reactions_create_for_commit_comment(owner, repo, comment_id, reactions_create_for_commit_comment_request)
        print("The response of ReactionsApi->reactions_create_for_commit_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReactionsApi->reactions_create_for_commit_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **comment_id** | **int**| The unique identifier of the comment. | 
 **reactions_create_for_commit_comment_request** | [**ReactionsCreateForCommitCommentRequest**](ReactionsCreateForCommitCommentRequest.md)|  | 

### Return type

[**Reaction**](Reaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reaction exists |  -  |
**201** | Reaction created |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reactions_create_for_issue**
> Reaction reactions_create_for_issue(owner, repo, issue_number, reactions_create_for_issue_request)

Create reaction for an issue

Create a reaction to an [issue](https://docs.github.com/rest/issues/issues#get-an-issue). A response with an HTTP `200` status means that you already added the reaction type to this issue.

### Example


```python
import github_openapi
from github_openapi.models.reaction import Reaction
from github_openapi.models.reactions_create_for_issue_request import ReactionsCreateForIssueRequest
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
    api_instance = github_openapi.ReactionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    issue_number = 56 # int | The number that identifies the issue.
    reactions_create_for_issue_request = {"content":"heart"} # ReactionsCreateForIssueRequest | 

    try:
        # Create reaction for an issue
        api_response = api_instance.reactions_create_for_issue(owner, repo, issue_number, reactions_create_for_issue_request)
        print("The response of ReactionsApi->reactions_create_for_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReactionsApi->reactions_create_for_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **issue_number** | **int**| The number that identifies the issue. | 
 **reactions_create_for_issue_request** | [**ReactionsCreateForIssueRequest**](ReactionsCreateForIssueRequest.md)|  | 

### Return type

[**Reaction**](Reaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**201** | Response |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reactions_create_for_issue_comment**
> Reaction reactions_create_for_issue_comment(owner, repo, comment_id, reactions_create_for_issue_comment_request)

Create reaction for an issue comment

Create a reaction to an [issue comment](https://docs.github.com/rest/issues/comments#get-an-issue-comment). A response with an HTTP `200` status means that you already added the reaction type to this issue comment.

### Example


```python
import github_openapi
from github_openapi.models.reaction import Reaction
from github_openapi.models.reactions_create_for_issue_comment_request import ReactionsCreateForIssueCommentRequest
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
    api_instance = github_openapi.ReactionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    comment_id = 56 # int | The unique identifier of the comment.
    reactions_create_for_issue_comment_request = {"content":"heart"} # ReactionsCreateForIssueCommentRequest | 

    try:
        # Create reaction for an issue comment
        api_response = api_instance.reactions_create_for_issue_comment(owner, repo, comment_id, reactions_create_for_issue_comment_request)
        print("The response of ReactionsApi->reactions_create_for_issue_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReactionsApi->reactions_create_for_issue_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **comment_id** | **int**| The unique identifier of the comment. | 
 **reactions_create_for_issue_comment_request** | [**ReactionsCreateForIssueCommentRequest**](ReactionsCreateForIssueCommentRequest.md)|  | 

### Return type

[**Reaction**](Reaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reaction exists |  -  |
**201** | Reaction created |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reactions_create_for_pull_request_review_comment**
> Reaction reactions_create_for_pull_request_review_comment(owner, repo, comment_id, reactions_create_for_pull_request_review_comment_request)

Create reaction for a pull request review comment

Create a reaction to a [pull request review comment](https://docs.github.com/rest/pulls/comments#get-a-review-comment-for-a-pull-request). A response with an HTTP `200` status means that you already added the reaction type to this pull request review comment.

### Example


```python
import github_openapi
from github_openapi.models.reaction import Reaction
from github_openapi.models.reactions_create_for_pull_request_review_comment_request import ReactionsCreateForPullRequestReviewCommentRequest
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
    api_instance = github_openapi.ReactionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    comment_id = 56 # int | The unique identifier of the comment.
    reactions_create_for_pull_request_review_comment_request = {"content":"heart"} # ReactionsCreateForPullRequestReviewCommentRequest | 

    try:
        # Create reaction for a pull request review comment
        api_response = api_instance.reactions_create_for_pull_request_review_comment(owner, repo, comment_id, reactions_create_for_pull_request_review_comment_request)
        print("The response of ReactionsApi->reactions_create_for_pull_request_review_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReactionsApi->reactions_create_for_pull_request_review_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **comment_id** | **int**| The unique identifier of the comment. | 
 **reactions_create_for_pull_request_review_comment_request** | [**ReactionsCreateForPullRequestReviewCommentRequest**](ReactionsCreateForPullRequestReviewCommentRequest.md)|  | 

### Return type

[**Reaction**](Reaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reaction exists |  -  |
**201** | Reaction created |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reactions_create_for_release**
> Reaction reactions_create_for_release(owner, repo, release_id, reactions_create_for_release_request)

Create reaction for a release

Create a reaction to a [release](https://docs.github.com/rest/releases/releases#get-a-release). A response with a `Status: 200 OK` means that you already added the reaction type to this release.

### Example


```python
import github_openapi
from github_openapi.models.reaction import Reaction
from github_openapi.models.reactions_create_for_release_request import ReactionsCreateForReleaseRequest
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
    api_instance = github_openapi.ReactionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    release_id = 56 # int | The unique identifier of the release.
    reactions_create_for_release_request = {"content":"heart"} # ReactionsCreateForReleaseRequest | 

    try:
        # Create reaction for a release
        api_response = api_instance.reactions_create_for_release(owner, repo, release_id, reactions_create_for_release_request)
        print("The response of ReactionsApi->reactions_create_for_release:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReactionsApi->reactions_create_for_release: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **release_id** | **int**| The unique identifier of the release. | 
 **reactions_create_for_release_request** | [**ReactionsCreateForReleaseRequest**](ReactionsCreateForReleaseRequest.md)|  | 

### Return type

[**Reaction**](Reaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reaction exists |  -  |
**201** | Reaction created |  -  |
**422** | Validation failed, or the endpoint has been spammed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reactions_create_for_team_discussion_comment_in_org**
> Reaction reactions_create_for_team_discussion_comment_in_org(org, team_slug, discussion_number, comment_number, reactions_create_for_team_discussion_comment_in_org_request)

Create reaction for a team discussion comment

Create a reaction to a [team discussion comment](https://docs.github.com/rest/teams/discussion-comments#get-a-discussion-comment).  A response with an HTTP `200` status means that you already added the reaction type to this team discussion comment.  > [!NOTE] > You can also specify a team by `org_id` and `team_id` using the route `POST /organizations/:org_id/team/:team_id/discussions/:discussion_number/comments/:comment_number/reactions`.  OAuth app tokens and personal access tokens (classic) need the `write:discussion` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.reaction import Reaction
from github_openapi.models.reactions_create_for_team_discussion_comment_in_org_request import ReactionsCreateForTeamDiscussionCommentInOrgRequest
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
    api_instance = github_openapi.ReactionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    discussion_number = 56 # int | The number that identifies the discussion.
    comment_number = 56 # int | The number that identifies the comment.
    reactions_create_for_team_discussion_comment_in_org_request = {"content":"heart"} # ReactionsCreateForTeamDiscussionCommentInOrgRequest | 

    try:
        # Create reaction for a team discussion comment
        api_response = api_instance.reactions_create_for_team_discussion_comment_in_org(org, team_slug, discussion_number, comment_number, reactions_create_for_team_discussion_comment_in_org_request)
        print("The response of ReactionsApi->reactions_create_for_team_discussion_comment_in_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReactionsApi->reactions_create_for_team_discussion_comment_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
 **discussion_number** | **int**| The number that identifies the discussion. | 
 **comment_number** | **int**| The number that identifies the comment. | 
 **reactions_create_for_team_discussion_comment_in_org_request** | [**ReactionsCreateForTeamDiscussionCommentInOrgRequest**](ReactionsCreateForTeamDiscussionCommentInOrgRequest.md)|  | 

### Return type

[**Reaction**](Reaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response when the reaction type has already been added to this team discussion comment |  -  |
**201** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reactions_create_for_team_discussion_comment_legacy**
> Reaction reactions_create_for_team_discussion_comment_legacy(team_id, discussion_number, comment_number, reactions_create_for_team_discussion_comment_in_org_request)

Create reaction for a team discussion comment (Legacy)

> [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the new \"[Create reaction for a team discussion comment](https://docs.github.com/rest/reactions/reactions#create-reaction-for-a-team-discussion-comment)\" endpoint.  Create a reaction to a [team discussion comment](https://docs.github.com/rest/teams/discussion-comments#get-a-discussion-comment).  A response with an HTTP `200` status means that you already added the reaction type to this team discussion comment.  OAuth app tokens and personal access tokens (classic) need the `write:discussion` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.reaction import Reaction
from github_openapi.models.reactions_create_for_team_discussion_comment_in_org_request import ReactionsCreateForTeamDiscussionCommentInOrgRequest
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
    api_instance = github_openapi.ReactionsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    discussion_number = 56 # int | The number that identifies the discussion.
    comment_number = 56 # int | The number that identifies the comment.
    reactions_create_for_team_discussion_comment_in_org_request = {"content":"heart"} # ReactionsCreateForTeamDiscussionCommentInOrgRequest | 

    try:
        # Create reaction for a team discussion comment (Legacy)
        api_response = api_instance.reactions_create_for_team_discussion_comment_legacy(team_id, discussion_number, comment_number, reactions_create_for_team_discussion_comment_in_org_request)
        print("The response of ReactionsApi->reactions_create_for_team_discussion_comment_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReactionsApi->reactions_create_for_team_discussion_comment_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
 **discussion_number** | **int**| The number that identifies the discussion. | 
 **comment_number** | **int**| The number that identifies the comment. | 
 **reactions_create_for_team_discussion_comment_in_org_request** | [**ReactionsCreateForTeamDiscussionCommentInOrgRequest**](ReactionsCreateForTeamDiscussionCommentInOrgRequest.md)|  | 

### Return type

[**Reaction**](Reaction.md)

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

# **reactions_create_for_team_discussion_in_org**
> Reaction reactions_create_for_team_discussion_in_org(org, team_slug, discussion_number, reactions_create_for_team_discussion_in_org_request)

Create reaction for a team discussion

Create a reaction to a [team discussion](https://docs.github.com/rest/teams/discussions#get-a-discussion).  A response with an HTTP `200` status means that you already added the reaction type to this team discussion.  > [!NOTE] > You can also specify a team by `org_id` and `team_id` using the route `POST /organizations/:org_id/team/:team_id/discussions/:discussion_number/reactions`.  OAuth app tokens and personal access tokens (classic) need the `write:discussion` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.reaction import Reaction
from github_openapi.models.reactions_create_for_team_discussion_in_org_request import ReactionsCreateForTeamDiscussionInOrgRequest
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
    api_instance = github_openapi.ReactionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    discussion_number = 56 # int | The number that identifies the discussion.
    reactions_create_for_team_discussion_in_org_request = {"content":"heart"} # ReactionsCreateForTeamDiscussionInOrgRequest | 

    try:
        # Create reaction for a team discussion
        api_response = api_instance.reactions_create_for_team_discussion_in_org(org, team_slug, discussion_number, reactions_create_for_team_discussion_in_org_request)
        print("The response of ReactionsApi->reactions_create_for_team_discussion_in_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReactionsApi->reactions_create_for_team_discussion_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
 **discussion_number** | **int**| The number that identifies the discussion. | 
 **reactions_create_for_team_discussion_in_org_request** | [**ReactionsCreateForTeamDiscussionInOrgRequest**](ReactionsCreateForTeamDiscussionInOrgRequest.md)|  | 

### Return type

[**Reaction**](Reaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**201** | Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reactions_create_for_team_discussion_legacy**
> Reaction reactions_create_for_team_discussion_legacy(team_id, discussion_number, reactions_create_for_team_discussion_in_org_request)

Create reaction for a team discussion (Legacy)

> [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the new [`Create reaction for a team discussion`](https://docs.github.com/rest/reactions/reactions#create-reaction-for-a-team-discussion) endpoint.  Create a reaction to a [team discussion](https://docs.github.com/rest/teams/discussions#get-a-discussion).  A response with an HTTP `200` status means that you already added the reaction type to this team discussion.  OAuth app tokens and personal access tokens (classic) need the `write:discussion` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.reaction import Reaction
from github_openapi.models.reactions_create_for_team_discussion_in_org_request import ReactionsCreateForTeamDiscussionInOrgRequest
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
    api_instance = github_openapi.ReactionsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    discussion_number = 56 # int | The number that identifies the discussion.
    reactions_create_for_team_discussion_in_org_request = {"content":"heart"} # ReactionsCreateForTeamDiscussionInOrgRequest | 

    try:
        # Create reaction for a team discussion (Legacy)
        api_response = api_instance.reactions_create_for_team_discussion_legacy(team_id, discussion_number, reactions_create_for_team_discussion_in_org_request)
        print("The response of ReactionsApi->reactions_create_for_team_discussion_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReactionsApi->reactions_create_for_team_discussion_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
 **discussion_number** | **int**| The number that identifies the discussion. | 
 **reactions_create_for_team_discussion_in_org_request** | [**ReactionsCreateForTeamDiscussionInOrgRequest**](ReactionsCreateForTeamDiscussionInOrgRequest.md)|  | 

### Return type

[**Reaction**](Reaction.md)

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

# **reactions_delete_for_commit_comment**
> reactions_delete_for_commit_comment(owner, repo, comment_id, reaction_id)

Delete a commit comment reaction

> [!NOTE] > You can also specify a repository by `repository_id` using the route `DELETE /repositories/:repository_id/comments/:comment_id/reactions/:reaction_id`.  Delete a reaction to a [commit comment](https://docs.github.com/rest/commits/comments#get-a-commit-comment).

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
    api_instance = github_openapi.ReactionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    comment_id = 56 # int | The unique identifier of the comment.
    reaction_id = 56 # int | The unique identifier of the reaction.

    try:
        # Delete a commit comment reaction
        api_instance.reactions_delete_for_commit_comment(owner, repo, comment_id, reaction_id)
    except Exception as e:
        print("Exception when calling ReactionsApi->reactions_delete_for_commit_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **comment_id** | **int**| The unique identifier of the comment. | 
 **reaction_id** | **int**| The unique identifier of the reaction. | 

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

# **reactions_delete_for_issue**
> reactions_delete_for_issue(owner, repo, issue_number, reaction_id)

Delete an issue reaction

> [!NOTE] > You can also specify a repository by `repository_id` using the route `DELETE /repositories/:repository_id/issues/:issue_number/reactions/:reaction_id`.  Delete a reaction to an [issue](https://docs.github.com/rest/issues/issues#get-an-issue).

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
    api_instance = github_openapi.ReactionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    issue_number = 56 # int | The number that identifies the issue.
    reaction_id = 56 # int | The unique identifier of the reaction.

    try:
        # Delete an issue reaction
        api_instance.reactions_delete_for_issue(owner, repo, issue_number, reaction_id)
    except Exception as e:
        print("Exception when calling ReactionsApi->reactions_delete_for_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **issue_number** | **int**| The number that identifies the issue. | 
 **reaction_id** | **int**| The unique identifier of the reaction. | 

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

# **reactions_delete_for_issue_comment**
> reactions_delete_for_issue_comment(owner, repo, comment_id, reaction_id)

Delete an issue comment reaction

> [!NOTE] > You can also specify a repository by `repository_id` using the route `DELETE delete /repositories/:repository_id/issues/comments/:comment_id/reactions/:reaction_id`.  Delete a reaction to an [issue comment](https://docs.github.com/rest/issues/comments#get-an-issue-comment).

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
    api_instance = github_openapi.ReactionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    comment_id = 56 # int | The unique identifier of the comment.
    reaction_id = 56 # int | The unique identifier of the reaction.

    try:
        # Delete an issue comment reaction
        api_instance.reactions_delete_for_issue_comment(owner, repo, comment_id, reaction_id)
    except Exception as e:
        print("Exception when calling ReactionsApi->reactions_delete_for_issue_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **comment_id** | **int**| The unique identifier of the comment. | 
 **reaction_id** | **int**| The unique identifier of the reaction. | 

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

# **reactions_delete_for_pull_request_comment**
> reactions_delete_for_pull_request_comment(owner, repo, comment_id, reaction_id)

Delete a pull request comment reaction

> [!NOTE] > You can also specify a repository by `repository_id` using the route `DELETE /repositories/:repository_id/pulls/comments/:comment_id/reactions/:reaction_id.`  Delete a reaction to a [pull request review comment](https://docs.github.com/rest/pulls/comments#get-a-review-comment-for-a-pull-request).

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
    api_instance = github_openapi.ReactionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    comment_id = 56 # int | The unique identifier of the comment.
    reaction_id = 56 # int | The unique identifier of the reaction.

    try:
        # Delete a pull request comment reaction
        api_instance.reactions_delete_for_pull_request_comment(owner, repo, comment_id, reaction_id)
    except Exception as e:
        print("Exception when calling ReactionsApi->reactions_delete_for_pull_request_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **comment_id** | **int**| The unique identifier of the comment. | 
 **reaction_id** | **int**| The unique identifier of the reaction. | 

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

# **reactions_delete_for_release**
> reactions_delete_for_release(owner, repo, release_id, reaction_id)

Delete a release reaction

> [!NOTE] > You can also specify a repository by `repository_id` using the route `DELETE delete /repositories/:repository_id/releases/:release_id/reactions/:reaction_id`.  Delete a reaction to a [release](https://docs.github.com/rest/releases/releases#get-a-release).

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
    api_instance = github_openapi.ReactionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    release_id = 56 # int | The unique identifier of the release.
    reaction_id = 56 # int | The unique identifier of the reaction.

    try:
        # Delete a release reaction
        api_instance.reactions_delete_for_release(owner, repo, release_id, reaction_id)
    except Exception as e:
        print("Exception when calling ReactionsApi->reactions_delete_for_release: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **release_id** | **int**| The unique identifier of the release. | 
 **reaction_id** | **int**| The unique identifier of the reaction. | 

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

# **reactions_delete_for_team_discussion**
> reactions_delete_for_team_discussion(org, team_slug, discussion_number, reaction_id)

Delete team discussion reaction

> [!NOTE] > You can also specify a team or organization with `team_id` and `org_id` using the route `DELETE /organizations/:org_id/team/:team_id/discussions/:discussion_number/reactions/:reaction_id`.  Delete a reaction to a [team discussion](https://docs.github.com/rest/teams/discussions#get-a-discussion).  OAuth app tokens and personal access tokens (classic) need the `write:discussion` scope to use this endpoint.

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
    api_instance = github_openapi.ReactionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    discussion_number = 56 # int | The number that identifies the discussion.
    reaction_id = 56 # int | The unique identifier of the reaction.

    try:
        # Delete team discussion reaction
        api_instance.reactions_delete_for_team_discussion(org, team_slug, discussion_number, reaction_id)
    except Exception as e:
        print("Exception when calling ReactionsApi->reactions_delete_for_team_discussion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
 **discussion_number** | **int**| The number that identifies the discussion. | 
 **reaction_id** | **int**| The unique identifier of the reaction. | 

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

# **reactions_delete_for_team_discussion_comment**
> reactions_delete_for_team_discussion_comment(org, team_slug, discussion_number, comment_number, reaction_id)

Delete team discussion comment reaction

> [!NOTE] > You can also specify a team or organization with `team_id` and `org_id` using the route `DELETE /organizations/:org_id/team/:team_id/discussions/:discussion_number/comments/:comment_number/reactions/:reaction_id`.  Delete a reaction to a [team discussion comment](https://docs.github.com/rest/teams/discussion-comments#get-a-discussion-comment).  OAuth app tokens and personal access tokens (classic) need the `write:discussion` scope to use this endpoint.

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
    api_instance = github_openapi.ReactionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    discussion_number = 56 # int | The number that identifies the discussion.
    comment_number = 56 # int | The number that identifies the comment.
    reaction_id = 56 # int | The unique identifier of the reaction.

    try:
        # Delete team discussion comment reaction
        api_instance.reactions_delete_for_team_discussion_comment(org, team_slug, discussion_number, comment_number, reaction_id)
    except Exception as e:
        print("Exception when calling ReactionsApi->reactions_delete_for_team_discussion_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
 **discussion_number** | **int**| The number that identifies the discussion. | 
 **comment_number** | **int**| The number that identifies the comment. | 
 **reaction_id** | **int**| The unique identifier of the reaction. | 

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

# **reactions_list_for_commit_comment**
> List[Reaction] reactions_list_for_commit_comment(owner, repo, comment_id, content=content, per_page=per_page, page=page)

List reactions for a commit comment

List the reactions to a [commit comment](https://docs.github.com/rest/commits/comments#get-a-commit-comment).

### Example


```python
import github_openapi
from github_openapi.models.reaction import Reaction
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
    api_instance = github_openapi.ReactionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    comment_id = 56 # int | The unique identifier of the comment.
    content = 'content_example' # str | Returns a single [reaction type](https://docs.github.com/rest/reactions/reactions#about-reactions). Omit this parameter to list all reactions to a commit comment. (optional)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List reactions for a commit comment
        api_response = api_instance.reactions_list_for_commit_comment(owner, repo, comment_id, content=content, per_page=per_page, page=page)
        print("The response of ReactionsApi->reactions_list_for_commit_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReactionsApi->reactions_list_for_commit_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **comment_id** | **int**| The unique identifier of the comment. | 
 **content** | **str**| Returns a single [reaction type](https://docs.github.com/rest/reactions/reactions#about-reactions). Omit this parameter to list all reactions to a commit comment. | [optional] 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Reaction]**](Reaction.md)

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

# **reactions_list_for_issue**
> List[Reaction] reactions_list_for_issue(owner, repo, issue_number, content=content, per_page=per_page, page=page)

List reactions for an issue

List the reactions to an [issue](https://docs.github.com/rest/issues/issues#get-an-issue).

### Example


```python
import github_openapi
from github_openapi.models.reaction import Reaction
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
    api_instance = github_openapi.ReactionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    issue_number = 56 # int | The number that identifies the issue.
    content = 'content_example' # str | Returns a single [reaction type](https://docs.github.com/rest/reactions/reactions#about-reactions). Omit this parameter to list all reactions to an issue. (optional)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List reactions for an issue
        api_response = api_instance.reactions_list_for_issue(owner, repo, issue_number, content=content, per_page=per_page, page=page)
        print("The response of ReactionsApi->reactions_list_for_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReactionsApi->reactions_list_for_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **issue_number** | **int**| The number that identifies the issue. | 
 **content** | **str**| Returns a single [reaction type](https://docs.github.com/rest/reactions/reactions#about-reactions). Omit this parameter to list all reactions to an issue. | [optional] 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Reaction]**](Reaction.md)

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
**410** | Gone |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reactions_list_for_issue_comment**
> List[Reaction] reactions_list_for_issue_comment(owner, repo, comment_id, content=content, per_page=per_page, page=page)

List reactions for an issue comment

List the reactions to an [issue comment](https://docs.github.com/rest/issues/comments#get-an-issue-comment).

### Example


```python
import github_openapi
from github_openapi.models.reaction import Reaction
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
    api_instance = github_openapi.ReactionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    comment_id = 56 # int | The unique identifier of the comment.
    content = 'content_example' # str | Returns a single [reaction type](https://docs.github.com/rest/reactions/reactions#about-reactions). Omit this parameter to list all reactions to an issue comment. (optional)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List reactions for an issue comment
        api_response = api_instance.reactions_list_for_issue_comment(owner, repo, comment_id, content=content, per_page=per_page, page=page)
        print("The response of ReactionsApi->reactions_list_for_issue_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReactionsApi->reactions_list_for_issue_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **comment_id** | **int**| The unique identifier of the comment. | 
 **content** | **str**| Returns a single [reaction type](https://docs.github.com/rest/reactions/reactions#about-reactions). Omit this parameter to list all reactions to an issue comment. | [optional] 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Reaction]**](Reaction.md)

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

# **reactions_list_for_pull_request_review_comment**
> List[Reaction] reactions_list_for_pull_request_review_comment(owner, repo, comment_id, content=content, per_page=per_page, page=page)

List reactions for a pull request review comment

List the reactions to a [pull request review comment](https://docs.github.com/rest/pulls/comments#get-a-review-comment-for-a-pull-request).

### Example


```python
import github_openapi
from github_openapi.models.reaction import Reaction
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
    api_instance = github_openapi.ReactionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    comment_id = 56 # int | The unique identifier of the comment.
    content = 'content_example' # str | Returns a single [reaction type](https://docs.github.com/rest/reactions/reactions#about-reactions). Omit this parameter to list all reactions to a pull request review comment. (optional)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List reactions for a pull request review comment
        api_response = api_instance.reactions_list_for_pull_request_review_comment(owner, repo, comment_id, content=content, per_page=per_page, page=page)
        print("The response of ReactionsApi->reactions_list_for_pull_request_review_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReactionsApi->reactions_list_for_pull_request_review_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **comment_id** | **int**| The unique identifier of the comment. | 
 **content** | **str**| Returns a single [reaction type](https://docs.github.com/rest/reactions/reactions#about-reactions). Omit this parameter to list all reactions to a pull request review comment. | [optional] 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Reaction]**](Reaction.md)

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

# **reactions_list_for_release**
> List[Reaction] reactions_list_for_release(owner, repo, release_id, content=content, per_page=per_page, page=page)

List reactions for a release

List the reactions to a [release](https://docs.github.com/rest/releases/releases#get-a-release).

### Example


```python
import github_openapi
from github_openapi.models.reaction import Reaction
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
    api_instance = github_openapi.ReactionsApi(api_client)
    owner = 'owner_example' # str | The account owner of the repository. The name is not case sensitive.
    repo = 'repo_example' # str | The name of the repository without the `.git` extension. The name is not case sensitive.
    release_id = 56 # int | The unique identifier of the release.
    content = 'content_example' # str | Returns a single [reaction type](https://docs.github.com/rest/reactions/reactions#about-reactions). Omit this parameter to list all reactions to a release. (optional)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List reactions for a release
        api_response = api_instance.reactions_list_for_release(owner, repo, release_id, content=content, per_page=per_page, page=page)
        print("The response of ReactionsApi->reactions_list_for_release:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReactionsApi->reactions_list_for_release: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **str**| The name of the repository without the &#x60;.git&#x60; extension. The name is not case sensitive. | 
 **release_id** | **int**| The unique identifier of the release. | 
 **content** | **str**| Returns a single [reaction type](https://docs.github.com/rest/reactions/reactions#about-reactions). Omit this parameter to list all reactions to a release. | [optional] 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Reaction]**](Reaction.md)

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

# **reactions_list_for_team_discussion_comment_in_org**
> List[Reaction] reactions_list_for_team_discussion_comment_in_org(org, team_slug, discussion_number, comment_number, content=content, per_page=per_page, page=page)

List reactions for a team discussion comment

List the reactions to a [team discussion comment](https://docs.github.com/rest/teams/discussion-comments#get-a-discussion-comment).  > [!NOTE] > You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/:org_id/team/:team_id/discussions/:discussion_number/comments/:comment_number/reactions`.  OAuth app tokens and personal access tokens (classic) need the `read:discussion` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.reaction import Reaction
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
    api_instance = github_openapi.ReactionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    discussion_number = 56 # int | The number that identifies the discussion.
    comment_number = 56 # int | The number that identifies the comment.
    content = 'content_example' # str | Returns a single [reaction type](https://docs.github.com/rest/reactions/reactions#about-reactions). Omit this parameter to list all reactions to a team discussion comment. (optional)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List reactions for a team discussion comment
        api_response = api_instance.reactions_list_for_team_discussion_comment_in_org(org, team_slug, discussion_number, comment_number, content=content, per_page=per_page, page=page)
        print("The response of ReactionsApi->reactions_list_for_team_discussion_comment_in_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReactionsApi->reactions_list_for_team_discussion_comment_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
 **discussion_number** | **int**| The number that identifies the discussion. | 
 **comment_number** | **int**| The number that identifies the comment. | 
 **content** | **str**| Returns a single [reaction type](https://docs.github.com/rest/reactions/reactions#about-reactions). Omit this parameter to list all reactions to a team discussion comment. | [optional] 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Reaction]**](Reaction.md)

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

# **reactions_list_for_team_discussion_comment_legacy**
> List[Reaction] reactions_list_for_team_discussion_comment_legacy(team_id, discussion_number, comment_number, content=content, per_page=per_page, page=page)

List reactions for a team discussion comment (Legacy)

> [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List reactions for a team discussion comment`](https://docs.github.com/rest/reactions/reactions#list-reactions-for-a-team-discussion-comment) endpoint.  List the reactions to a [team discussion comment](https://docs.github.com/rest/teams/discussion-comments#get-a-discussion-comment).  OAuth app tokens and personal access tokens (classic) need the `read:discussion` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.reaction import Reaction
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
    api_instance = github_openapi.ReactionsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    discussion_number = 56 # int | The number that identifies the discussion.
    comment_number = 56 # int | The number that identifies the comment.
    content = 'content_example' # str | Returns a single [reaction type](https://docs.github.com/rest/reactions/reactions#about-reactions). Omit this parameter to list all reactions to a team discussion comment. (optional)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List reactions for a team discussion comment (Legacy)
        api_response = api_instance.reactions_list_for_team_discussion_comment_legacy(team_id, discussion_number, comment_number, content=content, per_page=per_page, page=page)
        print("The response of ReactionsApi->reactions_list_for_team_discussion_comment_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReactionsApi->reactions_list_for_team_discussion_comment_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
 **discussion_number** | **int**| The number that identifies the discussion. | 
 **comment_number** | **int**| The number that identifies the comment. | 
 **content** | **str**| Returns a single [reaction type](https://docs.github.com/rest/reactions/reactions#about-reactions). Omit this parameter to list all reactions to a team discussion comment. | [optional] 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Reaction]**](Reaction.md)

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

# **reactions_list_for_team_discussion_in_org**
> List[Reaction] reactions_list_for_team_discussion_in_org(org, team_slug, discussion_number, content=content, per_page=per_page, page=page)

List reactions for a team discussion

List the reactions to a [team discussion](https://docs.github.com/rest/teams/discussions#get-a-discussion).  > [!NOTE] > You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/:org_id/team/:team_id/discussions/:discussion_number/reactions`.  OAuth app tokens and personal access tokens (classic) need the `read:discussion` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.reaction import Reaction
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
    api_instance = github_openapi.ReactionsApi(api_client)
    org = 'org_example' # str | The organization name. The name is not case sensitive.
    team_slug = 'team_slug_example' # str | The slug of the team name.
    discussion_number = 56 # int | The number that identifies the discussion.
    content = 'content_example' # str | Returns a single [reaction type](https://docs.github.com/rest/reactions/reactions#about-reactions). Omit this parameter to list all reactions to a team discussion. (optional)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List reactions for a team discussion
        api_response = api_instance.reactions_list_for_team_discussion_in_org(org, team_slug, discussion_number, content=content, per_page=per_page, page=page)
        print("The response of ReactionsApi->reactions_list_for_team_discussion_in_org:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReactionsApi->reactions_list_for_team_discussion_in_org: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **str**| The organization name. The name is not case sensitive. | 
 **team_slug** | **str**| The slug of the team name. | 
 **discussion_number** | **int**| The number that identifies the discussion. | 
 **content** | **str**| Returns a single [reaction type](https://docs.github.com/rest/reactions/reactions#about-reactions). Omit this parameter to list all reactions to a team discussion. | [optional] 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Reaction]**](Reaction.md)

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

# **reactions_list_for_team_discussion_legacy**
> List[Reaction] reactions_list_for_team_discussion_legacy(team_id, discussion_number, content=content, per_page=per_page, page=page)

List reactions for a team discussion (Legacy)

> [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing down and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List reactions for a team discussion`](https://docs.github.com/rest/reactions/reactions#list-reactions-for-a-team-discussion) endpoint.  List the reactions to a [team discussion](https://docs.github.com/rest/teams/discussions#get-a-discussion).  OAuth app tokens and personal access tokens (classic) need the `read:discussion` scope to use this endpoint.

### Example


```python
import github_openapi
from github_openapi.models.reaction import Reaction
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
    api_instance = github_openapi.ReactionsApi(api_client)
    team_id = 56 # int | The unique identifier of the team.
    discussion_number = 56 # int | The number that identifies the discussion.
    content = 'content_example' # str | Returns a single [reaction type](https://docs.github.com/rest/reactions/reactions#about-reactions). Omit this parameter to list all reactions to a team discussion. (optional)
    per_page = 30 # int | The number of results per page (max 100). For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 30)
    page = 1 # int | The page number of the results to fetch. For more information, see \"[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\" (optional) (default to 1)

    try:
        # List reactions for a team discussion (Legacy)
        api_response = api_instance.reactions_list_for_team_discussion_legacy(team_id, discussion_number, content=content, per_page=per_page, page=page)
        print("The response of ReactionsApi->reactions_list_for_team_discussion_legacy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReactionsApi->reactions_list_for_team_discussion_legacy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **int**| The unique identifier of the team. | 
 **discussion_number** | **int**| The number that identifies the discussion. | 
 **content** | **str**| Returns a single [reaction type](https://docs.github.com/rest/reactions/reactions#about-reactions). Omit this parameter to list all reactions to a team discussion. | [optional] 
 **per_page** | **int**| The number of results per page (max 100). For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 30]
 **page** | **int**| The page number of the results to fetch. For more information, see \&quot;[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api).\&quot; | [optional] [default to 1]

### Return type

[**List[Reaction]**](Reaction.md)

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

