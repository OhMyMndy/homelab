# Event

Event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**actor** | [**Actor**](Actor.md) |  | 
**repo** | [**EventRepo**](EventRepo.md) |  | 
**org** | [**Actor**](Actor.md) |  | [optional] 
**payload** | [**EventPayload**](EventPayload.md) |  | 
**public** | **bool** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from github_openapi.models.event import Event

# TODO update the JSON string below
json = "{}"
# create an instance of Event from a JSON string
event_instance = Event.from_json(json)
# print the JSON string representation of the object
print(Event.to_json())

# convert the object into a dict
event_dict = event_instance.to_dict()
# create an instance of Event from a dict
event_from_dict = Event.from_dict(event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


