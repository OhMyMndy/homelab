# CodespacesUpdateForAuthenticatedUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**machine** | **str** | A valid machine to transition this codespace to. | [optional] 
**display_name** | **str** | Display name for this codespace | [optional] 
**recent_folders** | **List[str]** | Recently opened folders inside the codespace. It is currently used by the clients to determine the folder path to load the codespace in. | [optional] 

## Example

```python
from github_openapi.models.codespaces_update_for_authenticated_user_request import CodespacesUpdateForAuthenticatedUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CodespacesUpdateForAuthenticatedUserRequest from a JSON string
codespaces_update_for_authenticated_user_request_instance = CodespacesUpdateForAuthenticatedUserRequest.from_json(json)
# print the JSON string representation of the object
print(CodespacesUpdateForAuthenticatedUserRequest.to_json())

# convert the object into a dict
codespaces_update_for_authenticated_user_request_dict = codespaces_update_for_authenticated_user_request_instance.to_dict()
# create an instance of CodespacesUpdateForAuthenticatedUserRequest from a dict
codespaces_update_for_authenticated_user_request_from_dict = CodespacesUpdateForAuthenticatedUserRequest.from_dict(codespaces_update_for_authenticated_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


