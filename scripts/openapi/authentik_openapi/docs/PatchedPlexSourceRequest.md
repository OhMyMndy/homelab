# PatchedPlexSourceRequest

Plex Source Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Source&#39;s display Name. | [optional] 
**slug** | **str** | Internal source name, used in URLs. | [optional] 
**enabled** | **bool** |  | [optional] 
**authentication_flow** | **str** | Flow to use when authenticating existing users. | [optional] 
**enrollment_flow** | **str** | Flow to use when enrolling new users. | [optional] 
**policy_engine_mode** | [**PolicyEngineMode**](PolicyEngineMode.md) |  | [optional] 
**user_matching_mode** | [**UserMatchingModeEnum**](UserMatchingModeEnum.md) | How the source determines if an existing user should be authenticated or a new user enrolled. | [optional] 
**user_path_template** | **str** |  | [optional] 
**client_id** | **str** | Client identifier used to talk to Plex. | [optional] 
**allowed_servers** | **List[str]** | Which servers a user has to be a member of to be granted access. Empty list allows every server. | [optional] 
**allow_friends** | **bool** | Allow friends to authenticate, even if you don&#39;t share a server. | [optional] 
**plex_token** | **str** | Plex token used to check friends | [optional] 

## Example

```python
from authentik_openapi.models.patched_plex_source_request import PatchedPlexSourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedPlexSourceRequest from a JSON string
patched_plex_source_request_instance = PatchedPlexSourceRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedPlexSourceRequest.to_json())

# convert the object into a dict
patched_plex_source_request_dict = patched_plex_source_request_instance.to_dict()
# create an instance of PatchedPlexSourceRequest from a dict
patched_plex_source_request_from_dict = PatchedPlexSourceRequest.from_dict(patched_plex_source_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


