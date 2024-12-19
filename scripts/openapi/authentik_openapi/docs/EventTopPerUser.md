# EventTopPerUser

Response object of Event's top_per_user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | **Dict[str, object]** |  | 
**counted_events** | **int** |  | 
**unique_users** | **int** |  | 

## Example

```python
from authentik_openapi.models.event_top_per_user import EventTopPerUser

# TODO update the JSON string below
json = "{}"
# create an instance of EventTopPerUser from a JSON string
event_top_per_user_instance = EventTopPerUser.from_json(json)
# print the JSON string representation of the object
print(EventTopPerUser.to_json())

# convert the object into a dict
event_top_per_user_dict = event_top_per_user_instance.to_dict()
# create an instance of EventTopPerUser from a dict
event_top_per_user_from_dict = EventTopPerUser.from_dict(event_top_per_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


