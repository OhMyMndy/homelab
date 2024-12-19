# PatchedDenyStageRequest

DenyStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**deny_message** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_deny_stage_request import PatchedDenyStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedDenyStageRequest from a JSON string
patched_deny_stage_request_instance = PatchedDenyStageRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedDenyStageRequest.to_json())

# convert the object into a dict
patched_deny_stage_request_dict = patched_deny_stage_request_instance.to_dict()
# create an instance of PatchedDenyStageRequest from a dict
patched_deny_stage_request_from_dict = PatchedDenyStageRequest.from_dict(patched_deny_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


