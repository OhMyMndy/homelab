# CopilotIdeCodeCompletions

Usage metrics for Copilot editor code completions in the IDE.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_engaged_users** | **int** | Number of users who accepted at least one Copilot code suggestion, across all active editors. Includes both full and partial acceptances. | [optional] 
**languages** | [**List[CopilotIdeCodeCompletionsLanguagesInner]**](CopilotIdeCodeCompletionsLanguagesInner.md) | Code completion metrics for active languages. | [optional] 
**editors** | [**List[CopilotIdeCodeCompletionsEditorsInner]**](CopilotIdeCodeCompletionsEditorsInner.md) |  | [optional] 

## Example

```python
from github_openapi.models.copilot_ide_code_completions import CopilotIdeCodeCompletions

# TODO update the JSON string below
json = "{}"
# create an instance of CopilotIdeCodeCompletions from a JSON string
copilot_ide_code_completions_instance = CopilotIdeCodeCompletions.from_json(json)
# print the JSON string representation of the object
print(CopilotIdeCodeCompletions.to_json())

# convert the object into a dict
copilot_ide_code_completions_dict = copilot_ide_code_completions_instance.to_dict()
# create an instance of CopilotIdeCodeCompletions from a dict
copilot_ide_code_completions_from_dict = CopilotIdeCodeCompletions.from_dict(copilot_ide_code_completions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


