# ConsentChallenge

Challenge info for consent screens

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ChallengeChoices**](ChallengeChoices.md) |  | 
**flow_info** | [**ContextualFlowInfo**](ContextualFlowInfo.md) |  | [optional] 
**component** | **str** |  | [optional] [default to 'ak-stage-consent']
**response_errors** | **Dict[str, List[ErrorDetail]]** |  | [optional] 
**pending_user** | **str** |  | 
**pending_user_avatar** | **str** |  | 
**header_text** | **str** |  | [optional] 
**permissions** | [**List[ConsentPermission]**](ConsentPermission.md) |  | 
**additional_permissions** | [**List[ConsentPermission]**](ConsentPermission.md) |  | 
**token** | **str** |  | 

## Example

```python
from authentik_openapi.models.consent_challenge import ConsentChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentChallenge from a JSON string
consent_challenge_instance = ConsentChallenge.from_json(json)
# print the JSON string representation of the object
print(ConsentChallenge.to_json())

# convert the object into a dict
consent_challenge_dict = consent_challenge_instance.to_dict()
# create an instance of ConsentChallenge from a dict
consent_challenge_from_dict = ConsentChallenge.from_dict(consent_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


