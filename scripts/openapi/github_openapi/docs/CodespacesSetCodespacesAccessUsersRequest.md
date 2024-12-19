# CodespacesSetCodespacesAccessUsersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_usernames** | **List[str]** | The usernames of the organization members whose codespaces be billed to the organization. | 

## Example

```python
from github_openapi.models.codespaces_set_codespaces_access_users_request import CodespacesSetCodespacesAccessUsersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CodespacesSetCodespacesAccessUsersRequest from a JSON string
codespaces_set_codespaces_access_users_request_instance = CodespacesSetCodespacesAccessUsersRequest.from_json(json)
# print the JSON string representation of the object
print(CodespacesSetCodespacesAccessUsersRequest.to_json())

# convert the object into a dict
codespaces_set_codespaces_access_users_request_dict = codespaces_set_codespaces_access_users_request_instance.to_dict()
# create an instance of CodespacesSetCodespacesAccessUsersRequest from a dict
codespaces_set_codespaces_access_users_request_from_dict = CodespacesSetCodespacesAccessUsersRequest.from_dict(codespaces_set_codespaces_access_users_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


