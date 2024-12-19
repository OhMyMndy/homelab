# WebhookSponsorshipEdited


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**changes** | [**WebhookSponsorshipEditedChanges**](WebhookSponsorshipEditedChanges.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 
**sponsorship** | [**WebhooksSponsorship**](WebhooksSponsorship.md) |  | 

## Example

```python
from github_openapi.models.webhook_sponsorship_edited import WebhookSponsorshipEdited

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSponsorshipEdited from a JSON string
webhook_sponsorship_edited_instance = WebhookSponsorshipEdited.from_json(json)
# print the JSON string representation of the object
print(WebhookSponsorshipEdited.to_json())

# convert the object into a dict
webhook_sponsorship_edited_dict = webhook_sponsorship_edited_instance.to_dict()
# create an instance of WebhookSponsorshipEdited from a dict
webhook_sponsorship_edited_from_dict = WebhookSponsorshipEdited.from_dict(webhook_sponsorship_edited_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


