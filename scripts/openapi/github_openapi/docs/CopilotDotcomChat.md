# CopilotDotcomChat

Usage metrics for Copilot Chat in github.com

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_engaged_users** | **int** | Total number of users who prompted Copilot Chat on github.com at least once. | [optional] 
**models** | [**List[CopilotDotcomChatModelsInner]**](CopilotDotcomChatModelsInner.md) | List of model metrics for a custom models and the default model. | [optional] 

## Example

```python
from github_openapi.models.copilot_dotcom_chat import CopilotDotcomChat

# TODO update the JSON string below
json = "{}"
# create an instance of CopilotDotcomChat from a JSON string
copilot_dotcom_chat_instance = CopilotDotcomChat.from_json(json)
# print the JSON string representation of the object
print(CopilotDotcomChat.to_json())

# convert the object into a dict
copilot_dotcom_chat_dict = copilot_dotcom_chat_instance.to_dict()
# create an instance of CopilotDotcomChat from a dict
copilot_dotcom_chat_from_dict = CopilotDotcomChat.from_dict(copilot_dotcom_chat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


