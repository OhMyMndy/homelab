# WebhookMemberRemoved


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**member** | [**WebhooksUser**](WebhooksUser.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_member_removed import WebhookMemberRemoved

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMemberRemoved from a JSON string
webhook_member_removed_instance = WebhookMemberRemoved.from_json(json)
# print the JSON string representation of the object
print(WebhookMemberRemoved.to_json())

# convert the object into a dict
webhook_member_removed_dict = webhook_member_removed_instance.to_dict()
# create an instance of WebhookMemberRemoved from a dict
webhook_member_removed_from_dict = WebhookMemberRemoved.from_dict(webhook_member_removed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


