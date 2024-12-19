# WebhookProjectsV2ItemRestored


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
from github_openapi.models.webhook_projects_v2_item_restored import WebhookProjectsV2ItemRestored

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectsV2ItemRestored from a JSON string
webhook_projects_v2_item_restored_instance = WebhookProjectsV2ItemRestored.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectsV2ItemRestored.to_json())

# convert the object into a dict
webhook_projects_v2_item_restored_dict = webhook_projects_v2_item_restored_instance.to_dict()
# create an instance of WebhookProjectsV2ItemRestored from a dict
webhook_projects_v2_item_restored_from_dict = WebhookProjectsV2ItemRestored.from_dict(webhook_projects_v2_item_restored_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


