# TimelineCrossReferencedEventSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**issue** | [**Issue**](Issue.md) |  | [optional] 

## Example

```python
from github_openapi.models.timeline_cross_referenced_event_source import TimelineCrossReferencedEventSource

# TODO update the JSON string below
json = "{}"
# create an instance of TimelineCrossReferencedEventSource from a JSON string
timeline_cross_referenced_event_source_instance = TimelineCrossReferencedEventSource.from_json(json)
# print the JSON string representation of the object
print(TimelineCrossReferencedEventSource.to_json())

# convert the object into a dict
timeline_cross_referenced_event_source_dict = timeline_cross_referenced_event_source_instance.to_dict()
# create an instance of TimelineCrossReferencedEventSource from a dict
timeline_cross_referenced_event_source_from_dict = TimelineCrossReferencedEventSource.from_dict(timeline_cross_referenced_event_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


