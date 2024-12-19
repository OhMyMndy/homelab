# OutpostHealth

Outpost health status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** |  | [readonly] 
**last_seen** | **datetime** |  | [readonly] 
**version** | **str** |  | [readonly] 
**golang_version** | **str** |  | [readonly] 
**openssl_enabled** | **bool** |  | [readonly] 
**openssl_version** | **str** |  | [readonly] 
**fips_enabled** | **bool** | Get FIPS enabled | [readonly] 
**version_should** | **str** |  | [readonly] 
**version_outdated** | **bool** |  | [readonly] 
**build_hash** | **str** |  | [readonly] 
**build_hash_should** | **str** |  | [readonly] 
**hostname** | **str** |  | [readonly] 

## Example

```python
from authentik_openapi.models.outpost_health import OutpostHealth

# TODO update the JSON string below
json = "{}"
# create an instance of OutpostHealth from a JSON string
outpost_health_instance = OutpostHealth.from_json(json)
# print the JSON string representation of the object
print(OutpostHealth.to_json())

# convert the object into a dict
outpost_health_dict = outpost_health_instance.to_dict()
# create an instance of OutpostHealth from a dict
outpost_health_from_dict = OutpostHealth.from_dict(outpost_health_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


