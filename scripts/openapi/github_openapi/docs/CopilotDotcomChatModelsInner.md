# CopilotDotcomChatModelsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the model used for Copilot code completion suggestions. If the default model is used will appear as &#39;default&#39;. | [optional] 
**is_custom_model** | **bool** | Indicates whether a model is custom or default. | [optional] 
**custom_model_training_date** | **str** | The training date for the custom model (if applicable). | [optional] 
**total_engaged_users** | **int** | Total number of users who prompted Copilot Chat on github.com at least once for each model. | [optional] 
**total_chats** | **int** | Total number of chats initiated by users on github.com. | [optional] 

## Example

```python
from github_openapi.models.copilot_dotcom_chat_models_inner import CopilotDotcomChatModelsInner

# TODO update the JSON string below
json = "{}"
# create an instance of CopilotDotcomChatModelsInner from a JSON string
copilot_dotcom_chat_models_inner_instance = CopilotDotcomChatModelsInner.from_json(json)
# print the JSON string representation of the object
print(CopilotDotcomChatModelsInner.to_json())

# convert the object into a dict
copilot_dotcom_chat_models_inner_dict = copilot_dotcom_chat_models_inner_instance.to_dict()
# create an instance of CopilotDotcomChatModelsInner from a dict
copilot_dotcom_chat_models_inner_from_dict = CopilotDotcomChatModelsInner.from_dict(copilot_dotcom_chat_models_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


