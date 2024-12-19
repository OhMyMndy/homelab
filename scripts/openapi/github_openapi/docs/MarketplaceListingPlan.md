# MarketplaceListingPlan

Marketplace Listing Plan

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**accounts_url** | **str** |  | 
**id** | **int** |  | 
**number** | **int** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**monthly_price_in_cents** | **int** |  | 
**yearly_price_in_cents** | **int** |  | 
**price_model** | **str** |  | 
**has_free_trial** | **bool** |  | 
**unit_name** | **str** |  | 
**state** | **str** |  | 
**bullets** | **List[str]** |  | 

## Example

```python
from github_openapi.models.marketplace_listing_plan import MarketplaceListingPlan

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceListingPlan from a JSON string
marketplace_listing_plan_instance = MarketplaceListingPlan.from_json(json)
# print the JSON string representation of the object
print(MarketplaceListingPlan.to_json())

# convert the object into a dict
marketplace_listing_plan_dict = marketplace_listing_plan_instance.to_dict()
# create an instance of MarketplaceListingPlan from a dict
marketplace_listing_plan_from_dict = MarketplaceListingPlan.from_dict(marketplace_listing_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


