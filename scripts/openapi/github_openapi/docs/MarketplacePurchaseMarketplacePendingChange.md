# MarketplacePurchaseMarketplacePendingChange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_installed** | **bool** |  | [optional] 
**effective_date** | **str** |  | [optional] 
**unit_count** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**plan** | [**MarketplaceListingPlan**](MarketplaceListingPlan.md) |  | [optional] 

## Example

```python
from github_openapi.models.marketplace_purchase_marketplace_pending_change import MarketplacePurchaseMarketplacePendingChange

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplacePurchaseMarketplacePendingChange from a JSON string
marketplace_purchase_marketplace_pending_change_instance = MarketplacePurchaseMarketplacePendingChange.from_json(json)
# print the JSON string representation of the object
print(MarketplacePurchaseMarketplacePendingChange.to_json())

# convert the object into a dict
marketplace_purchase_marketplace_pending_change_dict = marketplace_purchase_marketplace_pending_change_instance.to_dict()
# create an instance of MarketplacePurchaseMarketplacePendingChange from a dict
marketplace_purchase_marketplace_pending_change_from_dict = MarketplacePurchaseMarketplacePendingChange.from_dict(marketplace_purchase_marketplace_pending_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


