# EmailChallenge

Email challenge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ChallengeChoices**](ChallengeChoices.md) |  | 
**flow_info** | [**ContextualFlowInfo**](ContextualFlowInfo.md) |  | [optional] 
**component** | **str** |  | [optional] [default to 'ak-stage-email']
**response_errors** | **Dict[str, List[ErrorDetail]]** |  | [optional] 

## Example

```python
from authentik_openapi.models.email_challenge import EmailChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of EmailChallenge from a JSON string
email_challenge_instance = EmailChallenge.from_json(json)
# print the JSON string representation of the object
print(EmailChallenge.to_json())

# convert the object into a dict
email_challenge_dict = email_challenge_instance.to_dict()
# create an instance of EmailChallenge from a dict
email_challenge_from_dict = EmailChallenge.from_dict(email_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


