# WebhooksPreviousMarketplacePurchase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**WebhooksMarketplacePurchaseAccount**](WebhooksMarketplacePurchaseAccount.md) |  | 
**billing_cycle** | **str** |  | 
**free_trial_ends_on** | **object** |  | 
**next_billing_date** | **str** |  | [optional] 
**on_free_trial** | **bool** |  | 
**plan** | [**WebhooksPreviousMarketplacePurchasePlan**](WebhooksPreviousMarketplacePurchasePlan.md) |  | 
**unit_count** | **int** |  | 

## Example

```python
from github_openapi.models.webhooks_previous_marketplace_purchase import WebhooksPreviousMarketplacePurchase

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksPreviousMarketplacePurchase from a JSON string
webhooks_previous_marketplace_purchase_instance = WebhooksPreviousMarketplacePurchase.from_json(json)
# print the JSON string representation of the object
print(WebhooksPreviousMarketplacePurchase.to_json())

# convert the object into a dict
webhooks_previous_marketplace_purchase_dict = webhooks_previous_marketplace_purchase_instance.to_dict()
# create an instance of WebhooksPreviousMarketplacePurchase from a dict
webhooks_previous_marketplace_purchase_from_dict = WebhooksPreviousMarketplacePurchase.from_dict(webhooks_previous_marketplace_purchase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


