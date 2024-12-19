# WebhookSponsorshipTierChanged


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**changes** | [**WebhooksChanges8**](WebhooksChanges8.md) |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 
**sponsorship** | [**WebhooksSponsorship**](WebhooksSponsorship.md) |  | 

## Example

```python
from github_openapi.models.webhook_sponsorship_tier_changed import WebhookSponsorshipTierChanged

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSponsorshipTierChanged from a JSON string
webhook_sponsorship_tier_changed_instance = WebhookSponsorshipTierChanged.from_json(json)
# print the JSON string representation of the object
print(WebhookSponsorshipTierChanged.to_json())

# convert the object into a dict
webhook_sponsorship_tier_changed_dict = webhook_sponsorship_tier_changed_instance.to_dict()
# create an instance of WebhookSponsorshipTierChanged from a dict
webhook_sponsorship_tier_changed_from_dict = WebhookSponsorshipTierChanged.from_dict(webhook_sponsorship_tier_changed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


