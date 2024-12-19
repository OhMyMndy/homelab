# DeviceChallengeRequest

Single device challenge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_class** | **str** |  | 
**device_uid** | **str** |  | 
**challenge** | **Dict[str, object]** |  | 

## Example

```python
from authentik_openapi.models.device_challenge_request import DeviceChallengeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceChallengeRequest from a JSON string
device_challenge_request_instance = DeviceChallengeRequest.from_json(json)
# print the JSON string representation of the object
print(DeviceChallengeRequest.to_json())

# convert the object into a dict
device_challenge_request_dict = device_challenge_request_instance.to_dict()
# create an instance of DeviceChallengeRequest from a dict
device_challenge_request_from_dict = DeviceChallengeRequest.from_dict(device_challenge_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


