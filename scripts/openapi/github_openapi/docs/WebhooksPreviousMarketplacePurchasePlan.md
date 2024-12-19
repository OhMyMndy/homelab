# WebhooksPreviousMarketplacePurchasePlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bullets** | **List[str]** |  | 
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
from github_openapi.models.webhooks_previous_marketplace_purchase_plan import WebhooksPreviousMarketplacePurchasePlan

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksPreviousMarketplacePurchasePlan from a JSON string
webhooks_previous_marketplace_purchase_plan_instance = WebhooksPreviousMarketplacePurchasePlan.from_json(json)
# print the JSON string representation of the object
print(WebhooksPreviousMarketplacePurchasePlan.to_json())

# convert the object into a dict
webhooks_previous_marketplace_purchase_plan_dict = webhooks_previous_marketplace_purchase_plan_instance.to_dict()
# create an instance of WebhooksPreviousMarketplacePurchasePlan from a dict
webhooks_previous_marketplace_purchase_plan_from_dict = WebhooksPreviousMarketplacePurchasePlan.from_dict(webhooks_previous_marketplace_purchase_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


