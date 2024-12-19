# MarketplacePurchaseMarketplacePurchase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_cycle** | **str** |  | [optional] 
**next_billing_date** | **str** |  | [optional] 
**is_installed** | **bool** |  | [optional] 
**unit_count** | **int** |  | [optional] 
**on_free_trial** | **bool** |  | [optional] 
**free_trial_ends_on** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**plan** | [**MarketplaceListingPlan**](MarketplaceListingPlan.md) |  | [optional] 

## Example

```python
from github_openapi.models.marketplace_purchase_marketplace_purchase import MarketplacePurchaseMarketplacePurchase

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplacePurchaseMarketplacePurchase from a JSON string
marketplace_purchase_marketplace_purchase_instance = MarketplacePurchaseMarketplacePurchase.from_json(json)
# print the JSON string representation of the object
print(MarketplacePurchaseMarketplacePurchase.to_json())

# convert the object into a dict
marketplace_purchase_marketplace_purchase_dict = marketplace_purchase_marketplace_purchase_instance.to_dict()
# create an instance of MarketplacePurchaseMarketplacePurchase from a dict
marketplace_purchase_marketplace_purchase_from_dict = MarketplacePurchaseMarketplacePurchase.from_dict(marketplace_purchase_marketplace_purchase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


