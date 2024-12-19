# SyncStatus

Provider sync status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_running** | **bool** |  | [readonly] 
**tasks** | [**List[SystemTask]**](SystemTask.md) |  | [readonly] 

## Example

```python
from authentik_openapi.models.sync_status import SyncStatus

# TODO update the JSON string below
json = "{}"
# create an instance of SyncStatus from a JSON string
sync_status_instance = SyncStatus.from_json(json)
# print the JSON string representation of the object
print(SyncStatus.to_json())

# convert the object into a dict
sync_status_dict = sync_status_instance.to_dict()
# create an instance of SyncStatus from a dict
sync_status_from_dict = SyncStatus.from_dict(sync_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


