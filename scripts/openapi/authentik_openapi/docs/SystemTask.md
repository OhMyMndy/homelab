# SystemTask

Serialize TaskInfo and TaskResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | [readonly] 
**name** | **str** |  | 
**full_name** | **str** | Get full name with UID | [readonly] 
**uid** | **str** |  | [optional] 
**description** | **str** |  | 
**start_timestamp** | **datetime** |  | [readonly] 
**finish_timestamp** | **datetime** |  | [readonly] 
**duration** | **float** |  | [readonly] 
**status** | [**SystemTaskStatusEnum**](SystemTaskStatusEnum.md) |  | 
**messages** | [**List[LogEvent]**](LogEvent.md) |  | 
**expires** | **datetime** |  | [optional] 
**expiring** | **bool** |  | [optional] 

## Example

```python
from authentik_openapi.models.system_task import SystemTask

# TODO update the JSON string below
json = "{}"
# create an instance of SystemTask from a JSON string
system_task_instance = SystemTask.from_json(json)
# print the JSON string representation of the object
print(SystemTask.to_json())

# convert the object into a dict
system_task_dict = system_task_instance.to_dict()
# create an instance of SystemTask from a dict
system_task_from_dict = SystemTask.from_dict(system_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


