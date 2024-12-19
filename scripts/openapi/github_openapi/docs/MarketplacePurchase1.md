# MarketplacePurchase1


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
from github_openapi.models.marketplace_purchase1 import MarketplacePurchase1

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplacePurchase1 from a JSON string
marketplace_purchase1_instance = MarketplacePurchase1.from_json(json)
# print the JSON string representation of the object
print(MarketplacePurchase1.to_json())

# convert the object into a dict
marketplace_purchase1_dict = marketplace_purchase1_instance.to_dict()
# create an instance of MarketplacePurchase1 from a dict
marketplace_purchase1_from_dict = MarketplacePurchase1.from_dict(marketplace_purchase1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


