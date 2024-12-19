# CopilotIdeCodeCompletionsEditorsInner

Copilot code completion metrics for active editors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the given editor. | [optional] 
**total_engaged_users** | **int** | Number of users who accepted at least one Copilot code completion suggestion for the given editor. Includes both full and partial acceptances. | [optional] 
**models** | [**List[CopilotIdeCodeCompletionsEditorsInnerModelsInner]**](CopilotIdeCodeCompletionsEditorsInnerModelsInner.md) | List of model metrics for custom models and the default model. | [optional] 

## Example

```python
from github_openapi.models.copilot_ide_code_completions_editors_inner import CopilotIdeCodeCompletionsEditorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CopilotIdeCodeCompletionsEditorsInner from a JSON string
copilot_ide_code_completions_editors_inner_instance = CopilotIdeCodeCompletionsEditorsInner.from_json(json)
# print the JSON string representation of the object
print(CopilotIdeCodeCompletionsEditorsInner.to_json())

# convert the object into a dict
copilot_ide_code_completions_editors_inner_dict = copilot_ide_code_completions_editors_inner_instance.to_dict()
# create an instance of CopilotIdeCodeCompletionsEditorsInner from a dict
copilot_ide_code_completions_editors_inner_from_dict = CopilotIdeCodeCompletionsEditorsInner.from_dict(copilot_ide_code_completions_editors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


