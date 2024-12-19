# PromptStageRequest

PromptStage Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**fields** | **List[str]** |  | 
**validation_policies** | **List[str]** |  | [optional] 

## Example

```python
from authentik_openapi.models.prompt_stage_request import PromptStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PromptStageRequest from a JSON string
prompt_stage_request_instance = PromptStageRequest.from_json(json)
# print the JSON string representation of the object
print(PromptStageRequest.to_json())

# convert the object into a dict
prompt_stage_request_dict = prompt_stage_request_instance.to_dict()
# create an instance of PromptStageRequest from a dict
prompt_stage_request_from_dict = PromptStageRequest.from_dict(prompt_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


