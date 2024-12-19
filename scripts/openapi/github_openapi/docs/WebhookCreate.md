# WebhookCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The repository&#39;s current description. | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**master_branch** | **str** | The name of the repository&#39;s default branch (usually &#x60;main&#x60;). | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**pusher_type** | **str** | The pusher type for the event. Can be either &#x60;user&#x60; or a deploy key. | 
**ref** | **str** | The [&#x60;git ref&#x60;](https://docs.github.com/rest/git/refs#get-a-reference) resource. | 
**ref_type** | **str** | The type of Git ref object created in the repository. | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_create import WebhookCreate

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookCreate from a JSON string
webhook_create_instance = WebhookCreate.from_json(json)
# print the JSON string representation of the object
print(WebhookCreate.to_json())

# convert the object into a dict
webhook_create_dict = webhook_create_instance.to_dict()
# create an instance of WebhookCreate from a dict
webhook_create_from_dict = WebhookCreate.from_dict(webhook_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


