# MarketplacePurchase2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**WebhooksMarketplacePurchaseAccount**](WebhooksMarketplacePurchaseAccount.md) |  | 
**billing_cycle** | **str** |  | 
**free_trial_ends_on** | **object** |  | 
**next_billing_date** | **str** |  | 
**on_free_trial** | **bool** |  | 
**plan** | [**WebhooksPreviousMarketplacePurchasePlan**](WebhooksPreviousMarketplacePurchasePlan.md) |  | 
**unit_count** | **int** |  | 

## Example

```python
from github_openapi.models.marketplace_purchase2 import MarketplacePurchase2

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplacePurchase2 from a JSON string
marketplace_purchase2_instance = MarketplacePurchase2.from_json(json)
# print the JSON string representation of the object
print(MarketplacePurchase2.to_json())

# convert the object into a dict
marketplace_purchase2_dict = marketplace_purchase2_instance.to_dict()
# create an instance of MarketplacePurchase2 from a dict
marketplace_purchase2_from_dict = MarketplacePurchase2.from_dict(marketplace_purchase2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


