# Activity

Activity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**node_id** | **str** |  | 
**before** | **str** | The SHA of the commit before the activity. | 
**after** | **str** | The SHA of the commit after the activity. | 
**ref** | **str** | The full Git reference, formatted as &#x60;refs/heads/&lt;branch name&gt;&#x60;. | 
**timestamp** | **datetime** | The time when the activity occurred. | 
**activity_type** | **str** | The type of the activity that was performed. | 
**actor** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 

## Example

```python
from github_openapi.models.activity import Activity

# TODO update the JSON string below
json = "{}"
# create an instance of Activity from a JSON string
activity_instance = Activity.from_json(json)
# print the JSON string representation of the object
print(Activity.to_json())

# convert the object into a dict
activity_dict = activity_instance.to_dict()
# create an instance of Activity from a dict
activity_from_dict = Activity.from_dict(activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


