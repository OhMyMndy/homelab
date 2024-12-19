# PatchedPlexSourceConnectionRequest

Plex Source connection Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | [optional] 
**plex_token** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_plex_source_connection_request import PatchedPlexSourceConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedPlexSourceConnectionRequest from a JSON string
patched_plex_source_connection_request_instance = PatchedPlexSourceConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedPlexSourceConnectionRequest.to_json())

# convert the object into a dict
patched_plex_source_connection_request_dict = patched_plex_source_connection_request_instance.to_dict()
# create an instance of PatchedPlexSourceConnectionRequest from a dict
patched_plex_source_connection_request_from_dict = PatchedPlexSourceConnectionRequest.from_dict(patched_plex_source_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


