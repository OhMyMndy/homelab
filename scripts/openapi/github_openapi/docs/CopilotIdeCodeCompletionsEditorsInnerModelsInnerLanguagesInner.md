# CopilotIdeCodeCompletionsEditorsInnerModelsInnerLanguagesInner

Usage metrics for a given language for the given editor for Copilot code completions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the language used for Copilot code completion suggestions, for the given editor. | [optional] 
**total_engaged_users** | **int** | Number of users who accepted at least one Copilot code completion suggestion for the given editor, for the given language. Includes both full and partial acceptances. | [optional] 
**total_code_suggestions** | **int** | The number of Copilot code suggestions generated for the given editor, for the given language. | [optional] 
**total_code_acceptances** | **int** | The number of Copilot code suggestions accepted for the given editor, for the given language. Includes both full and partial acceptances. | [optional] 
**total_code_lines_suggested** | **int** | The number of lines of code suggested by Copilot code completions for the given editor, for the given language. | [optional] 
**total_code_lines_accepted** | **int** | The number of lines of code accepted from Copilot code suggestions for the given editor, for the given language. | [optional] 

## Example

```python
from github_openapi.models.copilot_ide_code_completions_editors_inner_models_inner_languages_inner import CopilotIdeCodeCompletionsEditorsInnerModelsInnerLanguagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CopilotIdeCodeCompletionsEditorsInnerModelsInnerLanguagesInner from a JSON string
copilot_ide_code_completions_editors_inner_models_inner_languages_inner_instance = CopilotIdeCodeCompletionsEditorsInnerModelsInnerLanguagesInner.from_json(json)
# print the JSON string representation of the object
print(CopilotIdeCodeCompletionsEditorsInnerModelsInnerLanguagesInner.to_json())

# convert the object into a dict
copilot_ide_code_completions_editors_inner_models_inner_languages_inner_dict = copilot_ide_code_completions_editors_inner_models_inner_languages_inner_instance.to_dict()
# create an instance of CopilotIdeCodeCompletionsEditorsInnerModelsInnerLanguagesInner from a dict
copilot_ide_code_completions_editors_inner_models_inner_languages_inner_from_dict = CopilotIdeCodeCompletionsEditorsInnerModelsInnerLanguagesInner.from_dict(copilot_ide_code_completions_editors_inner_models_inner_languages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


