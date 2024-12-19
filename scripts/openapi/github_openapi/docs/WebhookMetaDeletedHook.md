# WebhookMetaDeletedHook

The modified webhook. This will contain different keys based on the type of webhook it is: repository, organization, business, app, or GitHub Marketplace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | 
**config** | [**WebhookMetaDeletedHookConfig**](WebhookMetaDeletedHookConfig.md) |  | 
**created_at** | **str** |  | 
**events** | **List[str]** |  | 
**id** | **int** |  | 
**name** | **str** |  | 
**type** | **str** |  | 
**updated_at** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_meta_deleted_hook import WebhookMetaDeletedHook

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMetaDeletedHook from a JSON string
webhook_meta_deleted_hook_instance = WebhookMetaDeletedHook.from_json(json)
# print the JSON string representation of the object
print(WebhookMetaDeletedHook.to_json())

# convert the object into a dict
webhook_meta_deleted_hook_dict = webhook_meta_deleted_hook_instance.to_dict()
# create an instance of WebhookMetaDeletedHook from a dict
webhook_meta_deleted_hook_from_dict = WebhookMetaDeletedHook.from_dict(webhook_meta_deleted_hook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


