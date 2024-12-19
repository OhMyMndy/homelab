# WebhookOrgBlockBlocked


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**blocked_user** | [**WebhooksUser**](WebhooksUser.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_org_block_blocked import WebhookOrgBlockBlocked

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookOrgBlockBlocked from a JSON string
webhook_org_block_blocked_instance = WebhookOrgBlockBlocked.from_json(json)
# print the JSON string representation of the object
print(WebhookOrgBlockBlocked.to_json())

# convert the object into a dict
webhook_org_block_blocked_dict = webhook_org_block_blocked_instance.to_dict()
# create an instance of WebhookOrgBlockBlocked from a dict
webhook_org_block_blocked_from_dict = WebhookOrgBlockBlocked.from_dict(webhook_org_block_blocked_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


