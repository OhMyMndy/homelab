# GroupRequest

Group Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**is_superuser** | **bool** | Users added to this group will be superusers. | [optional] 
**parent** | **str** |  | [optional] 
**users** | **List[int]** |  | [optional] 
**attributes** | **Dict[str, object]** |  | [optional] 
**roles** | **List[str]** |  | [optional] 

## Example

```python
from authentik_openapi.models.group_request import GroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRequest from a JSON string
group_request_instance = GroupRequest.from_json(json)
# print the JSON string representation of the object
print(GroupRequest.to_json())

# convert the object into a dict
group_request_dict = group_request_instance.to_dict()
# create an instance of GroupRequest from a dict
group_request_from_dict = GroupRequest.from_dict(group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


