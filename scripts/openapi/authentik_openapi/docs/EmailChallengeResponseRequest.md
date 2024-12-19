# EmailChallengeResponseRequest

Email challenge resposen. No fields. This challenge is always declared invalid to give the user a chance to retry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** |  | [optional] [default to 'ak-stage-email']

## Example

```python
from authentik_openapi.models.email_challenge_response_request import EmailChallengeResponseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmailChallengeResponseRequest from a JSON string
email_challenge_response_request_instance = EmailChallengeResponseRequest.from_json(json)
# print the JSON string representation of the object
print(EmailChallengeResponseRequest.to_json())

# convert the object into a dict
email_challenge_response_request_dict = email_challenge_response_request_instance.to_dict()
# create an instance of EmailChallengeResponseRequest from a dict
email_challenge_response_request_from_dict = EmailChallengeResponseRequest.from_dict(email_challenge_response_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


