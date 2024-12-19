# CopilotIdeChat

Usage metrics for Copilot Chat in the IDE.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_engaged_users** | **int** | Total number of users who prompted Copilot Chat in the IDE. | [optional] 
**editors** | [**List[CopilotIdeChatEditorsInner]**](CopilotIdeChatEditorsInner.md) |  | [optional] 

## Example

```python
from github_openapi.models.copilot_ide_chat import CopilotIdeChat

# TODO update the JSON string below
json = "{}"
# create an instance of CopilotIdeChat from a JSON string
copilot_ide_chat_instance = CopilotIdeChat.from_json(json)
# print the JSON string representation of the object
print(CopilotIdeChat.to_json())

# convert the object into a dict
copilot_ide_chat_dict = copilot_ide_chat_instance.to_dict()
# create an instance of CopilotIdeChat from a dict
copilot_ide_chat_from_dict = CopilotIdeChat.from_dict(copilot_ide_chat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


