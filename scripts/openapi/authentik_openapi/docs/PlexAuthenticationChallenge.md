# PlexAuthenticationChallenge

Challenge shown to the user in identification stage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ChallengeChoices**](ChallengeChoices.md) |  | 
**flow_info** | [**ContextualFlowInfo**](ContextualFlowInfo.md) |  | [optional] 
**component** | **str** |  | [optional] [default to 'ak-source-plex']
**response_errors** | **Dict[str, List[ErrorDetail]]** |  | [optional] 
**client_id** | **str** |  | 
**slug** | **str** |  | 

## Example

```python
from authentik_openapi.models.plex_authentication_challenge import PlexAuthenticationChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of PlexAuthenticationChallenge from a JSON string
plex_authentication_challenge_instance = PlexAuthenticationChallenge.from_json(json)
# print the JSON string representation of the object
print(PlexAuthenticationChallenge.to_json())

# convert the object into a dict
plex_authentication_challenge_dict = plex_authentication_challenge_instance.to_dict()
# create an instance of PlexAuthenticationChallenge from a dict
plex_authentication_challenge_from_dict = PlexAuthenticationChallenge.from_dict(plex_authentication_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


