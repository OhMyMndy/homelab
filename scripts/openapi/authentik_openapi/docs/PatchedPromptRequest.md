# PatchedPromptRequest

Prompt Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**field_key** | **str** | Name of the form field, also used to store the value | [optional] 
**label** | **str** |  | [optional] 
**type** | [**PromptTypeEnum**](PromptTypeEnum.md) |  | [optional] 
**required** | **bool** |  | [optional] 
**placeholder** | **str** | Optionally provide a short hint that describes the expected input value. When creating a fixed choice field, enable interpreting as expression and return a list to return multiple choices. | [optional] 
**initial_value** | **str** | Optionally pre-fill the input with an initial value. When creating a fixed choice field, enable interpreting as expression and return a list to return multiple default choices. | [optional] 
**order** | **int** |  | [optional] 
**promptstage_set** | [**List[StageRequest]**](StageRequest.md) |  | [optional] 
**sub_text** | **str** |  | [optional] 
**placeholder_expression** | **bool** |  | [optional] 
**initial_value_expression** | **bool** |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_prompt_request import PatchedPromptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedPromptRequest from a JSON string
patched_prompt_request_instance = PatchedPromptRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedPromptRequest.to_json())

# convert the object into a dict
patched_prompt_request_dict = patched_prompt_request_instance.to_dict()
# create an instance of PatchedPromptRequest from a dict
patched_prompt_request_from_dict = PatchedPromptRequest.from_dict(patched_prompt_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


