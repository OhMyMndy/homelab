# InvitationStageRequest

InvitationStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**continue_flow_without_invitation** | **bool** | If this flag is set, this Stage will jump to the next Stage when no Invitation is given. By default this Stage will cancel the Flow when no invitation is given. | [optional] 

## Example

```python
from authentik_openapi.models.invitation_stage_request import InvitationStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InvitationStageRequest from a JSON string
invitation_stage_request_instance = InvitationStageRequest.from_json(json)
# print the JSON string representation of the object
print(InvitationStageRequest.to_json())

# convert the object into a dict
invitation_stage_request_dict = invitation_stage_request_instance.to_dict()
# create an instance of InvitationStageRequest from a dict
invitation_stage_request_from_dict = InvitationStageRequest.from_dict(invitation_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


