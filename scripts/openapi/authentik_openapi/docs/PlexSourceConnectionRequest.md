# PlexSourceConnectionRequest

Plex Source connection Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | 
**plex_token** | **str** |  | 

## Example

```python
from authentik_openapi.models.plex_source_connection_request import PlexSourceConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlexSourceConnectionRequest from a JSON string
plex_source_connection_request_instance = PlexSourceConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(PlexSourceConnectionRequest.to_json())

# convert the object into a dict
plex_source_connection_request_dict = plex_source_connection_request_instance.to_dict()
# create an instance of PlexSourceConnectionRequest from a dict
plex_source_connection_request_from_dict = PlexSourceConnectionRequest.from_dict(plex_source_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


