# WebhookMarketplacePurchasePendingChangeCancelled


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**effective_date** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**marketplace_purchase** | [**MarketplacePurchase2**](MarketplacePurchase2.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**previous_marketplace_purchase** | [**WebhooksPreviousMarketplacePurchase**](WebhooksPreviousMarketplacePurchase.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_marketplace_purchase_pending_change_cancelled import WebhookMarketplacePurchasePendingChangeCancelled

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMarketplacePurchasePendingChangeCancelled from a JSON string
webhook_marketplace_purchase_pending_change_cancelled_instance = WebhookMarketplacePurchasePendingChangeCancelled.from_json(json)
# print the JSON string representation of the object
print(WebhookMarketplacePurchasePendingChangeCancelled.to_json())

# convert the object into a dict
webhook_marketplace_purchase_pending_change_cancelled_dict = webhook_marketplace_purchase_pending_change_cancelled_instance.to_dict()
# create an instance of WebhookMarketplacePurchasePendingChangeCancelled from a dict
webhook_marketplace_purchase_pending_change_cancelled_from_dict = WebhookMarketplacePurchasePendingChangeCancelled.from_dict(webhook_marketplace_purchase_pending_change_cancelled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


