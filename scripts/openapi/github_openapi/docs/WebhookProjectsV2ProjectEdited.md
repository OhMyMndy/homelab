# WebhookProjectsV2ProjectEdited


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**changes** | [**WebhookProjectsV2ProjectEditedChanges**](WebhookProjectsV2ProjectEditedChanges.md) |  | 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | 
**projects_v2** | [**ProjectsV2**](ProjectsV2.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_projects_v2_project_edited import WebhookProjectsV2ProjectEdited

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectsV2ProjectEdited from a JSON string
webhook_projects_v2_project_edited_instance = WebhookProjectsV2ProjectEdited.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectsV2ProjectEdited.to_json())

# convert the object into a dict
webhook_projects_v2_project_edited_dict = webhook_projects_v2_project_edited_instance.to_dict()
# create an instance of WebhookProjectsV2ProjectEdited from a dict
webhook_projects_v2_project_edited_from_dict = WebhookProjectsV2ProjectEdited.from_dict(webhook_projects_v2_project_edited_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


