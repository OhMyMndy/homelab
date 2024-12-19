# WebhookSponsorshipPendingTierChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**changes** | [**WebhooksChanges8**](WebhooksChanges8.md) |  | 
**effective_date** | **str** | The &#x60;pending_cancellation&#x60; and &#x60;pending_tier_change&#x60; event types will include the date the cancellation or tier change will take effect. | [optional] 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 
**sponsorship** | [**WebhooksSponsorship**](WebhooksSponsorship.md) |  | 

## Example

```python
from github_openapi.models.webhook_sponsorship_pending_tier_change import WebhookSponsorshipPendingTierChange

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSponsorshipPendingTierChange from a JSON string
webhook_sponsorship_pending_tier_change_instance = WebhookSponsorshipPendingTierChange.from_json(json)
# print the JSON string representation of the object
print(WebhookSponsorshipPendingTierChange.to_json())

# convert the object into a dict
webhook_sponsorship_pending_tier_change_dict = webhook_sponsorship_pending_tier_change_instance.to_dict()
# create an instance of WebhookSponsorshipPendingTierChange from a dict
webhook_sponsorship_pending_tier_change_from_dict = WebhookSponsorshipPendingTierChange.from_dict(webhook_sponsorship_pending_tier_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


