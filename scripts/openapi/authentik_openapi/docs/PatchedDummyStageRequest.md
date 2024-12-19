# PatchedDummyStageRequest

DummyStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**throw_error** | **bool** |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_dummy_stage_request import PatchedDummyStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedDummyStageRequest from a JSON string
patched_dummy_stage_request_instance = PatchedDummyStageRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedDummyStageRequest.to_json())

# convert the object into a dict
patched_dummy_stage_request_dict = patched_dummy_stage_request_instance.to_dict()
# create an instance of PatchedDummyStageRequest from a dict
patched_dummy_stage_request_from_dict = PatchedDummyStageRequest.from_dict(patched_dummy_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


