# ConsentChallengeResponseRequest

Consent challenge response, any valid response request is valid

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | [optional] [default to 'ak-stage-consent']
**token** | **str** |  | 

## Example

```python
from authentik_openapi.models.consent_challenge_response_request import ConsentChallengeResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConsentChallengeResponseRequest from a JSON string
consent_challenge_response_request_instance = ConsentChallengeResponseRequest.from_json(json)
# print the JSON string representation of the object
print(ConsentChallengeResponseRequest.to_json())

# convert the object into a dict
consent_challenge_response_request_dict = consent_challenge_response_request_instance.to_dict()
# create an instance of ConsentChallengeResponseRequest from a dict
consent_challenge_response_request_from_dict = ConsentChallengeResponseRequest.from_dict(consent_challenge_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


