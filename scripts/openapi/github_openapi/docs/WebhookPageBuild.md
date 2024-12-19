# WebhookPageBuild


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build** | [**WebhookPageBuildBuild**](WebhookPageBuildBuild.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**id** | **int** |  | 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_page_build import WebhookPageBuild

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPageBuild from a JSON string
webhook_page_build_instance = WebhookPageBuild.from_json(json)
# print the JSON string representation of the object
print(WebhookPageBuild.to_json())

# convert the object into a dict
webhook_page_build_dict = webhook_page_build_instance.to_dict()
# create an instance of WebhookPageBuild from a dict
webhook_page_build_from_dict = WebhookPageBuild.from_dict(webhook_page_build_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


