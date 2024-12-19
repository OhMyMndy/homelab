# WebhookProjectsV2ItemArchived


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**changes** | [**WebhooksProjectChanges**](WebhooksProjectChanges.md) |  | 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | 
**projects_v2_item** | [**ProjectsV2Item**](ProjectsV2Item.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_projects_v2_item_archived import WebhookProjectsV2ItemArchived

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectsV2ItemArchived from a JSON string
webhook_projects_v2_item_archived_instance = WebhookProjectsV2ItemArchived.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectsV2ItemArchived.to_json())

# convert the object into a dict
webhook_projects_v2_item_archived_dict = webhook_projects_v2_item_archived_instance.to_dict()
# create an instance of WebhookProjectsV2ItemArchived from a dict
webhook_projects_v2_item_archived_from_dict = WebhookProjectsV2ItemArchived.from_dict(webhook_projects_v2_item_archived_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


