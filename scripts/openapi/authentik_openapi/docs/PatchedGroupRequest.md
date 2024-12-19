# PatchedGroupRequest

Group Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**is_superuser** | **bool** | Users added to this group will be superusers. | [optional] 
**parent** | **str** |  | [optional] 
**users** | **List[int]** |  | [optional] 
**attributes** | **Dict[str, object]** |  | [optional] 
**roles** | **List[str]** |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_group_request import PatchedGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedGroupRequest from a JSON string
patched_group_request_instance = PatchedGroupRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedGroupRequest.to_json())

# convert the object into a dict
patched_group_request_dict = patched_group_request_instance.to_dict()
# create an instance of PatchedGroupRequest from a dict
patched_group_request_from_dict = PatchedGroupRequest.from_dict(patched_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


