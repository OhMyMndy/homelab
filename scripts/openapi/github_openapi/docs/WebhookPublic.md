# WebhookPublic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_public import WebhookPublic

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPublic from a JSON string
webhook_public_instance = WebhookPublic.from_json(json)
# print the JSON string representation of the object
print(WebhookPublic.to_json())

# convert the object into a dict
webhook_public_dict = webhook_public_instance.to_dict()
# create an instance of WebhookPublic from a dict
webhook_public_from_dict = WebhookPublic.from_dict(webhook_public_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


