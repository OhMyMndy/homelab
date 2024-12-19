# WebhooksSponsorship


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | 
**maintainer** | [**WebhooksSponsorshipMaintainer**](WebhooksSponsorshipMaintainer.md) |  | [optional] 
**node_id** | **str** |  | 
**privacy_level** | **str** |  | 
**sponsor** | [**User2**](User2.md) |  | 
**sponsorable** | [**User2**](User2.md) |  | 
**tier** | [**SponsorshipTier**](SponsorshipTier.md) |  | 

## Example

```python
from github_openapi.models.webhooks_sponsorship import WebhooksSponsorship

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksSponsorship from a JSON string
webhooks_sponsorship_instance = WebhooksSponsorship.from_json(json)
# print the JSON string representation of the object
print(WebhooksSponsorship.to_json())

# convert the object into a dict
webhooks_sponsorship_dict = webhooks_sponsorship_instance.to_dict()
# create an instance of WebhooksSponsorship from a dict
webhooks_sponsorship_from_dict = WebhooksSponsorship.from_dict(webhooks_sponsorship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


