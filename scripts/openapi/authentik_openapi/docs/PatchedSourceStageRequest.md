# PatchedSourceStageRequest

SourceStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**source** | **str** |  | [optional] 
**resume_timeout** | **str** | Amount of time a user can take to return from the source to continue the flow (Format: hours&#x3D;-1;minutes&#x3D;-2;seconds&#x3D;-3) | [optional] 

## Example

```python
from authentik_openapi.models.patched_source_stage_request import PatchedSourceStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedSourceStageRequest from a JSON string
patched_source_stage_request_instance = PatchedSourceStageRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedSourceStageRequest.to_json())

# convert the object into a dict
patched_source_stage_request_dict = patched_source_stage_request_instance.to_dict()
# create an instance of PatchedSourceStageRequest from a dict
patched_source_stage_request_from_dict = PatchedSourceStageRequest.from_dict(patched_source_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


