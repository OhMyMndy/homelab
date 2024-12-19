# WebhooksMarketplacePurchaseAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**login** | **str** |  | 
**node_id** | **str** |  | 
**organization_billing_email** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from github_openapi.models.webhooks_marketplace_purchase_account import WebhooksMarketplacePurchaseAccount

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksMarketplacePurchaseAccount from a JSON string
webhooks_marketplace_purchase_account_instance = WebhooksMarketplacePurchaseAccount.from_json(json)
# print the JSON string representation of the object
print(WebhooksMarketplacePurchaseAccount.to_json())

# convert the object into a dict
webhooks_marketplace_purchase_account_dict = webhooks_marketplace_purchase_account_instance.to_dict()
# create an instance of WebhooksMarketplacePurchaseAccount from a dict
webhooks_marketplace_purchase_account_from_dict = WebhooksMarketplacePurchaseAccount.from_dict(webhooks_marketplace_purchase_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


