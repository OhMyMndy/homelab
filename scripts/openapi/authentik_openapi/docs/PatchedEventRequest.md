# PatchedEventRequest

Event Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **object** |  | [optional] 
**action** | [**EventActions**](EventActions.md) |  | [optional] 
**app** | **str** |  | [optional] 
**context** | **object** |  | [optional] 
**client_ip** | **str** |  | [optional] 
**expires** | **datetime** |  | [optional] 
**brand** | **object** |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_event_request import PatchedEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedEventRequest from a JSON string
patched_event_request_instance = PatchedEventRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedEventRequest.to_json())

# convert the object into a dict
patched_event_request_dict = patched_event_request_instance.to_dict()
# create an instance of PatchedEventRequest from a dict
patched_event_request_from_dict = PatchedEventRequest.from_dict(patched_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


