# PlexAuthenticationChallengeResponseRequest

Pseudo class for plex response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | [optional] [default to 'ak-source-plex']

## Example

```python
from authentik_openapi.models.plex_authentication_challenge_response_request import PlexAuthenticationChallengeResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlexAuthenticationChallengeResponseRequest from a JSON string
plex_authentication_challenge_response_request_instance = PlexAuthenticationChallengeResponseRequest.from_json(json)
# print the JSON string representation of the object
print(PlexAuthenticationChallengeResponseRequest.to_json())

# convert the object into a dict
plex_authentication_challenge_response_request_dict = plex_authentication_challenge_response_request_instance.to_dict()
# create an instance of PlexAuthenticationChallengeResponseRequest from a dict
plex_authentication_challenge_response_request_from_dict = PlexAuthenticationChallengeResponseRequest.from_dict(plex_authentication_challenge_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


