# SystemInfo

Get system information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_headers** | **Dict[str, str]** | Get HTTP Request headers | [readonly] 
**http_host** | **str** | Get HTTP host | [readonly] 
**http_is_secure** | **bool** | Get HTTP Secure flag | [readonly] 
**runtime** | [**SystemInfoRuntime**](SystemInfoRuntime.md) |  | 
**brand** | **str** | Currently active brand | [readonly] 
**server_time** | **datetime** | Current server time | [readonly] 
**embedded_outpost_disabled** | **bool** | Whether the embedded outpost is disabled | [readonly] 
**embedded_outpost_host** | **str** | Get the FQDN configured on the embedded outpost | [readonly] 

## Example

```python
from authentik_openapi.models.system_info import SystemInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SystemInfo from a JSON string
system_info_instance = SystemInfo.from_json(json)
# print the JSON string representation of the object
print(SystemInfo.to_json())

# convert the object into a dict
system_info_dict = system_info_instance.to_dict()
# create an instance of SystemInfo from a dict
system_info_from_dict = SystemInfo.from_dict(system_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


