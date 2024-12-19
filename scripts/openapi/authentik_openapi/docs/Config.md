# Config

Serialize authentik Config into DRF Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_reporting** | [**ErrorReportingConfig**](ErrorReportingConfig.md) |  | 
**capabilities** | [**List[CapabilitiesEnum]**](CapabilitiesEnum.md) |  | 
**cache_timeout** | **int** |  | 
**cache_timeout_flows** | **int** |  | 
**cache_timeout_policies** | **int** |  | 
**cache_timeout_reputation** | **int** |  | 

## Example

```python
from authentik_openapi.models.config import Config

# TODO update the JSON string below
json = "{}"
# create an instance of Config from a JSON string
config_instance = Config.from_json(json)
# print the JSON string representation of the object
print(Config.to_json())

# convert the object into a dict
config_dict = config_instance.to_dict()
# create an instance of Config from a dict
config_from_dict = Config.from_dict(config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


