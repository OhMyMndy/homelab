# WebhooksMarketplacePurchase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**WebhooksMarketplacePurchaseAccount**](WebhooksMarketplacePurchaseAccount.md) |  | 
**billing_cycle** | **str** |  | 
**free_trial_ends_on** | **str** |  | 
**next_billing_date** | **str** |  | 
**on_free_trial** | **bool** |  | 
**plan** | [**WebhooksMarketplacePurchasePlan**](WebhooksMarketplacePurchasePlan.md) |  | 
**unit_count** | **int** |  | 

## Example

```python
from github_openapi.models.webhooks_marketplace_purchase import WebhooksMarketplacePurchase

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksMarketplacePurchase from a JSON string
webhooks_marketplace_purchase_instance = WebhooksMarketplacePurchase.from_json(json)
# print the JSON string representation of the object
print(WebhooksMarketplacePurchase.to_json())

# convert the object into a dict
webhooks_marketplace_purchase_dict = webhooks_marketplace_purchase_instance.to_dict()
# create an instance of WebhooksMarketplacePurchase from a dict
webhooks_marketplace_purchase_from_dict = WebhooksMarketplacePurchase.from_dict(webhooks_marketplace_purchase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


