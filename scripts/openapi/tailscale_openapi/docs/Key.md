# Key

An API access token or Auth Key. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**expires** | **datetime** |  | [optional] 
**revoked** | **datetime** |  | [optional] 
**capabilities** | [**KeyCapabilities**](KeyCapabilities.md) |  | [optional] 
**description** | **str** |  | [optional] 
**invalid** | **bool** | Response for a revoked (deleted) or expired key will have an &#x60;invalid&#x60; field set to true.  | [optional] 
**user_id** | **str** | ID of the user who created this key, empty for keys created by OAuth clients.  | [optional] 

## Example

```python
from tailscale_openapi.models.key import Key

# TODO update the JSON string below
json = "{}"
# create an instance of Key from a JSON string
key_instance = Key.from_json(json)
# print the JSON string representation of the object
print(Key.to_json())

# convert the object into a dict
key_dict = key_instance.to_dict()
# create an instance of Key from a dict
key_from_dict = Key.from_dict(key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


