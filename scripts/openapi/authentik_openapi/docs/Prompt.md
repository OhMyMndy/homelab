# Prompt

Prompt Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**name** | **str** |  | 
**field_key** | **str** | Name of the form field, also used to store the value | 
**label** | **str** |  | 
**type** | [**PromptTypeEnum**](PromptTypeEnum.md) |  | 
**required** | **bool** |  | [optional] 
**placeholder** | **str** | Optionally provide a short hint that describes the expected input value. When creating a fixed choice field, enable interpreting as expression and return a list to return multiple choices. | [optional] 
**initial_value** | **str** | Optionally pre-fill the input with an initial value. When creating a fixed choice field, enable interpreting as expression and return a list to return multiple default choices. | [optional] 
**order** | **int** |  | [optional] 
**promptstage_set** | [**List[Stage]**](Stage.md) |  | [optional] 
**sub_text** | **str** |  | [optional] 
**placeholder_expression** | **bool** |  | [optional] 
**initial_value_expression** | **bool** |  | [optional] 

## Example

```python
from authentik_openapi.models.prompt import Prompt

# TODO update the JSON string below
json = "{}"
# create an instance of Prompt from a JSON string
prompt_instance = Prompt.from_json(json)
# print the JSON string representation of the object
print(Prompt.to_json())

# convert the object into a dict
prompt_dict = prompt_instance.to_dict()
# create an instance of Prompt from a dict
prompt_from_dict = Prompt.from_dict(prompt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


