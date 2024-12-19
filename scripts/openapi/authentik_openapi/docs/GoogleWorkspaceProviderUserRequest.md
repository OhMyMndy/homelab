# GoogleWorkspaceProviderUserRequest

GoogleWorkspaceProviderUser Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**google_id** | **str** |  | 
**user** | **int** |  | 
**provider** | **int** |  | 

## Example

```python
from authentik_openapi.models.google_workspace_provider_user_request import GoogleWorkspaceProviderUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleWorkspaceProviderUserRequest from a JSON string
google_workspace_provider_user_request_instance = GoogleWorkspaceProviderUserRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleWorkspaceProviderUserRequest.to_json())

# convert the object into a dict
google_workspace_provider_user_request_dict = google_workspace_provider_user_request_instance.to_dict()
# create an instance of GoogleWorkspaceProviderUserRequest from a dict
google_workspace_provider_user_request_from_dict = GoogleWorkspaceProviderUserRequest.from_dict(google_workspace_provider_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


