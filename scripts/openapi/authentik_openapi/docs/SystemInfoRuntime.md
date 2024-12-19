# SystemInfoRuntime

Get versions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**python_version** | **str** |  | 
**environment** | **str** |  | 
**architecture** | **str** |  | 
**platform** | **str** |  | 
**uname** | **str** |  | 
**openssl_version** | **str** |  | 
**openssl_fips_enabled** | **bool** |  | 
**authentik_version** | **str** |  | 

## Example

```python
from authentik_openapi.models.system_info_runtime import SystemInfoRuntime

# TODO update the JSON string below
json = "{}"
# create an instance of SystemInfoRuntime from a JSON string
system_info_runtime_instance = SystemInfoRuntime.from_json(json)
# print the JSON string representation of the object
print(SystemInfoRuntime.to_json())

# convert the object into a dict
system_info_runtime_dict = system_info_runtime_instance.to_dict()
# create an instance of SystemInfoRuntime from a dict
system_info_runtime_from_dict = SystemInfoRuntime.from_dict(system_info_runtime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


