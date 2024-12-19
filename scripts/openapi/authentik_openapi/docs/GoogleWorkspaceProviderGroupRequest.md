# GoogleWorkspaceProviderGroupRequest

GoogleWorkspaceProviderGroup Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**google_id** | **str** |  | 
**group** | **str** |  | 
**provider** | **int** |  | 

## Example

```python
from authentik_openapi.models.google_workspace_provider_group_request import GoogleWorkspaceProviderGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleWorkspaceProviderGroupRequest from a JSON string
google_workspace_provider_group_request_instance = GoogleWorkspaceProviderGroupRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleWorkspaceProviderGroupRequest.to_json())

# convert the object into a dict
google_workspace_provider_group_request_dict = google_workspace_provider_group_request_instance.to_dict()
# create an instance of GoogleWorkspaceProviderGroupRequest from a dict
google_workspace_provider_group_request_from_dict = GoogleWorkspaceProviderGroupRequest.from_dict(google_workspace_provider_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


