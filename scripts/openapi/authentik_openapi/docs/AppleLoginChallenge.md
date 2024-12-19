# AppleLoginChallenge

Special challenge for apple-native authentication flow, which happens on the client.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ChallengeChoices**](ChallengeChoices.md) |  | 
**flow_info** | [**ContextualFlowInfo**](ContextualFlowInfo.md) |  | [optional] 
**component** | **str** |  | [optional] [default to 'ak-source-oauth-apple']
**response_errors** | **Dict[str, List[ErrorDetail]]** |  | [optional] 
**client_id** | **str** |  | 
**scope** | **str** |  | 
**redirect_uri** | **str** |  | 
**state** | **str** |  | 

## Example

```python
from authentik_openapi.models.apple_login_challenge import AppleLoginChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of AppleLoginChallenge from a JSON string
apple_login_challenge_instance = AppleLoginChallenge.from_json(json)
# print the JSON string representation of the object
print(AppleLoginChallenge.to_json())

# convert the object into a dict
apple_login_challenge_dict = apple_login_challenge_instance.to_dict()
# create an instance of AppleLoginChallenge from a dict
apple_login_challenge_from_dict = AppleLoginChallenge.from_dict(apple_login_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


