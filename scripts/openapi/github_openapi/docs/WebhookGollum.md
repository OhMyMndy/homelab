# WebhookGollum


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**pages** | [**List[WebhookGollumPagesInner]**](WebhookGollumPagesInner.md) | The pages that were updated. | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_gollum import WebhookGollum

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookGollum from a JSON string
webhook_gollum_instance = WebhookGollum.from_json(json)
# print the JSON string representation of the object
print(WebhookGollum.to_json())

# convert the object into a dict
webhook_gollum_dict = webhook_gollum_instance.to_dict()
# create an instance of WebhookGollum from a dict
webhook_gollum_from_dict = WebhookGollum.from_dict(webhook_gollum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


