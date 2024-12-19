# EventPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**issue** | [**Issue**](Issue.md) |  | [optional] 
**comment** | [**IssueComment**](IssueComment.md) |  | [optional] 
**pages** | [**List[EventPayloadPagesInner]**](EventPayloadPagesInner.md) |  | [optional] 

## Example

```python
from github_openapi.models.event_payload import EventPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EventPayload from a JSON string
event_payload_instance = EventPayload.from_json(json)
# print the JSON string representation of the object
print(EventPayload.to_json())

# convert the object into a dict
event_payload_dict = event_payload_instance.to_dict()
# create an instance of EventPayload from a dict
event_payload_from_dict = EventPayload.from_dict(event_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


