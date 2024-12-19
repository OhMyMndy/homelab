# UserMarketplacePurchase

User Marketplace Purchase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_cycle** | **str** |  | 
**next_billing_date** | **datetime** |  | 
**unit_count** | **int** |  | 
**on_free_trial** | **bool** |  | 
**free_trial_ends_on** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**account** | [**MarketplaceAccount**](MarketplaceAccount.md) |  | 
**plan** | [**MarketplaceListingPlan**](MarketplaceListingPlan.md) |  | 

## Example

```python
from github_openapi.models.user_marketplace_purchase import UserMarketplacePurchase

# TODO update the JSON string below
json = "{}"
# create an instance of UserMarketplacePurchase from a JSON string
user_marketplace_purchase_instance = UserMarketplacePurchase.from_json(json)
# print the JSON string representation of the object
print(UserMarketplacePurchase.to_json())

# convert the object into a dict
user_marketplace_purchase_dict = user_marketplace_purchase_instance.to_dict()
# create an instance of UserMarketplacePurchase from a dict
user_marketplace_purchase_from_dict = UserMarketplacePurchase.from_dict(user_marketplace_purchase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


