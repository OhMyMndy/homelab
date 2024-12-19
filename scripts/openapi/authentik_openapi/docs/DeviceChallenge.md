# DeviceChallenge

Single device challenge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_class** | **str** |  | 
**device_uid** | **str** |  | 
**challenge** | **Dict[str, object]** |  | 

## Example

```python
from authentik_openapi.models.device_challenge import DeviceChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceChallenge from a JSON string
device_challenge_instance = DeviceChallenge.from_json(json)
# print the JSON string representation of the object
print(DeviceChallenge.to_json())

# convert the object into a dict
device_challenge_dict = device_challenge_instance.to_dict()
# create an instance of DeviceChallenge from a dict
device_challenge_from_dict = DeviceChallenge.from_dict(device_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


