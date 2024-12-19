# InvitationRequest

Invitation Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**expires** | **datetime** |  | [optional] 
**fixed_data** | **Dict[str, object]** |  | [optional] 
**single_use** | **bool** | When enabled, the invitation will be deleted after usage. | [optional] 
**flow** | **str** | When set, only the configured flow can use this invitation. | [optional] 

## Example

```python
from authentik_openapi.models.invitation_request import InvitationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InvitationRequest from a JSON string
invitation_request_instance = InvitationRequest.from_json(json)
# print the JSON string representation of the object
print(InvitationRequest.to_json())

# convert the object into a dict
invitation_request_dict = invitation_request_instance.to_dict()
# create an instance of InvitationRequest from a dict
invitation_request_from_dict = InvitationRequest.from_dict(invitation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


