# WebhookProjectsV2ProjectCreated

A project was created

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
from github_openapi.models.webhook_projects_v2_project_created import WebhookProjectsV2ProjectCreated

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectsV2ProjectCreated from a JSON string
webhook_projects_v2_project_created_instance = WebhookProjectsV2ProjectCreated.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectsV2ProjectCreated.to_json())

# convert the object into a dict
webhook_projects_v2_project_created_dict = webhook_projects_v2_project_created_instance.to_dict()
# create an instance of WebhookProjectsV2ProjectCreated from a dict
webhook_projects_v2_project_created_from_dict = WebhookProjectsV2ProjectCreated.from_dict(webhook_projects_v2_project_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


