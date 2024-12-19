# EventRepo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from github_openapi.models.event_repo import EventRepo

# TODO update the JSON string below
json = "{}"
# create an instance of EventRepo from a JSON string
event_repo_instance = EventRepo.from_json(json)
# print the JSON string representation of the object
print(EventRepo.to_json())

# convert the object into a dict
event_repo_dict = event_repo_instance.to_dict()
# create an instance of EventRepo from a dict
event_repo_from_dict = EventRepo.from_dict(event_repo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


