# LogEvent

Single log message with all context logged.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **datetime** |  | 
**log_level** | [**LogLevelEnum**](LogLevelEnum.md) |  | 
**logger** | **str** |  | 
**event** | **str** |  | 
**attributes** | **Dict[str, object]** |  | 

## Example

```python
from authentik_openapi.models.log_event import LogEvent

# TODO update the JSON string below
json = "{}"
# create an instance of LogEvent from a JSON string
log_event_instance = LogEvent.from_json(json)
# print the JSON string representation of the object
print(LogEvent.to_json())

# convert the object into a dict
log_event_dict = log_event_instance.to_dict()
# create an instance of LogEvent from a dict
log_event_from_dict = LogEvent.from_dict(log_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


