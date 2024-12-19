# StagePrompt

Serializer for a single Prompt field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_key** | **str** |  | 
**label** | **str** |  | 
**type** | [**PromptTypeEnum**](PromptTypeEnum.md) |  | 
**required** | **bool** |  | 
**placeholder** | **str** |  | 
**initial_value** | **str** |  | 
**order** | **int** |  | 
**sub_text** | **str** |  | 
**choices** | **List[str]** |  | 

## Example

```python
from authentik_openapi.models.stage_prompt import StagePrompt

# TODO update the JSON string below
json = "{}"
# create an instance of StagePrompt from a JSON string
stage_prompt_instance = StagePrompt.from_json(json)
# print the JSON string representation of the object
print(StagePrompt.to_json())

# convert the object into a dict
stage_prompt_dict = stage_prompt_instance.to_dict()
# create an instance of StagePrompt from a dict
stage_prompt_from_dict = StagePrompt.from_dict(stage_prompt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


