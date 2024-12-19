# PatchedInvitationStageRequest

InvitationStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**continue_flow_without_invitation** | **bool** | If this flag is set, this Stage will jump to the next Stage when no Invitation is given. By default this Stage will cancel the Flow when no invitation is given. | [optional] 

## Example

```python
from authentik_openapi.models.patched_invitation_stage_request import PatchedInvitationStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedInvitationStageRequest from a JSON string
patched_invitation_stage_request_instance = PatchedInvitationStageRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedInvitationStageRequest.to_json())

# convert the object into a dict
patched_invitation_stage_request_dict = patched_invitation_stage_request_instance.to_dict()
# create an instance of PatchedInvitationStageRequest from a dict
patched_invitation_stage_request_from_dict = PatchedInvitationStageRequest.from_dict(patched_invitation_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


