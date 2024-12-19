# CopilotIdeChatEditorsInner

Copilot Chat metrics, for active editors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the given editor. | [optional] 
**total_engaged_users** | **int** | The number of users who prompted Copilot Chat in the specified editor. | [optional] 
**models** | [**List[CopilotIdeChatEditorsInnerModelsInner]**](CopilotIdeChatEditorsInnerModelsInner.md) | List of model metrics for custom models and the default model. | [optional] 

## Example

```python
from github_openapi.models.copilot_ide_chat_editors_inner import CopilotIdeChatEditorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CopilotIdeChatEditorsInner from a JSON string
copilot_ide_chat_editors_inner_instance = CopilotIdeChatEditorsInner.from_json(json)
# print the JSON string representation of the object
print(CopilotIdeChatEditorsInner.to_json())

# convert the object into a dict
copilot_ide_chat_editors_inner_dict = copilot_ide_chat_editors_inner_instance.to_dict()
# create an instance of CopilotIdeChatEditorsInner from a dict
copilot_ide_chat_editors_inner_from_dict = CopilotIdeChatEditorsInner.from_dict(copilot_ide_chat_editors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


