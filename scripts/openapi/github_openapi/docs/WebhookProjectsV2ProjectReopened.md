# WebhookProjectsV2ProjectReopened


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
from github_openapi.models.webhook_projects_v2_project_reopened import WebhookProjectsV2ProjectReopened

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectsV2ProjectReopened from a JSON string
webhook_projects_v2_project_reopened_instance = WebhookProjectsV2ProjectReopened.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectsV2ProjectReopened.to_json())

# convert the object into a dict
webhook_projects_v2_project_reopened_dict = webhook_projects_v2_project_reopened_instance.to_dict()
# create an instance of WebhookProjectsV2ProjectReopened from a dict
webhook_projects_v2_project_reopened_from_dict = WebhookProjectsV2ProjectReopened.from_dict(webhook_projects_v2_project_reopened_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


