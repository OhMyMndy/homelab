# WebhookMarketplacePurchasePurchased


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
from github_openapi.models.webhook_marketplace_purchase_purchased import WebhookMarketplacePurchasePurchased

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMarketplacePurchasePurchased from a JSON string
webhook_marketplace_purchase_purchased_instance = WebhookMarketplacePurchasePurchased.from_json(json)
# print the JSON string representation of the object
print(WebhookMarketplacePurchasePurchased.to_json())

# convert the object into a dict
webhook_marketplace_purchase_purchased_dict = webhook_marketplace_purchase_purchased_instance.to_dict()
# create an instance of WebhookMarketplacePurchasePurchased from a dict
webhook_marketplace_purchase_purchased_from_dict = WebhookMarketplacePurchasePurchased.from_dict(webhook_marketplace_purchase_purchased_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


