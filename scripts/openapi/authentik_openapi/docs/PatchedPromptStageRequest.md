# PatchedPromptStageRequest

PromptStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**fields** | **List[str]** |  | [optional] 
**validation_policies** | **List[str]** |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_prompt_stage_request import PatchedPromptStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedPromptStageRequest from a JSON string
patched_prompt_stage_request_instance = PatchedPromptStageRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedPromptStageRequest.to_json())

# convert the object into a dict
patched_prompt_stage_request_dict = patched_prompt_stage_request_instance.to_dict()
# create an instance of PatchedPromptStageRequest from a dict
patched_prompt_stage_request_from_dict = PatchedPromptStageRequest.from_dict(patched_prompt_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


