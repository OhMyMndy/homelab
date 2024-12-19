# WebhookProjectsV2StatusUpdateCreated


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
from github_openapi.models.webhook_projects_v2_status_update_created import WebhookProjectsV2StatusUpdateCreated

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectsV2StatusUpdateCreated from a JSON string
webhook_projects_v2_status_update_created_instance = WebhookProjectsV2StatusUpdateCreated.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectsV2StatusUpdateCreated.to_json())

# convert the object into a dict
webhook_projects_v2_status_update_created_dict = webhook_projects_v2_status_update_created_instance.to_dict()
# create an instance of WebhookProjectsV2StatusUpdateCreated from a dict
webhook_projects_v2_status_update_created_from_dict = WebhookProjectsV2StatusUpdateCreated.from_dict(webhook_projects_v2_status_update_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


