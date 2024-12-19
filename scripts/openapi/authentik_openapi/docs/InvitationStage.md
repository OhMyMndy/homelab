# InvitationStage

InvitationStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**name** | **str** |  | 
**component** | **str** | Get object type so that we know how to edit the object | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**flow_set** | [**List[FlowSet]**](FlowSet.md) |  | [optional] 
**continue_flow_without_invitation** | **bool** | If this flag is set, this Stage will jump to the next Stage when no Invitation is given. By default this Stage will cancel the Flow when no invitation is given. | [optional] 

## Example

```python
from authentik_openapi.models.invitation_stage import InvitationStage

# TODO update the JSON string below
json = "{}"
# create an instance of InvitationStage from a JSON string
invitation_stage_instance = InvitationStage.from_json(json)
# print the JSON string representation of the object
print(InvitationStage.to_json())

# convert the object into a dict
invitation_stage_dict = invitation_stage_instance.to_dict()
# create an instance of InvitationStage from a dict
invitation_stage_from_dict = InvitationStage.from_dict(invitation_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


