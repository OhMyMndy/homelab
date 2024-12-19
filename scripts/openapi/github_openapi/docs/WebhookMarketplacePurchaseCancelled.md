# WebhookMarketplacePurchaseCancelled


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**effective_date** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**marketplace_purchase** | [**WebhooksMarketplacePurchase**](WebhooksMarketplacePurchase.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**previous_marketplace_purchase** | [**WebhooksPreviousMarketplacePurchase**](WebhooksPreviousMarketplacePurchase.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_marketplace_purchase_cancelled import WebhookMarketplacePurchaseCancelled

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMarketplacePurchaseCancelled from a JSON string
webhook_marketplace_purchase_cancelled_instance = WebhookMarketplacePurchaseCancelled.from_json(json)
# print the JSON string representation of the object
print(WebhookMarketplacePurchaseCancelled.to_json())

# convert the object into a dict
webhook_marketplace_purchase_cancelled_dict = webhook_marketplace_purchase_cancelled_instance.to_dict()
# create an instance of WebhookMarketplacePurchaseCancelled from a dict
webhook_marketplace_purchase_cancelled_from_dict = WebhookMarketplacePurchaseCancelled.from_dict(webhook_marketplace_purchase_cancelled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


