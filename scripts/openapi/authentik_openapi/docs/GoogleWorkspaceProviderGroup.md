# GoogleWorkspaceProviderGroup

GoogleWorkspaceProviderGroup Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**google_id** | **str** |  | 
**group** | **str** |  | 
**group_obj** | [**UserGroup**](UserGroup.md) |  | [readonly] 
**provider** | **int** |  | 
**attributes** | **object** |  | [readonly] 

## Example

```python
from authentik_openapi.models.google_workspace_provider_group import GoogleWorkspaceProviderGroup

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleWorkspaceProviderGroup from a JSON string
google_workspace_provider_group_instance = GoogleWorkspaceProviderGroup.from_json(json)
# print the JSON string representation of the object
print(GoogleWorkspaceProviderGroup.to_json())

# convert the object into a dict
google_workspace_provider_group_dict = google_workspace_provider_group_instance.to_dict()
# create an instance of GoogleWorkspaceProviderGroup from a dict
google_workspace_provider_group_from_dict = GoogleWorkspaceProviderGroup.from_dict(google_workspace_provider_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


