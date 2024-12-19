# CodespacesCreateForAuthenticatedUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_id** | **int** | Repository id for this codespace | 
**ref** | **str** | Git ref (typically a branch name) for this codespace | [optional] 
**location** | **str** | The requested location for a new codespace. Best efforts are made to respect this upon creation. Assigned by IP if not provided. | [optional] 
**geo** | **str** | The geographic area for this codespace. If not specified, the value is assigned by IP. This property replaces &#x60;location&#x60;, which is closing down. | [optional] 
**client_ip** | **str** | IP for location auto-detection when proxying a request | [optional] 
**machine** | **str** | Machine type to use for this codespace | [optional] 
**devcontainer_path** | **str** | Path to devcontainer.json config to use for this codespace | [optional] 
**multi_repo_permissions_opt_out** | **bool** | Whether to authorize requested permissions from devcontainer.json | [optional] 
**working_directory** | **str** | Working directory for this codespace | [optional] 
**idle_timeout_minutes** | **int** | Time in minutes before codespace stops from inactivity | [optional] 
**display_name** | **str** | Display name for this codespace | [optional] 
**retention_period_minutes** | **int** | Duration in minutes after codespace has gone idle in which it will be deleted. Must be integer minutes between 0 and 43200 (30 days). | [optional] 
**pull_request** | [**CodespacesCreateForAuthenticatedUserRequestOneOf1PullRequest**](CodespacesCreateForAuthenticatedUserRequestOneOf1PullRequest.md) |  | 

## Example

```python
from github_openapi.models.codespaces_create_for_authenticated_user_request import CodespacesCreateForAuthenticatedUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CodespacesCreateForAuthenticatedUserRequest from a JSON string
codespaces_create_for_authenticated_user_request_instance = CodespacesCreateForAuthenticatedUserRequest.from_json(json)
# print the JSON string representation of the object
print(CodespacesCreateForAuthenticatedUserRequest.to_json())

# convert the object into a dict
codespaces_create_for_authenticated_user_request_dict = codespaces_create_for_authenticated_user_request_instance.to_dict()
# create an instance of CodespacesCreateForAuthenticatedUserRequest from a dict
codespaces_create_for_authenticated_user_request_from_dict = CodespacesCreateForAuthenticatedUserRequest.from_dict(codespaces_create_for_authenticated_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


