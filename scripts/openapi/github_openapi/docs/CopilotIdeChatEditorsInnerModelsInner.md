# CopilotIdeChatEditorsInnerModelsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the model used for Copilot code completion suggestions. If the default model is used will appear as &#39;default&#39;. | [optional] 
**is_custom_model** | **bool** | Indicates whether a model is custom or default. | [optional] 
**custom_model_training_date** | **str** | The training date for the custom model. | [optional] 
**total_engaged_users** | **int** | The number of users who prompted Copilot Chat in the given editor and model. | [optional] 
**total_chats** | **int** | The total number of chats initiated by users in the given editor and model. | [optional] 
**total_chat_insertion_events** | **int** | The number of times users accepted a code suggestion from Copilot Chat using the &#39;Insert Code&#39; UI element, for the given editor. | [optional] 
**total_chat_copy_events** | **int** | The number of times users copied a code suggestion from Copilot Chat using the keyboard, or the &#39;Copy&#39; UI element, for the given editor. | [optional] 

## Example

```python
from github_openapi.models.copilot_ide_chat_editors_inner_models_inner import CopilotIdeChatEditorsInnerModelsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CopilotIdeChatEditorsInnerModelsInner from a JSON string
copilot_ide_chat_editors_inner_models_inner_instance = CopilotIdeChatEditorsInnerModelsInner.from_json(json)
# print the JSON string representation of the object
print(CopilotIdeChatEditorsInnerModelsInner.to_json())

# convert the object into a dict
copilot_ide_chat_editors_inner_models_inner_dict = copilot_ide_chat_editors_inner_models_inner_instance.to_dict()
# create an instance of CopilotIdeChatEditorsInnerModelsInner from a dict
copilot_ide_chat_editors_inner_models_inner_from_dict = CopilotIdeChatEditorsInnerModelsInner.from_dict(copilot_ide_chat_editors_inner_models_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


