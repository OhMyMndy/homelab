# WebhookDelete


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**pusher_type** | **str** | The pusher type for the event. Can be either &#x60;user&#x60; or a deploy key. | 
**ref** | **str** | The [&#x60;git ref&#x60;](https://docs.github.com/rest/git/refs#get-a-reference) resource. | 
**ref_type** | **str** | The type of Git ref object deleted in the repository. | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_delete import WebhookDelete

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookDelete from a JSON string
webhook_delete_instance = WebhookDelete.from_json(json)
# print the JSON string representation of the object
print(WebhookDelete.to_json())

# convert the object into a dict
webhook_delete_dict = webhook_delete_instance.to_dict()
# create an instance of WebhookDelete from a dict
webhook_delete_from_dict = WebhookDelete.from_dict(webhook_delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


