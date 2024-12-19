# WebhooksMarketplacePurchasePlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bullets** | **List[Optional[str]]** |  | 
**description** | **str** |  | 
**has_free_trial** | **bool** |  | 
**id** | **int** |  | 
**monthly_price_in_cents** | **int** |  | 
**name** | **str** |  | 
**price_model** | **str** |  | 
**unit_name** | **str** |  | 
**yearly_price_in_cents** | **int** |  | 

## Example

```python
from github_openapi.models.webhooks_marketplace_purchase_plan import WebhooksMarketplacePurchasePlan

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksMarketplacePurchasePlan from a JSON string
webhooks_marketplace_purchase_plan_instance = WebhooksMarketplacePurchasePlan.from_json(json)
# print the JSON string representation of the object
print(WebhooksMarketplacePurchasePlan.to_json())

# convert the object into a dict
webhooks_marketplace_purchase_plan_dict = webhooks_marketplace_purchase_plan_instance.to_dict()
# create an instance of WebhooksMarketplacePurchasePlan from a dict
webhooks_marketplace_purchase_plan_from_dict = WebhooksMarketplacePurchasePlan.from_dict(webhooks_marketplace_purchase_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


