# GoogleWorkspaceProviderUser

GoogleWorkspaceProviderUser Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**google_id** | **str** |  | 
**user** | **int** |  | 
**user_obj** | [**GroupMember**](GroupMember.md) |  | [readonly] 
**provider** | **int** |  | 
**attributes** | **object** |  | [readonly] 

## Example

```python
from authentik_openapi.models.google_workspace_provider_user import GoogleWorkspaceProviderUser

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleWorkspaceProviderUser from a JSON string
google_workspace_provider_user_instance = GoogleWorkspaceProviderUser.from_json(json)
# print the JSON string representation of the object
print(GoogleWorkspaceProviderUser.to_json())

# convert the object into a dict
google_workspace_provider_user_dict = google_workspace_provider_user_instance.to_dict()
# create an instance of GoogleWorkspaceProviderUser from a dict
google_workspace_provider_user_from_dict = GoogleWorkspaceProviderUser.from_dict(google_workspace_provider_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


