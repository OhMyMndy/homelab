# WebhookSponsorshipCancelled


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 
**sponsorship** | [**WebhooksSponsorship**](WebhooksSponsorship.md) |  | 

## Example

```python
from github_openapi.models.webhook_sponsorship_cancelled import WebhookSponsorshipCancelled

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSponsorshipCancelled from a JSON string
webhook_sponsorship_cancelled_instance = WebhookSponsorshipCancelled.from_json(json)
# print the JSON string representation of the object
print(WebhookSponsorshipCancelled.to_json())

# convert the object into a dict
webhook_sponsorship_cancelled_dict = webhook_sponsorship_cancelled_instance.to_dict()
# create an instance of WebhookSponsorshipCancelled from a dict
webhook_sponsorship_cancelled_from_dict = WebhookSponsorshipCancelled.from_dict(webhook_sponsorship_cancelled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


