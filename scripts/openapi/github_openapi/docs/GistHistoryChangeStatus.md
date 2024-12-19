# GistHistoryChangeStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**additions** | **int** |  | [optional] 
**deletions** | **int** |  | [optional] 

## Example

```python
from github_openapi.models.gist_history_change_status import GistHistoryChangeStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GistHistoryChangeStatus from a JSON string
gist_history_change_status_instance = GistHistoryChangeStatus.from_json(json)
# print the JSON string representation of the object
print(GistHistoryChangeStatus.to_json())

# convert the object into a dict
gist_history_change_status_dict = gist_history_change_status_instance.to_dict()
# create an instance of GistHistoryChangeStatus from a dict
gist_history_change_status_from_dict = GistHistoryChangeStatus.from_dict(gist_history_change_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


