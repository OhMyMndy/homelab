# IdentificationChallengeResponseRequest

Identification challenge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | [optional] [default to 'ak-stage-identification']
**uid_field** | **str** |  | 
**password** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.identification_challenge_response_request import IdentificationChallengeResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IdentificationChallengeResponseRequest from a JSON string
identification_challenge_response_request_instance = IdentificationChallengeResponseRequest.from_json(json)
# print the JSON string representation of the object
print(IdentificationChallengeResponseRequest.to_json())

# convert the object into a dict
identification_challenge_response_request_dict = identification_challenge_response_request_instance.to_dict()
# create an instance of IdentificationChallengeResponseRequest from a dict
identification_challenge_response_request_from_dict = IdentificationChallengeResponseRequest.from_dict(identification_challenge_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


