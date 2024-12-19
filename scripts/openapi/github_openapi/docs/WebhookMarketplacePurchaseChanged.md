# WebhookMarketplacePurchaseChanged


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**effective_date** | **str** |  | 
**enterprise** | [**EnterpriseWebhooks**](EnterpriseWebhooks.md) |  | [optional] 
**installation** | [**SimpleInstallation**](SimpleInstallation.md) |  | [optional] 
**marketplace_purchase** | [**WebhooksMarketplacePurchase**](WebhooksMarketplacePurchase.md) |  | 
**organization** | [**OrganizationSimpleWebhooks**](OrganizationSimpleWebhooks.md) |  | [optional] 
**previous_marketplace_purchase** | [**MarketplacePurchase**](MarketplacePurchase.md) |  | [optional] 
**repository** | [**RepositoryWebhooks**](RepositoryWebhooks.md) |  | [optional] 
**sender** | [**SimpleUser**](SimpleUser.md) |  | 

## Example

```python
from github_openapi.models.webhook_marketplace_purchase_changed import WebhookMarketplacePurchaseChanged

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookMarketplacePurchaseChanged from a JSON string
webhook_marketplace_purchase_changed_instance = WebhookMarketplacePurchaseChanged.from_json(json)
# print the JSON string representation of the object
print(WebhookMarketplacePurchaseChanged.to_json())

# convert the object into a dict
webhook_marketplace_purchase_changed_dict = webhook_marketplace_purchase_changed_instance.to_dict()
# create an instance of WebhookMarketplacePurchaseChanged from a dict
webhook_marketplace_purchase_changed_from_dict = WebhookMarketplacePurchaseChanged.from_dict(webhook_marketplace_purchase_changed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


