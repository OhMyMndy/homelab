# AuthenticatorDuoChallenge

Duo Challenge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ChallengeChoices**](ChallengeChoices.md) |  | 
**flow_info** | [**ContextualFlowInfo**](ContextualFlowInfo.md) |  | [optional] 
**component** | **str** |  | [optional] [default to 'ak-stage-authenticator-duo']
**response_errors** | **Dict[str, List[ErrorDetail]]** |  | [optional] 
**pending_user** | **str** |  | 
**pending_user_avatar** | **str** |  | 
**activation_barcode** | **str** |  | 
**activation_code** | **str** |  | 
**stage_uuid** | **str** |  | 

## Example

```python
from authentik_openapi.models.authenticator_duo_challenge import AuthenticatorDuoChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticatorDuoChallenge from a JSON string
authenticator_duo_challenge_instance = AuthenticatorDuoChallenge.from_json(json)
# print the JSON string representation of the object
print(AuthenticatorDuoChallenge.to_json())

# convert the object into a dict
authenticator_duo_challenge_dict = authenticator_duo_challenge_instance.to_dict()
# create an instance of AuthenticatorDuoChallenge from a dict
authenticator_duo_challenge_from_dict = AuthenticatorDuoChallenge.from_dict(authenticator_duo_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


