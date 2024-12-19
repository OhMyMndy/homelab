# MarketplacePurchase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**WebhooksMarketplacePurchaseAccount**](WebhooksMarketplacePurchaseAccount.md) |  | 
**billing_cycle** | **str** |  | 
**free_trial_ends_on** | **str** |  | 
**next_billing_date** | **str** |  | [optional] 
**on_free_trial** | **bool** |  | 
**plan** | [**WebhooksPreviousMarketplacePurchasePlan**](WebhooksPreviousMarketplacePurchasePlan.md) |  | 
**unit_count** | **int** |  | 

## Example

```python
from github_openapi.models.marketplace_purchase import MarketplacePurchase

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplacePurchase from a JSON string
marketplace_purchase_instance = MarketplacePurchase.from_json(json)
# print the JSON string representation of the object
print(MarketplacePurchase.to_json())

# convert the object into a dict
marketplace_purchase_dict = marketplace_purchase_instance.to_dict()
# create an instance of MarketplacePurchase from a dict
marketplace_purchase_from_dict = MarketplacePurchase.from_dict(marketplace_purchase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


