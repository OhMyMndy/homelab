# PromptRequest

Prompt Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**field_key** | **str** | Name of the form field, also used to store the value | 
**label** | **str** |  | 
**type** | [**PromptTypeEnum**](PromptTypeEnum.md) |  | 
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
from authentik_openapi.models.prompt_request import PromptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PromptRequest from a JSON string
prompt_request_instance = PromptRequest.from_json(json)
# print the JSON string representation of the object
print(PromptRequest.to_json())

# convert the object into a dict
prompt_request_dict = prompt_request_instance.to_dict()
# create an instance of PromptRequest from a dict
prompt_request_from_dict = PromptRequest.from_dict(prompt_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


