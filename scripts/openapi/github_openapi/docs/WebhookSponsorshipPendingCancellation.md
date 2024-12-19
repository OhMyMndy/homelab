# WebhookSponsorshipPendingCancellation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**effective_date** | **str** | The &#x60;pending_cancellation&#x60; and &#x60;pending_tier_change&#x60; event types will include the date the cancellation or tier change will take effect. | [optional] 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 
**sponsorship** | [**WebhooksSponsorship**](WebhooksSponsorship.md) |  | 

## Example

```python
from github_openapi.models.webhook_sponsorship_pending_cancellation import WebhookSponsorshipPendingCancellation

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSponsorshipPendingCancellation from a JSON string
webhook_sponsorship_pending_cancellation_instance = WebhookSponsorshipPendingCancellation.from_json(json)
# print the JSON string representation of the object
print(WebhookSponsorshipPendingCancellation.to_json())

# convert the object into a dict
webhook_sponsorship_pending_cancellation_dict = webhook_sponsorship_pending_cancellation_instance.to_dict()
# create an instance of WebhookSponsorshipPendingCancellation from a dict
webhook_sponsorship_pending_cancellation_from_dict = WebhookSponsorshipPendingCancellation.from_dict(webhook_sponsorship_pending_cancellation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


