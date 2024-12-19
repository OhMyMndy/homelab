# MarketplaceAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 
**id** | **int** |  | 
**type** | **str** |  | 
**node_id** | **str** |  | [optional] 
**login** | **str** |  | 
**email** | **str** |  | [optional] 
**organization_billing_email** | **str** |  | [optional] 

## Example

```python
from github_openapi.models.marketplace_account import MarketplaceAccount

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceAccount from a JSON string
marketplace_account_instance = MarketplaceAccount.from_json(json)
# print the JSON string representation of the object
print(MarketplaceAccount.to_json())

# convert the object into a dict
marketplace_account_dict = marketplace_account_instance.to_dict()
# create an instance of MarketplaceAccount from a dict
marketplace_account_from_dict = MarketplaceAccount.from_dict(marketplace_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


