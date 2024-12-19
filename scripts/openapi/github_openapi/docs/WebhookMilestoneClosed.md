# WebhookMilestoneClosed


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**milestone** | [**WebhooksMilestone**](WebhooksMilestone.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_milestone_closed import WebhookMilestoneClosed

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMilestoneClosed from a JSON string
webhook_milestone_closed_instance = WebhookMilestoneClosed.from_json(json)
# print the JSON string representation of the object
print(WebhookMilestoneClosed.to_json())

# convert the object into a dict
webhook_milestone_closed_dict = webhook_milestone_closed_instance.to_dict()
# create an instance of WebhookMilestoneClosed from a dict
webhook_milestone_closed_from_dict = WebhookMilestoneClosed.from_dict(webhook_milestone_closed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


