# WebhookMemberEdited


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**changes** | [**WebhookMemberEditedChanges**](WebhookMemberEditedChanges.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**member** | [**WebhooksUser**](WebhooksUser.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_member_edited import WebhookMemberEdited

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMemberEdited from a JSON string
webhook_member_edited_instance = WebhookMemberEdited.from_json(json)
# print the JSON string representation of the object
print(WebhookMemberEdited.to_json())

# convert the object into a dict
webhook_member_edited_dict = webhook_member_edited_instance.to_dict()
# create an instance of WebhookMemberEdited from a dict
webhook_member_edited_from_dict = WebhookMemberEdited.from_dict(webhook_member_edited_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


