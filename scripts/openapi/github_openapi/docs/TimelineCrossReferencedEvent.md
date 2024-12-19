# TimelineCrossReferencedEvent

Timeline Cross Referenced Event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **str** |  | 
**actor** | [**SimpleUser**](SimpleUser.md) |  | [optional] 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**source** | [**TimelineCrossReferencedEventSource**](TimelineCrossReferencedEventSource.md) |  | 

## Example

```python
from github_openapi.models.timeline_cross_referenced_event import TimelineCrossReferencedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineCrossReferencedEvent from a JSON string
timeline_cross_referenced_event_instance = TimelineCrossReferencedEvent.from_json(json)
# print the JSON string representation of the object
print(TimelineCrossReferencedEvent.to_json())

# convert the object into a dict
timeline_cross_referenced_event_dict = timeline_cross_referenced_event_instance.to_dict()
# create an instance of TimelineCrossReferencedEvent from a dict
timeline_cross_referenced_event_from_dict = TimelineCrossReferencedEvent.from_dict(timeline_cross_referenced_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


