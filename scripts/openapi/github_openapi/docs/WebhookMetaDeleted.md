# WebhookMetaDeleted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**hook** | [**WebhookMetaDeletedHook**](WebhookMetaDeletedHook.md) |  | 
**hook_id** | **int** | The id of the modified webhook. | 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**NullableRepositoryWebhooks**](NullableRepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_meta_deleted import WebhookMetaDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMetaDeleted from a JSON string
webhook_meta_deleted_instance = WebhookMetaDeleted.from_json(json)
# print the JSON string representation of the object
print(WebhookMetaDeleted.to_json())

# convert the object into a dict
webhook_meta_deleted_dict = webhook_meta_deleted_instance.to_dict()
# create an instance of WebhookMetaDeleted from a dict
webhook_meta_deleted_from_dict = WebhookMetaDeleted.from_dict(webhook_meta_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


