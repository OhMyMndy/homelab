# WebhookProjectsV2ProjectClosed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | 
**projects_v2** | [**ProjectsV2**](ProjectsV2.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_projects_v2_project_closed import WebhookProjectsV2ProjectClosed

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectsV2ProjectClosed from a JSON string
webhook_projects_v2_project_closed_instance = WebhookProjectsV2ProjectClosed.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectsV2ProjectClosed.to_json())

# convert the object into a dict
webhook_projects_v2_project_closed_dict = webhook_projects_v2_project_closed_instance.to_dict()
# create an instance of WebhookProjectsV2ProjectClosed from a dict
webhook_projects_v2_project_closed_from_dict = WebhookProjectsV2ProjectClosed.from_dict(webhook_projects_v2_project_closed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


