# WebhookDeployKeyDeleted


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**key** | [**WebhooksDeployKey**](WebhooksDeployKey.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_deploy_key_deleted import WebhookDeployKeyDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDeployKeyDeleted from a JSON string
webhook_deploy_key_deleted_instance = WebhookDeployKeyDeleted.from_json(json)
# print the JSON string representation of the object
print(WebhookDeployKeyDeleted.to_json())

# convert the object into a dict
webhook_deploy_key_deleted_dict = webhook_deploy_key_deleted_instance.to_dict()
# create an instance of WebhookDeployKeyDeleted from a dict
webhook_deploy_key_deleted_from_dict = WebhookDeployKeyDeleted.from_dict(webhook_deploy_key_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


