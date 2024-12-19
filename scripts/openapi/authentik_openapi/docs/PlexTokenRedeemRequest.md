# PlexTokenRedeemRequest

Serializer to redeem a plex token

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plex_token** | **str** |  | 

## Example

```python
from authentik_openapi.models.plex_token_redeem_request import PlexTokenRedeemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlexTokenRedeemRequest from a JSON string
plex_token_redeem_request_instance = PlexTokenRedeemRequest.from_json(json)
# print the JSON string representation of the object
print(PlexTokenRedeemRequest.to_json())

# convert the object into a dict
plex_token_redeem_request_dict = plex_token_redeem_request_instance.to_dict()
# create an instance of PlexTokenRedeemRequest from a dict
plex_token_redeem_request_from_dict = PlexTokenRedeemRequest.from_dict(plex_token_redeem_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


