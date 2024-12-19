# CopilotIdeCodeCompletionsEditorsInnerModelsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the model used for Copilot code completion suggestions. If the default model is used will appear as &#39;default&#39;. | [optional] 
**is_custom_model** | **bool** | Indicates whether a model is custom or default. | [optional] 
**custom_model_training_date** | **str** | The training date for the custom model. | [optional] 
**total_engaged_users** | **int** | Number of users who accepted at least one Copilot code completion suggestion for the given editor, for the given language and model. Includes both full and partial acceptances. | [optional] 
**languages** | [**List[CopilotIdeCodeCompletionsEditorsInnerModelsInnerLanguagesInner]**](CopilotIdeCodeCompletionsEditorsInnerModelsInnerLanguagesInner.md) | Code completion metrics for active languages, for the given editor. | [optional] 

## Example

```python
from github_openapi.models.copilot_ide_code_completions_editors_inner_models_inner import CopilotIdeCodeCompletionsEditorsInnerModelsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CopilotIdeCodeCompletionsEditorsInnerModelsInner from a JSON string
copilot_ide_code_completions_editors_inner_models_inner_instance = CopilotIdeCodeCompletionsEditorsInnerModelsInner.from_json(json)
# print the JSON string representation of the object
print(CopilotIdeCodeCompletionsEditorsInnerModelsInner.to_json())

# convert the object into a dict
copilot_ide_code_completions_editors_inner_models_inner_dict = copilot_ide_code_completions_editors_inner_models_inner_instance.to_dict()
# create an instance of CopilotIdeCodeCompletionsEditorsInnerModelsInner from a dict
copilot_ide_code_completions_editors_inner_models_inner_from_dict = CopilotIdeCodeCompletionsEditorsInnerModelsInner.from_dict(copilot_ide_code_completions_editors_inner_models_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


