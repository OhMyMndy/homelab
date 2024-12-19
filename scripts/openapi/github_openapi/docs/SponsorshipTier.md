# SponsorshipTier

The `tier_changed` and `pending_tier_change` will include the original tier before the change or pending change. For more information, see the pending tier change payload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | 
**description** | **str** |  | 
**is_custom_ammount** | **bool** |  | [optional] 
**is_custom_amount** | **bool** |  | [optional] 
**is_one_time** | **bool** |  | 
**monthly_price_in_cents** | **int** |  | 
**monthly_price_in_dollars** | **int** |  | 
**name** | **str** |  | 
**node_id** | **str** |  | 

## Example

```python
from github_openapi.models.sponsorship_tier import SponsorshipTier

# TODO update the JSON string below
json = "{}"
# create an instance of SponsorshipTier from a JSON string
sponsorship_tier_instance = SponsorshipTier.from_json(json)
# print the JSON string representation of the object
print(SponsorshipTier.to_json())

# convert the object into a dict
sponsorship_tier_dict = sponsorship_tier_instance.to_dict()
# create an instance of SponsorshipTier from a dict
sponsorship_tier_from_dict = SponsorshipTier.from_dict(sponsorship_tier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


