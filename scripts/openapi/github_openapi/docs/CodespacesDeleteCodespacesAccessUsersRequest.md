# CodespacesDeleteCodespacesAccessUsersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_usernames** | **List[str]** | The usernames of the organization members whose codespaces should not be billed to the organization. | 

## Example

```python
from github_openapi.models.codespaces_delete_codespaces_access_users_request import CodespacesDeleteCodespacesAccessUsersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CodespacesDeleteCodespacesAccessUsersRequest from a JSON string
codespaces_delete_codespaces_access_users_request_instance = CodespacesDeleteCodespacesAccessUsersRequest.from_json(json)
# print the JSON string representation of the object
print(CodespacesDeleteCodespacesAccessUsersRequest.to_json())

# convert the object into a dict
codespaces_delete_codespaces_access_users_request_dict = codespaces_delete_codespaces_access_users_request_instance.to_dict()
# create an instance of CodespacesDeleteCodespacesAccessUsersRequest from a dict
codespaces_delete_codespaces_access_users_request_from_dict = CodespacesDeleteCodespacesAccessUsersRequest.from_dict(codespaces_delete_codespaces_access_users_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


