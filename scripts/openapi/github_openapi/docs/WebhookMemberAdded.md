# WebhookMemberAdded


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**changes** | [**WebhookMemberAddedChanges**](WebhookMemberAddedChanges.md) |  | [optional] 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**member** | [**WebhooksUser**](WebhooksUser.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_member_added import WebhookMemberAdded

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMemberAdded from a JSON string
webhook_member_added_instance = WebhookMemberAdded.from_json(json)
# print the JSON string representation of the object
print(WebhookMemberAdded.to_json())

# convert the object into a dict
webhook_member_added_dict = webhook_member_added_instance.to_dict()
# create an instance of WebhookMemberAdded from a dict
webhook_member_added_from_dict = WebhookMemberAdded.from_dict(webhook_member_added_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


