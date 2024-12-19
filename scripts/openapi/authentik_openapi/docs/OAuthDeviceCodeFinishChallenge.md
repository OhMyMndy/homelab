# OAuthDeviceCodeFinishChallenge

Final challenge after user enters their code

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ChallengeChoices**](ChallengeChoices.md) |  | 
**flow_info** | [**ContextualFlowInfo**](ContextualFlowInfo.md) |  | [optional] 
**component** | **str** |  | [optional] [default to 'ak-provider-oauth2-device-code-finish']
**response_errors** | **Dict[str, List[ErrorDetail]]** |  | [optional] 

## Example

```python
from authentik_openapi.models.o_auth_device_code_finish_challenge import OAuthDeviceCodeFinishChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthDeviceCodeFinishChallenge from a JSON string
o_auth_device_code_finish_challenge_instance = OAuthDeviceCodeFinishChallenge.from_json(json)
# print the JSON string representation of the object
print(OAuthDeviceCodeFinishChallenge.to_json())

# convert the object into a dict
o_auth_device_code_finish_challenge_dict = o_auth_device_code_finish_challenge_instance.to_dict()
# create an instance of OAuthDeviceCodeFinishChallenge from a dict
o_auth_device_code_finish_challenge_from_dict = OAuthDeviceCodeFinishChallenge.from_dict(o_auth_device_code_finish_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


