# OutpostDefaultConfig

Global default outpost config

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **Dict[str, object]** |  | [readonly] 

## Example

```python
from authentik_openapi.models.outpost_default_config import OutpostDefaultConfig

# TODO update the JSON string below
json = "{}"
# create an instance of OutpostDefaultConfig from a JSON string
outpost_default_config_instance = OutpostDefaultConfig.from_json(json)
# print the JSON string representation of the object
print(OutpostDefaultConfig.to_json())

# convert the object into a dict
outpost_default_config_dict = outpost_default_config_instance.to_dict()
# create an instance of OutpostDefaultConfig from a dict
outpost_default_config_from_dict = OutpostDefaultConfig.from_dict(outpost_default_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


