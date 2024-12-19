# WebhookMetaDeletedHookConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** |  | 
**insecure_ssl** | **str** |  | 
**secret** | **str** |  | [optional] 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.webhook_meta_deleted_hook_config import WebhookMetaDeletedHookConfig

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMetaDeletedHookConfig from a JSON string
webhook_meta_deleted_hook_config_instance = WebhookMetaDeletedHookConfig.from_json(json)
# print the JSON string representation of the object
print(WebhookMetaDeletedHookConfig.to_json())

# convert the object into a dict
webhook_meta_deleted_hook_config_dict = webhook_meta_deleted_hook_config_instance.to_dict()
# create an instance of WebhookMetaDeletedHookConfig from a dict
webhook_meta_deleted_hook_config_from_dict = WebhookMetaDeletedHookConfig.from_dict(webhook_meta_deleted_hook_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


