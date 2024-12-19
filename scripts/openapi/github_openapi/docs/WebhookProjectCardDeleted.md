# WebhookProjectCardDeleted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**project_card** | [**ProjectCard**](ProjectCard.md) |  | 
**repository** | [**NullableRepositoryWebhooks**](NullableRepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_project_card_deleted import WebhookProjectCardDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectCardDeleted from a JSON string
webhook_project_card_deleted_instance = WebhookProjectCardDeleted.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectCardDeleted.to_json())

# convert the object into a dict
webhook_project_card_deleted_dict = webhook_project_card_deleted_instance.to_dict()
# create an instance of WebhookProjectCardDeleted from a dict
webhook_project_card_deleted_from_dict = WebhookProjectCardDeleted.from_dict(webhook_project_card_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


