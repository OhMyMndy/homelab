# WebhookProjectsV2StatusUpdateDeleted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | 
**projects_v2_status_update** | [**ProjectsV2StatusUpdate**](ProjectsV2StatusUpdate.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_projects_v2_status_update_deleted import WebhookProjectsV2StatusUpdateDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectsV2StatusUpdateDeleted from a JSON string
webhook_projects_v2_status_update_deleted_instance = WebhookProjectsV2StatusUpdateDeleted.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectsV2StatusUpdateDeleted.to_json())

# convert the object into a dict
webhook_projects_v2_status_update_deleted_dict = webhook_projects_v2_status_update_deleted_instance.to_dict()
# create an instance of WebhookProjectsV2StatusUpdateDeleted from a dict
webhook_projects_v2_status_update_deleted_from_dict = WebhookProjectsV2StatusUpdateDeleted.from_dict(webhook_projects_v2_status_update_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


