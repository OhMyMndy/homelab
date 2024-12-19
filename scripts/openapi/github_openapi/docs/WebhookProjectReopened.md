# WebhookProjectReopened


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**project** | [**WebhooksProject**](WebhooksProject.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_project_reopened import WebhookProjectReopened

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookProjectReopened from a JSON string
webhook_project_reopened_instance = WebhookProjectReopened.from_json(json)
# print the JSON string representation of the object
print(WebhookProjectReopened.to_json())

# convert the object into a dict
webhook_project_reopened_dict = webhook_project_reopened_instance.to_dict()
# create an instance of WebhookProjectReopened from a dict
webhook_project_reopened_from_dict = WebhookProjectReopened.from_dict(webhook_project_reopened_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


