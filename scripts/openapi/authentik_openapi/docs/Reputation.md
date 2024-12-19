# Reputation

Reputation Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [optional] 
**identifier** | **str** |  | 
**ip** | **str** |  | 
**ip_geo_data** | **object** |  | [optional] 
**ip_asn_data** | **object** |  | [optional] 
**score** | **int** |  | [optional] 
**updated** | **datetime** |  | [readonly] 

## Example

```python
from authentik_openapi.models.reputation import Reputation

# TODO update the JSON string below
json = "{}"
# create an instance of Reputation from a JSON string
reputation_instance = Reputation.from_json(json)
# print the JSON string representation of the object
print(Reputation.to_json())

# convert the object into a dict
reputation_dict = reputation_instance.to_dict()
# create an instance of Reputation from a dict
reputation_from_dict = Reputation.from_dict(reputation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


