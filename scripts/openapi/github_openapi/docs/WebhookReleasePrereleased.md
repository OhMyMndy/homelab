# WebhookReleasePrereleased


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**release** | [**Release**](Release.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | [optional] 

## Example

```python
from github_openapi.models.webhook_release_prereleased import WebhookReleasePrereleased

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookReleasePrereleased from a JSON string
webhook_release_prereleased_instance = WebhookReleasePrereleased.from_json(json)
# print the JSON string representation of the object
print(WebhookReleasePrereleased.to_json())

# convert the object into a dict
webhook_release_prereleased_dict = webhook_release_prereleased_instance.to_dict()
# create an instance of WebhookReleasePrereleased from a dict
webhook_release_prereleased_from_dict = WebhookReleasePrereleased.from_dict(webhook_release_prereleased_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


