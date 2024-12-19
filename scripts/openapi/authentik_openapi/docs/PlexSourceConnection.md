# PlexSourceConnection

Plex Source connection Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**user** | **int** |  | [readonly] 
**source** | [**Source**](Source.md) |  | [readonly] 
**identifier** | **str** |  | 
**plex_token** | **str** |  | 

## Example

```python
from authentik_openapi.models.plex_source_connection import PlexSourceConnection

# TODO update the JSON string below
json = "{}"
# create an instance of PlexSourceConnection from a JSON string
plex_source_connection_instance = PlexSourceConnection.from_json(json)
# print the JSON string representation of the object
print(PlexSourceConnection.to_json())

# convert the object into a dict
plex_source_connection_dict = plex_source_connection_instance.to_dict()
# create an instance of PlexSourceConnection from a dict
plex_source_connection_from_dict = PlexSourceConnection.from_dict(plex_source_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


