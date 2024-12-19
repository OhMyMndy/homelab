# GoogleWorkspaceProviderMappingRequest

GoogleWorkspaceProviderMapping Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**managed** | **str** | Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update. | [optional] 
**name** | **str** |  | 
**expression** | **str** |  | 

## Example

```python
from authentik_openapi.models.google_workspace_provider_mapping_request import GoogleWorkspaceProviderMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleWorkspaceProviderMappingRequest from a JSON string
google_workspace_provider_mapping_request_instance = GoogleWorkspaceProviderMappingRequest.from_json(json)
# print the JSON string representation of the object
print(GoogleWorkspaceProviderMappingRequest.to_json())

# convert the object into a dict
google_workspace_provider_mapping_request_dict = google_workspace_provider_mapping_request_instance.to_dict()
# create an instance of GoogleWorkspaceProviderMappingRequest from a dict
google_workspace_provider_mapping_request_from_dict = GoogleWorkspaceProviderMappingRequest.from_dict(google_workspace_provider_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


