# Invitation

Invitation Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**name** | **str** |  | 
**expires** | **datetime** |  | [optional] 
**fixed_data** | **Dict[str, object]** |  | [optional] 
**created_by** | [**GroupMember**](GroupMember.md) |  | [readonly] 
**single_use** | **bool** | When enabled, the invitation will be deleted after usage. | [optional] 
**flow** | **str** | When set, only the configured flow can use this invitation. | [optional] 
**flow_obj** | [**Flow**](Flow.md) |  | [readonly] 

## Example

```python
from authentik_openapi.models.invitation import Invitation

# TODO update the JSON string below
json = "{}"
# create an instance of Invitation from a JSON string
invitation_instance = Invitation.from_json(json)
# print the JSON string representation of the object
print(Invitation.to_json())

# convert the object into a dict
invitation_dict = invitation_instance.to_dict()
# create an instance of Invitation from a dict
invitation_from_dict = Invitation.from_dict(invitation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


