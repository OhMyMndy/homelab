# CodespacesCreateForAuthenticatedUserRequestOneOf1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pull_request** | [**CodespacesCreateForAuthenticatedUserRequestOneOf1PullRequest**](CodespacesCreateForAuthenticatedUserRequestOneOf1PullRequest.md) |  | 
**location** | **str** | The requested location for a new codespace. Best efforts are made to respect this upon creation. Assigned by IP if not provided. | [optional] 
**geo** | **str** | The geographic area for this codespace. If not specified, the value is assigned by IP. This property replaces &#x60;location&#x60;, which is closing down. | [optional] 
**machine** | **str** | Machine type to use for this codespace | [optional] 
**devcontainer_path** | **str** | Path to devcontainer.json config to use for this codespace | [optional] 
**working_directory** | **str** | Working directory for this codespace | [optional] 
**idle_timeout_minutes** | **int** | Time in minutes before codespace stops from inactivity | [optional] 

## Example

```python
from github_openapi.models.codespaces_create_for_authenticated_user_request_one_of1 import CodespacesCreateForAuthenticatedUserRequestOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of CodespacesCreateForAuthenticatedUserRequestOneOf1 from a JSON string
codespaces_create_for_authenticated_user_request_one_of1_instance = CodespacesCreateForAuthenticatedUserRequestOneOf1.from_json(json)
# print the JSON string representation of the object
print(CodespacesCreateForAuthenticatedUserRequestOneOf1.to_json())

# convert the object into a dict
codespaces_create_for_authenticated_user_request_one_of1_dict = codespaces_create_for_authenticated_user_request_one_of1_instance.to_dict()
# create an instance of CodespacesCreateForAuthenticatedUserRequestOneOf1 from a dict
codespaces_create_for_authenticated_user_request_one_of1_from_dict = CodespacesCreateForAuthenticatedUserRequestOneOf1.from_dict(codespaces_create_for_authenticated_user_request_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


