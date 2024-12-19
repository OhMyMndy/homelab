# CopilotIdeCodeCompletionsLanguagesInner

Usage metrics for a given language for the given editor for Copilot code completions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the language used for Copilot code completion suggestions. | [optional] 
**total_engaged_users** | **int** | Number of users who accepted at least one Copilot code completion suggestion for the given language. Includes both full and partial acceptances. | [optional] 

## Example

```python
from github_openapi.models.copilot_ide_code_completions_languages_inner import CopilotIdeCodeCompletionsLanguagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CopilotIdeCodeCompletionsLanguagesInner from a JSON string
copilot_ide_code_completions_languages_inner_instance = CopilotIdeCodeCompletionsLanguagesInner.from_json(json)
# print the JSON string representation of the object
print(CopilotIdeCodeCompletionsLanguagesInner.to_json())

# convert the object into a dict
copilot_ide_code_completions_languages_inner_dict = copilot_ide_code_completions_languages_inner_instance.to_dict()
# create an instance of CopilotIdeCodeCompletionsLanguagesInner from a dict
copilot_ide_code_completions_languages_inner_from_dict = CopilotIdeCodeCompletionsLanguagesInner.from_dict(copilot_ide_code_completions_languages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


